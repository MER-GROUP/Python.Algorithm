def is_valid_chess_board(_dict: dict) -> bool:
    figures = ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king')
    colour = ('w', 'b')
    desk = {}

    for k, v in _dict.items():
        print(desk) # test
        if not (1 <= int(k[0]) <= 8) and not ('a' <= k[-1] <= 'h'):
            return False
        elif 2 < len(k):
            return False
        elif 16 == len(desk):
            return False
        elif (k in desk) or (v in desk.values()):
            return False
        elif (v[0] not in colour) and (v[1:] not in figures):
            return False
        desk.setdefault(k, v)
    else:
        return True

if __name__:
    print(is_valid_chess_board({'1h': 'bking', '1a': 'wking'}))