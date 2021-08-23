# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def check_circles(x1, y1, r1, x2, y2, r2):
    if r1<r2:
        return distance(x1,y1,x2,y2)+r1<r2
    else:
        return distance(x1,y1,x2,y2)+r2<r1


c1= 0,0,1
c2= 1,1,1
print(check_circles(*c1,*c2))
