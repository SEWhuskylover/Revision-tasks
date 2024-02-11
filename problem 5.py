numbers = [20, 36, 12, 20, 48, 74, 353, 23, 98]
number_lfg = int(input("what number are u wanting to find?: "))
replace = int(input(f"what do you want to replace {number_lfg} with"))

if number_lfg in numbers:
    number_to_find = numbers.index(number_lfg)
    numbers[number_to_find] = replace
    print(numbers)
else:
    print(f"{number_lfg} is not in the list")
