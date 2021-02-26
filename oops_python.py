"""
This file is to demonstrate the presence of user defined keywords
Author:Ravikumar M Pise
Contact:ravikumar.pise@ltts.com
Date of creation:25/02/21
"""
import re  # To import regular expression
n = input("enter no of inputs:")


class Mini_project:  # to create Class
    def __init__(self):  # constructor
        self.count = 0  # initialize count as 0
        self.in_file = open("input.txt", "r")  # to open input file
        self.keyword = input("enter input keyword:")  # input from user
        self.out_file_name = self.keyword + '.txt'  # to creating txt file
        self.out_file = open(self.out_file_name, 'w')  # to open txt file

    def read_function(self):  # to define function to read
        file_read = self.in_file.read()
        f_list = re.split(r'\W+', str(file_read))  # to split words,store
        for i in range(len(f_list)):
            # to check match keyword to words of list
            match = re.fullmatch(self.keyword, f_list[i], re.M | re.I)
            if match:
                self.count += 1  # to increment count,keyword matches word
                # to store previous and next word of keyword
                string = f_list[i - 1] + " " + f_list[i] + " " + f_list[i + 1]
                self.out_file.write(string)  # to write string into out_file
                self.out_file.write("\n")  # to separate line by line
        self.out_file.write("Total " + self.keyword + " in input file is: ")
        self.out_file.write(str(self.count))  # to store number of keyword

    def close_file(self):  # function to close opened files
        self.in_file.close()  # to close in_file
        self.out_file.close()  # to close out_file


for r in range(int(n)):
    obj = Mini_project()  # to call class through object
    obj.read_function()   # to call read function
    obj.close_file()  # to call close function
