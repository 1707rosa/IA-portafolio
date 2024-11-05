def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def countPrime(list):
    counter = 0
    for number in list:
        if isPrime(number):
            counter+= 1
    return counter


numbers = [2, 8, 10, 15, 13, 29, 50, 149]
cantidadPrimos = countPrime(numbers)
print("Cantidad de números primos:", cantidadPrimos)
