# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
arr=[1,2,5,6,-10,-6]

def count_positives_sum_negatives(arr):
    negatives=[]
    positives=[]
    for i in arr:
        if i >0:
            positives.append(i)
        if i <0:
            negatives.append(i)
    sumar=len(positives),sum(negatives)
    if len(arr)==0:
        print(arr)
    else:
        print(list(sumar))


count_positives_sum_negatives(arr)















