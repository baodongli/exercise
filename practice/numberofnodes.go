package main

import (
    "fmt"
	"os"
	"strconv"
)

type BCTree struct {
	val int
    left, right *BCTree
}

func GetLeftHeight(bct *BCTree) uint32 {
    var height uint32
	for bct != nil {
	    height++
		bct = bct.left
	}
	return height - 1
}

func GetRightHeight(bct *BCTree) uint32 {
    var height uint32
	for bct != nil {
	    height++
		bct = bct.right
	}
	return height - 1
}

func GetNumberOfNodes(bct *BCTree) uint32 {
    if bct == nil {
        return 0
    }
    leftHeight := GetLeftHeight(bct.left)
    rightHeight := GetRightHeight(bct.right)
	var count uint32
    if leftHeight != 0 && leftHeight == rightHeight {
	    count = 2 << leftHeight
	} else {
	    leftCount := GetNumberOfNodes(bct.left)
		rightCount := GetNumberOfNodes(bct.right)
		count = leftCount + rightCount
	}

	fmt.Printf("Count %v\n", count + 1)
	return count + 1
}

var (
    n7 = BCTree{7, nil, nil}
	n8 = BCTree{8, nil, nil}
	n9 = BCTree{9, nil, nil}
    n4 = BCTree{4, &n8, &n9}
	n5 = BCTree{5, nil, nil}
	n6 = BCTree{6, nil, nil}
	n2 = BCTree{2, &n4, &n5}
	n3 = BCTree{3, &n6, &n7}
	n1 = BCTree{1, &n2, &n3}
)

func main() {
    var numOfNodes int
	numOfNodes, _ = strconv.Atoi(os.Args[1])
    nodeCount := GetNumberOfNodes(&n1)
	fmt.Printf("Node count: %v, %v\n", nodeCount, numOfNodes)
    nodeCount = GetNumberOfNodes(&n4)
	fmt.Printf("Node count: %v, %v\n", nodeCount, numOfNodes)
}
