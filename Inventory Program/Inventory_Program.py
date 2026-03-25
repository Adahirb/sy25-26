inventory = []

print("Options: [1] Add [2] Remove [3] List [4] Exit")
choice = input("Select an option (1-4): ")
while True:
    if choice == "1":
        item = input("Enter item name: ").strip().capitalize()
        total = int(input(f"How many {item}s?"))
        print(f"Updated: {item} (Total: {total})")
    elif choice == "2":
        name = input("Which item would you like to remove?: ").strip().capitalize()
        if name in inventory:
            print(f"Removed {name} from inventory.")
    elif choice == "3":
        print("Current Inventory")

    elif choice == "4":
        print("Exiting . . . Goodbye!")
        break
    else:
        print("Invaild Option")