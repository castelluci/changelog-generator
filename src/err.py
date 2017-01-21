import sys

def printe(*args, **kwargs):
	print('\n########## ERROR ##########', file=sys.stderr)
	print(*args, file=sys.stderr, **kwargs)
	print('###########################\n', file=sys.stderr)
