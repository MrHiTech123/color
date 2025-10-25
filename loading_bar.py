# A loading bar API.

# Usage: loading_command 2>&1 | loadingbar.py [bar_len] [time_per_bar]
# Requires: loading_command flushes stdout whenever it prints a line
# Effects: Whenever loading_command prints a line, that line will be shown, and a progress bar will be shown underneath it


import sty
from sys import argv, stdin

COLORS = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (64, 255, 0), (0, 255, 64), (0, 255, 255), (0, 128, 255), (0, 0, 255), (128, 0, 255), (255, 0, 255), (255, 0, 128)]

try:
	try:
		bar_len = int(argv[1])
	except IndexError:
		bar_len = 20
	try:
		time_per_bar = int(argv[2])
	except IndexError:
		time_per_bar = 4
except:
	print("Usage: loading_program | loadingbar.py [bar_len] [time_per_bar]")
	raise SystemExit(0)




def get_color(i: int) -> tuple[int, int, int]:
	return COLORS[i % len(COLORS)]

PREV_LINE = '\x1B[0F'
def back_to_prev() -> None:
	print(PREV_LINE, end="")

def color_bands(uncolored_string: str, offset: int) -> str:
	to_return = ''
	
	for i, char in enumerate(uncolored_string):
		to_return += sty.fg.rgb_call(*get_color(i + offset))
		to_return += char
	
	to_return += sty.fg.rs
	
	return to_return

def loading_bar_interior_frame(total_len: int, curr_len: int) -> str:
	return ('=' * (curr_len)) + ('>' if curr_len <= total_len else "") + (' ' * (total_len - curr_len))

def loading_bar_frame(total_len: int, curr_len: int):
	return '[' + color_bands(loading_bar_interior_frame(total_len, (curr_len % (bar_len + 1))), i // time_per_bar) + ']'

if __name__ == '__main__':
	i = 0
	print()
	while True:
		back_to_prev()
		try:
			print(input() + ' ' * (bar_len + 3))
		except EOFError:
			break
		print(loading_bar_frame(bar_len, i))
		i += 1

print(loading_bar_frame(bar_len, bar_len))

