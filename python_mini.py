
import re
count=0
string=" "
in_file = open("input.txt", "r")
keyword = input("enter input keyword:")
out_file_name = keyword+'.txt'
out_file = open(out_file_name, 'w')
file_read = in_file.read()
file_list1=file_read.split()
file_list=re.split(r"\W+",str(file_list1))
for i in range(len(file_list)):
    match = re.fullmatch(keyword, file_list[i], re.M | re.I)
    if match:
        count+=1
        string=file_list[i-1]+" "+file_list[i]+" "+file_list[i+1]
        out_file.write(string)
        out_file.write("\n")
out_file.write("Total number of "+keyword+" in input file are ")
out_file.write(str(count))
in_file.close()
out_file.close()