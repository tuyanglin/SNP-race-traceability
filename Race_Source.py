import xlrd
import pandas as pd
import numpy as np
from numpy import ndarray
from sys import argv


#这里是用来找出各样本所占的比例
def getSamples():
    #打开了excel，sample的表
    data = xlrd.open_workbook("NB.xlsx")
    table3 = data.sheet_by_name("sample")
    #取出两列内容存入列表中
    l1 = table3.col_values(0)#l1为各个种族的标签
    #row = len(l1)
    l2 = table3.col_values(1)#l2为各个种族样本数
    samples = {}
    #将第一个作key，第二个作为值,计算样本所占比例
    for i in range(1,len(l1)):
        samples[l1[i]] = (l2[i]/l2[0])#l2[0]为样本总数
    #print (samples)
    return samples
sample = getSamples()

#将上传的vcf格式文件中符合要求的相关位点匹配出来
def getTest():
    data = xlrd.open_workbook("NB2.xlsx")
    table = data.sheet_by_name("sample")
    sample_id = table.col_values(0)#所有用来计算比例的位置列表
    sample_id.pop(0)
    #print(sample_id)
    id = []
    allete = []
    testData = {}#将所得到的位置信息和突变匹配成一个字典
    filename = argv[1]#获得文件名
    with open(filename,"r") as f:
        for i in f:
            i = i.strip("\n")
            i = i.split("\t")
            if(len(i)<5):
                pass
            else:
                if(str(i[2]) in sample_id):
                    id.append(str(i[2]))
                    allete.append(i[4])
                else:
                    pass
    for i in range(len(id)):
        testData[id[i]] = allete[i]
    #print (testData)
    return testData
testData = getTest()

#这个函数可以返回一个P(C|CHB)*P(CHB)的DATAFRAME
def getData():
    #输出所有的列的数据，不以省略号的形式代替
    pd.set_option('display.max_columns',None)
    #将SNP位点的人群频率等相关信息读入一个dataframe中
    df = pd.read_excel("NB2.xlsx")
    #print (df)
    df["total"] = 0
    #增加一个类型转换使其和excel中数据类型相匹配
    #利用for循环计算P(C|CHB)*P(CHB),并生成全概率total列
    for i in sample.keys():
        df[i] = df[i]*sample[i]
        df["total"] = df["total"] + df[i]
    for i in sample.keys():
        df[i] = df[i]/df["total"]
    return df.drop(["total"],axis = 1)#返回一个去掉了全概率的data表
data = getData()
#print (data.values)
#print (data)


def classification(data,sample):
    total = 0
    result = sample
    #将result这个字典的值清空，作为存放祖源比例结果的新字典
    for i in result.keys():
        result[i] = 0
    #每一次循环都将更新祖源分析的比例，增加一个button，以用户的回复作为循环判断的条件。
    for i in testData.keys():
        position = i#输入所测得的位置
        SNP = testData[i]#输入对应的SNP信息
        idx = data.index[data["position"] == position].tolist()#找到与输入位置对应的行的索引,类型为列表
        ser = data.loc[idx]["allete"]#将索引得到的series存入ser变量中
        if (ser[idx[0]] == SNP):#判断是否为可用等位基因突变
            for i in result.keys():#遍历结果库，找寻可判断为各种族的概率
                #print (data.loc[idx][i].values)
                #这里是用了dataframe的.values属性，将确定位置的值从dataframe中提取出来形成一个array，再用float()转型成浮点数形式
                result[i] = result[i] + float(data.loc[idx][i].values)#将该位置有突变的情况下可做出的判断概率加入结果中
                #print (type(result[i]))
        else:
            #print ("noop")
            pass
    total = sum(result.values())
    if(total == 0):
        total = 1
    else:
        pass
    for i in result.keys():
        result[i] = result[i]/total
    return result

P = classification(data,sample)#这个就是计算得到的结果，即各成分的比例
P = sorted(P.items(),key = lambda x: x[1],reverse = True)#对计算得到的比例从大到小排序生成一个列表。
with open("result_date","a") as ffw:
    ffw.write("国内族群区分："+'\n')
    for i in P:
        ffw.write(str(i)+'\t')
    ffw.write('\n')