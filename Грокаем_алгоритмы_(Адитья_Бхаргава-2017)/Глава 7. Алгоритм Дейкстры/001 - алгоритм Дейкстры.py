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