spam = ['яблоки', 'бананы', 'тофу', 'коты']
# 1
def func (arr: list) -> str:
    if arr:
        res = ', '.join(arr)
        idx = res.rfind(', ')
        return res[:idx] + ' и ' + arr[-1]
    return ''

# 2
def func (arr: list) -> str:
    s = ''
    for i, w in enumerate(arr):
        if 0 == i:
            s += w
        elif i == len(arr)-1:
            s += ' и ' + w
        else:
            s += ', ' + w
    return s 

if __name__:
    print(func(spam))
    print(func([]))