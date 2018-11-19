#Задача1

d = {'яблоко': 1, 'банан': 2, 'киви': 3, 'арбуз': 4}
d = sorted(d.items(), key=lambda x: x[-1])
for key, value in d:
    print('{0:>10} {1:<2}'.format(key, value))

#Задача2
x = [1, 2, 3, 4]
y = [1, 222, 4, 333]
result = list(set(x) - set(y))
print(result)

#Задача3
x = [1, 2, 6, 5]
y = []
for i in x:
    if i % 2 == 0:
        y.append(i / 4)
    else:
        y.append(i * 2)
    i += 1
print(y)