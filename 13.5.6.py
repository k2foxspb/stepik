def is_palindrome(text):
    count = []
    for i in range(len(text)):
        if text[i].isalpha():
            y = text[i].lower()
            count.append(y)
    if count == count[::-1]:
        return True
    else:
        return False


txt = 'А роза упала на лапу Азор.'
print(is_palindrome(txt))
