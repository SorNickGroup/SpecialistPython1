# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def get_count_items_on_end_page(num_items, items_on_page):
    count = num_items % items_on_page
    if count == 0:
        count += items_on_page
    return count


print(get_count_items_on_end_page(2, 3))
print(get_count_items_on_end_page(21, 3))
