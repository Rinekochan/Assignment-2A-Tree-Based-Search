import sys


def arg_parse():
	argc = len(sys.argv)
	if argc != 3:
		print('Usage: python3 search.py <filename> <method>')
	else:
		filename = sys.argv[1]
		method = sys.argv[2]

	return (filename, method)

def main():
	filename, method = arg_parse()

	print("{} {}".format(filename, method));
