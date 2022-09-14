def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count == 1:
            return True
        else:
            return False


print(is_one_away('bike', 'bike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))
