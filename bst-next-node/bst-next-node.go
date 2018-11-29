package main

import (
	"fmt"
)

type Node struct {
	left, right, parent *Node
	val                 int
}

func leftMostNode(n *Node) *Node {
	if n == nil {
		return nil
	}
	for n.left != nil {
		n = n.left
	}
	return n
}

func next(n *Node) *Node {
	if n.right != nil {
		return leftMostNode(n.right)
	}
	parent := n.parent
	for parent != nil && parent.left != n {
		n = parent
		parent = n.parent
	}
	return parent
}

func main() {
	n30 := &Node{nil, nil, nil, 30}
	n40 := &Node{n30, nil, nil, 40}
	n30.parent = n40
	n80 := &Node{nil, nil, nil, 80}
	n70 := &Node{nil, n80, nil, 70}
	n80.parent = n70
	n60 := &Node{n40, n70, nil, 60}
	n40.parent = n60
	n70.parent = n60
	n110 := &Node{nil, nil, nil, 110}
	n100 := &Node{n60, n110, nil, 100}
	n60.parent = n100
	n110.parent = n100
	n105 := &Node{nil, nil, n110, 105}
	n110.left = n105

	nn := next(n100)
	if nn != nil {
		fmt.Printf("Next node: %v\n", nn.val)
	} else {
		fmt.Printf("No next node for: %v\n", n100)
	}
}
