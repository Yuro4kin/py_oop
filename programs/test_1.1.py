
# Объявите класс Point3D для точек с тремя координатами x, y, z.
# Создайте несколько экземпляров этого класса и через них выведите в консоль значения x,y,z.

# Далее, сделайте следующие манипуляции:
# - поменяйте любое значение координаты в классе Point3D и посмотрите как это повлияет на отображаемые величины экземпляров класса;
# - удалите координату z в классе Point3D и убедитесь, что она будет отсутствовать во всех экземплярах;
# - поменяйте координату в каком-либо экземпляре класса и посмотрите на результат.




class Point3D:
    "Класс Point3D для определения точек на плоскости"
    x = 1           #  определили три переменные класса Point
    y = 2
    z = 3

pt = Point3D()
pt1 = Point3D()
pt2 = Point3D()

print( pt.x, pt1.y, pt2.z )
print( id(pt), id(pt1), id(pt2), id(Point3D), sep="\n" )

print( pt.x, pt.y, pt.z )
print( id(pt), id(pt1), id(pt2), id(Point3D), sep="\n" )

Point3D.x = 100
print( pt.x, pt1.y, pt2.z )
print( id(pt), id(pt1), id(pt2), id(Point3D), sep="\n" )
print( pt.x, pt.y, pt.z )
print( id(pt), id(pt1), id(pt2), id(Point3D), sep="\n" )

print(Point3D, Point3D.x, Point3D.y, Point3D.z)
print("x в экземпляре класса также изменился на 100: ", (pt.x, pt.y, pt.z))
print( id(pt), id(Point3D), sep="\n" )
print( "id - pt: " ,id(pt), "id - Point: ", id(Point3D), sep="\n" )

print("Пустая коллекция из локальных переменных в экземпляре класса pt", pt.__dict__)
pt.x = 5
print("Пустая коллекция из локальных переменных в экземпляре класса pt", pt.__dict__)
print( pt.x, pt1.y, pt2.z )
print(Point3D, Point3D.x, Point3D.y, Point3D.z)
print( id(pt), id(pt1), id(pt2), id(Point3D), sep="\n" )
print( pt.x, pt.y, pt.z )
print( id(pt), id(pt1), id(pt2), id(Point3D), sep="\n" )

print(Point3D, Point3D.x, Point3D.y, Point3D.z)