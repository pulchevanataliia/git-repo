# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    if n<1 or n>m :
        return []
    fib_list = []
    fib1 = 0
    fib2 = 1
    fib = 1
    i=2
    if n ==1:
        fib_list.append(1)
    while i <= m:
        if i >= n:
            fib_list.append(fib)
        fib1 = fib2
        fib2 = fib
        fib = fib1+fib2
        i += 1
    return fib_list

print(fibonacci(5,10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
        start = 0
        end = len(origin_list)-1
        while end > start:
            current = start
            while current < end:
                if origin_list[current] > origin_list[current+1]:
                    temp = origin_list[current]
                    origin_list[current] = origin_list[current+1]
                    origin_list[current+1] = temp
                current = current +1
            end -=1

        return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
print(sort_to_max([2]))