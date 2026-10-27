'''
date	20201217
author	Wumian_Tony
detail	all learnt kinds of sorting algorithms
'''

from os import system
from random import *

def default_compare(x, y):
	# True: x and y should be swap, Tendency: small -> big
	return x > y

def reverse_compare(x, y):
	# the reverse of default
	return not default_compare(x, y)

def compare_sort(xlist, cmp = default_compare, display = False):
	length = len(xlist)
	for i in range(length - 1):
		for j in range(i + 1, length):
			if cmp(xlist[i], xlist[j]):
				xlist[i], xlist[j] = xlist[j], xlist[i]
				if display:
					print(xlist)

def selection_sort(xlist, cmp = default_compare, display = False):
	for i in range(len(xlist) - 1):
		value = xlist[i]
		point = i
		for j in range(i, len(xlist)):
			if cmp(value, xlist[j]):
				value = xlist[j]
				point = j
		xlist[point] = xlist[i]
		xlist[i] = value
		if display:
			print(xlist)

def insertion_sort(xlist, cmp = default_compare, display = False):
	for i in range(1, len(xlist)):
		for j in range(i + 1):
			if cmp(xlist[j], xlist[i]):
				xlist.insert(j, xlist.pop(i))
				if display:
					print(xlist)
				break

def bubble_sort(xlist, cmp = default_compare, display = False):
	for i in range(len(xlist) - 1, -1, -1):
		for j in range(0, i):
			if cmp(xlist[j], xlist[j + 1]):
				xlist[j], xlist[j + 1] = xlist[j + 1], xlist[j]
				if display:
					print(xlist)

def merge_sort(xlist, cmp = default_compare, display = False):
	if len(xlist) < 2:
		return
	mid = len(xlist) // 2
	left = xlist[:mid]
	right = xlist[mid:]
	if display:
		print(left, right)
	result = []
	merge_sort(left, cmp, display)
	merge_sort(right, cmp, display)
	while len(left) * len(right) > 0:
		if cmp(right[0], left[0]):
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	result = result + left + right
	if display:
		print(result)
	for i in range(len(result)):
		xlist[i] = result[i]

def quick_sort(xlist, cmp = default_compare, display = False):
	if len(xlist) < 2:
		return
	key = xlist.pop(0)
	left = []
	right = []
	for each in xlist:
		if cmp(key, each):
			left.append(each)
		else:
			right.append(each)
	if display:
		print(left, key, right)
	quick_sort(left, cmp, display)
	quick_sort(right, cmp, display)
	xlist.append(None)
	result = left + [key] + right
	if display:
		print(result)
	for i in range(len(result)):
		xlist[i] = result[i]

def hash_sort(xlist, display = False):
	# also called radix sort
	maximum = max(xlist)
	minimum = min(xlist)
	hash_table = [False] * (maximum - minimum + 1)
	for each in xlist:
		hash_table[each - minimum] += 1
	result = []
	for i in range(len(hash_table)):
		if hash_table[i]:
			for times in range(hash_table[i]):
				result.append(i + minimum)
	if display:
		for i in range(len(hash_table)):
			if hash_table[i]:
				print(str(i + minimum) + ":", hash_table[i], "times")
	for i in range(len(result)):
		xlist[i] = result[i]

def heap_sort(xlist, cmp = default_compare, display = False):

	if display:
		system('"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" https://www.runoob.com/wp-content/uploads/2019/03/heapSort.gif')

	def lchild(parent):
		return parent * 2 + 1
	def rchild(parent):
		return (parent + 1) * 2
	def parent(child):
		return (child - 1) // 2

	length = len(xlist)

	# create max heap
	for i in range(parent(length - 1), -1, -1):
		point = i
		while True:
			if point > parent(length - 1):
				break
			extreme = point
			if cmp(xlist[lchild(point)], xlist[extreme]):
				extreme = lchild(point)
			if cmp(xlist[rchild(point)], xlist[extreme]):
				extreme = rchild(point)
			if extreme == point:
				break
			xlist[point], xlist[extreme] = xlist[extreme], xlist[point]
			point = extreme

	# reform heap
	for i in range(length - 1, -1, -1):
		xlist[0], xlist[i] = xlist[i], xlist[0]
		point = 0
		while True:
			if point > parent(i):
				break
			extreme = point
			if i > lchild(point) and cmp(xlist[lchild(point)], xlist[extreme]):
				extreme = lchild(point)
			if i > rchild(point) and cmp(xlist[rchild(point)], xlist[extreme]):
				extreme = rchild(point)
			if extreme == point:
				break
			xlist[point], xlist[extreme] = xlist[extreme], xlist[point]
			point = extreme

def test():

	sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	shuffle(sample)
	print("Sample:\t", sample,"\n\nDefault (min -> max)")
	test = sample.copy()
	compare_sort(test)
	print("Compare:", test)
	test = sample.copy()
	selection_sort(test)
	print("Select:\t", test)
	test = sample.copy()
	insertion_sort(test)
	print("Insert:\t", test)
	test = sample.copy()
	bubble_sort(test)
	print("Bubble:\t", test)
	test = sample.copy()
	merge_sort(test)
	print("Merge:\t", test)
	test = sample.copy()
	quick_sort(test)
	print("Quick:\t", test)
	test = sample.copy()
	hash_sort(test)
	print("Hash:\t", test)
	test = sample.copy()
	heap_sort(test)
	print("Heap:\t", test)
	print("\n\nReverse (max -> min)")
	test = sample.copy()
	compare_sort(test, reverse_compare)
	print("Compare:", test)
	test = sample.copy()
	selection_sort(test, reverse_compare)
	print("Select:\t", test)
	test = sample.copy()
	insertion_sort(test, reverse_compare)
	print("Insert:\t", test)
	test = sample.copy()
	bubble_sort(test, reverse_compare)
	print("Bubble:\t", test)
	test = sample.copy()
	merge_sort(test, reverse_compare)
	print("Merge:\t", test)
	test = sample.copy()
	quick_sort(test, reverse_compare)
	print("Quick:\t", test)
	test = sample.copy()
	heap_sort(test, reverse_compare)
	print("Hash: \t N/A\nHeap:\t", test)
	"""
	sample = []
	for i in range(randint(1, 100)):
		sample.append(randint(1, 100))
	shuffle(sample)
	print("\n\nSample:\n\n", len(sample), "\n\n", sample,"\n\nDefault (min -> max)")
	test = sample.copy()
	compare_sort(test)
	print("Compare:", test)
	test = sample.copy()
	selection_sort(test)
	print("Select:\t", test)
	test = sample.copy()
	insertion_sort(test)
	print("Insert:\t", test)
	test = sample.copy()
	bubble_sort(test)
	print("Bubble:\t", test)
	test = sample.copy()
	merge_sort(test)
	print("Merge:\t", test)
	test = sample.copy()
	quick_sort(test)
	print("Quick:\t", test)
	test = sample.copy()
	hash_sort(test)
	print("Hash:\t", test)
	test = sample.copy()
	heap_sort(test)
	print("Heap:\t", test)
	print("\n\nReverse (max -> min)")
	test = sample.copy()
	compare_sort(test, reverse_compare)
	print("Compare:", test)
	test = sample.copy()
	selection_sort(test, reverse_compare)
	print("Select:\t", test)
	test = sample.copy()
	insertion_sort(test, reverse_compare)
	print("Insert:\t", test)
	test = sample.copy()
	bubble_sort(test, reverse_compare)
	print("Bubble:\t", test)
	test = sample.copy()
	merge_sort(test, reverse_compare)
	print("Merge:\t", test)
	test = sample.copy()
	quick_sort(test, reverse_compare)
	print("Quick:\t", test)
	test = sample.copy()
	heap_sort(test, reverse_compare)
	print("Hash: \t N/A\nHeap:\t", test)
	"""

def education():
	sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	shuffle(sample)
	print("sample: ", sample)

	copy = sample.copy()
	print("\n[Compare Sort]")
	print(copy)
	compare_sort(copy, display = True)

	copy = sample.copy()
	print("\n[Selection Sort]")
	print(copy)
	selection_sort(copy, display = True)

	copy = sample.copy()
	print("\n[Insertion Sort]")
	print(copy)
	insertion_sort(copy, display = True)

	copy = sample.copy()
	print("\n[Bubble Sort]")
	print(copy)
	bubble_sort(copy, display = True)

	copy = sample.copy()
	print("\n[Merge Sort]")
	print(copy)
	merge_sort(copy, display = True)

	copy = sample.copy()
	print("\n[Quick Sort]")
	print(copy)
	quick_sort(copy, display = True)

	copy = sample.copy()
	print("\n[Hash Sort]")
	print(copy)
	hash_sort(copy, display = True)

	# copy = sample.copy()
	# print("\n[Heap Sort]")
	# print(copy)
	# heap_sort(sample, display = True)

def main():
	'''
	main func.
	'''
	#test()
	education()
	system("pause")

if __name__ == '__main__':
	main()
