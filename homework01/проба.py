import random

mnozh1 = (random.randint(1, 15) for _ in range(10))
mnozh2 = (random.randint(1, 15) for _ in range(10))

print(f"Первое множество: {mnozh1}")
print(f"Второе множество: {mnozh2}")
# 1:
if mnozh1 == mnozh2:
    print("Множества совпадают.")
else:
    print("Множества не совпадают.")
# 2:
if mnozh1.issubset(mnozh2):
    print("Множество 1 является подмножеством множества 2.")
elif mnozh2.issubset(mnozh1):
    print("Множество 2 является подмножеством множества 1.")
else:
    print("Ни одно из множеств не является подмножеством другого.")

# 3:
obshelem = mnozh1.intersection(mnozh2)
if obshelem:
    print(f"Общие элементы:", obshelem)
# 4:
else:
    print("Общих элементов нет.")
    obedin = mnozh1.union(mnozh2)
    print(f"Объединение множеств:", obedin)