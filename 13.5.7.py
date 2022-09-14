def is_valid_password(password):
    res = password.split(':')
    if len(res) > 3:
        return False
    count = 0
    count_true = 0
    x = res[0]
    y = int(res[1])
    z = int(res[2])
    if x == x[::-1]:
        count += 1
    for i in range(1, y + 1):
        if y % i == 0:
            count_true += 1
    if count_true == 2:
        count += 1
    if z % 2 == 0:
        count += 1
    if count == 3:
        return True
    else:
        return False


print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
