package main

func timSort(array []int) {
	arrayLen := len(array)
	minRun := 32

	// Sort the small runs using insertion sort
	for i := 0; i < arrayLen; i += minRun {
		end := min(i+minRun, arrayLen)
		insertionSort(array[i:end])
	}

	// Merge the sorted runs using merge sort
	currentRunSize := minRun
	for currentRunSize < arrayLen {
		for leftStart := 0; leftStart < arrayLen; leftStart += 2 * currentRunSize {
			middleIndex := min(leftStart+currentRunSize, arrayLen)
			rightEnd := min(leftStart+2*currentRunSize, arrayLen)

			leftArray := array[leftStart:middleIndex]
			rightArray := array[middleIndex:rightEnd]
			mergedArray := merge(leftArray, rightArray)

			copy(array[leftStart:rightEnd], mergedArray)
		}
		currentRunSize *= 2
	}
}

func insertionSort(array []int) {
	n := len(array)
	for i := 1; i < n; i++ {
		key := array[i]
		j := i - 1
		for j >= 0 && key < array[j] {
			array[j+1] = array[j]
			j--
		}
		array[j+1] = key
	}
}
