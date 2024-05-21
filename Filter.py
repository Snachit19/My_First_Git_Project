#It's takes same arguments as map filters the list acording to function given
#The function given as argument should be a function that returns bool as a result
def is_even(num: int)-> bool:
    return num % 2 == 0

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_2 = filter(is_even, list_1)

print(list(list_2))