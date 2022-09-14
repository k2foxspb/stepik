

# объявление функции
def is_password_good(password):
    p = 0
    x = 0
    y = 0
    z = 0
    for i in range(len(password)):
        x += 1
        if password[i].isdigit():
            p += 1
        elif password[i] == password[i].upper():
            y += 1
        elif password[i] == password[i].lower():
            z += 1


    if x >= 8 and y > 0 and z > 0 and p > 0:
        return True
    else:
        return False


# вызываем функцию

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
