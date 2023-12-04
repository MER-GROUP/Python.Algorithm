import pprint

mydict = {5: '555', 4: '444', 3: '333', 2: '222', 1: '111'}

pprint.pprint(mydict, width=20)
print(pprint.pformat(mydict, width=20))
print(mydict)