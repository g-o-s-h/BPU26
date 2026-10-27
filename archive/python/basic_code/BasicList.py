'''
date	20201118 to 20201119
author	Wumian_Tony
detail	few basic func. dealing list type
'''

from os import system

def percent_even(xlist):
	'''
	input:	list
	output:	float
	calculate the percent of even numbers in a list
	'''
	count = 0
	for each in xlist:
		if each % 2 == 0:
			count += 1
	return (count / len(xlist)) * 100

def is_unique(xlist):
	'''
	input:	list
	output:	boolean
	indicate whether every number in the list are unique or not
	'''
	new_list = []
	for each in xlist:
		if each not in new_list:
			new_list.append(each)
		else:
			return False
	return True

def longest_sorted_sequence(xlist):
	'''
	input:	list
	output:	integer
	indicate how long of sorted sequence in the list
	'''
	count = 0
	max_length = 0
	for i in range(len(xlist) - 1):
		if xlist[i] > xlist[i + 1]:
			if max_length < count:
				max_length = count
			count = 0
		count += 1
	if max_length < count:
		max_length = count
	return max_length

def contains(xlist, ylist):
	'''
	input:	list
	output:	boolean
	indicate whether 1st-list is perfectly include in 2nd-list
	'''
	flag = True
	for i in range(len(ylist) - len(xlist) + 1):
		flag = True
		for j in range(len(xlist)):
			if xlist[j] != ylist[i + j]:
				flag = False
				break
		if flag:
			return True
	return False

def collapse(xlist):
	'''
	input:	list
	output:	list
	add every 2 numbers in the given list together, return a half-size list
	'''
	result = []
	if len(xlist) % 2 == 1:
		xlist += [0]
	for i in range(0, len(xlist), 2):
		result.append(xlist[i] + xlist[i + 1])
	return result

def append(xlist, ylist):
	'''
	input:	list
	output:	list
	append 1st-list and 2nd-list to a new returned list
	'''
	result = []
	for each in xlist:
		result.append(each)
	for each in ylist:
		result.append(each)
	return result

def vowel_count(xstr):
	'''
	input:	string
	output:	dictionary
	count A E I O U for the given string and return as a dictionary
	'''
	stat_dict = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
	for each in xstr:
		if each.upper() in ['A', 'E', 'I', 'O', 'U']:
			stat_dict[each.upper()] += 1
	return stat_dict

def cmp_basiclist(x, y):
	'''
	input:	integer
	output:	boolean
	func. use in even_before_odd
	'''
	factor_x = (x % 2 == 0)
	factor_y = (y % 2 == 0)
	if factor_x < factor_y:
		return True
	elif factor_x == factor_y and x > y:
		return True
	else:
		return False

def even_before_odd(xlist):
	'''
	input:	list
	output:	none
	rearrange the elements in the list to make every even number appears before the odd one, and also sorted
	'''
	if len(xlist) == 1:
		return xlist

	else:
		half_size = len(xlist) // 2
		result_former = even_before_odd(xlist[:half_size])
		result_latter = even_before_odd(xlist[half_size:])
		result = []
		for i in range(len(xlist)):
			if len(result_former) == 0:
				result.append(result_latter.pop(0))
			elif len(result_latter) == 0:
				result.append(result_former.pop(0))
			elif cmp_basiclist(result_former[0], result_latter[0]):
				result.append(result_latter.pop(0))
			else:
				result.append(result_former.pop(0))
		return result

def matrix_add(xlist, ylist):
	'''
	input:	list
	output:	list
	merge the 2 matrix together by adding the value in the relative same position together
	'''
	result = [[0] * len(xlist[0])] * len(xlist)
	for i in range(len(xlist)):
		for j in range(len(xlist[i])):
			result[i][j] = xlist[i][j] + ylist[i][j]
	return result

def is_magic_square(xlist):
	'''
	input:	list
	output:	boolean
	indicate whether the given matrix is:
	1)	in a square shape
	2)	every sum in row, column, and diagonal are equal
	'''
	for each in xlist:
		if len(xlist) != len(each):
			return False

	test_sum = None
	for each in xlist:
		if test_sum == None:
			test_sum = sum(each)
		elif sum(each) != test_sum:
			return False
	
	for i in range(len(xlist)):
		test_column = []
		for j in range(len(xlist)):
			test_column.append(xlist[j][i])
		if sum(test_column) != test_sum:
			return False
	
	temp = []
	for i in range(len(xlist)):
		temp.append(xlist[i][i])
	if sum(temp) != test_sum:
		return False

	temp = []
	for i in range(len(xlist)):
		temp.append(xlist[len(xlist) - i - 1][i])
	if sum(temp) != test_sum:
		return False
	return True

def test():
	print(percent_even([1, 2, 3]))
	print(is_unique([1, 9, 2, 5, 4]))
	print(is_unique([1, 9, 2, 5, 4, 5]))
	print(longest_sorted_sequence([1, 2, 3, 4, 5, 1, 1, 1, 1, 1, 6, 1, 2, 3, 4, 2, 3, 4, 5, 6]))
	print(contains([1, 2, 3], [3, 4, 1, 2, 3, 4]))
	print(contains([1, 2, 1], [3, 4, 1, 2, 3, 4]))
	print(collapse([1, 2, 3, 4, 5, 6, 7]))
	print(append([1, 2, 3], [4, 5, 6, 7]))
	print(vowel_count("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
	print(cmp_basiclist(3, 2), cmp_basiclist(3, 4))
	print(even_before_odd([1, 5, 2, 4, 7, 9, 5, 3, 2, 4, 3]))
	print(matrix_add([[1, 2], [3, 4]], [[9, 8], [7, 6]]))
	print(is_magic_square([[11, 18, 25, 2, 9], [10, 12, 19, 21, 3], [4, 6, 13, 20, 22], [23, 5, 7, 14, 16], [17, 24, 1, 8, 15]]))

def main():
	'''
	empty main func.
	'''
	test()
	system("pause")

if __name__ == '__main__':
	main()
