# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"




def reverse_words(text):
    nose=[]
    for i in text.split(" "):              
        nose.append(i[::-1])        #[::-1] devuelve un str ordenador al reves
    print(" ".join(nose))
        


#-------------------------------------------------------------------------------------------------------   

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))









text="This is an example!"

reverse_words(text)