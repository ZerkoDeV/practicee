def find_longest_word(words:list):
    longest_word:str = words[0]
    for word in words:
        if len(word) > len(longes_word):
            longest_word = word
    return longest_word
print(find_longest_word(["mikhael","ini apa apa","suka ayam"]))