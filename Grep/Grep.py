import glob

files = glob.glob("*.txt") 

#file_name = input("Enter a file name: ")

pathern = input("Enter the pathern: ")

for file_name in files:
    file = open(file_name, "r")
    lines = file.readlines()
    for i, line in enumerate(lines):
        if pathern in line:
            
            print(file_name,i+1, line.strip())