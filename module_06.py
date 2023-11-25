
# def real_len(text):
#     control_characters = {'\n', '\f', '\r', '\t', '\v'}
    
#     # Використовуємо генератор списку для створення нового рядка без керівних символів
#     cleaned_str = ''.join(char for char in text if char not in control_characters)
    
#     return len(cleaned_str)

# # Приклад використання:
# string1 = 'Alex\nKdfe23\t\f\v.\r'
# string2 = 'Al\nKdfe23\t\v.\r'

# result1 = real_len(string1)
# result2 = real_len(string2)

# print("Довжина рядка без керівних символів у рядку 1:", result1)
# print("Довжина рядка без керівних символів у рядку 2:", result2)

# //================================================================

# def find_articles(key, letter_case=False):
#     result = []

#     for article in articles_dict:
#         title = article["title"]
#         author = article["author"]

#         # Враховуємо регістр літер при необхідності
#         if not letter_case:
#             title = title.lower()
#             author = author.lower()
#             key = key.lower()

#         # Перевіряємо, чи є збіг з ключем у заголовку або авторі
#         if key in title or key in author:
#             result.append({
#                 "author": article["author"],
#                 "title": article["title"],
#                 "year": article["year"],
#             })

#     return result

# # Приклад використання
# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]

# # key = "ocean"
# # result = find_articles(key, letter_case=False)
# # print(result)
# print(find_articles('Ocean'))

# //================================================================

# def sanitize_phone_number(phone_number):
#     # Видаляємо всі пробіли, а потім всі інші символи, крім цифр
#     cleaned_number = phone_number.replace(" ", "").replace("(", "").replace(")", "").replace("-", "").replace("+", "")
    
#     return cleaned_number

# # import re

# # def sanitize_phone_number(phone_number):
# #     # Видаляємо всі символи, крім цифр
# #     cleaned_number = re.sub(r'\D', '', phone_number)
    
# #     return cleaned_number

# # Приклад використання
# phone_numbers = [
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# for number in phone_numbers:
#     sanitized_number = sanitize_phone_number(number)
#     print(sanitized_number)

# //================================================================

# def is_check_name(fullname, first_name):
#     # Перевіряємо, чи fullname починається з first_name (чутливо до регістру)
#     return fullname.startswith(first_name)

# # Приклад використання
# fullname = "John Doe"
# first_name1 = "John"
# first_name2 = "Sam"

# result1 = is_check_name(fullname, first_name1)
# result2 = is_check_name(fullname, first_name2)

# print(result1)  # Виведе True, оскільки "John Doe" починається з "John"
# print(result2)  # Виведе False, оскільки "John Doe" не починається з "Sam"

# //================================================================

# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone

# def get_phone_numbers_for_countries(list_phones):
#     def get_country_code(phone):
#         # Визначає код країни за префіксом телефонного номера
#         if phone.startswith("81"):
#             return "JP"
#         elif phone.startswith("65"):
#             return "SG"
#         elif phone.startswith("886"):
#             return "TW"
#         elif phone.startswith("380"):
#             return "UA"
#         else:
#             return "UA"  # Якщо код країни не відомий, використовуємо "UA" за замовчуванням

#     # Нормалізуємо та сортуємо телефонні номери
#     sanitized_phones = [sanitize_phone_number(phone) for phone in list_phones]
#     sorted_phones = sorted(sanitized_phones, key=get_country_code)

#     # Створюємо словник зі списками телефонних номерів для кожної країни
#     phone_numbers_by_country = {}
#     for country_code in ["JP", "SG", "TW", "UA"]:
#         phone_numbers_by_country[country_code] = [phone for phone in sorted_phones if get_country_code(phone) == country_code]

#     return phone_numbers_by_country

# # Приклад використання
# list_of_phones = [
#     "+81 123-456-789",
#     "+65 98765432",
#     "+886 987654321",
#     "050-111-22-22",
#     "380501112211",
#     "+380501233234",
#     "+81 98765432",
#     "+65 123-456-789",
#     "+886 123456789"
# ]

# result = get_phone_numbers_for_countries(list_of_phones)
# print(result)

# //================================================================

# def is_spam_words(text, spam_words, space_around=False):
#     # Переводимо весь текст у нижній регістр
#     text_lower = text.lower()

#     for word in spam_words:
#         word_lower = word.lower()

#         if space_around:
#             # Якщо space_around=True, шукаємо слово, яке окремо стоїть в тексті
#             if f' {word_lower} ' in f' {text_lower} ' or text_lower.startswith(f'{word_lower} ') or text_lower.endswith(f' {word_lower}') or f'{word_lower} ' in text_lower or f' {word_lower}' in text_lower:
#                 return True
#         else:
#             # Шукаємо слово взагалі, незалежно від того, чи воно окреме чи входить в інше слово
#             if word_lower in text_lower or text_lower.startswith(f'{word_lower} ') or text_lower.endswith(f' {word_lower}'):
#                 return True

#     return False

# # Приклад використання
# print(is_spam_words("У діда в руках молоток.", ["лоток"]))  # True
# print(is_spam_words("У діда в руках молоток.", ["лоток"], True))  # False
# print(is_spam_words("У кота порожній лоток.", ["лоток"]))  # True
# print(is_spam_words("У кота порожній лоток.", ["лоток"], True))  # True

# //================================================================

# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# LATIN_SYMBOLS = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                  "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = dict(zip(map(ord, CYRILLIC_SYMBOLS), LATIN_SYMBOLS * 2))
# TRANS.update(dict(zip(map(ord, CYRILLIC_SYMBOLS.upper()), map(str.upper, LATIN_SYMBOLS * 2))))


# def translate(name):
#     return name.translate(TRANS)


# # Приклад використання
# print(translate("Дмитро Короб"))  # Dmitro Korob
# print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk

# //================================================================

# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

# def formatted_grades(students):
#     result = []
    
#     # Перерахуємо студентів і їх оцінки
#     for i, (name, grade) in enumerate(students.items(), start=1):
#         points = grades.get(grade, 0)
#         formatted_row = f"{i:>4}|{name:<10}|{grade:^5}|{points:^5}"
#         result.append(formatted_row)
    
#     return result

# # Приклад використання
# students = {'Nick': 'A', 'Olga': 'B', 'Boris': 'FX', 'Anna': 'C'}
# for el in formatted_grades(students):
#     print(el)

# //================================================================

# def formatted_numbers():
#     result = []

#     # Заголовок таблиці
#     header = "| decimal  |   hex    |  binary  |"
#     result.extend([header])

#     # Форматування чисел від 0 до 15
#     for i in range(16):
#         decimal = f"{i:<10}"
#         hexadecimal = f"{hex(i)[2:]:^10}"
#         binary = f"{bin(i)[2:]:>10}"
#         row = f"|{decimal}|{hexadecimal}|{binary}|"
#         result.extend([row])

#     return result

# # Виведення відформатованих рядків
# for el in formatted_numbers():
#     print(el)

# //================================================================

# import re

# def find_word(text, word):
#     result = {
#         'result': False,
#         'first_index': None,
#         'last_index': None,
#         'search_string': word,
#         'string': text
#     }

#     # Використання регулярних виразів для пошуку слова у тексті
#     pattern = re.compile(re.escape(word))
#     match = pattern.search(text)

#     if match:
#         result['result'] = True
#         result['first_index'] = match.start()
#         result['last_index'] = match.end()
#         result['search_string'] = match.group()

#     return result

# # Приклад використання
# result1 = find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"
# )
# print(result1)

# result2 = find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "python"
# )
# print(result2)

# //================================================================

# import re

# def find_all_words(text, word):
#     # Використання регулярного виразу для пошуку всіх збігів слова з урахуванням регістру
#     pattern = re.compile(re.escape(word), re.IGNORECASE)
    
#     # Пошук всіх збігів у тексті за допомогою re.findall
#     matches = pattern.findall(text)
    
#     # Повернення списку з усіма знаходженнями слова
#     return matches

# # Приклад використання
# text = "Python is a powerful programming language. Python is versatile and easy to learn."
# word_to_find = "pyThon"
# result = find_all_words(text, word_to_find)
# print(result)

# //================================================================

# import re

# def replace_spam_words(text, spam_words):
#     # Створення регулярного виразу для пошуку заборонених слів з урахуванням регістру
#     pattern = re.compile(r'\b(?:' + '|'.join(re.escape(word) for word in spam_words) + r')\b', re.IGNORECASE)
    
#     # Заміна заборонених слів на шаблон '*'
#     result = pattern.sub(lambda match: '*' * len(match.group(0)), text)
    
#     return result

# # Приклад використання
# text = "This is a sample text with some bad words like bad, evil, and terrible."
# spam_words = ["bad", "evil", "terrible"]
# result_text = replace_spam_words(text, spam_words)
# print(result_text)

# //================================================================

# import re

# def find_all_emails(text):
#     # pattern = re.compile(r'[A-Za-z0-9._%+-]{2,}@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}')
#     # result = pattern.findall(text)
#     # # # Видаляємо цифри на початку email
#     # result = [re.sub(r'^\d', '', email) for email in result]
#     # # Видаляємо email, якщо до @ тільки цифри
#     # result = [email for email in result if not re.match(r'^\d+@', email)]

#     pattern = re.compile(r'[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}')
#     result = pattern.findall(text)
#     return result

# # Приклад використання
# text = "Simple email cool@api.io cool@api.i first.middle.last@iana.or a2@test.com a3@test.com.io 222111@test.com"
# text1 = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"
# emails = find_all_emails(text)
# emails1 = find_all_emails(text1)
# print(emails)
# print(emails1)

# //================================================================

# import re

# def find_all_phones(text):
#     pattern = re.compile(r'\+\d{3}\(\d{2}\)\d{3}-\d{1,2}-\d{2,3}')
#     # result = pattern.findall(text)
#     result = [phone[:17] for phone in pattern.findall(text) if len(phone) >= 17]
#     return result

# # Приклад використання
# text = "MIrma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787"
# phones = find_all_phones(text)
# print(phones)

# //================================================================

# import re

# def find_all_links(text):
#     result = []
#     iterator = re.finditer(r'https?://[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*\.[A-Za-z]{2,}', text)
#     for match in iterator:
#         result.append(match.group())
#     return result

# # Приклад використання
# text = "The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com"
# links = find_all_links(text)
# print(links)



