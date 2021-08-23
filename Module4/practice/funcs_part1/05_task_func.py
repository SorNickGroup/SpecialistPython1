# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def can_triangle(p1, p2, p3):
    a = distance(*p2, *p1)
    b = distance(*p2, *p3)
    c = distance(*p3, *p1)
    return a + b > c and a + c > b and b + c > a

def triangle_square(p1, p2, p3):
    a = distance(*p2, *p1)
    b = distance(*p2, *p3)
    c = distance(*p3, *p1)
    return 1/4*(4*a**2*b**2-(a**2+b**2-c**2)**0.5)**0.5

def triangle_perim(p1, p2, p3):
    a = distance(*p2, *p1)
    b = distance(*p2, *p3)
    c = distance(*p3, *p1)
    return a+b+c

point1=10, 12
point2=14, 18
point3=12, 12
if can_triangle(point1,point2,point3)==True:
    print(f"Площадь треугольника = {triangle_square(point1,point2,point3):.2f}, периметр = {triangle_perim(point1,point2,point3):.2f}")
else:
    print("По заданным точкам треугольник построить нельзя")
