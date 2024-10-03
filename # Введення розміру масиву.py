# Введення розміру масиву
n = int(input("Введіть розмір масиву: "))

# Створення та заповнення масиву
arr = []
for i in range(n):
    element = int(input(f"Введіть елемент {i + 1}: "))
    arr.append(element)

# Обчислення суми елементів з парними індексами
sum_even_indices = sum(arr[::2])

# Виведення результатів
print("Введений масив:", arr)
print("Сума елементів з парними індексами:", sum_even_indices)