#Скачайте файл по ссылке
#Прочитайте его и подсчитайте количество слов в тексте

with open('referat.txt', 'r', encoding='utf-8') as referat:
    text = referat.read()
    print(text)