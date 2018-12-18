package main

import (
	"fmt"
	"sync"
	"time"
)

var count, count1, count2, count3, count4 int

type Node struct {
	next *Node
	prev *Node
	val  int
}

type linkList struct {
	head *Node
	tail *Node
	size int
}

func newNode(val int) *Node {
	return &Node{nil, nil, val}
}

func (ll *linkList) isEmpty() bool {
	return ll.head == nil
}

func (ll *linkList) addFirst(n *Node) {
	if ll.head == nil {
		ll.head = n
		ll.tail = n
		ll.head.prev = nil
		n.next = nil
	} else {
		n.next = ll.head
		ll.head.prev = n
		ll.head = n
	}
	ll.size++
}

func (ll *linkList) removeFirst() *Node {
	if ll.head == nil {
		return nil
	}
	n := ll.head
	ll.head = ll.head.next
	if ll.head == nil {
		ll.tail = nil
	} else {
		ll.head.prev = nil
	}
	ll.size--
	return n
}

func (ll *linkList) addLast(n *Node) {
	n.next = nil
	if ll.tail == nil {
		ll.head = n
		ll.tail = n
		ll.head.prev = nil
	} else {
		ll.tail.next = n
		n.prev = ll.tail
		ll.tail = n
	}
	ll.size++
}

func (ll *linkList) removeLast() *Node {
	if ll.tail == nil {
		return nil
	}
	n := ll.tail
	ll.tail = n.prev
	if ll.tail == nil {
		ll.head = nil
	} else {
		ll.tail.next = nil
	}
	ll.size--
	return n
}

func (ll *linkList) addAll(n *Node) {
	for ; n != nil; n = n.next {
		ll.addLast(newNode(n.val))
	}
}

var cloneCount int

func (ll *linkList) clone() *linkList {
	cloneCount++
	new := &linkList{nil, nil, 0}
	for n := ll.head; n != nil; n = n.next {
		new.addLast(newNode(n.val))
	}
	return new
}

func (ll *linkList) String() string {
	seq := "["
	for n := ll.head; n != nil; n = n.next {
		seq = fmt.Sprintf("%v %v", seq, n.val)
	}
	seq = fmt.Sprintf("%v]", seq)
	return seq
}

var concatCount int

func concatList(first, second *linkList) *linkList {
	concatCount++
	new := &linkList{nil, nil, 0}
	for n := first.head; n != nil; n = n.next {
		new.addLast(newNode(n.val))
	}
	for n := second.head; n != nil; n = n.next {
		new.addLast(newNode(n.val))
	}
	return new
}

func weaveList2(first, second *Node, prefix *linkList) {
	level++
	f := first
	for f != nil {
		s := second
		prefix.addLast(newNode(f.val))
		secPrefix := &linkList{}
		for s != nil {
			secPrefix.addLast(newNode(s.val))
			if f.next != nil {
				weaveList2(f.next, s.next, concatList(prefix, secPrefix))
			}
			s = s.next
		}
		f = f.next
		if f == nil && s == nil {
			fmt.Println(concatList(prefix, secPrefix))
			count2++
		}
	}
	level--
}

func weaveList3(first, second *linkList) {
	prefix := make([]int, 1, first.size+second.size+1)
	prefix[0] = 16
	weave(first.head, second.head, prefix)
	prefix = prefix[:1]
	weave(second.head, first.head, prefix)
}

func weave(first, second *Node, prefix []int) {
	f := first
	for f != nil {
		s := second
		prefix = append(prefix, f.val)
		size1 := len(prefix)
		for s != nil {
			prefix = append(prefix, s.val)
			size2 := len(prefix)
			if f.next != nil {
				weave(f.next, s.next, prefix)
				prefix = prefix[:size2]
			}
			s = s.next
		}
		f = f.next
		if f == nil && s == nil {
			pre := make([]int, len(prefix))
			copy(pre, prefix)
			fmt.Println(pre)
			count3++
		}
		prefix = prefix[:size1]
	}
}

var level int

func weaveList(first, second, prefix *linkList) {
	if first.isEmpty() || second.isEmpty() {
		result := prefix.clone()
		result.addAll(first.head)
		result.addAll(second.head)
		fmt.Println(result)
		count1++
		level--
		return
	}

	/*
		fmt.Printf("Level: %v\n", level)
		for i := 0; i < level*2; i++ {
			fmt.Printf("$ ")
		}
		fmt.Printf("%v", first)
		fmt.Printf("%v", second)
		fmt.Printf("%v\n\n", prefix)
		level++
	*/
	headFirst := first.removeFirst()
	prefix.addLast(headFirst)
	weaveList(first, second, prefix)
	prefix.removeLast()
	first.addFirst(headFirst)

	/*
		fmt.Printf("LEVEL: %v\n", level)
		for i := 0; i < level*2; i++ {
			fmt.Printf("@ ")
		}
		fmt.Printf("%v", first)
		fmt.Printf("%v", second)
		fmt.Printf("%v\n\n", prefix)
	*/
	headSecond := second.removeFirst()
	prefix.addLast(headSecond)
	weaveList(first, second, prefix)
	prefix.removeLast()
	second.addFirst(headSecond)
}

func getCombination(start, total, sample int, prefix, diff []int) {
	if sample == 0 {
		fmt.Println(prefix)
		for i := prefix[len(prefix)-1] + 1; i <= total; i++ {
			diff = append(diff, i)
		}
		fmt.Println(diff)
		count++
		return
	}
	for p := start; p <= total - sample; p++ {
		size := len(prefix)
		diffSize := len(diff)
		if size == 0 {
			for i := 0; i < p; i++ {
				diff = append(diff, i+1)
			}
		} else {
			for i := prefix[size-1] + 1; i < p+1; i++ {
				diff = append(diff, i)
			}
		}
		prefix = append(prefix, p+1)
		getCombination(p+1, total, sample-1, prefix, diff)
		prefix = prefix[:size]
		diff = diff[:diffSize]
	}
}

func combination(total, sample int) {
	prefix := make([]int, 0, total)
	diff := make([]int, 0, total-sample)
	getCombination(0, total, sample, prefix, diff)
}

type weaveTwoArrayCtrl struct {
	parent        int
	total         int
	prefix, diff  []int
	first, second *linkList
}

func weaveTwoArray(start, sample int, wtaCtrl *weaveTwoArrayCtrl) {
	if sample == 0 {
		for i := wtaCtrl.prefix[len(wtaCtrl.prefix)-1] + 1; i <= wtaCtrl.total; i++ {
			wtaCtrl.diff = append(wtaCtrl.diff, i)
		}
		arr := make([]int, wtaCtrl.total+1)
		arr[0] = wtaCtrl.parent
		index := 0
		for n := wtaCtrl.first.head; n != nil; n = n.next {
			arr[wtaCtrl.prefix[index]] = n.val
			index++
		}
		index = 0
		for n := wtaCtrl.second.head; n != nil; n = n.next {
			arr[wtaCtrl.diff[index]] = n.val
			index++
		}
		fmt.Println(arr)
		count4++
		return
	}
	for p := start; p <= wtaCtrl.total - sample; p++ {
		size := len(wtaCtrl.prefix)
		diffSize := len(wtaCtrl.diff)
		if size == 0 {
			for i := 0; i < p; i++ {
				wtaCtrl.diff = append(wtaCtrl.diff, i+1)
			}
		} else {
			for i := wtaCtrl.prefix[size-1] + 1; i < p+1; i++ {
				wtaCtrl.diff = append(wtaCtrl.diff, i)
			}
		}
		wtaCtrl.prefix = append(wtaCtrl.prefix, p+1)
		weaveTwoArray(p+1, sample-1, wtaCtrl)
		wtaCtrl.prefix = wtaCtrl.prefix[:size]
		wtaCtrl.diff = wtaCtrl.diff[:diffSize]
	}
}

func weaveList4(first, second *linkList) {
	prefix := make([]int, 0, first.size+second.size)
	diff := make([]int, 0, second.size)
	wta := &weaveTwoArrayCtrl{16, first.size + second.size, prefix, diff, first, second}
	weaveTwoArray(0, first.size, wta)
}

// Not accurate time-wise
func withGoRoutine() {
	var wg sync.WaitGroup
	stop := make(chan int)
	go func(stop <-chan int) {
		wg.Add(1)
		first := &linkList{}
		second := &linkList{}
		for v := 1; v < 5; v++ {
			first.addLast(newNode(v))
		}

		for v := 8; v < 8+3; v++ {
			second.addLast(newNode(v))
		}

		t := time.Now()
		weaveList3(first, second)
		d := time.Since(t)
		fmt.Printf("Time1: %v, Total number of possible arrays: %v, cloneCount: %v, concatCount: %v\n", d, count3, cloneCount, concatCount)
		wg.Done()
		<-stop
	}(stop)

	go func(stop <-chan int) {
		wg.Add(1)
		first := &linkList{}
		second := &linkList{}
		for v := 1; v < 5; v++ {
			first.addLast(newNode(v))
		}

		for v := 8; v < 8+3; v++ {
			second.addLast(newNode(v))
		}

		t := time.Now()
		prefix := &linkList{}
		prefix.addFirst(newNode(6))
		weaveList(first, second, prefix)
		d := time.Since(t)
		fmt.Printf("Time2: %v, Total number of possible arrays: %v, cloneCount: %v, concatCount: %v\n", d, count1, cloneCount, concatCount)
		wg.Done()
		<-stop
	}(stop)

	go func(stop <-chan int) {
		wg.Add(1)
		first := &linkList{}
		second := &linkList{}
		for v := 1; v < 5; v++ {
			first.addLast(newNode(v))
		}

		for v := 8; v < 8+3; v++ {
			second.addLast(newNode(v))
		}

		t := time.Now()
		prefix := &linkList{}
		prefix.addFirst(newNode(6))
		weaveList2(first.head, second.head, prefix)
		prefix = &linkList{}
		prefix.addFirst(newNode(6))
		weaveList2(second.head, first.head, prefix)
		d := time.Since(t)
		fmt.Printf("Time3: %v, Total number of possible arrays: %v, cloneCount: %v, concatCount: %v\n", d, count2, cloneCount, concatCount)
		wg.Done()
		<-stop
	}(stop)

	go func(stop <-chan int) {
		wg.Add(1)
		first := &linkList{}
		second := &linkList{}
		for v := 1; v < 5; v++ {
			first.addLast(newNode(v))
		}

		for v := 8; v < 8+3; v++ {
			second.addLast(newNode(v))
		}

		t := time.Now()
		weaveList4(first, second)
		d := time.Since(t)
		fmt.Printf("Time4: %v, Total number of possible arrays: %v\n", d, count4)
		wg.Done()
		<-stop
	}(stop)

	wg.Wait()
	// Enough time for output on display
	time.Sleep(1 * time.Second)
	stop <- 0
}

// The 4th method using combination seems to be the fastest
func main() {
	first := &linkList{}
	second := &linkList{}
	for v := 1; v < 10; v++ {
		first.addLast(newNode(v))
	}

	for v := 20; v < 20+8; v++ {
		second.addLast(newNode(v))
	}

	t := time.Now()
	weaveList3(first, second)
	d := time.Since(t)
	fmt.Printf("Time1: %v, Total number of possible arrays: %v, cloneCount: %v, concatCount: %v\n", d, count3, cloneCount, concatCount)

	t = time.Now()
	prefix := &linkList{}
	prefix.addFirst(newNode(16))
	weaveList(first, second, prefix)
	d = time.Since(t)
	fmt.Printf("Time2: %v, Total number of possible arrays: %v, cloneCount: %v, concatCount: %v\n", d, count1, cloneCount, concatCount)

	t = time.Now()
	prefix = &linkList{}
	prefix.addFirst(newNode(16))
	weaveList2(first.head, second.head, prefix)
	prefix = &linkList{}
	prefix.addFirst(newNode(16))
	weaveList2(second.head, first.head, prefix)
	d = time.Since(t)
	fmt.Printf("Time3: %v, Total number of possible arrays: %v, cloneCount: %v, concatCount: %v\n", d, count2, cloneCount, concatCount)

	t = time.Now()
	weaveList4(first, second)
	d = time.Since(t)
	fmt.Printf("Time4: %v, Total number of possible arrays: %v\n", d, count4)
}
