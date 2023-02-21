"""
Time Complexity: Worst case time complexity is O(N2) and average case time complexity is O(N*logN)
Auxiliary Space: O(1)
"""
import random


def partition(start, end, nums):
    """
    output of partition is =>
    1. pivot has moved to its correct position in sorted array
    2. all the elements left to pivot are smaller than pivot
        and all the elements right to pivot are greater than pivot
    """
    pivot = random.randrange(start, end + 1)
    nums[pivot], nums[end] = nums[end], nums[pivot]
    pivot = start
    for index in range(start, end):  # it will not go till end because end contains nothing but pivot
        if nums[index] <= nums[end]:
            nums[pivot], nums[index] = nums[index], nums[pivot]
            pivot += 1
    nums[pivot], nums[end] = nums[end], nums[pivot]
    return pivot


def quicksort(start, end, nums):
    if start >= end:
        return
    pivot = partition(start, end, nums)
    quicksort(start, pivot - 1, nums)
    quicksort(pivot + 1, end, nums)


def main():
    nums = [100, 56, 34, 56, 3, 78, 6, 3, 67, 45, 67, 4, 23, 89, 21]
    quicksort(0, len(nums) - 1, nums)
    print(nums)

    nums = [104, 34, 56, 31, 78, 6, 3, 67, 67, 4, 23, 89, 21]
    quicksort(0, len(nums) - 1, nums)
    print(nums)

    nums = [104, 34, 57, 31, 78, 4, 23, 899, 21]
    quicksort(0, len(nums) - 1, nums)
    print(nums)


if __name__ == "__main__":
    main()

