
import threading

value = 0


def increment(value):
	return value + 1


lock = threading.Lock() # it imp to initialize lock here, a single lock object will be acquired and released by both the threads

def traverse():
	global value
	for index in range(1000000):
		with lock:  # if lock is not used here, there will be race condition as both threads will try to attempt value simultaneously
			value = increment(value) # this is critical section
		

def process():
	t1 = threading.Thread(target=traverse)
	t2 = threading.Thread(target=traverse)
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	

def main():
	process()
	print(value)	# prints 2000000


if __name__ == "__main__":
	main()
	
