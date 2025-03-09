
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
        if (public * answer) % totient  == 1:
            return answer
        answer += 1
def encrypt(value, public, n):
    return (value ** public) % n

def decrypt(encrypted_value, private, n):
    return (encrypted_value ** private) % n


prime_number_1 = 37
prime_number_2 = 13

n = prime_number_1 * prime_number_2
t = (prime_number_1 - 1) * (prime_number_2 - 1)

e = get_prime(3, t)

d = get_private(e, t)
# Note: number cannot be bigger than n (481)
encryption_number = int(input())

encrypted = encrypt(encryption_number, e, n)
print(encrypted)

decrypted = decrypt(encrypted, d, n)
print(decrypted)





