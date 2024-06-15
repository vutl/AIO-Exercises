def count_chars(string):
    char_count = {}
    for char in string:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
        

string1 = "Happiness"
string2 = 'smiles'
print(count_chars(string1))
print(count_chars(string2)) 