import re


class mini_project():
    def __init__(self):
        self.count = 0
        self.in_file = open("input.txt", "r")
        self.keyword = input("enter input keyword:")
        self.out_file_name = self.keyword + '.txt'
        self.out_file = open(self.out_file_name, 'w')

    def read_function(self):
        file_read = self.in_file.read()
        file_list = re.split(r"\W+", str(file_read))
        for i in range(len(file_list)):
            match = re.fullmatch(self.keyword, file_list[i], re.M | re.I)
            if match:
                self.count += 1
                string = file_list[i - 1] + " " + file_list[i] + " " + file_list[i + 1]
                self.out_file.write(string)
                self.out_file.write("\n")
        self.out_file.write("Total number of " + self.keyword + " in input file are ")
        self.out_file.write(str(self.count))
    def close_file(self):
        self.in_file.close()
        self.out_file.close()


obj = mini_project()
obj.read_function()
obj.close_file()
