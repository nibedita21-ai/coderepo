def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(arr):
    primes = [num for num in arr if is_prime(num)]
    return primes

array = [1, 2, 3, 4, 5, 6,7,8,9,10 ]
prime_numbers = find_primes(array)
print("Prime numbers in the array:", prime_numbers)