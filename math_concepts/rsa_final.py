import random
import math

public_key = 1
private_key = 1
n = 1
list_of_primes = []

def prime_numbers(range_value):
    numbs = [True] * range_value
    numbs[0] = [False]
    numbs[1] = [False]
    for i in range(2, range_value):
        for j in range(i * 2, range_value, i):
            numbs[j] = False

    for i in range(len(numbs)):
        if numbs[i]:
            list_of_primes.append(i)

def get_random_prime():
    random_number = list_of_primes.pop(random.randint(1, len(list_of_primes) - 1))
    return random_number

def set_keys():
    global public_key, private_key, n
    first_prime = get_random_prime()
    second_prime = get_random_prime()
    n = first_prime * second_prime
    phi = (first_prime - 1) * (second_prime - 1)

    e = 2
    while True:
        if math.gcd(e, phi) == 1:
            break

        e += 1

    d = 2
    while True:
        if (d * e) % phi == 1:
            break

        d += 1

    public_key = e
    private_key = d

def encryption(text):
    result = []
    for character in text:
        encrypted = ord(character) ** public_key % n
        result.append(encrypted)

    return result

def decryption(encrypted_text):
    result = ""
    for values in encrypted_text:
        decrypted = values ** private_key % n
        result += chr(decrypted)

    return result


prime_numbers(500)
set_keys()
message = input()
encrypted_message = encryption(message)
decrypted_message = decryption(encrypted_message)
print("Encrypted message:")
print("".join(str(x) for x in encrypted_message))
print("Decrypted message:")
print(decrypted_message)



