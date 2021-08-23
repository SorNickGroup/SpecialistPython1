# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

a= 0,0
b= -5,1
c= 4,-1

tri_sides=[]
tri_sides.append({"name":"AB", "dist":distance(*a,*b)})
tri_sides.append({"name":"AC", "dist":distance(*a,*c)})
tri_sides.append({"name":"BC", "dist":distance(*b,*c)})
print(tri_sides)
min_side=tri_sides[0];
for side in tri_sides:
    if min_side["dist"] > side["dist"]:
        min_side = side
print("Самый короткий отрезок: ", min_side["name"])  # Выводим название отрезка, например “АС”.
