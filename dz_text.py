#Скачайте файл по ссылке
#Прочитайте его и подсчитайте количество слов в тексте

#Решение строкой
with open('referat.txt', 'r', encoding='utf-8') as referat:
    count_word_sum = 0 
    for line in referat:
        line = line.replace('\n', '')
        count_word = len(line.split(' '))
        count_word_sum += count_word 
    print('Это решение сделано с циклом for. Ответ = {}'.format(count_word_sum))

#Решение текстом 
with open('referat.txt', 'r', encoding='utf-8') as referat:
    print('Это решение с целым текстом. Ответ = {}'.format(len(referat.read().split(' '))))