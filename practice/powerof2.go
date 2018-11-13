package main

import (
    "fmt"
    "os"
    "strconv"
)

func powerof2(num int) int {
    if (num < 0) {
		fmt.Println("0")
		return 0
    } else if (num == 1) {
		fmt.Println("1")
		return 1
	} else {
		prev := powerof2(num / 2)
		cur := prev * 2
		fmt.Printf("%v\n", cur)
		return cur
	}
}

func main() {
    num, err := strconv.Atoi(os.Args[1])
	if err == nil {
		powerof2(num)
	} else {
		fmt.Printf("Input a number please: %v: %v\n", os.Args[1], err)
	}
}
