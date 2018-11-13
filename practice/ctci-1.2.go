package main

import (
    "fmt"
    "os"
)

type countMap map[rune]uint

func getCountMap(str string) (cm countMap) {
    cm = make(countMap)
	for _, ch := range str {
		cm[ch]++
	}
	return
}

func checkPermutation(str1, str2 string) {
    str1CountMap := getCountMap(str1)
	str2CountMap := getCountMap(str2)
	for ch, count := range str1CountMap {
	    if count != str2CountMap[ch] {
		    fmt.Printf("'%v' is not a permutation of '%v'\n", str1, str2)
			return
		}
	}
	fmt.Printf("'%v' is a permutation of '%v'\n", str1, str2)
}

func main() {
    if (len(os.Args) != 3) {
	    fmt.Println("Please provide two strings as input")
		os.Exit(1)
    }

	checkPermutation(os.Args[1], os.Args[2])
}
