
import re
in_file=open("input.txt","r")       #this line is to read the input file created
keyword=input("enter input keyword:")
file_read=in_file.read()
out_file_name=keyword+'.txt'
out_file=open(out_file_name,'w')
match=re.findall(keyword,file_read,re.M|re.I)
if match:
    out_file.write(str(len(match)))
    out_file.write(str(match))
else:
        print("none")
in_file.close()
out_file.close()
