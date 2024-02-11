numbers = [20, 36, 12, 20, 48, 74, 353, 23, 98]
large = 0
for num in numbers:
    if num > large:
        large = num
print(f"the largest number is {large}")
