def translation(text:str):
    vowel:list = ['a','e','i','u','o',' ']
    final_text:str = ""
    for char in text:
        if not vowel.__contains__(char):
            final_text += 'o' + char
        else:
            final_text += char
    return final_text
print(translation("this is fun"))