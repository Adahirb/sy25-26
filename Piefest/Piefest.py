print("/n---Py-Fest 2026 Stage Manager ---")
print("1. View Lineup & Total Time")
print("2. Add a New Band")
print("3. Move First Band to End (Late Arrival)")
print("4. Remove a Band by Name")
print("5. Move Band to Specific Position") # New Feature!
print("6. Exit")


if choice == "1":
    total_time = 0
    duration = int(input("Enter performance duration (minutes): "))

