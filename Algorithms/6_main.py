#compact implementation of timsort

def insertion_sort(array, left=0, right=None):
	if right is None:
		right = len(array) - 1

	#Loop from the element indicated by
	#left until the element indicated by right
	for i in range(left + 1, right +1):
		#this is the element we want to position in its correct place 
		key_item = array[i]

		#initialize the variable that will be used to find the correct position of the element referenced by key_item
		#do this only if the key_item is small than its adjacent values 
		while j >= left and array [j] > key_item:
			array[j +1] = array[j]
			j -= 1

		array[j + 1] = key_item

	return array 