#Задание 1
data = (([1, 2], ['012', 'abc']), [4, 3])
result = data[0][1][1][2]
print(result)

#Задание 2
data = (10, 3.14, 2 + 5j, ('hello',), (), [])
print(data[3][0])

#Задание 3
matreshka = (
    1,
    (
        2.5,
        (
            3 + 4j,
            (
                'final string',
                ()
            )
        )
    )
)

print(matreshka[1][1][1][0])

#Задание 4
data = (1, 2, 3, 4, 5)

#Способ 1: Положительные индексы
print("Положительные индексы:")
print(data[0])
print(data[2])
print(data[0:3])

#Способ 2: Отрицательные индексы
print("\nОтрицательные индексы:")
print(data[-5])
print(data[-3])
print(data[-5:-2])

#Задание 5
data = ((1, 2, ('Ok!', 3)), ('tuple', 4), 5)
print(data[0][2][0])

#Задание 6
data = (3, 's', 1, 5, 's')
print(len(data))
print(data.count('s'))
print(data.index('s'))

#Задание 7
data = (['кит', 1, 3], 5)

data[0][0] = 'кот'
data[0].remove(1)
data[0][1] **= 2

try:
    data[1] *= 2
except TypeError as e:
    print("Ошибка:", e)

print("После изменений:", data)

#Задание 8
def tpl_sort(tpl):
    if all(isinstance(x, int) for x in tpl):
        return tuple(sorted(tpl))
    return tpl

#Задание 9
def slicer(tpl, element):
    if tpl.count(element) == 0:
        return ()
    elif tpl.count(element) == 1:
        start = tpl.index(element)
        return tpl[start:]
    else:
        start = tpl.index(element)
        end = tpl.index(element, start + 1)
        return tpl[start:end + 1]

#Задание 10
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'grade', 'city'])

students = (
    Student('Данил', 19, 4.8, 'Алейск'),
    Student('Иван', 20, 3.9, 'СПб'),
    Student('Мария', 18, 5.0, 'Казань'),
    Student('Петр', 21, 4.2, 'Новосибирск'),
    Student('Елена', 22, 4.5, 'Екатеринбург'),
    Student('Сергей', 20, 3.7, 'Томск'),
    Student('Ольга', 19, 4.9, 'Воронеж'),
)

def good_students(students):
    avg_grade = sum(s.grade for s in students) / len(students)
    good = [s.name for s in students if s.grade >= avg_grade]
    print(f"Ученики {', '.join(good)} в этом семестре хорошо учатся!")

good_students(students)