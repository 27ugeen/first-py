# def get_grade(key):
#     grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
#     return grade.get(key, None)

# def get_description(key):
#     description = {
#         "A": "Perfectly",
#         "B": "Very good",
#         "C": "Good",
#         "D": "Satisfactorily",
#         "E": "Enough",
#         "FX": "Unsatisfactorily",
#         "F": "Unsatisfactorily",
#     }
#     return description.get(key, None)

# def get_student_grade(option):
#     if option == "grade":
#         return get_grade
#     elif option == "description":
#         return get_description
#     else:
#         return None

# # Приклад використання:
# selected_function = get_student_grade("grade")
# if selected_function:
#     result = selected_function("A")
#     print(result)  # Повинно вивести 5

# selected_function = get_student_grade("description")
# if selected_function:
#     result = selected_function("B")
#     print(result)  # Повинно вивести "Very good"

# selected_function = get_student_grade("invalid_option")
# if selected_function:
#     result = selected_function("C")
#     print(result)  # Повинно вивести None, оскільки "invalid_option" не відповідає жодній опції

# //================================================================

# DEFAULT_DISCOUNT = 0.05

# def get_discount_price_customer(price, customer):
#     # Перевірка, чи є поле "discount" в словнику customer
#     if "discount" in customer:
#         # Використовуємо значення "discount" як знижку
#         discount = customer["discount"]
#     else:
#         # Використовуємо глобальну змінну DEFAULT_DISCOUNT, якщо поле "discount" відсутнє
#         discount = DEFAULT_DISCOUNT

#     # Розрахунок ціни з урахуванням знижки
#     discounted_price = price * (1 - discount)

#     return discounted_price

# # Приклад використання:
# product_price = 100
# customer1 = {"name": "Dima"}
# customer2 = {"name": "Boris", "discount": 0.15}

# result1 = get_discount_price_customer(product_price, customer1)
# result2 = get_discount_price_customer(product_price, customer2)

# print(result1)  # Припустимий результат для клієнта без знижки
# print(result2)  # Припустимий результат для клієнта із знижкою 0.15


# //================================================================

# def caching_fibonacci():
#     # Словник для збереження обчислених значень Фібоначчі
#     cache = {}

#     # Внутрішня функція fibonacci для обчислення чисел Фібоначчі
#     def fibonacci(n):
#         # Перевірка, чи число Фібоначчі вже є в кеші
#         if n in cache:
#             return cache[n]
        
#         # Обчислення числа Фібоначчі
#         if n == 0:
#             result = 0
#         elif n == 1:
#             result = 1
#         else:
#             result = fibonacci(n - 1) + fibonacci(n - 2)
        
#         # Збереження обчисленого значення у кеші
#         cache[n] = result
        
#         return result

#     # Повертаємо внутрішню функцію fibonacci
#     return fibonacci

# # Приклад використання:
# fibonacci_func = caching_fibonacci()

# # Обчислення чисел Фібоначчі з використанням кеша
# result1 = fibonacci_func(5)
# result2 = fibonacci_func(8)
# result3 = fibonacci_func(5)  # Значення 5 повинно бути взяте з кеша

# print(result1)  # Повинно вивести 5
# print(result2)  # Повинно вивести 21
# print(result3)  # Повинно вивести 5 (з кеша)

# //================================================================

# def discount_price(discount):
#     # Внутрішня функція для розрахунку ціни з урахуванням знижки
#     def calculate_discounted_price(price):
#         # Розрахунок ціни зі знижкою
#         discounted_price = price * (1 - discount)
#         return discounted_price

#     # Повертаємо внутрішню функцію для подальшого використання
#     return calculate_discounted_price

# # Приклад використання:
# cost_15 = discount_price(0.15)
# cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)

# price = 100
# print(cost_15(price))  # Повинно вивести 85.0
# print(cost_10(price))  # Повинно вивести 90.0
# print(cost_05(price))  # Повинно вивести 95.0

# //================================================================

# def format_phone_number(func):
#     def wrapper(phone):
#         # Викликаємо оригінальну функцію
#         result = func(phone)

#         # Додаємо префікс +38 для коротких номерів
#         if len(result) < 12:
#             result = "+38" + result
#         elif len(result) == 12:
#             result = "+" + result

#         return result

#     return wrapper
    

# @format_phone_number
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#             .removeprefix("+")
#             .replace("(", "")
#             .replace(")", "")
#             .replace("-", "")
#             .replace(" ", "")
#     )
#     return new_phone

# # Приклад використання:
# phone_number = sanitize_phone_number("123-456-789")
# phone_number2 = sanitize_phone_number("123-456-789-000")
# print(phone_number)
# print(phone_number2)

# //================================================================

# import re

# def generator_numbers(string=""):
#     # Знаходимо всі цілі числа в рядку
#     numbers = [int(match.group()) for match in re.finditer(r'\b\d+\b', string)]
    
#     # Повертаємо числа як генератор
#     for number in numbers:
#         yield number

# def sum_profit(string):
#     # Викликаємо generator_numbers для отримання генератора чисел
#     numbers_generator = generator_numbers(string)
    
#     # Сумуємо числа з генератора
#     total_profit = sum(numbers_generator)
    
#     return total_profit

# # Приклад використання:
# profit_string = "The resulting profit was: from the southern possessions $100, from the northern colonies $500, and the king gave $1000."

# total_profit = sum_profit(profit_string)
# print(total_profit)  # Повинно вивести 1600

# //================================================================

# def normal_name(names):
#     # Використовуємо функцію capitalize для перетворення першої літери великою
#     return list(map(str.capitalize, names))

# # Приклад використання:
# name = ["dan", "jane", "steve", "mike"]
# result = normal_name(name)
# print(result)

# //================================================================

# def get_emails(list_contacts):
#     # Використовуємо функцію map для витягування email з кожного словника контакту
#     emails = list(map(lambda contact: contact["email"], list_contacts))
#     return emails

# # Приклад використання:
# contacts = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     # Додайте інші контакти за необхідності
# ]

# result = get_emails(contacts)
# print(result)

# //================================================================

# def positive_values(payment):
#     # Використовуємо функцію filter для відфільтрування додатних значень
#     positive_payments = list(filter(lambda x: x > 0, payment))
#     return positive_payments

# # Приклад використання:
# payment = [100, -3, 400, 35, -100]

# result = positive_values(payment)
# print(result)

# //================================================================

# def get_favorites(contacts):
#     # Використовуємо функцію filter для відфільтрування обраних контактів
#     favorite_contacts = list(filter(lambda contact: contact["favorite"], contacts))
#     return favorite_contacts

# # Приклад використання:
# contacts = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     {
#         "name": "John Doe",
#         "email": "john.doe@example.com",
#         "phone": "(123) 456-7890",
#         "favorite": True,
#     },
#     # Додайте інші контакти за необхідності
# ]

# result = get_favorites(contacts)
# print(result)

# //================================================================

# from functools import reduce

# def sum_numbers(numbers):
#     # Використовуємо функцію reduce для обчислення суми елементів
#     result = reduce(lambda x, y: x + y, numbers)
#     return result

# # Приклад використання:
# numbers = [3, 4, 6, 9, 34, 12]
# total_sum = sum_numbers(numbers)
# print(total_sum)

# //================================================================

# from functools import reduce

# def amount_payment(payment):
#     # Використовуємо функцію reduce для підсумовування додатніх значень
#     total_payment = reduce(lambda x, y: x + y if y > 0 else x, payment, 0)
#     return total_payment

# # Приклад використання:
# payment = [1, -3, 4]
# total = amount_payment(payment)
# print(total)
