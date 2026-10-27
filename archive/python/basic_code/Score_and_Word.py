'''
date	20201119
author	Wumian_Tony
detail	training for 10 simple func.
since these func. are not so useful, there's no seperately comments for them
'''

def scores_increasing(xlist):
	for i in range(len(xlist) - 1):
		if xlist[i] > xlist[i + 1]:
			return False
	return True

def scores100(xlist):
	for i in range(len(xlist) - 1):
		if xlist[i] + xlist[i + 1] == 200:
			return True
	return False

def average(xlist, start, end):
	'''
	a sub-func. used in score_average
	'''
	total = 0
	for i in range(start, end):
		total += xlist[i]
	return total // (end - start)

def scores_average(xlist):
	'''
	the average will be change to integer
	'''
	half_size = len(xlist) // 2
	aver_former = average(xlist, 0, half_size)
	aver_latter = average(xlist, half_size, len(xlist))
	return max(aver_former, aver_latter)

def words_count(xlist, length):
	count = 0
	for each in xlist:
		if len(each) == length:
			count += 1
	return count

def words_front(xlist, n):
	result = []
	for i in range(n):
		result.append(xlist[i])
	return result

def words_without_list(xlist, n):
	result = []
	for each in xlist:
		if len(each) != n:
			result.append(each)
	return result

def has_one(x):
	if x % 10 == 1:
		return True
	if x < 10:
		return False
	return has_one(x // 10)

def get_digit(x):
	'''
	a sub-func. in divides_self
	'''
	if x < 10:
		return [x]
	return get_digit(x // 10) + [x % 10]

def divides_self(x):
	digits = get_digit(x)
	for each in digits:
		if each == 0 or x % each != 0:
			return False
	return True

def copy_evens(xlist, n):
	count = 0
	result = []
	for each in xlist:
		if each % 2 == 0:
			result.append(each)
			count += 1
		if count == n:
			break
	return result

def copy_endy(xlist, n):
	count = 0
	result = []
	for each in xlist:
		if (0 <= each and each <= 10) or (90 <= each and each <= 100):
			result.append(each)
			count += 1
		if count == n:
			break
	return result

def test():
	print(scores_increasing([1, 3, 4]))
	print(scores_increasing([1, 3, 2]))
	print(scores_increasing([1, 1, 4]))
	print()
	print(scores100([1, 100, 100]))
	print(scores100([1, 100, 99, 100]))
	print(scores100([100, 1, 100, 100]))
	print()
	print(scores_average([2, 2, 4, 4]))
	print(scores_average([4, 4, 4, 2, 2, 2]))
	print(scores_average([3, 4, 5, 1, 2, 3]))
	print(scores_average([1, 2, 3, 4, 1, 2.5, 3]))
	print()
	print(words_count(["a", "bb", "b", "ccc"], 1))
	print(words_count(["a", "bb", "b", "ccc"], 3))
	print(words_count(["a", "bb", "b", "ccc"], 4))
	print(words_count(["a", "bb", "b", "ccc"], 2))
	print()
	print(words_front(["a", "b", "c", "d"], 1))
	print(words_front(["a", "b", "c", "d"], 2))
	print(words_front(["a", "b", "c", "d"], 3))
	print(words_front(["a", "b", "c", "d"], 4))
	print()
	print(words_without_list(["a", "bb", "b", "ccc"], 1))
	print(words_without_list(["a", "bb", "b", "ccc"], 3))
	print(words_without_list(["a", "bb", "b", "ccc"], 4))
	print(words_without_list(["a", "bb", "b", "ccc"], 2))
	print()
	print(has_one(10))
	print(has_one(22))
	print(has_one(220))
	print(has_one(9999901))
	print()
	print(divides_self(128))
	print(divides_self(12))
	print(divides_self(120))
	print(divides_self(121))
	print()
	print(copy_evens([3, 2, 4, 5, 8], 2))
	print(copy_evens([3, 2, 4, 5, 8], 3))
	print(copy_evens([6, 1, 2, 4, 5, 8], 3))
	print()
	print(copy_endy([9, 11, 90, 22, 6], 2))
	print(copy_endy([9, 11, 90, 22, 6], 3))
	print(copy_endy([12, 1, 1, 13, 0, 20], 2))

def main():
	'''
	empty main func.
	'''

if __name__ == '__main__':
	main()
