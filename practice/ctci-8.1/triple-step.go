package main

import (
	"fmt"
	"os"
	"strconv"
)

var (
	stairs  int
	choices int
)

func countChoices(cs int) {
	remaining := stairs - cs
	if remaining <= 1 {
		choices++
	} else {
		if remaining >= 3 {
			countChoices(cs + 3)
		}
		if remaining >= 2 {
			countChoices(cs + 2)
		}
		countChoices(cs + 1)
	}
}

func startCountWays(n int) int {
	memo := make([]int, n+1)
	for i := 0; i <= n; i++ {
		memo[i] = -1
	}
	return countWays(n, memo)
}

func countWays(n int, memo []int) int {
	switch {
	case n < 0:
		return 0
	case n == 0:
		return 1
	case memo[n] > -1:
		return memo[n]
	default:
		memo[n] = countWays(n-1, memo) + countWays(n-2, memo) + countWays(n-3, memo)
		return memo[n]
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("Please provide the number of stairs\n")
		os.Exit(-1)
	}

	var err error
	stairs, err = strconv.Atoi(os.Args[1])

	if err != nil {
		fmt.Printf("Please provide the number of stairs\n")
		os.Exit(-1)
	}

	countChoices(0)
	fmt.Printf("Number of choices going up the '%v' stairs: %v, %v\n", stairs, choices, startCountWays(stairs))
}
