# Ask a mathematician: "What proportion of natural numbers contain at least one digit 9 somewhere in their decimal representation?"

# You might get the answer "Almost all of them", or "100%".

# Clearly though, not all whole numbers contain a 9.

# In this kata we ask the question: "How many Integers in the range [0..n] contain at least one 9 in their decimal representation?"

# In other words, write the function:

# nines :: Integer -> Integer
# Where, for example:

# nines 1  = 0
# nines 10 = 1     -- 9
# nines 90 = 10    -- 9, 19, 29, 39, 49, 59, 69, 79, 89, 90
# When designing your solution keep in mind that your function will be tested against some large numbers (up to 10^38)




def nines(n):
    count=0
    for x in range(n+1):
        for i in str(x):
            if i == "9":
                count+=1
                break

    
    print(count)











nines(100)



