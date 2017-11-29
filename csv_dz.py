import csv
list_answer = [{'привет': 'И тебе привет!', 'как дела': 'Лучше всех', 'пока': 'Увидимся'}]

with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['привет', 'как дела', 'пока']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for get_answer in list_answer:
        writer.writerow(get_answer)