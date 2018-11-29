package main

import (
	"fmt"
)

type Node struct {
	left, right *Node
	val         int
}

var lastItem *int

// Keep the last item and compare the current against it
func checkBST(n *Node) bool {
	if n == nil {
		return true
	}

	if valid := checkBST(n.left); !valid {
		return false
	}
	if lastItem != nil && n.val <= *lastItem {
		return false
	}

	lastItem = &n.val
	return checkBST(n.right)
}

// a BST must satisfy left.data <= current.data < right.data for every node in the subtree
// Therefore, on the left tree, the min starts with nil, max is the data in the current node (the subtree's parent)
// on the right tree, the min is the data in the current node(the subtree's parent), the max starts as nil
// as it recurses, the min or max is the parent node's data depending on if its a left tree or right tree.
func checkBST2(n *Node, min, max *int) bool {
	if n == nil {
		return true
	}

	if (min != nil && n.val <= *min) || (max != nil && n.val > *max) {
		return false
	}

	return checkBST2(n.left, min, &n.val) && checkBST2(n.right, &n.val, max)
}

func main() {
	n1 := &Node{nil, nil, 20}
	n2 := &Node{n1, nil, 20}

	isBST := checkBST(n2)
	fmt.Printf("BST with in-order traversal: %v, min/max: %v\n", isBST, checkBST2(n2, nil, nil))
}
