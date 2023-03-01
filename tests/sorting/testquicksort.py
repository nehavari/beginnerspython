from unittest import TestCase
import sorting.quicksort

class TestQuickSort(TestCase):

	def testPartition(self):
		print(partition(1, 3, [4, 34, 1]))
		
