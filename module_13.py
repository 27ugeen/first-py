# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# point = Point(5, 10)
# print(point.x)  # 5
# print(point.y)  # 10

# //================================================================

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, value):
#         self.__x = value

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, value):
#         self.__y = value

# # Приклад використання:
# point = Point(5, 10)

# print(point.x)  # 5
# print(point.y)  # 10

# # Використання setter
# point.x = 15
# point.y = 20

# print(point.x)  # 15
# print(point.y)  # 20

# //================================================================

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if type(x) in (int, float):
#             self.__x = x
          

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if type(y) in (int, float):
#             self.__y = y
            

# # Приклад використання:
# point = Point("a", 10)

# print(point.x)  # None
# print(point.y)  # 10

# # Встановлення нових значень з правильним типом
# point.x = 5
# point.y = 20

# print(point.x)  # 5
# print(point.y)  # 20

# # Встановлення нових значень з неправильним типом
# point.x = "b"
# point.y = "c"

# print(point.x)  # None
# print(point.y)  # None

# //================================================================

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         elif index == 1:
#             return self.coordinates.y
#         else:
#             raise IndexError("Vector index out of range")

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         elif index == 1:
#             self.coordinates.y = value
#         else:
#             raise IndexError("Vector index out of range")

# # Приклад використання:
# vector = Vector(Point(1, 10))

# print(vector.coordinates.x)  # 1
# print(vector.coordinates.y)  # 10

# vector[0] = 10  # Встановлюємо координату x вектора 10

# print(vector[0])  # 10
# print(vector[1])  # 10

# //================================================================

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"


# # Приклад використання:
# point = Point(1, 10)
# vector = Vector(point)

# print(point)  # Point(1,10)
# print(vector)  # Vector(1,10)

# //================================================================

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value is None:
#             return self.coordinates.x, self.coordinates.y
#         elif isinstance(value, (int, float)):
#             return self.coordinates.x * value, self.coordinates.y * value
#         else:
#             raise ValueError("Invalid argument. Must be a number.")

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

# # Приклад використання:
# vector = Vector(Point(1, 10))

# print(vector())  # (1, 10)
# print(vector(5))  # (5, 50)

# //================================================================

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, other):
#         if isinstance(other, Vector):
#             new_x = self.coordinates.x + other.coordinates.x
#             new_y = self.coordinates.y + other.coordinates.y
#             return Vector(Point(new_x, new_y))
#         else:
#             raise TypeError("Unsupported operand type. Must be Vector.")

#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             new_x = self.coordinates.x - other.coordinates.x
#             new_y = self.coordinates.y - other.coordinates.y
#             return Vector(Point(new_x, new_y))
#         else:
#             raise TypeError("Unsupported operand type. Must be Vector.")

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

# # Приклад використання:
# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(10, 10))

# vector3 = vector2 + vector1
# vector4 = vector2 - vector1

# print(vector3)  # Vector(11,20)
# print(vector4)  # Vector(9,0)

# //================================================================

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         return self.coordinates.x * vector.coordinates.x + self.coordinates.y * vector.coordinates.y

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

# # Приклад використання:
# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(10, 10))

# scalar = vector2 * vector1

# print(scalar)  # 110

# //================================================================

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         return (
#                 self.coordinates.x * vector.coordinates.x
#                 + self.coordinates.y * vector.coordinates.y
#         )

#     def len(self):
#         return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

# # Приклад використання:
# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(10, 10))

# print(vector1.len())  # 10.04987562112089
# print(vector2.len())  # 14.142135623730951

# //================================================================

# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             self.coordinates.x = self.coordinates.x * value
#             self.coordinates.y = self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.y - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         return (
#             self.coordinates.x * vector.coordinates.x
#             + self.coordinates.y * vector.coordinates.y
#         )

#     def len(self):
#         return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

#     def __eq__(self, vector):
#         return self.len() == vector.len()

#     def __ne__(self, vector):
#         return self.len() != vector.len()

#     def __lt__(self, vector):
#         return self.len() < vector.len()

#     def __gt__(self, vector):
#         return self.len() > vector.len()

#     def __le__(self, vector):
#         return self.len() <= vector.len()

#     def __ge__(self, vector):
#         return self.len() >= vector.len()

# # Приклад використання:
# vector1 = Vector(Point(1, 10))
# vector2 = Vector(Point(3, 10))

# print(vector1 == vector2)  # False
# print(vector1 != vector2)  # True
# print(vector1 > vector2)   # False
# print(vector1 < vector2)   # True
# print(vector1 >= vector2)  # False
# print(vector1 <= vector2)  # True

# //================================================================

from random import randrange


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
            self.coordinates.x * vector.coordinates.x
            + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return self.len() != vector.len()

    def __lt__(self, vector):
        return self.len() < vector.len()

    def __gt__(self, vector):
        return self.len() > vector.len()

    def __le__(self, vector):
        return self.len() <= vector.len()

    def __ge__(self, vector):
        return self.len() >= vector.len()


class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = [
            Vector(Point(randrange(max_points + 1), randrange(max_points + 1)))
            for _ in range(max_vectors)
        ]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.vectors):
            raise StopIteration
        else:
            vector = self.vectors[self.current_index]
            self.current_index += 1
            return vector


class RandomVectors:
    def __new__(cls, max_vectors, max_points):
        return Iterable(max_vectors, max_points)


# Приклад використання:
vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)
