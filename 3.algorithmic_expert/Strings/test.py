# maximumCharacterFrequencies , countCharacterFrequencies

words = ["this", "that", "did", "deed", "them!", "a"]

def minimumCharactersForWords(words):
    maximumCharacterFrequencies = {}
    for word in words:
        characterFrequencies = countCharacterFrequencies
    # return countCharacterFrequencies

def countCharacterFrequencies(string):
    characterFrequencies = {}
    for character in string:
        if character not in characterFrequencies:
            characterFrequencies[character] += 0
        characterFrequencies[character] += 1
    return countCharacterFrequencies  

print(minimumCharactersForWords(words))