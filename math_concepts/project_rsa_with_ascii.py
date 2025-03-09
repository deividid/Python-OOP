import random

list_of_primes = []

def get_primes_list():

    numbs = [True] * 100
    numbs[0] = False
    numbs[1] = False
    for i in range(2, 100):
        for j in range(2 * i, 100, i):
            numbs[j] = False

    for i in range(len(numbs)):
        if numbs[i] == True:
            list_of_primes.append(i)

def get_random_prime():
    random_position = random.randint(0, len(list_of_primes) - 1)

    return list_of_primes.pop(random_position)




def get_prime(x, y):
    while True:
        prime = True
        for i in range(2, x):
            if x % i == 0:
                prime = False

        if prime == True and y % x != 0:
            return x

        x = x + 1

def get_private(public, totient):
    answer = 1
    while True:
        if (public * answer) % totient == 1:
            return answer
        answer += 1

def encrypt(value, public, n):
    return (value ** public) % n

def decrypt(encrypted_value, private, n):
    return (encrypted_value ** private) % n

def text_encode(text, public, n):
    result = []
    for letters in text:
        result.append(encrypt(ord(letters), public, n))

    return result

def decode(encrypted_text, private, n):
    result = []
    for numbs in encrypted_text:
        result.append(chr(decrypt(numbs, private, n)))

    return ''.join(result)


get_primes_list()
first_prime = get_random_prime()
second_prime= get_random_prime()
n = first_prime * second_prime
t = (first_prime - 1) * (second_prime - 1)

public_key = get_prime(3, t)
private_key = get_private(public_key, t)

message = input()

encrypted_message = text_encode(message, public_key, n)
print(''.join([str(x) for x in encrypted_message]))
print(decode(encrypted_message, private_key, n))


