#Читаем строку из файла, затем создаем цикл
text = open('dataset_3363_2.txt').read().strip().split()
a = str(text)
key = ''
x = ''
m = ''
s = ''
for i in range(len(a)):
  x = ''
  if a[i].isalpha() == True:
    key = a[i]
    if '0' <= a[i+1] <= '9':
        x = x + a[i+1]
    if '0' <= a[i+2] <= '9':
        x = x + a[i+1]
        print(x) 
        
 p = int(x)
 m = p * key
 s.append(m)
 print(s)
    
#Затем идем циклом по строке, записываем символ в переменную (key) и пока обьект в границах от 0 до 9, то добавляем цифры к переменой (x)
#Затем в новую строку(s) через append дописываем Количество(x) * Букву(key)
#Еще как вариант можно накапливать все цифры в переменную строчного типа, пока не встретим букву. потом приводим эту строку к int
#Выводим

#Поиск чисел в строке через while
s = input()
l = len(s)
integ = []
i = 0
while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))

print(integ)

#Поиск чисел в строке через if
line = input()
num_out_of_line = []
str_num = ""
 
for i in range(len(line)):
    if line[i] in "0123456789":
        str_num += line[i]
        try:
            if line[i+1] not in "0123456789":
                num_out_of_line.append(str_num)
                str_num = ""
        except:
            num_out_of_line.append(str_num)
 
print(list(map(int, num_out_of_line)))

#для справки
S.isdigit() #Состоит ли строка из цифр
S.isalpha() #Состоит ли строка из букв
