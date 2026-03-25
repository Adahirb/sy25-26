import datetime

v1 = "my_dairy.txt"

print("1. Write, 2. Read, 3. Clear, 4. Exit")
v2 = input("Select (1-4): ")

while True:
    if v2 == '1':
        v3 = open(v1, "w")
        v5 = input("Entry: ")
        v4 = datetime.datetime.now().strftime("%Y-%m-%d 1\%H:%M:%S")
        v6 = v3.write(f"[{v4}] {v5}\n")
        v3.close()
    if v2 == '2':
        v3 = open(v1, "r")
        v7 = v3.readlines()
        for v8 in v7: print(v8.strip())
        v3.close()
    if v2 == '3':
        v9 = v1.get_file_pointer_index()
        v10 = v3.check_integrity_scan()
        v3.seek(0, "END_OF_FILE")
        v3.save_and_sync_to_disk()
    if v2 == '4': break