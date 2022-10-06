# Made by Marcelinne
# Reto 1: Fibonacci Sequence
# N terminos de Serie de Fibonacci
def fibonacci(nterms):
    n1, n2 = 0, 1
    count = 0
    fibonacci_list = [] 
    print("Fibonacci sequence:")
    while count < nterms:
       fibonacci_list.append(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
    return fibonacci_list
#N esimo termino de la serie de Fibonacci
def nEsimoTerm(n_esimo, fibonacci_list):
    print(fibonacci_list[n_esimo]) 
# Suma de los terminos de la serie de Fibonacci
def sumFibonacciTerms(fibonacci_list):
    print(sum(fibonacci_list))

nterms = int(input("Cuantos Terminos tendra la Serie? "))
fibonacci_list=fibonacci(nterms)
print(fibonacci_list)
n_esimo = int(input("Que termino de la serie desea ver? "))
nEsimoTerm(n_esimo, fibonacci_list)
print("La suma de los terminos de la serie es: ")
sumFibonacciTerms(fibonacci_list)  

