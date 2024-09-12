# Task
# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

# Mind the input validation.

# Example
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6
# Input validation
# If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.


# def sum_array(arr):
#     if arr==None:
#         print(0)
#     elif len(arr)>1:
#         m=min(arr)
#         n=max(arr)
#         res=(sum(arr))
#         print(res-m-n)
#     else:
#         print(0)



# array1={ 6, 2, 1, 8, 10 } 
# array2={ 1, 1, 11, 2, 3 } 
# array3=None



# sum_array(arr=array1)# 16
# sum_array(arr=array2)# 6
# sum_array(arr=array3)# 0

#-------------------------------------------------------------------------------------------------------   


def sum_array(arr):
    if not arr or len(arr) == 1:  #si no hay arr o no hay longitud en arr que sea ==1 retorna 0
        print(0)
    else:
        print(sum(arr) - min(arr) - max(arr))



array1={ 6, 2, 1, 8, 10 } 
array2={ 1, 1, 11, 2, 3 } 
array3=None



sum_array(arr=array1)# 16
sum_array(arr=array2)# 6
sum_array(arr=array3)# 0










