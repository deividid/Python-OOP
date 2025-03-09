
class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return cls(int(value))
        else:
            return "value is not a float"

    @classmethod
    def from_roman(cls, numeral: str):
        roman = {"I": 1,"V": 5, "X": 10, "L": 50, "C": 100, "D": 500,"M": 1000}
        result = 0
        for i in range(len(numeral)):
            if numeral != 0:
                if roman[numeral[i]] < roman[numeral[i - 1]]:
                    result -= roman[numeral[i]]

                else:
                    result += roman[numeral[i]]
            else:
                result += roman[numeral[i]]

        return cls(result)

    @classmethod
    def from_string(cls, number):
        if isinstance(number, str) and number.isdigit():
            return cls(int(number))
        else:
            return "wrong type"

first_num = Integer(10)

print(first_num.value)

second_num = Integer.from_roman("IV")

print(second_num.value)

print(Integer.from_float("2.6"))

print(Integer.from_string(2.6))
