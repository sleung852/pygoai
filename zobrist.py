import random

from pygoai.gotypes import Player, Point

def to_python(player_state):
	if player_state is None:
		return 'None'
	if player_state == Player.black:
		return Player.black
	return Player.white

MAX63 = 0x7fffffffffffffff

table = {}
empty_board = 0
for r in range(1, 20):
	for c in range(1, 20):
		for state in (Player.black, Player.white):
			code = random.randint(0, MAX63)
			table[Point(row, col), state] = code

print('from .gotypes import Player, Point\n')
print("__all__ = ['HASH_CODE', 'EMPTY_BOARD\n']")
print('HASH_CODE = {')
for (pt, state), hash_code in table.items():
	print('    ({}, {}): {},'.format(pt, to_python(state), hash_code))
print('}\n')
print('EMPTY_BOARD = {}'.format(empty_board))