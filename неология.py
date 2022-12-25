#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#задание 1


# In[ ]:


phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'


# In[ ]:


phrase_1 = len(phrase_1)


# In[ ]:


phrase_2 = len(phrase_2)


# In[ ]:


if phrase_1 > phrase_2:
    print('Фраза 1 длиннее фразы 2')
elif  phrase_1 < phrase_2:
    print('Фраза 2 длиннее фразы 1')
else:
    print('Фразы равной длины')


# In[ ]:


#задание 2


# In[ ]:


year = 2007


# In[ ]:


import calendar
print(calendar.isleap(year))


# In[ ]:


l_year = calendar.isleap(year)


# In[ ]:


if l_year is False:
    print('Обычный год')
else:
    print('Високосный год')


# In[ ]:


#задание 3


# In[ ]:


months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
bd_day = input('Введите день: ')
bd_month = input('Введите месяц: ')

if not isinstance(bd_day, int):
    print('Вы ввели не число')
if not bd_month in months:
    print('Вы ввели несуществующий месяц')
print('Ваш знак зодиака: ')


# In[ ]:


months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

bd_day = input('Введите день: ')
bd_month = input('Введите месяц: ')

if not bd_day.isdigit():
    print('Вы ввели не число')
if not bd_month.lower() in [i.lower() for i in months]:
    print('Вы ввели несуществующий месяц')
bd_day = int(bd_day)
bd_month = bd_month.capitalize()

result = None
if (bd_month == 'Январь' and 1 <= bd_day <= 20) or (bd_month == 'Декабрь' and 22 <= bd_day <= 31):
    result = 'Козерог'
if (bd_month == 'Февраль' and 1 <= bd_day <= 18) or (bd_month == 'Январь' and 21 <= bd_day <= 31):
    result = 'Водолей'
if (bd_month == 'Март' and 1 <= bd_day <= 20) or (bd_month == 'Февраль' and 19 <= bd_day <= 29):
    result = 'Рыбы'
if (bd_month == 'Апрель' and 1 <= bd_day <= 20) or (bd_month == 'Март' and 21 <= bd_day <= 31):
    result = 'Овен'
if (bd_month == 'Май' and 1 <= bd_day <= 21) or (bd_month == 'Апрель' and 21 <= bd_day <= 30):
    result = 'Телец'
if (bd_month == 'Июнь' and 1 <= bd_day <= 21) or (bd_month == 'Май' and 22 <= bd_day <= 31):
    result = 'Близнецы'
if (bd_month == 'Июль' and 1 <= bd_day <= 22) or (bd_month == 'Июнь' and 22 <= bd_day <= 30):
    result = 'Рак'
if (bd_month == 'Август' and 1 <= bd_day <= 23) or (bd_month == 'Июль' and 23 <= bd_day <= 31):
    result = 'Лев'
if (bd_month == 'Сентябрь' and 1 <= bd_day <= 22) or (bd_month == 'Август' and 24 <= bd_day <= 31):
    result = 'Дева'
if (bd_month == 'Октябрь' and 1 <= bd_day <= 23) or (bd_month == 'Сентябрь' and 23 <= bd_day <= 30):
    result = 'Весы'
if (bd_month == 'Ноябрь' and 1 <= bd_day <= 22) or (bd_month == 'Октябрь' and 24 <= bd_day <= 31):
    result = 'Скорпион'
if (bd_month == 'Декабрь' and 1 <= bd_day <= 21) or (bd_month == 'Ноябрь' and 23 <= bd_day <= 30):
    result = 'Стрелец'
    
print('Ваш знак зодиака: ', result)


# In[ ]:


width = 3
length = 201
height = 45


box_list = [width, length, height]

if all([i <= 15 for i in box_list]):
    print('Коробка №1')
elif any([i > 200 for i in box_list]):
    print('Упаковка для лыж')
elif any([15 < i < 50 for i in box_list]):
    print('Коробка №2')
else:
    print('Коробка №3')


# In[ ]:




