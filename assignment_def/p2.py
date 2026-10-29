def square_deco(func):
    def wrapper(x,y):
        result = func(x*x,y*y)
        return result

    return wrapper

@square_deco
def add(a,b):
    return a+b

result = add(4,2)
print(result)