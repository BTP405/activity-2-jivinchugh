def getPrimeNumbers(n):
    return [number for number in range(2, n + 1) if is_prime(number)]

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True
    
result = getPrimeNumbers(10)
print("Prime numbers", result)