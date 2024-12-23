package main

import (
	"fmt"
)

func parallelMergeSort(arr []int, c chan []int) {
	if len(arr) <= 1 {
		c <- arr
		close(c)
		return
	}

	mid := len(arr) / 2
	leftChan := make(chan []int)
	rightChan := make(chan []int)

	go parallelMergeSort(arr[:mid], leftChan)
	go parallelMergeSort(arr[mid:], rightChan)

	left := <-leftChan
	right := <-rightChan

	c <- merge(left, right)
	close(c)
}

func merge(left, right []int) []int {
	result := make([]int, len(left)+len(right))
	l, r := 0, 0
	for i := 0; i < len(result); i++ {
		if l >= len(left) {
			result[i] = right[r]
			r++
			continue
		}
		if r >= len(right) {
			result[i] = left[l]
			l++
			continue
		}
		if left[l] < right[r] {
			result[i] = left[l]
			l++
		} else {
			result[i] = right[r]
			r++
		}
	}
	return result
}

func main() {
	arr := []int{4, 3, 2, 10, 12, 1, 5, 6}
	c := make(chan []int)
	go parallelMergeSort(arr, c)
	result := <-c
	fmt.Println(result)
}