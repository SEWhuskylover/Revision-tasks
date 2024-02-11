def count(character_lfg, sentence):
    count_count = 0
    for character in sentence:
        if character == character_lfg:
            count_count += 1
    return count_count


sentence_person = input("whats the senetence u need counted: ")
character_person = input("what letter do u need counted: ")

print(f"you used the character {character_person} {count(character_person, sentence_person)} times")
