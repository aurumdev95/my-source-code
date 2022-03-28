#this is the quick sort algorithm
def quicksort(sequence):
	length = len(sequence)
	if length <= 1:
		return sequence
	else:
		pivot = sequence.pop()
		
	items_greater = []
	items_lower = []
	
	for item in sequence:
		if item > pivot:
			items_greater.append(item)
		else:
			items_lower.append(item)
	return quicksort(items_lower) + [pivot] + quicksort(items_greater)
	
	
#print(quicksort([1, 4, 2, 5, 6, 2, 9, 7, 3, 0]))