verse = input('Введите стих: ')
phrases = verse.split()
syllables_count = []
for phrase in phrases:
    syllables = 0
    for letter in phrase:
        if letter.lower() in 'аеёюяиыэоу':
            syllables += 1
    syllables_count.append(syllables)
if len(set(syllables_count)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
