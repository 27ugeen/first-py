# from datetime import datetime

# def get_days_from_today(date, current_date=None):
#     # Перетворюємо рядок у формат datetime
#     date_object = datetime.strptime(date, '%Y-%m-%d')

#     # Визначаємо поточну дату, якщо параметр не вказано
#     if current_date is None:
#         today = datetime.now()
#     else:
#         today = datetime.strptime(current_date, '%Y-%m-%d')

#     # Вираховуємо різницю в днях
#     delta = today - date_object

#     # Повертаємо кількість днів (ігноруючи години, хвилини та секунди)
#     return delta.days

# # Приклад використання:
# days_difference = get_days_from_today("2021-10-09")
# print(f"Кількість днів від поточної дати до '2021-10-09': {days_difference}")

# # Або можна вказати конкретну поточну дату:
# current_date = '2021-05-05'
# days_difference_custom_date = get_days_from_today("2021-10-09", current_date)
# print(f"Кількість днів від {current_date} до '2021-10-09': {days_difference_custom_date}")

# //================================================================

# from calendar import monthrange

# def get_days_in_month(month, year):
#     # Використовуємо monthrange для отримання кількості днів у місяці
#     days_in_month = monthrange(year, month)[1]
    
#     return days_in_month

# # Приклад використання:
# month_number = 2  # Лютий
# year_number = 2023  # Рік

# days_in_february = get_days_in_month(month_number, year_number)
# print(f"Кількість днів у лютому {year_number} року: {days_in_february}")

# from datetime import date

# def get_days_in_month(month, year):
#     # Перевірка чи рік є високосним
#     is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#     # Визначення кількості днів у місяці
#     if month == 2:
#         return 29 if is_leap_year else 28
#     elif month in {4, 6, 9, 11}:
#         return 30
#     else:
#         return 31

# # Приклад використання:
# month_number = 2  # Лютий
# year_number = 2023  # Рік

# days_in_february = get_days_in_month(month_number, year_number)
# print(f"Кількість днів у лютому {year_number} року: {days_in_february}")

# //================================================================

# from datetime import datetime

# def get_str_date(date):
#     # Перетворюємо рядок у формат datetime
#     date_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')

#     # Визначаємо назву дня тижня, число, назву місяця та рік
#     day_name = date_object.strftime('%A')
#     day = date_object.strftime('%d')
#     month_name = date_object.strftime('%B')
#     year = date_object.strftime('%Y')

#     # Складаємо рядок з визначеними значеннями
#     formatted_date = f"{day_name} {day} {month_name} {year}"

#     return formatted_date

# # Приклад використання:
# db_date = '2021-05-27 17:08:34.149Z'
# formatted_date = get_str_date(db_date)
# print(formatted_date)

# //================================================================

# from random import sample

# def get_numbers_ticket(min_value, max_value, quantity):
#     # Перевірка умов обмежень на параметри функції
#     if min_value < 1 or max_value > 1000 or min_value >= quantity or quantity >= max_value:
#         return []

#     # Створення випадкового набору чисел без дублікатів
#     numbers = sorted(sample(range(min_value, max_value), quantity))

#     return numbers

# # Приклад використання:
# min_value = 1
# max_value = 49
# quantity = 6

# ticket_numbers = get_numbers_ticket(min_value, max_value, quantity)
# print(ticket_numbers)

# from random import randrange

# def get_numbers_ticket(min_value, max_value, quantity):
#     # Перевірка умов обмежень на параметри функції
#     if min_value < 1 or max_value > 1000 or min_value >= quantity or quantity >= max_value:
#         return []

#     # Створення випадкового набору чисел без дублікатів
#     numbers = []
#     while len(numbers) < quantity:
#         num = randrange(min_value, max_value)
#         if num not in numbers:
#             numbers.append(num)

#     return sorted(numbers)

# # Приклад використання:
# min_value = 1
# max_value = 49
# quantity = 6

# ticket_numbers = get_numbers_ticket(min_value, max_value, quantity)
# print(ticket_numbers)

# //================================================================

# import random

# def get_random_winners(quantity, participants):
#     # Отримуємо перелік ключів (унікальних ідентифікаторів бази даних)
#     participant_ids = list(participants.keys())

#     # Перевірка, чи кількість переможців не більша за кількість користувачів
#     if quantity > len(participant_ids):
#         return []

#     # Перемішуємо список ідентифікаторів
#     random.shuffle(participant_ids)

#     # Вибираємо випадкових переможців
#     winners = random.sample(participant_ids, k=quantity)

#     return winners

# # Приклад використання:
# participants = {
#     "603d2cec9993c627f0982404": "test@test.com",
#     "603f79022922882d30dd7bb6": "test11@test.com",
#     "60577ce4b536f8259cc225d2": "test2@test.com",
#     "605884760742316c07eae603": "vitanlhouse@gmail.com",
#     "605b89080c318d66862db390": "elhe2013@gmail.com",
# }

# winners = get_random_winners(2, participants)
# print(winners)

# //================================================================

# from decimal import Decimal, getcontext

# def decimal_average(number_list, signs_count):
#     # Встановлюємо кількість значущих цифр
#     getcontext().prec = signs_count

#     # Перетворюємо всі числа у списку до типу Decimal
#     decimal_numbers = [Decimal(str(num)) for num in number_list]

#     # Обчислюємо середнє арифметичне
#     average = sum(decimal_numbers) / Decimal(len(decimal_numbers))

#     return average

# # Приклад використання:
# result1 = decimal_average([3, 5, 77, 23, 0.57], 6)
# print(result1)  # Виведе: 21.714

# result2 = decimal_average([31, 55, 177, 2300, 1.57], 9)
# print(result2)  # Виведе: 512.91400

# //================================================================

# import collections

# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

# def convert_list(cats):
#     # Перевіряємо, чи введений список - список іменованих кортежів
#     if all(isinstance(cat, Cat) for cat in cats):
#         # Перетворюємо іменовані кортежі в словники
#         return [cat._asdict() for cat in cats]
#     # Перевіряємо, чи введений список - список словників
#     elif all(isinstance(cat, dict) for cat in cats):
#         # Перетворюємо словники в іменовані кортежі
#         return [Cat(**cat) for cat in cats]
#     else:
#         # Якщо тип не визначений, повертаємо порожній список
#         return []

# # Приклад використання:
# cats_namedtuple = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
# cats_dict = [
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ]

# converted_namedtuple_to_dict = convert_list(cats_namedtuple)
# converted_dict_to_namedtuple = convert_list(cats_dict)

# print(converted_namedtuple_to_dict)
# print(converted_dict_to_namedtuple)

# //================================================================

# from collections import Counter

# def get_count_visits_from_ip(ips):
#     # Використовуємо Counter для підрахунку кількості входжень кожної IP адреси
#     ip_count = Counter(ips)
#     return dict(ip_count)

# def get_frequent_visit_from_ip(ips):
#     # Використовуємо Counter для підрахунку кількості входжень кожної IP адреси
#     ip_count = Counter(ips)

#     # Знаходимо найбільш часто уживаний IP і його кількість входжень
#     most_common_ip, count = ip_count.most_common(1)[0]

#     return most_common_ip, count

# # Приклад використання:
# IP = [
#     "85.157.172.253",
#     "66.50.38.43",
#     "85.157.172.253",
#     "66.50.38.43",
#     "66.50.38.43",
#     "66.50.38.43",
#     "192.168.0.1",
# ]

# count_visits = get_count_visits_from_ip(IP)
# frequent_visit = get_frequent_visit_from_ip(IP)

# print("Count Visits:", count_visits)
# print("Most Frequent Visit:", frequent_visit)


# //================================================================

# from collections import deque

# MAX_LEN = 5  # Задайте бажаний максимальний розмір lifo

# lifo = deque(maxlen=MAX_LEN)

# def push(element):
#     lifo.appendleft(element)

# def pop():
#     if lifo:
#         return lifo.popleft()
#     else:
#         return None  # або можна породити виняток або використати інше значення за замовчуванням

# # Приклад використання:
# push(1)
# push(2)
# push(3)

# print(lifo)  # Виведе: deque([3, 2, 1], maxlen=5)

# value = pop()
# print(value)  # Виведе: 3

# print(lifo)  # Виведе: deque([2, 1], maxlen=5)

# //================================================================

# from collections import deque

# MAX_LEN = 5  # Задайте бажаний максимальний розмір fifo

# fifo = deque(maxlen=MAX_LEN)

# def push(element):
#     fifo.append(element)

# def pop():
#     if fifo:
#         return fifo.popleft()
#     else:
#         return None  # або можна породити виняток або використати інше значення за замовчуванням

# # Приклад використання:
# push(1)
# push(2)
# push(3)

# print(fifo)  # Виведе: deque([1, 2, 3], maxlen=5)

# value = pop()
# print(value)  # Виведе: 1

# print(fifo)  # Виведе: deque([2, 3], maxlen=5)
