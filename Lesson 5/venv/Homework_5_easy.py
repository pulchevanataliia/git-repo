# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
def new(name):
    path = os.path.join(name)
    try:
        os.mkdir(path)
        print("Папка " + name + " создана")
    except:
        print("Данная директория уже существует")
if __name__ == "__main__":
    for i in range(1,10):
        new("dir_" + str(i))
def dir_remove(removedir):
    decision = input("Вы уверены, что хотите удалить, выбранную директорию? (Y/N): ")
    if decision == "Y" or decision == "y":
        try:
            os.rmdir(removedir)
            print("Директория " + removedir + " успешно удалена")
        except:
            print("Путь указан неверно")
    else:
        print("Отмена")
if __name__ == "__main__":
    for j in range(1,10):
        dir_remove("dir_" + str(j))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def contains():
    current = [os.listdir()]
    print(current)
contains()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
def file_copy():
    shutil.copy(r"hw05_easy.py",r"hw05_easy_copy.py")
file_copy()