from dict_of_translation import dict_of_translation


def palladium_transliterate(text):
    rules = dict_of_translation
    
    max_length = max(len(key) for key in rules.keys())
    
    lower_text = text.lower()
    result = []
    not_translated = []
    i = 0
    n = len(lower_text)
    
    while i < n:
        found = False
        for l in range(max_length, 0, -1):
            if i + l > n:
                continue  
            
            substr = lower_text[i:i+l]
            if substr in rules:
                result.append(rules[substr])
                i += l
                found = True
                break
        
        if not found:
            not_translated.append(lower_text[i])
            i += 1
    
    transliterated = ''.join(result)
    if text and text[0].isupper():
        transliterated = transliterated[0].upper() + transliterated[1:]
    
    if len(not_translated) > 0:
        raise ValueError(f"ОШИБКА, НЕТ ПОДХОДЯЩЕГО ПЕРЕВОДА ДЛЯ {''.join(not_translated)}")

    return transliterated
