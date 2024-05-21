#Using map
#Map takes a function as one argument and takes as iterable as second argument 
def Capitalize_Ascii(word: str)-> int:
    return sum(ord(x) for x in word.capitalize())

animals = ['cat', 'dog', 'cow']

animal_output = list(map(Capitalize_Ascii, animals))

print(animal_output)

numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x ** 2, numbers)
print(list(squares))