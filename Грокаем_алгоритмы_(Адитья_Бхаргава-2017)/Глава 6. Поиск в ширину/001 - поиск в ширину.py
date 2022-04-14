'''
Алгоритм для решения задачи поиска кратчайшего пути называется поиском в ширину.
Два вопроса, на которые может ответить алго­ритм поиска в ширину:
    вопрос 1:
        существует ли путь от узла А к узлу В?
    вопрос 2:
        как выглядит кратчайший путь от узла А к узлу В?
'''

# создание графа 1
# создание хеш-таблицы (словаря)
graph = {}
graph["you"] = ["claire", "alice", "bob"]
# вывод соседних узлов
print(graph["you"])

# создание графа 2
# создание хеш-таблицы (словаря)
# В хеш-таблицах эле­менты не упорядочены, 
    # поэтому добавлять пары ключ-значение - можно в любом порядке.
graph = {}
graph["you"] = ["claire", "alice", "bob"]
graph["claire"] = ["tom", "jonny"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["tom"] = []
graph["jonny"] = []
graph["peggy"] = []
graph["anuj"] = []
# вывод всего графа
print(graph)

# импорт модуля - очередь
from collections import deque
# создаем очередь
search_deque = deque()
# заполняем очередь
search_deque += graph["you"]
# search_deque += graph["claire"]
# search_deque += graph["alice"]
# search_deque += graph["bob"]
# search_deque += graph["tom"]
# search_deque += graph["jonny"]
# search_deque += graph["peggy"]
# search_deque += graph["anuj"]
# вывод очереди
print(search_deque)

# функция - искомый конечный узел
def person_is_seller(name):
    return "m" == name[-1]

# алгоритм поиска в ширину
def breadth_first_search(deque):
    # создаем локальную очередь
    search_deque = deque
    # пока очередь не пуста
    while search_deque:
        # из очереди извлекается первый человек
        person = search_deque.popleft()
        # проверяем, является ли этот человек 
        # продавцом манго
        if person_is_seller(person):
            # да, это продавец манго
            print(f"{person} is a mango seller")
            return True
        else:
            # не, не является. 
            # все друзья этого человека добавляются в 
            # очередь списка
            search_deque += graph[person]
    # в очереди нет продавца манго
    return False

# вызов алгоритма поиска в ширину
breadth_first_search(search_deque)