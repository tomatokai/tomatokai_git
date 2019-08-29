#二分法演算法的案例
numbers = [5,17,33,41,55,61,80]
find = 55

low = 0
high = len(numbers) - 1

while low <= high:
	mid = (low + high) // 2
	if numbers[mid] > find:
		high = mid - 1
	elif numbers[mid] < find:
		low = mid + 1
	else:
		break
print(mid)
