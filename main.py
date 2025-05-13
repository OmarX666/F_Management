import os

source = input("Enter Your Source Path: ").strip()
target = input("Enter Your Target Path: ").strip()

files = os.listdir(source)

for i in files:

    print(i)