runner_info = ("Chris", 540, 54)
miles_splits = [8.5, 8.2, 8.4]

miles_splits.append(8.3)
print(miles_splits)

print(runner_info[0], sum(miles_splits))

total_time = 0
total_miles = 0

for split in miles_splits:
    total_miles = total_miles + 1
    total_time = total_time + split
print("total time", total_time, "total_miles", total_miles)