#!/usr/bin/python3
import os
import sys
import linecache

famFile = './QC.fam'
qcFile = './QC.6.Q'

with open (famFile,"r") as fp,open (qcFile,"r") as fh,open ("new_result","a+") as fw:
	file1 = fp.readlines()
	file2 = fh.readlines()

	file1_name = []
	file2_EAS = []
	file2_SAS = []
	file2_AFR = []
	file2_EUR = []
	file2_MIX = []

	file1_name.append('Name')
	for line in file1:
		element = line.split()
		file1_name.append(element[0])

	file2_EAS.append('EAS')
	file2_SAS.append('SAS')
	file2_AFR.append('AFR')
	file2_EUR.append('EUR')
	file2_MIX.append('MIX')

	for line in file2:
		element = line.split()
		mix = eval(element[4]) + eval(element[5])
		file2_EAS.append(element[0])
		file2_SAS.append(element[1])
		file2_AFR.append(element[2])
		file2_EUR.append(element[3])
		file2_MIX.append(str(mix))

	
	for i in range(len(file1_name)):
		line = ''
		line = '\t'.join([file1_name[i],file2_EAS[i],file2_SAS[i],file2_AFR[i],file2_EUR[i],file2_MIX[i]])
		line += '\n'
		fw.write(line)

new_resultFile = './new_result'
count = 0
fg = open(new_resultFile, "r", encoding='utf-8')
while 1:
    buffer = fg.read(8*1024*1024)
    if not buffer:
        break
    count += buffer.count('\n')
fg.close()
linecache.updatecache(new_resultFile)
with open ("result_date","w") as fr:
	fr.write("国际族群区分："+'\n')
	for i in range(2506,count+1):
		a = linecache.getline(new_resultFile,i)
		fr.write(a)
linecache.clearcache()


