def basic_calculations(a, b, operator):
    if operator == 'multiply':
        return a * b
    if operator == 'divide':
        return a // b
    if operator == 'add':
        return a + b
    if operator == 'subtract':
        return a - b


operator = input()
a = int(input())
b = int(input())

print(basic_calculations(a, b, operator))
