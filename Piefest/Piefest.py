print("/n---Py-Fest 2026 Stage Manager ---")
print("1. View Lineup & Total Time")
print("2. Add a New Band")
print("3. Move First Band to End (Late Arrival)")
print("4. Remove a Band by Name")
print("5. Move Band to Specific Position") # New Feature!
print("6. Exit")

choice = input("Select an option (1-6): ")
i = ("Code Play", "Indie", 30),("The Pythonistas", "Rock", 45), ("Syntax Error", "Metal", 60)
current_index = i
if choice == "1":
    lineup = i
    print("\n--- Current Lineup ---")