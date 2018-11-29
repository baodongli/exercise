package main

import (
	"fmt"
)

// Complete the hourglassSum function below.
func hourglassSum(arr [][]int32) int32 {
	sum := int32(0)
	for row := 0; row <= len(arr)-3; row++ {
		for col := 0; col <= len(arr[row])-3; col++ {
			newSum := arr[row][col] + arr[row][col+1] + arr[row][col+2] +
				arr[row+1][col+1] +
				arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
			if newSum > sum {
				sum = newSum
			}
		}
	}
	return sum
}

func main() {
	arr := [][]int32{
		{-1, -1, 0, -9, -2, -2},
		{-2, -1, -6, -8, -2, -5},
		{-1, -1, -1, -2, -3, -4},
		{-1, -9, -2, -4, -4, -5},
		{-7, -3, -3, -2, -9, -9},
		{-1, -3, -1, -2, -4, -5},
	}
	fmt.Println(hourglassSum(arr))
}
