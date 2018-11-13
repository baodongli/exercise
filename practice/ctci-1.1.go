package main

import (
   "fmt" 
   "os"
   "strings"
)

func isUnique(input string) {
	unique := "unique"
	for i, ch := range input {
	    if strings.Contains(input[i + 1: ], string(ch)) {
		    unique = "duplicate"
			break;
		}
	}
	fmt.Printf("The input string '%v' contains %v charactors\n", input, unique)
}

func isUnique1(input string) {
	unique := "unique"
	wc := make(map[rune]bool)
	for _, ch := range input {
	    if wc[ch] {
		    unique = "duplicate"
			break
		}
		wc[ch] = true
	}
	fmt.Printf("The input string '%v' contains %v charactors\n", input, unique)
}

func main() {
	if len(os.Args) <= 1 {
	    fmt.Printf("Please provide a string\n")
		os.Exit(1)
	}
    input := os.Args[1]
    isUnique(input)
	isUnique1(input)
}
