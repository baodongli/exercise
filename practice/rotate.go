package main

import (
	"fmt"
)

// Complete the rotLeft function below.
func rotLeft(a []int32, d int32) []int32 {
	shiftCount := d % int32(len(a))
	if shiftCount == 0 {
		return a
	}
	result := make([]int32, len(a))
	for i := int32(0); i < int32(len(a)); i++ {
		newPos := (i - shiftCount + int32(len(a))) % int32(len(a))
		result[newPos] = a[i]
	}
	return result
}

func main() {
	a := []int32{41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51}
	fmt.Println(rotLeft(a, 10))
}
