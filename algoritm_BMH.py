symbols = "ете"

# Этап 1: формирование таблицы смещений

unique_elements = set()  # уникальные символы в образе
symbols_length = len(symbols)  # число символов в образе
dict_offset = {}     # словарь смещений

for i in range(symbols_length - 2, -1, -1):  # итерации с предпоследнего символа
    if symbols[i] not in unique_elements:        # если символ еще не добавлен в таблицу
        dict_offset[symbols[i]] = symbols_length - i - 1
        unique_elements.add(symbols[i])

if symbols[symbols_length - 1] not in unique_elements:     # отдельно формируем последний символ
    dict_offset[symbols[symbols_length - 1]] = symbols_length

dict_offset['*'] = symbols_length              # смещения для прочих символов

print(dict_offset)

# Этап 2: поиск образа в строке

base_string = "метеоданные"
string_length = len(base_string)

if string_length >= symbols_length:
    i = symbols_length - 1       # счетчик проверяемого символа в строке

    while i < string_length:
        base_string_number = 0
        j = 0
        flBreak = False
        for j in range(symbols_length - 1, -1, -1):
            if base_string[i - base_string_number] != symbols[j]:
                if j == symbols_length-1:
                    off = dict_offset[base_string[i]] if dict_offset.get(base_string[i], False) else dict_offset['*']  # смещение, если не равен последний символ образа
                else:
                    off = dict_offset[symbols[j]]   # смещение, если не равен не последний символ образа

                i += off    # смещение счетчика строки
                flBreak = True  # если несовпадение символа, то flBreak = True
                break

            base_string_number += 1          # смещение для сравниваемого символа в строке

        if not flBreak:          # если дошли до начала образа, значит, все его символы совпали
            print(f"образ найден по индексу {i - base_string_number + 1}")
            break
    else:
        print("образ не найден")
else:
    print("образ не найден")
