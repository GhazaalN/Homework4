def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    return "odd"


number = int(input("Enter an integer: "))
print(even_or_odd(number))
