from dict_of_translation import dict_of_translation


def palladium_transliterate(text):
    rules = dict_of_translation
    if not rules:
        raise ValueError("Словарь транслитерации пуст.")

    max_key_length = max(len(key) for key in rules.keys()) if rules else 0
    lower_text = text.lower()
    n = len(lower_text)

    # Создание массива для динамического программирования
    dp = [False] * (n + 1)
    dp[n] = True  # Пустая строка в конце

    for i in range(n - 1, -1, -1):
        for length in range(1, max_key_length + 1):
            if i + length > n:
                continue
            substr = lower_text[i:i + length]
            if substr in rules and dp[i + length]:
                dp[i] = True
                break  # Достаточно одного совпадения

    result = []
    not_translated = []
    i = 0

    while i < n:
        found = False
        # Проверяем возможные длины от максимальной до 1
        max_possible_length = min(max_key_length, n - i)
        for length in range(max_possible_length, 0, -1):
            substr = lower_text[i:i + length]
            if substr in rules and dp[i + length]:
                result.append(rules[substr])
                i += length
                found = True
                break
        if not found:
            # Проверяем одиночный символ как последний шанс
            if lower_text[i] in rules:
                result.append(rules[lower_text[i]])
                i += 1
                found = True
            else:
                not_translated.append(lower_text[i])
                i += 1

        if not found and not_translated:
            break  # Не удалось перевести текущий символ

    if not_translated:
        raise ValueError(f"ОШИБКА: Нет перевода для символов {''.join(not_translated)}")

    transliterated = ''.join(result)
    if text and text[0].isupper():
        transliterated = transliterated[0].upper() + transliterated[1:].lower()

    return transliterated


if __name__ == "__main__":

    text = "YINGUO"

    print(palladium_transliterate(text))