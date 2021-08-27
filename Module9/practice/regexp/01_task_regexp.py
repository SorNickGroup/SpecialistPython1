# Дано произвольное предложение. Слова разделены пробелами. Предложение содержит знаки препинания.
# Найдите:
# 1) первое слово из строки
# 2) первые два символа каждого слова
# 3) все слова начинающиеся на гласную букву
# 4) все слова начинающиеся на согласную букву
# 5) все уникальные(без дубликатов) знаки препинания

import re

text = "Why do we use it? It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."

template = r"^[A-Z]\w+"
res = re.findall(template, text)
print(res)
template = r"\b\w{2}"
res = re.findall(template, text)
print(res)
template = r"\b[aeiouy]\w+"
res = re.findall(template, text)
print(res)
template = r"([^\w\s'])\s"
res = re.findall(template, text)
print(set(res))
