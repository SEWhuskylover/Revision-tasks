count = 0
sentance = input("write a sentance: ")
for character in sentance:
    if character == "e":
        count += 1
print(f"you used the letter E {count} times")
