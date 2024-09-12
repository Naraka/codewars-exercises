# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.






def maxSequence(arr):
    maxl = 0
    maxg = 0
    for n in arr:
        maxl = max(0, maxl + n) #para la variable maxl hacemos el maximo como minimo 0 de la variable en si mas el recorrido en el argumento
        
        maxg = max(maxg,maxl) #el maxg va comparando y guardando el maximo numero que compara en maxg
    print(maxg)
 





# 0-2=0     
# 0+1=1
# 1-3=0
# 0+4=4
# 4-1=3
# 3+2=5                #subsecuencia del for, maxl
# 5+1=6
# 6-5=1
# 1+4=5






arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4] #subsecuencia = si la suma maxima entre uno y otro da 0 o negativo no lo suma ni resta

maxSequence(arr)