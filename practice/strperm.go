package main

import (
    "fmt"
    "os"
	//"strconv"
	//"strings"
)

func permutation(str string, prefix string) {
	if len(str) == 0 {
		fmt.Println(prefix)
	} else {
		for i := 0; i < len(str); i++ {
			rem := str[:i] + str[i+1:]
			newprefix := prefix + string(str[i])
			permutation(rem, newprefix)
		}
	}
}

func main() {
	str := os.Args[1]
	permutation(str, "")
}
