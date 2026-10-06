def is_prime(num):
    if num < 2:
        return False

    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 1

    return True


number = int(input("Enter an integer: "))
print(is_prime(number))
