# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""








def order(sentence):
    sentence=str(sentence)
    sentence=sentence.split(" ")

    frase=[]
    numero=[]
    for i in range(len(sentence)):

        for a in sentence[i]:
            if a in "1,2,3,4,5,6,7,8,9":
                frase.append(sentence[i])
                numero.append(a)
    
    sentence=list(zip(frase,numero))

    def take_number(elem):
        return elem[-1]
    sentence=sorted(sentence,key=take_number)


    result=[]
    for x in sentence:
        result.append(x[0])
        


    print(" ".join(result))

#--------------------------------------------------------------------------- 
#--------------------------------------------------------------------------- 

    

def order(sentence):
    if not sentence:
        return ""
    result = []    #the list that will eventually become our setence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
  
    print(" ".join(result))








order("is2 Thi1s T4est 3a")
order("4of Fo1r pe6ople g3ood th5e the2")
order("")