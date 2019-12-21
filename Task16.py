weight = int(input("Your weight: "))
print("Your weight each year on the moon next 15 years: ")
for i in range(weight, weight + 16):
    print(i * 0.165)
    