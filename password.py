import random

chars = 'abcdefghijklnopqrstuvwxyz+-/*!&$#?=@<>ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
bchis = 'abcdefghijklnopqrstuvwxyz+-/*!&$#?=@<>ABCDEFGHIJKLMNOPQRSTUVWXYZ'
bsim = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
bbig = 'abcdefghijklnopqrstuvwxyz+-/*!&$#?=@<>1234567890'
bsimbig = 'abcdefghijklnopqrstuvwxyz1234567890'
bchisbig = 'abcdefghijklnopqrstuvwxyz+-/*!&$#?=@<>'
bsimchis = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
stroch = 'abcdefghijklnopqrstuvwxyz'
length = int(input('Длина пароля?'+ "\n"))

a = str(input('Использовать символы в пароле? '))
b = str(input('Использовать заглавыные буквы в пароле? '))
c = str(input('Использовать числа в пароле? '))

for n in range(1):
    password =''
    for i in range (length):
      if a == 'Да':
        if b == 'Да':
          if c == 'Да':
            password += random.choice(chars)
      if a == 'Да':
        if b == 'Да':
          if c == 'Нет':
            password += random.choice(bchis)
      if a == 'Нет':
        if b == 'Да':
          if c == 'Да':
            password += random.choice(bsim)
      if a == 'Да':
        if b == 'Нет':
          if c == 'Да':
            password += random.choice(bbig)
      if a == 'Нет':
        if b == 'Нет':
          if c == 'Да':
            password += random.choice(bsimbig)
      if a == 'Да':
        if b == 'Нет':
          if c == 'Нет':
            password += random.choice(bchisbig)
      if a == 'Нет':
        if b == 'Да':
          if c == 'Нет':
            password += random.choice(bsimchis)
      if a == 'Нет':
        if b == 'Нет':
          if c == 'Нет':
              password += random.choice(stroch)
      
print(password)