# SNP-race-traceability
利用SNP信息进行人类种族溯源  
**文件说明**  
admixture_linux-1.3.0.tar.gz 和 plink_linux_x86_64.zip是溯源系统需要的几个软件，解压就行  
NB.xlsx、NB2.xlsx、all.vcf 是程序运行中需要的一些文件。  
Race_Source.py 是对国内种族溯源的脚本  
fileprocess.py 是对VCF文件进行处理   
result.py 是对国际溯源结果的分析  
testdate.vcf 为测试数据  
snp_admix.sh 是主要的运行shell脚本 方式（以测试数据为例）：./snp_admix.sh all.vcf testdate.vcf 即可得到结果。  
SNP位点信息的.xlsx 这个是SNP位点信息，我们溯源系统也正是在该基础上进行，所以测试数据是这些位点的。   
所有脚本都是基于python3
对了，其中还需要安装vcftools这个软件，网上找安装方式。  
