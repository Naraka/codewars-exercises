def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []

    for number in range(a, b + 1):
        sumatory = 0
        for n in range(len(str(number))):
            sumatory += int(str(number)[n])**(n+1)
            if sumatory == number:
                result.append(number)
    return result




print(sum_dig_pow(1, 100)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
print(sum_dig_pow(10, 89)) #[89]
print(sum_dig_pow(89, 135)) #[89, 135]
print(sum_dig_pow(1, 10)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]