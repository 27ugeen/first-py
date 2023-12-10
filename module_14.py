# import pickle

# def write_contacts_to_file(filename, contacts):
#     with open(filename, 'wb') as file:
#         pickle.dump(contacts, file)

# def read_contacts_from_file(filename):
#     try:
#         with open(filename, 'rb') as file:
#             contacts = pickle.load(file)
#         return contacts
#     except FileNotFoundError:
#         # Обробка винятку, якщо файл не існує
#         print(f"File '{filename}' not found. Returning an empty list.")
#         return []

# # Приклад використання:
# contacts_list = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     # Додайте інші контакти за необхідності
# ]

# # Запис у файл
# write_contacts_to_file('contacts.pkl', contacts_list)

# # Читання з файлу
# read_contacts = read_contacts_from_file('contacts.pkl')
# print(read_contacts)

# //================================================================

# import json

# def write_contacts_to_file(filename, contacts):
#     data = {"contacts": contacts}
#     with open(filename, 'w') as file:
#         json.dump(data, file)

# def read_contacts_from_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             data = json.load(file)
#         return data.get("contacts", [])
#     except FileNotFoundError:
#         # Обробка винятку, якщо файл не існує
#         print(f"File '{filename}' not found. Returning an empty list.")
#         return []

# # Приклад використання:
# contacts_list = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     # Додайте інші контакти за необхідності
# ]

# # Запис у файл
# write_contacts_to_file('contacts.json', contacts_list)

# # Читання з файлу
# read_contacts = read_contacts_from_file('contacts.json')
# print(read_contacts)

# //================================================================

# import csv

# def write_contacts_to_file(filename, contacts):
#     with open(filename, 'w', newline='') as file:
#         fieldnames = ["name", "email", "phone", "favorite"]
#         writer = csv.DictWriter(file, fieldnames=fieldnames)

#         # Запис заголовків
#         writer.writeheader()

#         # Запис кожного контакту
#         for contact in contacts:
#             writer.writerow(contact)

# def read_contacts_from_file(filename):
#     contacts = []
#     with open(filename, 'r', newline='') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             # Перетворення favorite з рядка в логічний тип
#             row["favorite"] = row["favorite"].lower() == 'true'
#             contacts.append(row)
#     return contacts

# # Приклад використання:
# contacts_list = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     # Додайте інші контакти за необхідності
# ]

# # Запис у файл
# write_contacts_to_file('contacts.csv', contacts_list)

# # Читання з файлу
# read_contacts = read_contacts_from_file('contacts.csv')
# print(read_contacts)

# //================================================================

# import pickle

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite

# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         self.filename = filename
#         if contacts is None:
#             contacts = []
#         self.contacts = contacts

#     def save_to_file(self):
#         with open(self.filename, 'wb') as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, 'rb') as file:
#             return pickle.load(file)

# # Приклад роботи:
# contacts = [
#     Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
#     Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False),
# ]

# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()

# person_from_file = persons.read_from_file()

# print(persons == person_from_file)  # False
# print(persons.contacts[0] == person_from_file.contacts[0])  # False
# print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
# print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
# print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True

# //================================================================

# import pickle

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite

# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         self.filename = filename
#         if contacts is None:
#             contacts = []
#         self.contacts = contacts
#         self.count_save = 0  # Доданий атрибут count_save

#     def save_to_file(self):
#         with open(self.filename, 'wb') as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, 'rb') as file:
#             return pickle.load(file)

#     def __getstate__(self):
#         state = self.__dict__.copy()
#         state['count_save'] += 1
#         return state

# # Приклад роботи:
# contacts = [
#     Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
#     Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False),
# ]

# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()
# first = persons.read_from_file()
# first.save_to_file()
# second = first.read_from_file()
# second.save_to_file()
# third = second.read_from_file()

# print(persons.count_save)  # 0
# print(first.count_save)  # 1
# print(second.count_save)  # 2
# print(third.count_save)  # 3

# //================================================================

# import pickle

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite

# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         self.filename = filename
#         if contacts is None:
#             contacts = []
#         self.contacts = contacts
#         self.count_save = 0
#         self.is_unpacking = False  # Доданий атрибут is_unpacking

#     def save_to_file(self):
#         with open(self.filename, 'wb') as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, 'rb') as file:
#             return pickle.load(file)

#     def __getstate__(self):
#         state = self.__dict__.copy()
#         state['count_save'] += 1
#         return state

#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         self.is_unpacking = True

# # Приклад роботи:
# contacts = [
#     Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
#     Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False),
# ]

# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()
# person_from_file = persons.read_from_file()
# print(persons.is_unpacking)  # False
# print(person_from_file.is_unpacking)  # True

# //================================================================

# import copy

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite

# def copy_class_person(person):
#     return copy.copy(person)

# # Приклад коду:
# person = Person(
#     "Allen Raymond",
#     "nulla.ante@vestibul.co.uk",
#     "(992) 914-3792",
#     False,
# )

# copy_person = copy_class_person(person)

# print(copy_person == person)  # False
# print(copy_person.name == person.name)  # True

# //================================================================

# import copy
# import pickle

# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite

# def copy_class_person(person):
#     return copy.copy(person)

# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename = filename
#         self.contacts = contacts
#         self.is_unpacking = False
#         self.count_save = 0

#     def save_to_file(self):
#         with open(self.filename, "wb") as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, "rb") as file:
#             content = pickle.load(file)
#         return content

#     def __getstate__(self):
#         attributes = self.__dict__.copy()
#         attributes["count_save"] = attributes["count_save"] + 1
#         return attributes

#     def __setstate__(self, value):
#         self.__dict__ = value
#         self.is_unpacking = True

# def copy_class_contacts(contacts):
#     return copy.deepcopy(contacts)

# # Приклад коду:
# contacts = [
#     Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
#     Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False),
# ]

# persons = Contacts("user_class.dat", contacts)

# new_persons = copy_class_contacts(persons)

# new_persons.contacts[0].name = "Another name"

# print(persons.contacts[0].name)  # Allen Raymond
# print(new_persons.contacts[0].name)  # Another name

# //================================================================

import copy
import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        return Person(self.name, self.email, self.phone, self.favorite)

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        # "Поверхнева" копія об'єкта (не копія елементів в списку)
        return Contacts(self.filename, self.contacts)

    def __deepcopy__(self, memo):
        # Глибока копія об'єкта (включаючи копії елементів у списку)
        copied_contacts = Contacts(self.filename, copy.deepcopy(self.contacts, memo))
        copied_contacts.is_unpacking = self.is_unpacking
        copied_contacts.count_save = self.count_save
        return copied_contacts
