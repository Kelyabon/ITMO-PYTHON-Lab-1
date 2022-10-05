import csv
import random

# 'ID', 'Название', 'Тип', 'Автор', 'Автор (ФИО)', 'Возрастное ограничение на книгу', 'Дата поступления', 'Цена поступления', 'Кол-во выдач', 'Дата списания книги', 'Инвентарный номер', 'Выдана до', 'Жанр книги'

with open('books.csv', 'r') as books_csv:
    # Со списками работать проще + обрезаю заголовки
    books = list(csv.reader(books_csv, delimiter=';'))[1:]
    # Количество записей
    amount = len(books)
    # Количество книг с названием > 30 символов
    fst_ex = 0
    # Все теги с повторениями
    tags_list = list()
    # Все книги дешевле 200р
    cheap_books = list()
    for book in books:
        book_name = book[1]
        price = book[7].replace(',', '.')
        if len(book_name) > 30:
            fst_ex += 1
        tags_list += book[-1].split('# ')
        if float(price) < 200:
            cheap_books += [book]
    tags = sorted(set(tags_list))
    cheap_books_sorted_by_popularity = sorted(cheap_books, key=lambda x: x[8], reverse=True)
    print(f'Общее количество записей (без учета заголовков): {amount}\n')
    print(f'Количество записей с названием длинее 30 символов: {fst_ex}\n')
    print('*Допзадание* Все имеющиеся теги:', tags, '\n')
    fst_text_to_print = '*Допзадание* 20 самых популярных книг до 200р:\n'
    for index in range(20):
        fst_text_to_print += f'   {index + 1}. {cheap_books_sorted_by_popularity[index][3]}. {cheap_books_sorted_by_popularity[index][1]} - {cheap_books_sorted_by_popularity[index][6].split("-")[0]} г.\n'
    print(fst_text_to_print)
    # Поиск по авторам
    artist_search = '1'
    # 20 рандомных книг
    random_books = '2'
    # Закрыть программу
    quit_word = 'quit'
    while True:
        what_to_do = input('Чтобы открыть поиск по авторам, введите "1"\n'
                           'Чтобы сгенерировать список 20 рандомных книг, введите "2"\n'
                           'Чтобы закрыть программу введите "quit"\n'
                           '>>>')
        if what_to_do == artist_search:
            artist_name = input('Произведения какого автора вы хотите найти?\n'
                                '>>>')
            artist_books = list()
            for book in books:
                if (artist_name.lower() in book[3].lower()) or (artist_name.lower() in book[4].lower()):
                    artist_books += [f'{book[3]}. {book[1]} - {book[6].split("-")[0]} г.']
            artist_books = sorted(artist_books)
            len_ab = len(artist_books)
            if len_ab == 0:
                print(f'По запросу "{artist_name}" ничего не найдено\n')
            else:
                text_to_print = f'По запросу "{artist_name}" найдено {len_ab} записей'
                if len_ab <= 20:
                    text_to_print += ':\n   ' + '\n   '.join(artist_books)
                    print(text_to_print)
                else:
                    max_page = round(len_ab / 20, 2)
                    if str(max_page).endswith('.0'):
                        max_page = int(max_page)
                    else:
                        max_page = int(str(max_page).split('.')[0]) + 1
                    text_to_print += '\nНа странице показано только 20 из них\n   ' + \
                                     '\n   '.join(artist_books[:20]) + \
                                     f'\n\nВы сейчас на 1 странице из {max_page}\n' \
                                     'Чтобы перейти на другую страницу, введите ее номер\n' \
                                     'Чтобы вернуться в главное меню введите, что угодно, кроме цифр'
                    page = input(text_to_print + '\n>>>')
                while page.isdigit():
                    page = int(page)
                    if page > max_page:
                        page = input('Столько страниц нет. Введите другое число\n'
                                     '>>>')
                    else:
                        page = input('   ' +
                                     '\n   '.join(artist_books[20 * (page - 1):20 * page]) + \
                                     f'\n\nВы сейчас на {page} странице из {max_page}\n' \
                                     'Чтобы перейти на другую страницу, введите ее номер\n' \
                                     'Чтобы вернуться в главное меню введите, что угодно, кроме цифр\n'
                                     '>>>')
        elif what_to_do == random_books:
            with open('20BooksToRead.txt', 'w') as books_to_read_txt:
                text_to_write = ''
                books_to_read = random.sample(books, 20)
                for index in range(20):
                    text_to_write += f'{index + 1}. {books_to_read[index][3]}. {books_to_read[index][1]} - {books_to_read[index][6].split("-")[0]} г.\n'
                books_to_read_txt.write(text_to_write)
            print("Список был сгенерирован и успешно сохранен в файле 20BooksToRead.txt")
        elif what_to_do == quit_word:
            print('Надеюсь, вам понравилось')
            break
        else:
            print('Такого варианта не предусмотрено')
