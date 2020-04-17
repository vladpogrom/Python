text = open('dataset_3363_3(1).txt').read().lower().strip().split() #читаем строки в список
mn = list(set(text)) #создаем копию списка без повторяющихся значений через множество
word = mn[0] #присваиваем макс значения, в качестве превого элемента списка
count_max = text.count(word)

#циклом сравниваем с макисмальным, затем если числа равны, то сравниваем строки
for i in mn:
  if text.count(i) > count_max:
    count_max = text.count(i)
    word = i
  if text.count(i) == count_max:
    if i > word:
      word = i
    else:
      word = word
print(word, count_max) #выводим
