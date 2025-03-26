# Задание 1
# Способ 1
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
result = dict_1.copy()
result.update(dict_2)
print(result)
# Способ 2
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
result = dict_1 | dict_2
print(result)
#Задание 2
def max_dict(*dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                if value > result[key]:
                    result[key] = value
            else:
                result[key] = value
    return result

def sum_dict(*dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result

# Исходные словари
dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}

# Тестирование функций
print(max_dict(dict_1, dict_2))
print(sum_dict(dict_1, dict_4, dict_3))
print(max_dict(dict_1, dict_2, dict_3, dict_4))
print(sum_dict(dict_1, dict_2, dict_3, dict_4))