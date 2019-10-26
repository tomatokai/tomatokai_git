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

#合併排序法案例
def Merge_Sort(array):
	if len(array) > 1:
		mid = len(array) //2 
		left_array = array[:mid]
		right_array = array[mid:]
		
		Merge_Sort(left_array)
		Merge_Sort(right_array)

		right_index = 0;
		left_index = 0;
		merged_index = 0;
		while right_index < len(right_array) and left_index < len(left_array):
			if (right_array[right_index] < left_array[left_index]):
				array[merged_index] = right_array[right_index]
				right_index = right_index + 1
			else:
				array[merged_index] = left_array[left_index]
				left_index = left_idnex + 1
			
			megred_index = megred_index + 1
