# def total_salary(path):
#     total = 0

#     try:
#         # Відкриваємо файл за вказаним шляхом
#         file = open(path, 'r')

#         # Читаємо рядки файлу
#         line = file.readline()
#         while line:
#             # Розбиваємо рядок на прізвище та заробітну плату
#             parts = line.strip().split(',')
#             if len(parts) == 2:
#                 # Додаємо заробітну плату до загальної суми
#                 total += float(parts[1])
            
#             # Читаємо наступний рядок
#             line = file.readline()
#     except FileNotFoundError:
#         print(f"File not found: {path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # Закриваємо файл
#         if file:
#             file.close()

#     return total

# # Приклад використання
# file_path = "example.txt"
# total = total_salary(file_path)
# print(f"Total salary: {total}")

# //================================================================

# def write_employees_to_file(employee_list, path):
#     try:
#         # Відкриваємо файл за вказаним шляхом у режимі запису ("w")
#         file = open(path, 'w')

#         # Проходимося по кожному відділу та його співробітникам
#         for department_employees in employee_list:
#             # Записуємо кожного співробітника з нового рядка
#             for employee in department_employees:
#                 file.write(employee + '\n')

#             # Розділяємо відділи порожнім рядком
#             # file.write('\n')

#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # Закриваємо файл
#         if file:
#             file.close()

# # Приклад використання
# employee_list = [
#     ['Robert Stivenson,28', 'Alex Denver,30'],
#     ['Drake Mikelsson,19']
# ]

# file_path = "employees.txt"
# write_employees_to_file(employee_list, file_path)

# //================================================================

# def read_employees_from_file(path):
#     employees = []

#     try:
#         # Відкриваємо файл за вказаним шляхом у режимі читання ("r")
#         file = open(path, 'r')

#         # Читаємо вміст файлу
#         lines = file.readlines()

#         # Проходимося по кожному рядку та додаємо його до списку співробітників, видаляючи символ кінця рядка
#         for line in lines:
#             employee = line.strip()
#             if employee:
#                 employees.append(employee)

#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # Закриваємо файл
#         if file:
#             file.close()

#     return employees

# # Приклад використання
# file_path = "employees.txt"
# employee_list = read_employees_from_file(file_path)
# print(employee_list)

# //================================================================

# def add_employee_to_file(record, path):
#     try:
#         # Відкриваємо файл за вказаним шляхом у режимі додавання ("a")
#         file = open(path, 'a')

#         # Додаємо запис про співробітника до файлу та переходимо на новий рядок
#         file.write(record + '\n')

#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # Закриваємо файл
#         if file:
#             file.close()

# # Приклад використання
# file_path = "employees.txt"
# new_employee_record = "Drake Mikelsson,19"
# add_employee_to_file(new_employee_record, file_path)

# //================================================================

# def get_cats_info(path):
#     cat_list = []

#     try:
#         # Відкриваємо файл за вказаним шляхом у режимі читання ("r") за допомогою менеджера контексту with
#         with open(path, 'r') as file:
#             # Читаємо кожен рядок з файлу
#             for line in file:
#                 # Розділяємо рядок на частини по комі
#                 parts = line.strip().split(',')

#                 # Створюємо словник із даними кота та додаємо його до списку
#                 cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]}
#                 cat_list.append(cat_info)

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     # Повертаємо список котів
#     return cat_list

# # Приклад використання
# file_path = "cats.txt"
# cats_info = get_cats_info(file_path)
# print(cats_info)

# //================================================================

# def get_recipe(path, search_id):
#     try:
#         # Відкриваємо файл за вказаним шляхом у режимі читання ("r") за допомогою менеджера контексту with
#         with open(path, 'r') as file:
#             # Читаємо кожен рядок з файлу
#             for line in file:
#                 # Розділяємо рядок на частини по комі
#                 parts = line.strip().split(',')

#                 # Якщо перший елемент рядка (ідентифікатор) дорівнює search_id
#                 if parts[0] == search_id:
#                     # Створюємо словник із даними рецепта та повертаємо його
#                     recipe_info = {
#                         "id": parts[0],
#                         "name": parts[1],
#                         "ingredients": parts[2:]
#                     }
#                     return recipe_info

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     # Якщо рецепта із зазначеним search_id у файлі немає, повертаємо None
#     return None

# # Приклад використання
# file_path = "recipes.txt"
# search_id = "60b90c3b13067a15887e1ae4"
# recipe = get_recipe(file_path, search_id)
# print(recipe)

# //================================================================

# def sanitize_file(source, output):
#     try:
#         # Відкриваємо файл source за вказаним шляхом у режимі читання ("r") за допомогою менеджера контексту with
#         with open(source, 'r') as source_file:
#             # Читаємо вміст файлу source
#             source_content = source_file.read()

#         # Очищаємо вміст від цифр
#         sanitized_content = ''.join(char for char in source_content if not char.isdigit())

#         # Відкриваємо файл output у режимі запису ("w") за допомогою менеджера контексту with
#         with open(output, 'w') as output_file:
#             # Записуємо очищений вміст у файл output
#             output_file.write(sanitized_content)

#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Приклад використання
# source_file_path = "source.txt"
# output_file_path = "output.txt"
# sanitize_file(source_file_path, output_file_path)

# //================================================================

# def save_applicant_data(source, output):
#     try:
#         # Відкриваємо файл output у режимі запису ("w") за допомогою менеджера контексту with
#         with open(output, 'w') as output_file:
#             # Ітеруємося по кожному словнику абітурієнта у списку
#             for applicant in source:
#                 # Формуємо рядок для запису у файл
#                 line = f"{applicant['name']},{applicant['specialty']},{applicant['math']},{applicant['lang']},{applicant['eng']}\n"
#                 # Записуємо рядок у файл
#                 output_file.write(line)

#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Приклад використання
# applicants_list = [
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ]

# output_file_path = "output.txt"
# save_applicant_data(applicants_list, output_file_path)

# //================================================================

# def is_equal_string(utf8_string, utf16_string):
#     try:
#         # Декодуємо рядки та нормалізуємо їх
#         decoded_utf8 = utf8_string.decode('utf-8').casefold()
#         decoded_utf16 = utf16_string.decode('utf-16').casefold()

#         # Кодування в UTF-16
#         # utf_16_str = decoded_utf8.encode('utf-16') 

#         # Порівнюємо декодовані та нормалізовані рядки
#         return decoded_utf8 == decoded_utf16

#     except UnicodeDecodeError:
#         # Якщо виникає помилка під час декодування, рядки не можна порівняти
#         return False

# # Приклад використання
# utf8_str = b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82'  # Привіт у кодуванні UTF-8
# utf16_str = b'?\x04@\x048\x042\x04V\x04B\x04'  # Привіт у кодуванні UTF-16

# result = is_equal_string(utf8_str, utf16_str)
# print(result)  # Очікується True, оскільки рядки мають однаковий зміст

# //================================================================

# def save_credentials_users(path, users_info):
#     with open(path, 'wb') as file:
#         for username, password in users_info.items():
#             user_data = f"{username}:{password}\n".encode('utf-8')
#             file.write(user_data)

# # Приклад виклику функції зі словником користувачів
# users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
# save_credentials_users('credentials.bin', users_info)

# //================================================================

# def get_credentials_users(path):
#     result = []
#     with open(path, 'rb') as file:
#         for line in file:
#             decoded_line = line.decode('utf-8').strip()
#             result.append(decoded_line)
#     return result

# # Приклад виклику функції
# credentials_list = get_credentials_users('credentials.bin')
# print(credentials_list)

# //================================================================

# import base64

# def encode_data_to_base64(data):
#     encoded_data = []
#     for item in data:
#         encoded_pair = f"{base64.b64encode(item.encode()).decode()}"
#         encoded_data.append(encoded_pair)
#     return encoded_data

# # Приклад виклику функції
# credentials_list = ['andry:uyro18890D', 'steve:oppjM13LL9e']
# encoded_credentials = encode_data_to_base64(credentials_list)
# print(encoded_credentials)

# //================================================================

# import shutil

# def create_backup(path, file_name, employee_residence):
#     # Створюємо бінарний файл та записуємо у нього дані
#     with open(f"{path}/{file_name}", 'wb') as file:
#         for name, country in employee_residence.items():
#             line = f"{name} {country}\n"
#             file.write(line.encode('utf-8'))

#     # Архівуємо теку
#     shutil.make_archive("backup_folder", 'zip', path)

#     # Повертаємо шлях до архіву
#     return f"{path}/backup_folder.zip"

# # Приклад використання
# employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}
# result = create_backup('.', 'employee_data.txt', employee_residence)
# print(result)

# //================================================================

# import shutil

# def unpack(archive_path, path_to_unpack):
#     shutil.unpack_archive(archive_path, path_to_unpack)

# # Приклад використання
# unpack('backup_folder.zip', 'unpacked_data')
