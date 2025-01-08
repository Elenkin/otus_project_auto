import csv
import json

from files import JSON_FILE_PATH
from files import CSV_FILE_PATH
from files import RESULT_FILE_PATH

# Считываем данные из CSV и JSON файлов
with open(CSV_FILE_PATH, 'r') as f:
    books = list(csv.DictReader(f))

with open(JSON_FILE_PATH, 'r') as f:
    users = json.load(f)

list_users = []
for person in range(len(users)):
    fields_for_user = {
        "name": users[person]["name"],
        "gender": users[person]["gender"],
        "address": users[person]["address"],
        "age": users[person]["age"],
        "books": []
    }
    list_users.append(fields_for_user)
    print(list_users)

list_books = []
for book in range(len(books)):
    fields_for_book = {
        "Title": books[book]["Title"],
        "Author": books[book]["Author"],
        "Pages": books[book]["Pages"],
        "Genre": books[book]["Genre"]
    }
    list_books.append(fields_for_book)

# Вычисляем, сколько книг достанется каждому пользователю по умолчанию
books_count = len(list_books) // len(list_users)

# Остаток книг, которые нужно распределить
book_residuals = len(list_books) % len(list_users)
book_index = 0

# распределяем книги между пользователями i — это индекс текущего пользователя в списке list_users
for i, user in enumerate(list_users):
    # Срез книг для текущего пользователя с проверкой условия остатка
    user_books = list_books[book_index:book_index + books_count + (1 if i < book_residuals else 0)]

    # Добавляем книги текущему пользователю
    user["books"] = user_books

    # Обновляем индекс для следующего пользователя
    book_index += len(user_books)

# Записываем результат в JSON файл result.json
with open(RESULT_FILE_PATH, 'w') as f:
    json.dump(list_users, f, indent=4)