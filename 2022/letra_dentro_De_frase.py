# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False







def scramble(s1, s2):


    s1=list(s1)
    s2=list(s2)

    nose=[]

    for i in range(len(s2)):
        if s2[i] in s1:
            nose.append(True)
        else:
            nose.append(False)
    
    print(all(nose))


#--------------------------------------------------------------------------- 







def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c): #si la cuenta de s1 contando con las letras de s2, es menor que la cuenta de las letras de s2 
            return False
    return True
    
scramble('u', 'a')
scramble('katas', 'steak')
scramble('scriptjava', 'javascript')




