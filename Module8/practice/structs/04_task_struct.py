# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один
union_dict = dictionary_1.copy()
union_dict.update(dictionary_2)

print(union_dict)
