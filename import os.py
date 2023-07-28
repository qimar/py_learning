import os

source = "D:\\Python\\Python36-32\\Lib\\os.py"

try:
    os.O_CREAT(source)
    
except FileNotFoundError:
    print("File not found")
 