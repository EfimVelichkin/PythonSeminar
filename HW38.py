import os
phonebook = 'phonebook.txt'

if not os.path.exists('phonebook.txt'):
        with open('phonebook.txt', 'w', encoding='utf-8') as f:
            f.write('')

def add_contact(name, phone):
    with open('phonebook.txt', 'a', encoding='utf-8') as f:
        f.write(f'{name}:{phone}\n')

def edit_contact(number, name=None, phone=None):
    number = int(number)
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if number < 1 or number > len(lines):
        print('Некорректный номер контакта')
        return

    lines[number-1] = f'{name or lines[number-1].split(":")[0]}:{phone or lines[number-1].split(":")[1]}'

    with open('phonebook.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(lines))

def delete_contact(number):
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if number < 1 or number > len(lines):
        print('\nНекорректный номер контакта\n')
        return

    del lines[number-1]

    with open('phonebook.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(lines))

def show_phonebook():
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        print('\nТелефонная книга пуста\n')
        return

    for i, line in enumerate(lines):
        name, phone = line.split(':')
        print(f'{i+1}. {name}: {phone}', end='')

def main_menu():
    work = True
    while work:
        answer = input('Телефоная книга:\n'
                    '1.Читать книгу\n'
                    '2.Удалить пользователя\n'
                    '3.Добавить пользователя\n'
                    '4.Редактировать пользователя\n'
                    '5.Выход\n')
        
        match answer:
            case '1':
                show_phonebook()
            case '2':
                ID = int(input('Введите ID: '))
                delete_contact(number=ID)
            case '3':
                Surname = input('Введите фамилию: ')
                Name = input('Введите имя: ')
                MiddleName = input('Введите отчество: ')
                name = Surname +' '+Name+' '+MiddleName
                phone = input('Введите номер: ')
                add_contact(name, phone)
            case '4':
                edit = input('1.Поправки в ФИО\n'
                            '2.Поправки в номере\n')
                match edit:
                    case '1':
                        ID = input('Введите ID: ')
                        new_name = input('Внесите поправки в ФИО: ')
                        edit_contact(number=ID, name=new_name)
                    case '2':
                        number = input('Введите ID: ')
                        new_phone = input('Внесите поправки в номере: ')
                        edit_contact(number, phone=new_phone+'\n')
                    case _:
                        print('Введено некорректное значение: ')
            case '5':
                work = False
            case _:
                print('\n--Введено некорректное значение, милорд!--\n')

main_menu()
