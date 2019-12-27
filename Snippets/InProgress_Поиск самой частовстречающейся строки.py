```
Читаем строки в одну строку(str_in), приводим это к множеству (mn)
Считываем первое значение множества = (word) и считаем count = (count_max)
Затем циклом записываем значение из множества в переменную(x[i]) и считаем str_in.count(x)
Если x[i] > count_max, то count_max = x[i], word = x
Если x[i] = count_max, то 
  Если x > word, то wor1 = x, иначе continiue
В конце выводим print(word, count_max)

```

#чтение нескольких строк
l=inf.read().split() 

#чтение нескольких строк в одну без пробелов
text = open("text.txt", 'r')
s = text.read().replace('\n', ' ').lower().split()
text.close()

#чтение нескольких строк в одну без пробелов
text = open('dataset_3363_3.txt').read().lower().strip().split()

#прошлый код, считает для каждого слова количество его вхождений
st = input().lower().split()
mn = set(st)
for i in mn:
    print(i, st.count(i))
