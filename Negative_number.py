class NegativeNumberError(Exception):
    def __init__(self, value, message="Число не должно быть отрицательным."):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} Получено: {self.value}"

def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    else:
        print(f"Число {number} является положительным.")

# Проверка функции с отрицательным числом
try:
    check_positive_number(-10)
except NegativeNumberError as e:
    print(e)

# Проверка функции с положительным числом
try:
    check_positive_number(10)
except NegativeNumberError as e:
    print(e)
