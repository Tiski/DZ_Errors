def convert_to_int(value):
    try:
        result = int(value)
        print(f"Успешное преобразование: {result}")
        return result
    except ValueError:
        print("Ошибка: Невозможно преобразовать строку в целое число.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        print("Попытка преобразования завершена.")

# Проверка функции с корректной строкой
convert_to_int("123")

# Проверка функции с некорректной строкой
convert_to_int("abc")

# Проверка функции с другим типом данных
convert_to_int([1, 2, 3])
