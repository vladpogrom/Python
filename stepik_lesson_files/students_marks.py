text = open('dataset_3363_4.txt', 'r', encoding='utf-8').read().split('\n')
x = 0
sum_1 = 0
sum_2 = 0
sum_3 = 0
for i in text:
  c = str(i).split(';')
  av_sum = (int(c[1]) + int(c[2]) + int(c[3])) / 3
  f = open('answer.txt', 'a')
  f.write(str(av_sum) + '\n')
  x +=1
  sum_1 += int(c[1])
  sum_2 += int(c[2])
  sum_3 += int(c[3])
sum_1 = sum_1 / x
sum_2 = sum_2 / x
sum_3 = sum_3 / x
f = open('answer.txt', 'a')
f.write(str(sum_1) + ' ')
f = open('answer.txt', 'a')
f.write(str(sum_2) + ' ')
f = open('answer.txt', 'a')
f.write(str(sum_3) + ' ')
print(sum_3)
