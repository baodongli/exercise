package main

import (
	"fmt"
)

type node struct {
	val         int
	left, right *node
}

var (
	n1     = &node{1, nil, nil}
	n3     = &node{3, nil, nil}
	n2     = &node{2, n1, n3}
	length = int(3)
)

func copyArray(ta []int) (na []int) {
	na = make([]int, len(ta))
	for i := range ta {
		na[i] = ta[i]
	}
	return
}

func printArray(ta []int, n *node) []int {
	if n == nil {
		if len(ta) == length {
			fmt.Printf("%v\n", ta)
		}
		return
	}

	if n.left != nil {
		if n.right != nil {
			taNew := copyArray(ta)
			taNew = append(taNew, n.left.val)
			taNew = append(taNew, n.right.val)
			tal := printArray(taNew, n.left)
			_ = printArray(tal, n.right)

			taNew = copyArray(ta)
			taNew = append(taNew, n.righ.val)
			taNew = append(taNew, n.left.val)

			tal = printArray(taNew, n.left)
			_ = printArray(tal, n.right)
		} else {
			taNew := copyArray(ta)
			ta = append(taNew, n.left.val)
			printArray(taNew, n.left)
		}
	} else {
		taNew := copyArray(ta)
		ta = append(taNew, n.right.val)
		printArray(taNew, n.right)
	}
}

func main() {
	printArray([]int{n2.val}, n2)
}
