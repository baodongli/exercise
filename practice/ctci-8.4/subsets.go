package main

import (
	"fmt"
	"os"
	"strconv"
)

func findSubsets(set []int) [][]int {
	subsets := make([][]int, 0)
	switch {
	case len(set) == 0:
		return [][]int{}
	case len(set) == 1:
		return [][]int{set}
	default:
		ss := findSubsets(set[1:])
		subsets = append(subsets, []int{set[0]})
		subsets = append(subsets, ss...)
		for _, sset := range ss {
			sset = append([]int{set[0]}, sset...)
			subsets = append(subsets, sset)
		}
		return subsets
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("Please provide the number of stairs\n")
		os.Exit(-1)
	}

	length, err := strconv.Atoi(os.Args[1])

	if err != nil {
		fmt.Printf("Please provide the number of stairs\n")
		os.Exit(-1)
	}

	set := make([]int, length)
	for i := 0; i < length; i++ {
		set[i] = i + 1
	}

	sset := findSubsets(set)
	fmt.Printf("Subsets (%v): %v\n", len(sset), sset)
}
