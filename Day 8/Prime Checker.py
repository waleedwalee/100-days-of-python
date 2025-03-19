def prime_chechker(number):
    is_prime = True
    for i in range(2, number):
        if i % 2 == 0:
            is_prime = False
    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input())
prime_chechker(number=n)