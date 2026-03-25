all_potatoes = [0,2,5,1,0,8,3,0]
perfect_potatoes = []
for p in all_potatoes:
    if p == 0:
        perfect_potatoes.append(p)
num_total = len(all_potatoes)
num_perfect = len(perfect_potatoes)
percentage = (num_perfect/num_total) * 100
print(f"Batch quality: {percentage}% perfect")
print(f"Perfect potatoes found: {num_perfect}")


blemish_count = []
for i in range (5):
     count = int(input(f"Enter blemish for potatos {i+1}: "))
     blemish_count.append(count)
total = sum(blemish_count)
average = total/len(blemish_count)
print(f"Average blemish per potato: {average}")
print(f"total blemish: {total}")


weight = float(input("Enter potato weight in grams: "))
if weight < 100:
    grade = "Small"
elif 100 <= weight <=200:
    grade = "Medium"
else:
    grade = "Large"
print(f"This is a {grade} potato")

