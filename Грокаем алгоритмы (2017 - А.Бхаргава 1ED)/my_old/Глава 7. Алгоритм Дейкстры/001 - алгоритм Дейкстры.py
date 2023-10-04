# алгоритм Дейкстры (Edsger Wybe Dijkstra)
# алгоритм Дейкстры состоит из четырех шагов:
    # 1. Найти узел с наименьшей стоимостью (то есть узел, до которого можно
    # добраться за минимальное время).
    # 2. Проверить, существует ли более дешевый путь к соседям этого узла,
    # и если существует, обновить их стоимости.
    # 3. Повторять, пока это не будет сделано для всех узлов графа.
    # 4. Вычислить итоговый путь.
# В алгоритме Дейкстры каждому сегменту присваивается число (вес), 
# а ал­горитм Дейкстры находит путь с наименьшим суммарным весом.

'''
Шпаргалка
1. Поиск в ширину вычисляет кратчайший путь в невзвешенном графе.
2. Алгоритм Дейкстры вычисляет кратчайший путь во взвешенном графе.
3. Алгоритм Дейкстры работает только в том случае, если все веса поло­жительны.
4. При наличии отрицательных весов используйте алгоритм Беллмана­-Форда.
'''

graph = dict()
graph['start'] = dict()
graph['start']['a'] = 6
graph['start']['b'] = 2
# вывод ключей графа (узлов)
print("graph.keys() =", graph.keys())
# вывод ключей графа ключа start (соседей начального узла)
print("graph['start'].keys() =", graph['start'].keys())
# узнать веса ребер
print("graph['start']['a'] =", graph['start']['a'])
print("graph['start']['b'] =", graph['start']['b'])
# Включим в граф остальные узлы и их соседей
graph['a'] = dict()
graph['a']['fin'] = 1
graph['b'] = dict()
graph['b']['a'] = 3
graph['b']['fin'] = 5
# У конечного уэла нет соседей
graph['fin'] = dict()
# print("graph['fin'].keys() =", graph['fin'].keys())
# print("type(graph['fin'].keys()) =", type(graph['fin'].keys()))

# Код создания таблицы стоимостей costs
# определение бесконечност
infinity = float('inf')
# print('infinity =', infinity)
# таблица стоимости
costs = dict()
# определение стоимостей
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# Код создания таблицы родителей parents
parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# Список для отслеживания всех уже обработанных уз­лов
processed = list()

# Найти узел с наименьшей стоимостью
# среди необработанных
def find_lowest_cost_node(costs):
    # назначаем максимальную стоимость узла
    lowest_cost = float('inf')
    # узел с наименьшей стоимостью
    lowest_cost_node = None
    # перебираем узлы в хэш-таблице стоимость (costs)
    for node in costs:
        # получаем стоимость текущего узла
        cost = costs[node]
        # если этот узел с наименьшей стоимостью
        # из уже виденных и он еще не был обработан...
        if cost < lowest_cost and node not in processed:
            # ...он назначается новым кзлом
            # с ноименьшей стоимостью
            # (обновляем наименьшую стоимость)
            lowest_cost = cost
            # обновляем узел с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node

# Найти узел с наименьшей стоимостью
# среди необработанных
node = find_lowest_cost_node(costs)
# test
print('test node =', node)

# если обработаны все узлы
# то цикл while завершен
while node is not None:
    # берем стоимость узла
    cost = costs[node]
    # берем соседей узла
    neighbors = graph[node]
    # перебрать всех соседей текущего узла
    for n in neighbors.keys():
        # узнаем стоимость до соседа
        new_cost = cost + neighbors[n]
        # если к соседу можно быстрее добраться 
        # через текущий узел
        if costs[n] > new_cost:
            # то обновить стоимость для этого узла
            costs[n] = new_cost
            # этот узел становится новым родителем для соседа
            parents[n] = node
    # узел помечается как обработанный
    processed.append(node)
    # найти следующий узел для обработки 
    # и повторить цикл
    node = find_lowest_cost_node(costs)

# test
print('test parents =', parents)
print('test costs =', costs)