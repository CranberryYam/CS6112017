def is_prime(n):
    x = 2;
    divisorFound = False
    while x < n:
        if n%x==0:
            divisorFound = True
        x = x+1
    return not divisorFound


print(is_prime(2))
print(is_prime(21))


def is_prime_by_form(n):
    if n==1 or n==2 or n==3:
        return True
    elif n%6==1 or n%6==5:
        return True
    return False

print(is_prime_by_form(2))
print(is_prime_by_form(23))


def print_primes_to(n):
    x = 1
    while x<=n:
        if is_prime_by_form(x):
            print('prime: '+str(x))
        x=x+1


print_primes_to(13)

def print_primes_of_first(n):
    primes = 0
    x = 1
    while primes<=n:
        if is_prime_by_form(x):
            primes=primes+1
            print('the '+str(primes)+'th prime: '+str(x))
        x=x+1

print_primes_of_first(5)





