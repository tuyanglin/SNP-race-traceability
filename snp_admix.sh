#！/bin/bash
#Filename:admix.sh
#Author:Yanglin Tu Shuo Yang
#Date:5-22-2018

###Merge two VCF files to all_new.vcf########
file_name=$(basename $2 .vcf)
mkdir $file_name
cd $file_name
cp ../$1 ./
cp ../$2 ./
cp ../NB.xlsx ./
cp ../NB2.xlsx ./
python3 ../fileprocess.py $1 $2

# step 1  vcftools
admixture=/usr/local/src/admixture_linux-1.3.0/admixture
vcftools --vcf all_new.vcf --plink --out xj
# step 2
plink --noweb --file xj --geno 0.05 --maf 0.05 --make-bed --out QC
# step 3
for K in 6 ;do $admixture --cv QC.bed ${K}|tee log${K}.out;done
# step 4 besk K
grep -h CV log*.out 

######Invoking a python script######
python3 ../result.py
python3 ../Race_Source.py $2
