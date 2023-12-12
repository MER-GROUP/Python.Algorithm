def display_inventory(inventory: dict) -> None:
    print("Инвентарь:")
    item_total = 0
    # for k, v in sorted(inventory.items()):
    # for k, v in sorted(inventory.items(), key=lambda x: (x[0],[1])):
    for k, v in sorted(inventory.items(), key=lambda x: x[0]):
        print(f'  {k} = {v}')
    print("Всего элементов: " + str(item_total))

if __name__:
    stuff = {
        'веревка': 1,
        'факел': 6,
        'золотая монета': 42,
        'кинжал': 1,
        'стрела': 12
    }
    display_inventory(stuff)