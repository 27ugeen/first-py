# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

# # Створення екземпляру класу Animal
# animal = Animal(name="Leo", species="Lion")

# # Виведення деякої інформації про екземпляр
# print(f"Animal's name: {animal.name}")
# print(f"Animal's species: {animal.species}")

# //================================================================

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         # Покищо використовуємо оператор pass, можна додати реалізацію звуку тварини тут
#         pass

# # Створення екземпляру класу Animal
# animal = Animal(nickname="Fluffy", weight=10)

# # Доступ до властивостей об'єкта
# print(f"Animal's nickname: {animal.nickname}")
# print(f"Animal's weight: {animal.weight}")

# # Виклик методу say
# animal.say()

# //================================================================

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, new_weight):
#         self.weight = new_weight

# # Створення екземпляру класу Animal
# animal = Animal("Simon", 10)

# # Доступ до властивостей об'єкта
# print(f"Animal's nickname: {animal.nickname}")
# print(f"Animal's weight: {animal.weight}")

# # Виклик методу change_weight
# animal.change_weight(12)

# # Перевірка зміненої ваги
# print(f"Animal's new weight: {animal.weight}")

# //================================================================

# class Animal:
#     color = "white"

#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

#     def change_color(self, new_color):
#         Animal.color = new_color

# # Створення екземплярів класу Animal
# first_animal = Animal("Fluffy", 15)
# second_animal = Animal("Buddy", 20)

# # Виведення початкових значень змінної color для обох екземплярів
# print(f"First Animal's color: {first_animal.color}")
# print(f"Second Animal's color: {second_animal.color}")

# # Виклик методу change_color для зміни значення змінної класу color для першого екземпляру
# first_animal.change_color("red")

# # Виведення змінених значень змінної color для обох екземплярів
# print(f"First Animal's color after change: {first_animal.color}")
# print(f"Second Animal's color after change: {second_animal.color}")

# //================================================================

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

# class Cat(Animal):
#     def say(self):
#         return "Meow"

# # Створення екземпляру класу Cat
# cat = Cat("Simon", 10)

# # Виведення інформації про кота
# print(f"Cat's nickname: {cat.nickname}")
# print(f"Cat's weight: {cat.weight}")

# # Виклик методу say для кота
# cat_sound = cat.say()
# print(f"Cat says: {cat_sound}")

# //================================================================

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

# class Dog(Animal):
#     def __init__(self, nickname, weight, breed):
#         super().__init__(nickname, weight)
#         self.breed = breed

#     def say(self):
#         return "Woof"

# # Створення екземпляру класу Dog
# dog = Dog("Barbos", 23, "labrador")

# # Виведення інформації про собаку
# print(f"Dog's nickname: {dog.nickname}")
# print(f"Dog's weight: {dog.weight}")
# print(f"Dog's breed: {dog.breed}")

# Виклик методу say для собаки
# dog_sound = dog.say()
# print(f"Dog says: {dog_sound}")

# //================================================================

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Owner:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def info(self):
#         return {'name': self.name, 'age': self.age, 'address': self.address}


# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner):
#         self.breed = breed
#         self.owner = owner
#         super().__init__(nickname, weight)

#     def say(self):
#         return "Woof"

#     def who_is_owner(self):
#         return self.owner.info()


# # Створення екземпляра класу Owner
# dog_owner = Owner("John Doe", 35, "123 Main Street")

# # Створення екземпляра класу Dog з власником
# dog = Dog("Buddy", 20, "Labrador", dog_owner)

# # Виведення інформації про собаку та власника
# print(f"Dog's nickname: {dog.nickname}")
# print(f"Dog's weight: {dog.weight}")
# print(f"Dog's breed: {dog.breed}")

# # Виклик методу who_is_owner для отримання інформації про власника
# owner_info = dog.who_is_owner()
# print("Owner's info:")
# print(f"Name: {owner_info['name']}")
# print(f"Age: {owner_info['age']}")
# print(f"Address: {owner_info['address']}")


# //================================================================

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class Dog(Animal):
#     def say(self):
#         return "Woof"
    
# class CatDog(Cat, Dog):
#     def info(self):
#         return f"{self.nickname}-{self.weight}"

# class DogCat(Dog, Cat):
#     def info(self):
#         return f"{self.nickname}-{self.weight}"

# # Приклад використання
# cat_dog_instance = CatDog("Fluffy", 5)
# dog_cat_instance = DogCat("Buddy", 10)

# # Виведення інформації про екземпляри
# print("CatDog info:", cat_dog_instance.info())
# print("DogCat info:", dog_cat_instance.info())

# # Виклик методу say для отримання звуків
# print("CatDog says:", cat_dog_instance.say())
# print("DogCat says:", dog_cat_instance.say())

# //================================================================

# from collections import UserDict

# class LookUpKeyDict(UserDict):
#     def lookup_key(data, value):
#         keys = []
#         for key in data:
#             if data[key] == value:
#                 keys.append(key)
#         return keys

# # Приклад використання
# lookup_dict = LookUpKeyDict({'a': 1, 'b': 2, 'c': 1})

# # Виклик методу lookup_key класу LookUpKeyDict
# result_keys = LookUpKeyDict.lookup_key(lookup_dict, 1)

# # Виведення результату
# print("Keys with value 1:", result_keys)

# //================================================================

# from collections import UserList

# class AmountPaymentList(UserList):
#     def amount_payment(payment):
#         sum = 0
#         for value in payment:
#             if value > 0:
#                 sum = sum + value
#         return sum

# //================================================================

# from collections import UserString

# class NumberString(UserString):
#     def number_count(self):
#         count = sum(char.isdigit() for char in self.data)
#         return count

# # Приклад використання
# num_string = NumberString("Hello123World456")
# count_of_numbers = num_string.number_count()

# print("Number of digits:", count_of_numbers)

# //================================================================

# class IDException(Exception):
#     pass

# def add_id(id_list, employee_id):
#     if not employee_id.startswith('01'):
#         raise IDException("Employee ID must start with '01'")
    
#     id_list.append(employee_id)
#     return id_list

# # Приклад використання
# employee_ids = ['0101', '0123', '0222']

# try:
#     new_ids = add_id(employee_ids, '0345')  # Це викличе виняток, оскільки '0345' не починається з '01'
# except IDException as e:
#     print(f"Error: {e}")

# new_ids = add_id(employee_ids, '0111')  # Це додасть '0111' до списку, оскільки відповідає умовам
# print("Updated ID list:", new_ids)


# //================================================================

# Something wrong! Check
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class CatDog:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         return self.cat.say()

#     def change_weight(self, weight):
#         self.cat.change_weight(weight)

# //================================================================

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, contact_id):
        self.contacts = list(filter(lambda contact: contact["id"] != contact_id, self.contacts))
        
        
            