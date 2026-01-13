
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fc(n):
    ff = factorial(n)
    result_list = []
    
    for i in range(ff, 0, -1):
        result_list.append(factorial(i))
    return ff, result_list

num = int(input('Введите натуральное число:\n'))
factorial, chain = fc(num)
print(f'Факториал числа {num} = {factorial}')
print(f'Цепочка факториалов: {chain}')        
             