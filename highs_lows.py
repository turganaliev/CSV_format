import csv

#Представление дат на диаграмме
from datetime import datetime

#Нанесение данных на диаграмму
from matplotlib import pyplot as plt

#Разбор заголовка файлов CSV
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

#Печать заголовков и их позиций
#for index, column_header in enumerate(header_row):
    #print(index, column_header)

#Извлечение и чтение данных
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    #print(highs)

# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5, linewidth=1)
plt.plot(dates, lows, c='blue', alpha=0.5, linewidth=1)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Форматирование диаграммы
title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
plt.title(title, fontsize=16)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
