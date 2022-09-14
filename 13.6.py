def is_pangram(text):
    count = 0
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(x)):
        if x[i] in text.lower():
            count += 1
    if count == len(x):
        return True
    else:
        return False


print(is_pangram('Jackdaws love my big sphinx of quartz'))