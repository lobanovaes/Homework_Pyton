# #5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# # Пример:
# # для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))

def get_fibonacci(num):
    if num == 0:
        fibonacci = [0]   
        return fibonacci
    fibonacci = [0, 1]    
    for i in range(0, num-1):
        fib1 = fibonacci[i]    
        fib2 = fibonacci[i+1]    
        fib = fib1 + fib2
        fibonacci.append(fib)    
    return fibonacci

def get_negafibonacci(fibonacci): 
    negafibonacci = []       
    n = 0
    for i in fibonacci:
        negafib = ((-1)**(n+1))*i
        negafibonacci.append(negafib)
        n+=1
    negafibonacci.reverse()  
    return negafibonacci

fibonacci = get_fibonacci(int(input('введите число: ')))
negafibonacci = get_negafibonacci(fibonacci)

print(negafibonacci[:-1]+fibonacci)