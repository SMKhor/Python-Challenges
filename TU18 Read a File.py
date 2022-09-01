import time

my_filename = input("Name of text file you want to read: ")

with open(my_filename,"r") as whole_file:
   for line in whole_file:
        print(line,end="")
        time.sleep(3)
