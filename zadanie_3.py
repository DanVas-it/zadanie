def set_gen(numbers):
    result = set()
    count = {}

    for num in numbers:
        if num in count:
            count[num] += 1
            repeated_num = str(num) * count[num]
            result.add(repeated_num)
        else:
            count[num] = 1
            result.add(num)

    return result
# Тесты
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(set_gen(list_1))
print(set_gen(list_2))
print(set_gen(list_3))