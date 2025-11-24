def generate_binary_strings(n):
    """
    Рекурсивно генерирует все бинарные строки длины n

    Args:
        n: длина бинарных строк

    Returns:
        Список всех возможных бинарных строк длины n
    """
    # Базовый случай: строка длины 0
    if n == 0:
        return [""]

    # Базовый случай: строка длины 1
    if n == 1:
        return ["0", "1"]

    # Рекурсивный случай:
    # Генерируем все строки длины n-1 и добавляем к каждой "0" и "1"
    shorter_strings = generate_binary_strings(n - 1)

    result = []
    for string in shorter_strings:
        result.append(string + "0")
        result.append(string + "1")

    return result


# Примеры использования
print("Бинарные строки длины 2:")
print(generate_binary_strings(2))
print("\nБинарные строки длины 3:")
print(generate_binary_strings(3))
