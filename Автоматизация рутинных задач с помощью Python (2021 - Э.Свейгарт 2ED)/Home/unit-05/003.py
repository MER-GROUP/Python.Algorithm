def add_to_inventory(inventory: dict, added_items: list) -> dict:
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    print(f'Инвентарь:')
    for k, v in sorted(inventory.items()):
        print(f'  {k} - {v}')
    print(f'Всего элементов: {sum(inventory.values())}')

    return inventory


if __name__:
    inv = {
        'золотая монета': 42,
        'веревка': 1
    }

    dragon_loot = [
        'золотая монета',
        'кинжал',
        'золотая монета',
        'золотая монета',
        'рубин'
    ]

    add_to_inventory(inv, dragon_loot)