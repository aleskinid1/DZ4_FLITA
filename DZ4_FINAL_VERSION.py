def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr

# Чтение
with open('read.txt', 'r') as file:
    numbers = [int(num) for num in file.read().split()]

# Сортировка
sorted_numbers = shell_sort(numbers)

# Запись
with open('output.txt', 'w') as file:
    file.write(' '.join(str(number) for number in sorted_numbers))

print("Сортировка завершена. Результат записан в файл 'output.txt'.")
