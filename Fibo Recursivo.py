def fibo(n):
    n = int(n)
    suma = 0
    if (n >= 2):
        suma = fibo(n - 1) + fibo(n - 2)
    elif (n != 0):
        suma = 1
    return suma


numero = input("Introduce un numero: ")

##print(numero)
print(fibo(numero))
