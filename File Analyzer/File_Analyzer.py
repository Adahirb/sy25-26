import glob

# Get all .txt files in the directory

files = glob.glob("server_dump/*.txt") 

print(files)

OK_count = 0
WARN_count = 0
ERROR_count = 0

for file in files:
    file = open(file, "r")
    contents = file.readline()
    file.close()
    
    if "OK" in contents:
        OK_count += 1
    elif "WARN" in contents:
        WARN_count += 1
    elif "ERROR" in contents:
        ERROR_count += 1

print(f"OK: {OK_count}")
print(f"WARN: {WARN_count}")
print(f"ERROR: {ERROR_count}")
