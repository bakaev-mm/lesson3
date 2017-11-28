#Напечатайте в консоль даты: вчера, сегодня, месяц назад
#Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import date, timedelta, time, datetime

dt = date.today()
delta = timedelta(days = 1)

print('Сегодня {}'.format(dt))
yesterday = dt - delta
print('Вчера {}'.format(yesterday))
last_week = dt - delta * 7
print('Неделя назад {}'.format(last_week))
last_month = dt.replace(month=dt.month - 1)
print('Месяц назад {}'.format(last_month))
