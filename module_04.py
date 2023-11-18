# //================================================================
# def amount_payment(payment):
#     res = 0
#     for i in payment:
#         if i < 0:
#             continue
#         res += i
#     return res
    
# print(amount_payment([1, -3, 4]))

# //================================================================
# def prepare_data(data):
#     data_sorted = sorted(data)
#     data_sorted.pop(0)
#     data_sorted.pop()
#     return data_sorted



# //================================================================
# def format_ingredients(ingredients_list):
#     if not ingredients_list:
#         return ""
    
#     formatted_ingredients = ""
#     for i, ingredient in enumerate(ingredients_list):
#         if len(ingredients_list) == 1:
#             formatted_ingredients += ingredient
#             return formatted_ingredients
        
#         if i == len(ingredients_list) - 1:
#             # Останній інгредієнт
#             formatted_ingredients += "and " + ingredient
#         elif i == len(ingredients_list) - 2:
#             formatted_ingredients += ingredient + " "
#         else:
#             formatted_ingredients += ingredient + ", "

#     return formatted_ingredients


# # Приклад використання:
# ingredients_list = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
# formatted_string = format_ingredients(ingredients_list)
# print(formatted_string)
# print(format_ingredients(['2 eggs']))
# print(len(["2 eggs"]))


# //================================================================
# def get_grade(ects_grade):
#     grade_mapping = {
#         "F": 1,
#         "FX": 2,
#         "E": 3,
#         "D": 3,
#         "C": 4,
#         "B": 5,
#         "A": 5
#     }

#     grade = grade_mapping.get(ects_grade, None)

#     if grade is not None:
#         return grade
#     else:
#         return None

# //================================================================
# def get_description(ects_grade):
#     description_mapping = {
#         "F": "Unsatisfactorily",
#         "FX": "Unsatisfactorily",
#         "E": "Enough",
#         "D": "Satisfactorily",
#         "C": "Good",
#         "B": "Very good",
#         "A": "Perfectly"
#     }

#     description = description_mapping.get(ects_grade, None)

#     if description is not None:
#         return description
#     else:
#         return None

# Приклад використання:
# ects_grade = "D"
# print(get_grade(ects_grade))
# print(get_description(ects_grade))

# //================================================================
# def lookup_key(data, value):
#     res = []
#     for key, val in data.items():
#         if val == value:
#             res.append(key)
#     return res

# print(lookup_key({"a":1, "b":2}, 2))
# print(lookup_key({"a":1, "b":2}, 4))

# //================================================================
# def split_list(scores):
#     if not scores:
#         return [], []

#     average_score = sum(scores) / len(scores)

#     below_average = [score for score in scores if score <= average_score]
#     above_average = [score for score in scores if score > average_score]

#     return below_average, above_average


# def split_list(scores):
#     if not scores:
#         return [], []

#     # Знаходження середнього значення
#     sum_of_scores = sum(scores)
#     average_score = sum_of_scores / len(scores)

#     # Розділення списку на дві частини
#     below_average = []
#     above_average = []

#     for score in scores:
#         if score <= average_score:
#             below_average.append(score)
#         else:
#             above_average.append(score)

#     return below_average, above_average

# Приклад використання:
# test_scores = [70, 85, 60, 90, 75]
# below_average, above_average = split_list(test_scores)

# print("Scores below or equal to average:", below_average)
# print("Scores above average:", above_average)

# //================================================================
    
# def calculate_distance(coordinates):
#     if len(coordinates) <= 1:
#         return 0

#     points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}

#     total_distance = 0
#     for i in range(len(coordinates) - 1):
#         # Створення кортежу для пошуку в словнику
#         point_key = (min(coordinates[i], coordinates[i + 1]), max(coordinates[i], coordinates[i + 1]))
        
#         # Додавання відстані до загальної відстані
#         total_distance += points.get(point_key, 0)

#     return total_distance

# # Приклад використання:
# path_coordinates = [0, 1, 3, 2, 0]
# distance = calculate_distance(path_coordinates)
# print("Загальна відстань пролітку дрона:", distance)

# //================================================================
    
# def game(terra, power):
#     for sublist in terra:
#         for energy in sublist:
#             if energy <= power:
#                 power += energy
#             else:
#                 break  # переходимо до наступного списку

#     return power

# # Приклад використання:
# input_lists = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
# initial_power = 1

# result_power = game(input_lists, initial_power)
# print("Загальна енергія гравця:", result_power)

# //================================================================
# def is_valid_pin_codes(pin_codes):
#     if not pin_codes:  # Перевірка на порожній список
#         return False

#     # Перевірка на дублікати
#     if len(pin_codes) != len(set(pin_codes)):
#         return False

#     for pin in pin_codes:
#         # Перевірка на довжину та наявність тільки цифр
#         if len(pin) != 4 or not pin.isdigit():
#             return False

#     return True

# # Приклад використання:
# valid_pin_codes = ['1101', '9034', '0011']
# invalid_pin_codes = ['12345', '9876', '000', '903a']

# print(is_valid_pin_codes(valid_pin_codes))  # True
# print(is_valid_pin_codes(invalid_pin_codes))  # False

# //================================================================
# from random import randint, seed

# def get_random_password():
#     # seed(42)  # Якщо вам потрібна відтворюваність, використовуйте seed
#     password_length = 8
#     password_characters = [chr(randint(40, 126)) for _ in range(password_length)]
#     return ''.join(password_characters)

# # Приклад використання:
# random_password = get_random_password()
# print("Випадковий пароль:", random_password)

# //================================================================
# def is_valid_password(password):
#     if len(password) != 8:
#         return False

#     has_upper = any(char.isupper() for char in password)
#     has_lower = any(char.islower() for char in password)
#     has_digit = any(char.isdigit() for char in password)

#     return has_upper and has_lower and has_digit

# # Приклад використання:
# password1 = "Abcdef12"
# password2 = "abcdef12"
# password3 = "ABCDEF12"
# password4 = "12345678"

# print(is_valid_password(password1))  # True
# print(is_valid_password(password2))  # False (не містить верхнього регістру)
# print(is_valid_password(password3))  # False (не містить нижнього регістру)
# print(is_valid_password(password4))  # False (не містить літер)

# //================================================================
# def get_password():
#     max_attempts = 100
#     attempts = 0

#     while attempts < max_attempts:
#         password = get_random_password()

#         if is_valid_password(password):
#             return password

#         attempts += 1

#     raise RuntimeError("Не вдалося згенерувати надійний пароль протягом заданої кількості спроб.")

# # Приклад використання:
# generated_password = get_password()
# print("Згенерований надійний пароль:", generated_password)

# //================================================================
# from pathlib import Path

# def parse_folder(path):
#     files = []
#     folders = []

#     if not path.is_dir():
#         raise ValueError("Зазначений шлях не є директорією.")

#     for el in path.iterdir():
#         if el.is_dir():
#             folders.append(el.name)
#         else:
#             files.append(el.name)
            
#     return files, folders


# # Приклад використання:
# folder_path = Path("/Users/gineugene/Documents/GoIT/Projects/first-py")  # Замініть це на шлях до вашої директорії
# result = parse_folder(folder_path)

# print("Список файлів:", result[0])
# print("Список директорій:", result[1])

# //================================================================
# import sys

# def parse_args():
#     # Отримати аргументи командного рядка, за винятком імені скрипта (sys.argv[0])
#     arguments = sys.argv[1:]

#     # Скласти аргументи в рядок, розділений пробілами
#     result = ' '.join(arguments)

#     return result

# # Приклад використання:
# args_string = parse_args()
# print("Аргументи командного рядка:", args_string)
