# 1. Объявите класс Calendar для хранения даты: день, месяц, год.
# Определите свойства для записи и считывания этой информации из этого класса.
# (Дополнение: используя __slots__ разрешите использовать только строго определенные локальные свойства в экземплярах класса).


#  Создадим в конструкторе три private атрибута (можно обращаться только внутри класса) ●  __<имя атрибута> (с двумя подчеркиваниями)
class Calendar:
    def __init__(self, x = 0, y = 0, z = 0):       # объявлен один конструктор
        self.__x = x
        self.y = y
        self.__z = z

    # Внутри класса Calendar создадим спец. метод -  для записи другого значения, если хотим изменить координату
    # Получился метод публичный, открытый setCorrds через который мы можем менять значение закрытых атрибутов __x, __y, __z
    def setDate(self, x, y, z):           # set - сеттер - означает установить, задать, координату Corrds, два параметра x, y
        self.__x = x                      # внутри метода setCorrds через два параметра мы можем обращаться к этим закрытым св-вам
        self.y = y
        self.__z = z

    # Внутри класса Point1 создадим спец. метод -  для записи другого значения, если хотим изменить координату
        # Получился метод публичный, открытый getCorrds через который мы можем менять значение закрытых атрибутов __x, __y
    def getDate(self):                       # get - геттер
        return self.__x, self.y, self.__z  # будем возвращать кортеж этих значений

pt = Calendar(12, 8, 2021)                          # вызвали конструктор, когда создали экземпляр классa pt
print( pt.getDate() )                               # вызов метода getDate - возвращает кортеж этих значений
pt.y = "08"                                         # чтобы програмист не мог изменять атрибуты x, y  экземпляра класса pt ИЗ ВНЕ - их следует делать закрытыми
print( pt.getDate() )                               # выведем в консоль измененные атрибуты x, y  экземпляра класса pt

pt.setDate(14, 9, 2021)                             # вызов метода setDate с тремя аргументами
print( pt.getDate())                                # вызов метода getDate - возвращает кортеж этих значений
                                                    # с помощью публичных методов setDate и getDate мы можем задавать и выводить (получать)
                                                    # соответствующие локальные св-ва экземпляра класса pt

######################################################################################################

class Calendar2:
    _slots_ = ["__d", "__m", "__y"]
    def __init__(self, d, m, y):
        if Calendar2.__check(d, m, y):
            self.__d = d
            self.__m = m
            self.__y = y
        else:
            raise ValueError('Неверный формат')

    def getDate(self):
        return f'Дата: {self.__d}.{self.__m}.{self.__y}'

    def __check(d,m,y):
            if isinstance(d, int) and d < 32 and isinstance(m, int) and m <= 12\
               and isinstance(y, int):
                return True
            return False


    def setDate(self, d, m, y):
        if Calendar2.__check(d,m,y):
            self.__d = d
            self.__m = m
            self.__y = y
        else:
            raise ValueError('Неверный формат')

pt2 = Calendar2(2, 6, 2021)
print( pt2.getDate())

######################################################################################################

class Calendar3:

    _slots_ = ['__day','__month','__year','__date']

    def __date_validator(day, month, year):
        return isinstance(day,int) and 0 < day < 32 and isinstance(month,int) and  0 < month < 13 and\
                        isinstance(year,int) and 0 <= year


    def __init__(self, day = 3, month = 12, year = 2008):
        if Calendar3.__date_validator(day, month, year):
            self.__day = day
            self.__month = month
            self.__year = year
            self.__date = {'day': self.__day, 'month': self.__month, 'year': self.__year}
        else:
            raise Exception("All characters should be integers and at right range!(day,month,year)")


    def date_getter(self):
        return self.__date


    def date_setter(self, day, month, year):
        if Calendar3.__date_validator(day, month, year):
            self.__day = day
            self.__month = month
            self.__year = year
            self.__date = {'day': self.__day, 'month': self.__month, 'year': self.__year}
        else:
            print("All characters should be integers and at right range!(day,month,year)")

d_test = Calendar3(30,2,2020)
print(d_test.date_getter())

#############################################################################################


# ЗАДАНИЕ 1.
# (Дополнение: используя _slots_ разрешите использовать только строго определенные
# локальные свойства в экземплярах класса).
# (Поскольку использование _slots_ исключает применение дескриптора, основанного на словарных
# значениях, я запретила свободное назначение аргументов извне, можно только через метод setDate())

class Calendar4:
    """Класс для хранения даты: день, месяц, год."""

    _slots_ = ('__day', '__month', '__year')

    def __checkValue(x):
        return isinstance(x, int)

    def __init__(self, day=0, month=0, year=0):
        for elem in [day, month, year]:
            if Calendar4.__checkValue(elem):
                self.__day = day
                self.__month = month
                self.__year = year
            else:
                raise AttributeError

    def getDate(self):
        if self.__month > 9:
            return f'сегодня {self.__day}/{self.__month}/{self.__year}'
        else:
            return f'сегодня {self.__day}/0{self.__month}/{self.__year}'

    def setDate(self, day, month, year):
        if Calendar4.__checkValue(day) and Calendar4.__checkValue(month) and Calendar4.__checkValue(year):
            self.__day = day
            self.__month = month
            self.__year = year
#        else:
 #           raise AttributeError("Координаты должны быть числами")


date = Calendar4(9, 7, 1988)
#print(date.month)  # проверяем приватность (получили ошибку)

print(date.getDate())
date.setDate(5, 22, 1999)
print(date.getDate())
date.setDate(26, '7', 1973)  # пытаемся ввести не число
# получили ошибку
print(date.getDate())  # убеждаемся, что дату изменить не удалось

# пробуем добавить атрибут
date.minute = 59
print(date.minute)

