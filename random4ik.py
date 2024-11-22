import random

# 1
print('Задание 1')
for i in range(10):
    print(random.randint(1, 10))

# 2
print('Задание 2')
for i in range(10):
    print(random.randint(0, 1))

# 3
print('Задание 3')
for i in range(10):
    print(round(random.uniform(-5, 5), 3))

# 4
# print('Задание 4')
# for i in range(20):
#     random_chislo = (random.uniform(-100,100))
#     print(sum(random_chislo))

# 5
print('Задание 5')
a = 'feinioq24i45knki  jaiohgigoi 4rhasggasohsoi 5 ijaoi;g'.replace(' ', '')
print(a[random.randint(0, len(a))])
arr = list(a)
print(a)

# 6
print('Задание 6')
osnova = 'Всем привет меня зовут Егор я увлекаюсь стант-райдингом и футболом'
main = osnova.split()
vibor = random.choice(main)
print(osnova)
print(vibor)

# 7
print('Задание 7')
print(chr(random.randint(97,122)))

# 8
print('Задание 8')
for line in range(20):
    print(chr(random.randint(65,90)))

# 9
print('Задание 9')
for k in range(15):
    simvoli = chr(random.randint(33,47))
    print(simvoli)
