# D. Unnatural Language Processing
vowel = ["a", "e"]
consonant = ["b", "c", "d"]


def split_syllables(word):
    syllables = []
    curWord = ""
    isFirstVowel = True
    for i in range(len(word)):
        if i > 0:
            if word[i] in consonant and word[i - 1] in consonant:
                syllables.append(curWord)
                curWord = ""
                isFirstVowel = True
            elif word[i] in vowel and word[i - 1] in consonant:
                if isFirstVowel:
                    isFirstVowel = False
                else:
                    syllables.append(curWord[:-1])
                    curWord = curWord[-1]
        curWord += word[i]
    syllables.append(curWord)
    return ".".join(syllables)


t = int(input())
for _ in range(t):
    n = int(input())
    word = input()
    print(split_syllables(word))
