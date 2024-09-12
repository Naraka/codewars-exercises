# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count_letter(s):
    dictionary = {}
    for caracter in s:
        dictionary[caracter] = s.count(caracter)
    return dictionary


print(count_letter('aa'))
print(count_letter("aba"))
print(count_letter('aabb'))