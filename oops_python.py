'''
This file is to demonstrate the presence of user defined keywords

Author:Ravikumar M Pise
Contact:ravikumar.pise@ltts.com
Date of creation:25/02/21
'''

import re  # To import regular expression

class mini_project():  # to create Class
    def __init__(self):  # constructor
        self.count = 0  #initialize count as 0
        self.in_file = open("input.txt", "r")  # to open input file
        self.keyword = input("enter input keyword:")  # to input keyword from user
        self.out_file_name = self.keyword + '.txt'  # to crete text file of name keyword
        self.out_file = open(self.out_file_name, 'w')  # to open above created file

    def read_function(self):  # to define function to read
        file_read = self.in_file.read()
        file_list = re.split(r"\W+", str(file_read))  # to split words of input file and to store it in a list
        for i in range(len(file_list)):
            match = re.fullmatch(self.keyword, file_list[i], re.M | re.I)  # to check match keyword to words of list
            if match:
                self.count += 1  # to increment count if keyword matches with word in list
                string = file_list[i - 1] + " " + file_list[i] + " " + file_list[i + 1]  # to store previous and next word of keyword
                self.out_file.write(string)  # to write string into out_file
                self.out_file.write("\n")  # to separate line by line
        self.out_file.write("Total number of " + self.keyword + " in input file are ")
        self.out_file.write(str(self.count))  # to store number of keywords present in input file
    def close_file(self):  # function to close opened files
        self.in_file.close()  # to close in_file
        self.out_file.close()  # to close out_file


obj = mini_project()  # to call class through object
obj.read_function()   # to call read function
obj.close_file()  # to call close function
