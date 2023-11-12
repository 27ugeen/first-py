# print("Hello world")

# print("Hello Git")

# a = None

# print(f"first a {a}")

# a = "string"

# print(f"second a {a}")

# a = 5

# print(f"third a {a}")


# first_name = "Margo"
# last_name = "Robbie"
# full_name = f"{first_name} {last_name}"

# a = -2 + 3j
# b = 4 + 2.1j
# result = a + b
# print(result)

# import math

# a = -2
# b = 7
# c = -6
# D = b
# x1 =
# x2 =


# a = input('Введіть число')
# a = int(a)
# if a > 0:
#     print('Число додатне')
# elif a == 1:
#     print('Число дорівнює 1')
# else:
#     print("a <= 0")

# fruit = "apple"

# for i in fruit:
#     print(i)

# a = 5

# while a < 10:
#     print(a)
#     a += 1


# while True:
#     user_input = input("enter exit:")
#     print(user_input)
#     if user_input == "exit":
#         break

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break

# val = 'abc'
# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(val > 0)
# finally:
#     print("This will be printed anyway")


# def printNumber(a,b):
#     if a > b:
#         print("a is greater than b")
#     elif a == b:
#         print("a is equal b")
#     else:
#         print("a is less than b")

# printNumber(2,4)
# printNumber(2, 3.5)

# def sum(a,b):
#     return a**b

# print(sum(2,3))

# def factorial(n):
#     if n <= 1:
#         r = 1
#     else:
#         r = n * factorial(n - 1)  
#     return r
    
# print(factorial(5))

# import math

# sinPi = math.sin(math.pi)
# print(sinPi)

# def say_hello(name):
#     print(f'Hello {name}')



# def main():
#     print("You imported hello.py")
#     say_hello('user')

# # for arg in sys.argv:
# #     print(arg)
# if __name__ == '__main__':
#     main()

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num > 0:
#     sum += num
#     num -= 1
    
# print(sum)

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = first if (first < second) else second

# while first%gcd != 0 or second%gcd != 0:
#     gcd -= 1
#     print(gcd)

# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num != 0:
#     for el in range(num +1):
#         sum += el   
#     num = int(input("Enter integer (0 for output): "))

# print(sum)

# def first(size, *args):
#     # Використовуємо *args для збору позиційних аргументів
#     return size + sum(args)

# def second(size, **kwargs):
#     # Використовуємо **kwargs для збору ключових аргументів
#     return size + sum(kwargs.values())

# # Приклади використання
# result1 = first(5, "first", "second", "third")
# print(result1)  # Результат: 14 (5 + 3 + 4 + 3)

# result2 = first(1, "Alex", "Boris")
# print(result2)  # Результат: 9 (1 + 4 + 5)

# result3 = second(3, comment_one="first", comment_two="second", comment_third="third")
# print(result3)  # Результат: 13 (3 + 3 + 6 + 4)

# result4 = second(10, comment_one="Alex", comment_two="Boris")
# print(result4)  # Результат: 20 (10 + 4 + 5)


def cost_delivery(quantity, *_, discount=0):
    if discount < 0 or discount > 1:
        raise ValueError("Знижка повинна бути від 0 до 1")

    first_item_price = 5
    additional_item_price = 2

    total_price = first_item_price + (quantity - 1) * additional_item_price

    if discount > 0:
        total_price = total_price * (1 - discount)

    return total_price

    
res = cost_delivery(2, 1, 2, 3)
print(res)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Приклади використання
n = 10  # Виберіть бажаний номер члена ряду Фібоначчі
result = fibonacci(n)
print(f"Член ряду Фібоначчі під номером {n} дорівнює {result}")
