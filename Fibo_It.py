def fibo(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
    
numero = input("Introduce un numero: ")

##print(numero)
print(fibo(numero))