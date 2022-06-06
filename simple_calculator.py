x = int(input('x = '))
y = int(input('y = '))
op = input('op = ')
def arithmetics(x,y,op):
    if op == "+":
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
print(arithmetics(x,y,op))
