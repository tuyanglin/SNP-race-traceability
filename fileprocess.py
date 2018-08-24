import sys
import re
import linecache

train_file = sys.argv[1]
test_file = sys.argv[2]

new_hash = {}

with open(test_file,'r') as fb:
	string = "#CHROM"
	linenum = 0
	test_header = fb.readline()
	while test_header:
			linenum += 1
			if string in test_header.strip():
				count = linecache.getline(test_file,linenum+1)
				count_new = [x for x in count.strip().split('\t')]
				new_hash[count_new[2]] = linenum+1
			test_header = fb.readline()
		
	with open("all_new.vcf",'w') as fw:
		with open(train_file,'r') as fh:
			num = 0
			header = fh.readline()
			while  header:
				num += 1
				if string not in header.strip():
					fw.write(header)
				else:
					now_line = header.strip()
					now_line_list = [x for x in now_line.split('\t')]

					num += 1

					next_line = fh.readline().strip()
					next_line_list = [x for x in next_line.split('\t')]
					locate_num = new_hash[next_line_list[2]]

					test_line = linecache.getline(test_file,locate_num-1).strip()
					test_line_list = [x for x in test_line.split('\t')]
					test_line_new = now_line_list + test_line_list[9:]
					for i in test_line_new:
						fw.write(i+'\t')
					fw.write('\n')


					test_line_next = linecache.getline(test_file,locate_num).strip()
					test_line_next_list = [x for x in test_line_next.split('\t')]
					test_line_next_new = next_line_list + test_line_next_list[9:]
					for i in test_line_next_new:
						fw.write(i+'\t')
					fw.write('\n')


				header = fh.readline()

					











	#for i in range(28):
		#linenum = 255 * i + 254
		#count = linecache.getline(fh,linenum)
		#count_next = linecache.getline(fh,linenum+1)




 




#	testline = linecache.getline(fb, 254)
#	test_nextline = linecache.getline(fb, 255)
#	testline_append = testline[10:]
#	test_nextline_append = test_nextline[10:]
#	with open(train_file,'w') as fb:
#		theline = linecache.getline(fb, 254)
#		the_nextline = linecache.getline(fb, 255)
#		theline