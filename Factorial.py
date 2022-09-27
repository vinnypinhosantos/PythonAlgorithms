import timeit


# Na função iterativa, percorremos do número 2 até o último valor 1 a 1.
def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


# Uma função recursiva chama a si mesma na sua execução
def recursive_factorial(n):
    if n == 1:
        return n
    else:
        # Nesse caso, ela chama a si mesma e guarda cada execução em uma pilha.
        # O último a entrar (no caso, o 1) é o primeiro a terminar a sua execução
        temp = recursive_factorial(n-1)
        return temp * n


print(iterative_factorial(5))
print(f"Tempo do Fatorial Iterativo: {timeit.timeit('iterative_factorial(5)', 'from __main__ import iterative_factorial', number=1000)}")

print(recursive_factorial(5))
print(f"Tempo do Fatorial Recursivo: {timeit.timeit('recursive_factorial(5)', 'from __main__ import recursive_factorial', number=1000)}")
