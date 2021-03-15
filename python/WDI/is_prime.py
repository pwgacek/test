
def is_prime(num):
    if num == 1 or num == 0:  return False
    if num == 2 or num == 3: return True

    if num % 2 == 0 or num % 3 == 0 : return False

    i = 5
    while i*i <= num :
        if num % i == 0 : return False
        i+=2
        if num % i == 0 : return False
        i+=4
    return True

print(is_prime(423423))
 