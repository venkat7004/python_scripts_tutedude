#!/usr/bin/env python3
# This script writes two lines of input to a file and then reads the content back.
# It assumes the file path is D:/python/output.txt. 

with open("D:/python/output.txt", "w") as file:
    line1=input("Enter first line: ")
    file.write(line1 + "\n")
    line2=input("Enter second line: ")
    file.write(line2 + "\n")

with open("D:/python/output.txt", "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content) 