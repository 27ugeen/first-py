# from setuptools import setup

# def do_setup(args_dict):
#     setup(**args_dict)

# # Приклад використання
# args_dict = {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }

# do_setup(args_dict)

# //================================================================

# from setuptools import setup

# def do_setup(args_dict, requires):
#     setup(**args_dict, install_requires=requires)

# # def do_setup(args_dict, requires):
# #     setup(name=args_dict['name'],
# #           version=args_dict['version'],
# #           description=args_dict['description'],
# #           url=args_dict['url'],
# #           author=args_dict['author'],
# #           author_email=args_dict['author_email'],
# #           license=args_dict['license'],
# #           packages=args_dict['packages'],
# #           install_requires=requires)

# # Приклад використання
# args_dict = {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }

# requires = ["requests", "numpy"]

# do_setup(args_dict, requires)

# //================================================================

# from setuptools import setup

# def do_setup(args_dict, requires, entry_points):
#     setup(**args_dict, install_requires=requires, entry_points=entry_points)

# # def do_setup(args_dict, requires, entry_points):
# #     setup(name=args_dict['name'],
# #           version=args_dict['version'],
# #           description=args_dict['description'],
# #           url=args_dict['url'],
# #           author=args_dict['author'],
# #           author_email=args_dict['author_email'],
# #           license=args_dict['license'],
# #           packages=args_dict['packages'],
# #           install_requires=requires,
# #           entry_points=entry_points
# #           )

# # Приклад використання
# args_dict = {
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }

# requires = ["requests", "numpy"]

# entry_points = {
#     "console_scripts": [
#         "my_script = useful.module:main",
#     ],
# }

# do_setup(args_dict, requires, entry_points)

# //================================================================

# def is_integer(s):
#     # Вилучаємо початкові та кінцеві прогалини
#     s = s.strip()

#     # Перевіряємо, чи є хоча б один символ
#     if not s:
#         return False

#     # Перевіряємо, чи є початковий знак
#     if s[0] in ['+', '-']:
#         # Видаляємо початковий знак
#         s = s[1:]

#     # Перевіряємо, чи залишився хоча б один символ після видалення знаку
#     if not s:
#         return False

#     # Перевіряємо, чи всі символи залишеного рядка є цифрами
#     return s.isdigit()

# # Приклад використання
# print(is_integer("123"))       # True
# print(is_integer("   +456  "))   # True
# print(is_integer("+789"))      # True
# print(is_integer("-987"))      # True
# print(is_integer("3.14"))      # False
# print(is_integer("abc"))       # False
# print(is_integer(""))           # False

# //================================================================

# def capital_text(s):
#     result = ''
#     capitalize_next = True

#     for char in s:
#         if char.isalpha():
#             if capitalize_next:
#                 result += char.upper()
#                 capitalize_next = False
#             else:
#                 result += char.lower()
#         elif char in ['.', '!', '?']:
#             capitalize_next = True
#             result += char
#         else:
#             result += char

#     return result

# # Приклад використання
# text = "this is a sample text. it has multiple sentences. what do you think?"
# capitalized_text = capital_text(text)
# print(capitalized_text)

# //================================================================

# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#     found_word = ""

#     if reverse:
#         riddle = riddle[::-1]

#     start_index = riddle.find(start_letter)

#     if start_index != -1:
#         remaining_riddle = riddle[start_index:]

#         letters_to_read = word_length
#         current_index = 0

#         while current_index < len(remaining_riddle):
#             current_letter = remaining_riddle[current_index]

#             found_word += current_letter
#             letters_to_read -= 1

#             if letters_to_read == 0:
#                 break

#             current_index += 1

#     return found_word


# # Приклад використання:
# riddle_str = "mi1powperet"
# result = solve_riddle(riddle_str, 3, 'r', True)
# print(result)  # Виведе "rep"

# # Приклад використання:
# riddle_str = "pfhigoalnorabcikjsdfo"
# result = solve_riddle(riddle_str, 4, "g")
# print(result)  # Виведе "goal"

# //================================================================

# def data_preparation(list_data):
#     cleaned_data = []

#     for sublist in list_data:
#         if len(sublist) > 2:
#             sublist.remove(max(sublist))
#             sublist.remove(min(sublist))
#         cleaned_data.extend(sublist)

#     return sorted(cleaned_data, reverse=True)

# # Приклад використання:
# input_data = [[1, 2, 3], [3, 4], [5, 6]]
# result = data_preparation(input_data)
# print(result)

# //================================================================

# def token_parser(s):
#     operators = set("+-*/()")
#     tokens = []
#     current_token = ""

#     for char in s:
#         if char.isdigit() or char == '.':
#             current_token += char
#         elif char in operators:
#             if current_token:
#                 tokens.append(current_token)
#                 current_token = ""
#             tokens.append(char)
#         elif char.isspace():
#             if current_token:
#                 tokens.append(current_token)
#                 current_token = ""

#     if current_token:
#         tokens.append(current_token)

#     return tokens

# # Приклад використання:
# math_expression = "2+ 34-5 * 3"
# result = token_parser(math_expression)
# print(result)

# //================================================================

# def all_sub_lists(data):
#     result = [[]]

#     for i in range(len(data)):
#         result.append([data[i]])

#     result = result + [[data[i], data[i + 1]] for i in range(len(data) - 1)]

#     for i in range(len(data)):
#         for j in range(i + 1, len(data) + 1):
#             sublist = data[i:j]
#             if sublist not in result:
#                 result.append(sublist)

#     if data in result:
#         result.remove(data)
#         result.append(data)

#     return result

# # Приклад використання:
# original_list = [1, 2, 3]
# result = all_sub_lists(original_list)
# print(result)

# # Приклад використання:
# original_list = [4, 6, 1, 3]
# result = all_sub_lists(original_list)
# print(result)

# //================================================================

# def make_request(keys, values):
#     # Перевірка на відповідність довжин списків keys та values
#     if len(keys) != len(values):
#         print("Помилка: довжина списків keys та values не збігається")
#         return {}

#     # Створення словника
#     request_dict = dict(zip(keys, values))

#     return request_dict

# # Приклад використання
# keys = ['name', 'age', 'city']
# values = ['John', 25, 'New York']

# result = make_request(keys, values)
# print(result)


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# # Використання zip для об'єднання списків у послідовність кортежів
# zipped = zip(list1, list2)

# # Перетворення результату в список кортежів
# result = list(zipped)

# print(result)

# //================================================================

# def sequence_buttons(string):
#     # Створення словника, який відповідає символам на кнопках
#     button_mapping = {
#         '1': [".", ",", "?", "!", ":"],
#         '2': ["A", "B", "C"],
#         '3': ["D", "E", "F"],
#         '4': ["G", "H", "I"],
#         '5': ["J", "K", "L"],
#         '6': ["M", "N", "O"],
#         '7': ["P", "Q", "R", "S"],
#         '8': ["T", "U", "V"],
#         '9': ["W", "X", "Y", "Z"],
#         '0': [" "]
#     }

#     result_sequence = ""

#     for char in string:
#         # Перетворення символу в верхній регістр
#         char = char.upper()

#         # Пошук кнопки, якій відповідає символ
#         for button, symbols in button_mapping.items():
#             if char in symbols:
#                 # Знайдена кнопка, додаємо до послідовності
#                 result_sequence += button * (symbols.index(char) + 1)
#                 break

#     return result_sequence

# # Приклад використання
# input_text = "Hello, World!"
# output_sequence = sequence_buttons(input_text)
# print(output_sequence)

# //================================================================

# def file_operations(path, additional_info, start_pos, count_chars):
#     # Запис додаткової інформації в кінець файлу
#     with open(path, 'a') as file:
#         file.write(additional_info)

#     # Відкриття файлу для читання та зчитування рядка
#     with open(path, 'r') as file:
#         # Встановлення позиції в файлі
#         file.seek(start_pos)

#         # Читання та повернення рядка заданої довжини
#         result_str = file.read(count_chars)

#     return result_str

# # Приклад використання
# file_path = 'example.txt'
# info_to_add = 'This is additional info.'
# start_position = 10
# chars_to_read = 5

# result = file_operations(file_path, info_to_add, start_position, chars_to_read)
# print(result)

# //================================================================

# def get_employees_by_profession(path, profession):
#     # Відкриття файлу за допомогою with для читання
#     with open(path, 'r') as file:
#         # Отримання рядків з файлу за допомогою readlines()
#         lines = file.readlines()

#     # Знайдені рядки, де є вказана profession
#     matching_lines = [line for line in lines if profession in line]

#     # Об'єднання знайдених рядків в один рядок з використанням '\n' як роздільника
#     result_string = '\n'.join(matching_lines)

#     # Прибирання зайвих пробілів та символів нового рядка
#     result_string = result_string.replace('\n', '').strip()

#     # Прибирання значення profession
#     result_string = result_string.replace(profession, '')

#     return result_string.rstrip()

# # Приклад використання
# file_path = 'employees.txt'
# desired_profession = 'courier'

# result = get_employees_by_profession(file_path, desired_profession)
# print(result)

# //================================================================

# def to_indexed(source_file, output_file):
#     # Відкриття вхідного файлу за допомогою with для читання
#     with open(source_file, 'r') as source:
#         # Читання рядків з вхідного файлу
#         lines = source.readlines()

#     # Запис номерованих рядків у вихідний файл
#     with open(output_file, 'w') as output:
#         # Запис номерованих рядків у вихідний файл
#         for i, line in enumerate(lines):
#             indexed_line = f"{i}: {line}"
#             output.write(indexed_line)

# # Приклад використання
# input_file_path = 'input.txt'
# output_file_path = 'output.txt'

# to_indexed(input_file_path, output_file_path)

# //================================================================

# def flatten(data):
#     # Якщо вхідний список порожній, повертаємо порожній список
#     if not data:
#         return []

#     # Якщо перший елемент списку є списком
#     if isinstance(data[0], list):
#         # Рекурсивно викликаємо функцію з першим елементом списку та конкатенуємо результат з рекурсивним викликом функції для решти списку
#         return flatten(data[0]) + flatten(data[1:])
#     else:
#         # Якщо перший елемент списку не є списком, конкатенуємо його з рекурсивним викликом функції для решти списку
#         return [data[0]] + flatten(data[1:])

# # Приклад використання
# nested_list = [1, 2, [3, 4, [5, 6]], 7]
# flat_list = flatten(nested_list)
# print(flat_list)

# //================================================================

# def decode(encoded_list):
#     decoded_list = []

#     # Функція для додавання розшифрованих значень до списку
#     def add_decoded(value, count):
#         decoded_list.extend([value] * count)

#     # Рекурсивна функція для декодування
#     def decode_recursive(lst):
#         if not lst:
#             return

#         # Додаємо розшифровані значення до списку
#         add_decoded(lst[0], lst[1])

#         # Рекурсивно викликаємо функцію для решти списку
#         decode_recursive(lst[2:])

#     # Викликаємо рекурсивну функцію для початкового списку
#     decode_recursive(encoded_list)

#     return decoded_list

# # Приклад використання
# encoded_list = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
# decoded_result = decode(encoded_list)
# print(decoded_result)

# //================================================================

# def encode(data):
#     if not data:
#         return []

#     def encode_helper(sublist):
#         if not sublist:
#             return []

#         count = 1
#         while count < len(sublist) and sublist[count] == sublist[0]:
#             count += 1

#         encoded = [sublist[0], count]
#         rest_encoded = encode_helper(sublist[count:])
#         return encoded + rest_encoded

#     if isinstance(data, str):
#         data = list(data)

#     return encode_helper(data)

# # Приклад використання:
# input_list = ["X", "X", "X", "X", "X", "Z", "X", "Y", "Y", "Y", "Y", "Z", "Z"]
# encoded_list = encode(input_list)
# print(encoded_list)

# input_str = "XXXXXZXYYYYZZ"
# encoded_str = encode(input_str)
# print(encoded_str)
