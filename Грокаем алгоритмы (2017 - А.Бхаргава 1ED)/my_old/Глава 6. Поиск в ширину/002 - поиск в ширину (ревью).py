'''
Алгоритм для решения задачи поиска кратчайшего пути называется поиском в ширину.
Два вопроса, на которые может ответить алго­ритм поиска в ширину:
    вопрос 1:
        существует ли путь от узла А к узлу В?
    вопрос 2:
        как выглядит кратчайший путь от узла А к узлу В?
'''

# создание графа
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

# функция - искомый конечный узел (продавец манго)
def person_is_seller(name):
    return "m" == name[-1]

# функция - алгоритм поиска в ширину
def breadth_first_search(name):

    # импорт модуля - очередь
    from collections import deque
    # создаем очередь
    search_deque = deque()
    # заполняем очередь
    search_deque += graph[name]
    # список проверенных людей
    searched = list()

    # пока очередь не пуста
    while search_deque:
        # из очереди извлекается первый человек
        person = search_deque.popleft()
        # если человек раньше не проверялся
        if not person in searched:
            # проверяем, является ли этот человек 
            # продавцом манго
            if person_is_seller(person):
                # да, это продавец манго
                print(f"{person} is a mango seller")
                return True
            else:
                # нет, не является. 
                # все друзья этого человека добавляются в 
                # очередь списка
                search_deque += graph[person]
                # добавляем человека в список проверенных
                searched.append(person)
    # в очереди нет продавца манго
    return False

# вызов алгоритма поиска в ширину
breadth_first_search("you")