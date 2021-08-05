
# 2.1. Создайте класс Point3D, который хранит координаты в виде списка.
# Пропишите у него конструктор для создания экземпляров с локальными координатами.
# Также добавьте методы, позволяющие изменять координаты и получать их (в виде кортежа).


# Зададим в классе Point3D метод setCoords
class Point3D:

    # Пропишем конструктор в классе Point3D для создания экземпляров с локальными координатами.
    def __init__(self, x, y, z):    # Передадим через метод __init__ два аргумента
        self.x = x               # в теле метода __init__ создадим две переменные x, y
        self.y = y
        self.z = z

     #   print("Проверка создания экземпляра класса Point3D")  # Проверка создания экземпляра класса Point3D


    "Класс Point3D для хранения координаты в виде списка"
    x = 1
    y = 1
    z = 1

    def setCoords(self, x, y, z): # любой метод объявленный внутри класса имеет параметр self, ( x, y - передали в качестве следующих параметров)
        self.a = x                # с помощью метода setCoords можем переопределять координаты точки класса Point и присвоим переданное значение x, y
        self.b = y
        self.c = z

        print(self.__dict__)      # вывод всех локальных переменных self





print(Point3D, id(Point3D))
lst = [Point3D.x, Point3D.y, Point3D.z]
print(type(lst), lst)


pt = Point3D(Point3D.x, Point3D.y, Point3D.z)  # в момент создания экземпляра класса выполняется ф-ция def __init__(self):, и значит метод  __init__ был выполнен
print(type(pt), pt)

print("constructor __init__:", pt.__dict__)
pt = Point3D(55, 100, 200)             # в момент создания экземпляра класса выполняется ф-ция def __init__(self):, и значит метод  __init__ был выполнен
print("constructor __init__:", pt.__dict__)
pt1 = Point3D(51, 101, 201)
print("constructor __init__:", pt1.__dict__)


j = tuple([Point3D.x, Point3D.y, Point3D.z])
print(j)
jj = tuple([pt.x, pt.y, pt.z])
print(jj)
jjj = tuple([pt1.x, pt1.y, pt1.z])
print(jjj)





#########################################################################

class Point3DD:
    'класс, который хранит координаты в виде списка.'

    def __init__(self, x=0, y=0, z=0):
        'Создание экземпляра класса Point3D'
        self.x, self.y, self.z = x, y, z
        self.lst = [self.x, self.y, self.z]

    def listCoord(self, x=0, y=0, z=0):
        'Изменить координаты и вывести в виде кортежа'
        self.x, self.y, self.z = x, y, z
        self.lst = tuple()
        self.tuple = (self.x, self.y, self.z)
        print(self.tuple)

ptA = Point3DD(6, 7, 9)
print(f'список координат класса Point3DD: {ptA.lst}')
print(f'новый экземпляр с локальными координатами: {ptA.__dict__}')
ptA.listCoord(13, 27, 36)   # Меняем локальные координаты экземпляра и выводим в печать
ptA.x = 500                 # Меняем одну локальную координату для проверки
print(ptA.__dict__)
print("Измененные координаты в виде кортежа: ", (ptA.x, ptA.y, ptA.z) )

