import requests


def open_new_link(filename):
    link = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + filename, 'r')
    print(link.text)
    finish = link.text
    return finish

link_for = open("dataset_3378_3.txt", 'r')
line_for = link_for.readline().strip()
r_for = requests.get(line_for)
filename = r_for.text

if filename[0:2] != "We":
    open_new_link(filename)
else:
    print(filename)




#1)Создаем функцию, куда будем принимать текст!!! из файла(если первые два символа  [0:2] не We)
# и приклеивать к концу ссылки данной в задании. Если находим We печатаем текст.

#2)Читаем из файла текст- ссылку, отрезая всё лишнее.

#3)Читаем с ссылки текст, как текст!!!(.txt) и закидываем в функцию.

#PS: Если что-то не получается, то ставим print(), где только можно, с описанием где находитесь и актуальной переменной.
# И так вы найдёте свою ошибку.

#Я добавил ещё счётчик переходов, который также нужно закидывать в функцию вторым параметром. И показывал сами переходы.
