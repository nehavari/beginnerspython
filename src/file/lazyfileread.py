"""
lazy file reading generator
"""
import sys

def lazyread(fileobject):
	while True:
		data = fileobject.readline()
		if not data:
			break
		yield data
		

def read(filepath):
	with open(filepath) as fileobject:
		lazy = next(lazyread(fileobject))
		print(sys.getsizeof(lazy))
		print(lazy)
	
	with open(filepath) as fileobject:
		instant = fileobject.readline()
		print(sys.getsizeof(instant))
		print(instant)


def main():
	filepath = "/home/nvcv/Documents/git/beginnerspython/beginnerspython/src/sorting/quicksort.py"
	read(filepath)


if __name__ == "__main__":
	main()	
		
