def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True
n=int(input())
print(isprime(n))