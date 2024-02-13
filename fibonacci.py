numero = int(input("Digite um número inteiro para descobrir se ele pertence a sequência de Fibonacci: "))

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

if is_fibonacci(numero):
    print(f'{numero} pertence à sequência de Fibonacci.')
else:
    print(f'{numero} não pertence à sequência de Fibonacci.')