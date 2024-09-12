"""

Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

"""
def split_string(s):
    if len(s) %2 != 0:
        s = s + "_"
    array = []
    for i in range(0,len(s),2):
        array.append(s[i:i+2])
    return array

s = "absdfas"
print(split_string(s))
