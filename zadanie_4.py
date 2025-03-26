def superset(set_a, set_b):
    if set_a == set_b:
        print("Множества равны")
    elif set_a.issuperset(set_b) and set_a != set_b:
        print(f"Объект {set_a} является чистым супермножеством")
    elif set_b.issuperset(set_a) and set_b != set_a:
        print(f"Объект {set_b} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")


# Тесты
set_1 = {1, 8, 3, 5}
set_2 = {3, 5}
set_3 = {5, 3, 8, 1}
set_4 = {90, 100}

superset(set_1, set_2)
superset(set_1, set_3)
superset(set_2, set_3)
superset(set_4, set_2)