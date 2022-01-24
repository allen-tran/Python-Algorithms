def detectCapitalUse(word):
    if word == word.upper():
        return True
    elif word == word.lower():
        return True
    elif word[0].isupper():
        for i in range(1, len(word)):
            if word[i].isupper():
                return False
            
        return True
    return False