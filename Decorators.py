def sum_print(func):
    def wrapper(*args,**kwargs):
        print("using decorator")
        return func(*args,**kwargs)
    return wrapper

@sum_print
def sum(a: float,b: float)-> float:
    return a + b

@sum_print
def mul(a: float,b: float)-> float:
    return a * b

x = sum_print(sum)(10,20)
print(x)

y = sum_print(mul)(10,20)
print(y)