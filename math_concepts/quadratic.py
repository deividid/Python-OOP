from math import sqrt

def factorial(n):
    result = n
    for i in range(n - 1, 1, -1):
        result = result * i
    return result


def encode(text):
    result = ""
    count = 0
    previous_letter = ""
    letter_possition = 0
    for letter in text:
        letter_possition += 1


        if letter == previous_letter:
            count += 1
        else:
            if previous_letter == "":
                previous_letter = letter
                count += 1
            else:
                if count > 1:
                    result += (previous_letter + str(count))
                else:
                    result += previous_letter

                previous_letter = letter
                count = 1

        if letter_possition == len(text):
            result += (previous_letter + str(count))
    return result

def decode(text):
    possition_count = 0
    number = 0
    letter = ""
    result = ""
    for characters in text:
        possition_count += 1
        try:
            number = int(characters)
            if possition_count == len(text):
                result += number * letter

        except:
            if letter == "":
                letter = characters
            else:
                if number == 0:
                    result += letter

                else:
                    result += number * letter

                number = 0
                letter = characters

    return result

assert encode("AABCCCDEEEE") == "A2BC3DE4"
assert decode("A2BC3DE4") == "AABCCCDEEEE"

