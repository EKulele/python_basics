# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

# for i in range(1,10):
#     os.mkdir("dir_"+str(i))

# for i in range(1,10):
#     os.rmdir("dir_"+str(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# for i in os.listdir("."):
#     if os.path.isdir(i)== True:
#         print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
def duplicate (filename):
		if os.path.isfile(filename):
			newfile = filename+".duplicate"
			shutil.copy(filename, newfile)
			if os.path.exists(newfile):
				print("Создан файл",newfile)
				return True
			else:
				print("Возникли проблемы")
				return False

for i in os.listdir("."):
    if i == "Less_05_easy.py":
        #newfile = i + ".duplicate"
        duplicate(i)
        print(i)

