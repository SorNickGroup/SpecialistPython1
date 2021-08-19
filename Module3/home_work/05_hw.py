# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

i=0
max_len_word=0
pos_longest_word=-1;
while i<len(names):
    current_len_word=len(names[i])
    if(current_len_word>max_len_word):
        pos_longest_word=i
        max_len_word=current_len_word
    i+=1
print(names[pos_longest_word])
