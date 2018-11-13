package main

import (
    "fmt"
	"os"
	"strconv"
)

type linkedList struct {
    value int
	next *linkedList
}

func createLinkedList(vals []string) *linkedList {
    var ll, head, tail *linkedList

    for _, str := range vals {
	    val, err := strconv.Atoi(str)
		if err != nil {
		    fmt.Printf("Please enter integer value: %v", str)
			os.Exit(1)
		}
		ll = &linkedList{value: val, next: nil}
		if head == nil {
			head = ll
			tail = ll
		} else {
		    tail.next = ll
			tail = ll
		}
	}
	return head
}

func partition(ll *linkedList, pv int) {
    parPtr := ll
	runner := ll
	for parPtr != nil && parPtr.value < pv {
		parPtr = parPtr.next
	}
    runner =  parPtr
	for runner != nil && runner.value >= pv {
		runner = runner.next
	}
	for parPtr != nil && runner != nil {
	    if runner.value < parPtr.value {
		    tmpVal := parPtr.value
		    parPtr.value = runner.value
			runner.value = tmpVal
		}
		for parPtr != nil && parPtr.value < pv {
			parPtr = parPtr.next
		}
		for runner != nil && runner.value >= pv {
			runner = runner.next
		}
	}
}

func printErr() {
	fmt.Println("Please enter a partition value followed by a sequence of values")
	os.Exit(1)
}

func main() {
    if len(os.Args) < 2 {
        printErr()
	}

	pv, err := strconv.Atoi(os.Args[1])
	if err != nil {
        printErr()
	}

    ll := createLinkedList(os.Args[2:])
	partition(ll, pv)
	for ll != nil {
	    fmt.Printf("%v ", ll.value)
		ll = ll.next
	}
	fmt.Println("")
}
