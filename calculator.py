def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def calculator(x, y, operator):
    operations = {
        '+': add,
        '-': substract,
        '*': multiply
    }

    if operator in operations:
        return operations[operator](x,y)
    else:
        return "Invalid operator"

if __name__ == "__main__":
    print("Simple Calculator")
    x = 5
    y = 4
    operator = '-'
    
    result = calculator(x,y,operator)
    print("Result: ", result)
    
