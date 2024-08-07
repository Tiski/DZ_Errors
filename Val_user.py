def validate_user_input(data):
    if not isinstance(data, dict):
        raise TypeError("Данные должны быть словарем.")
    
    if 'name' not in data:
        raise ValueError("Ключ 'name' отсутствует в данных.")
    
    if not isinstance(data['name'], str):
        raise ValueError("Значение ключа 'name' должно быть строкой.")
    
    if 'age' not in data:
        raise ValueError("Ключ 'age' отсутствует в данных.")
    
    if not (isinstance(data['age'], int) and data['age'] > 0):
        raise ValueError("Значение ключа 'age' должно быть положительным числом.")

# Проверка функции с корректными данными
try:
    validate_user_input({"name": "Alice", "age": 30})
    print("Данные пользователя корректны.")
except Exception as e:
    print(f"Ошибка: {e}")

# Проверка функции с отсутствующим ключом name
try:
    validate_user_input({"age": 30})
except Exception as e:
    print(f"Ошибка: {e}")

# Проверка функции с некорректным значением для age
try:
    validate_user_input({"name": "Alice", "age": "тридцать"})
except Exception as e:
    print(f"Ошибка: {e}")

# Проверка функции с отрицательным значением для age
try:
    validate_user_input({"name": "Alice", "age": -5})
except Exception as e:
    print(f"Ошибка: {e}")

# Проверка функции с некорректным типом входных данных
try:
    validate_user_input("Некорректные данные")
except Exception as e:
    print(f"Ошибка: {e}")
