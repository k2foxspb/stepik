def convert_to_python_case(text):
    res = (text[0].lower())

    for i in range(len(text)):
        if text[i] == text[i].lower():
            res += text[i]
        elif text[i] == text[i].upper() and text[i] != text[0]:
            res += '_' + text[i].lower()

    return res


print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))