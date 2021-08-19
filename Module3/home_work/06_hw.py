# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

i=0
brands=[]
current_brand=""
while i<len(items):
    current_brand=items[i].get("brand")
    if(brands.count(current_brand)==0):
        brands.append(current_brand)
    i+=1
print(brands);

print("На складе больше всего товаров брэнда(ов): ")

i=0
max_count_goods_brand=0
brands_count_goods={}
brands_max_goods=[]
while i<len(items):
    current_brand=items[i].get("brand")
    count=brands_count_goods.setdefault(current_brand, 0) +1
    brands_count_goods[current_brand]=count
    if max_count_goods_brand<count :
        max_count_goods_brand=count       
    i+=1
for key, value in brands_count_goods.items():
    if value==max_count_goods_brand:
        brands_max_goods.append(key)
print(brands_max_goods)

print("На складе самый дорогой товар брэнда(ов): ")

i=0
max_price=0
dict_brands_max_price={}
max_price_brands=[]
while i<len(items):
    current_brand=items[i].get("brand")
    price=items[i].get("price")
    dict_brands_max_price[current_brand]=price
    if max_price<price :
        max_price=price       
    i+=1
for key, value in dict_brands_max_price.items():
    if value==max_price:
        max_price_brands.append(key)
print(max_price_brands)
