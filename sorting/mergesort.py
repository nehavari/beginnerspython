"""
implementation of merge sort
note that its inplace implementation and sort the elements in the same input array.
two subarray buffers are created in merge function and later tthey are merged to the original array.
time comlexity : O(n*logn)
space complexity: O(n)
"""

def merge(array, start, mid, end):

	subarray1, subarray2 = array[start: mid + 1], array[mid + 1: end + 1]
	subarray1.append(float('inf')) # this helps keeping conditions simple
	subarray2.append(float('inf')) # thanks to CLRS book
	index =	index1 = index2 = 0
	
	for index in range(start, end + 1):
		if subarray1[index1] <= subarray2[index2]:
			array[index] = subarray1[index1]
			index1 += 1
		else:
			array[index] = subarray2[index2]
			index2 += 1
	

def mergesort(array, start, end):
	if start < end:
		mid = (start + end) // 2
		mergesort(array, start, mid)
		mergesort(array, mid + 1, end)
		merge(array, start, mid, end)
	

def main():
	array = [100, 56, 34, 56, 3, 0, 78, 6, 3, 67, 45, 67, 4, 23, 89, 21]
	mergesort(array, 0, len(array) - 1)
	print(array)

	array = [104, 34, 56, 31, 78, 6, 3, 67, 67, 4, 23, 89, 21]
	mergesort(array, 0, len(array) - 1)
	print(array)

	array = [104, 34, 57, 31, 78, 4, 23, 899, 21]
	mergesort(array, 0, len(array) - 1)
	print(array)


if __name__ == "__main__":
	main()
	
