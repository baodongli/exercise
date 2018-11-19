package main

import (
	"fmt"
)

type Gender int

const (
	MALE = iota
	FEMAL
)

type Person struct {
	gender Gender
	age    int
	name   string
}

func main() {
	persons := []Person{{0, 10, "Chris"}, {1, 10, "Megan"}}

	persons2 := make([]Person, 2)
	// Comments 1
	// Copy: the first argument is the destinatio, and must be a slice (allocated by make)
	// copy copies the content
	n := copy(persons2, persons)
	fmt.Printf("n = %v, %v\n", n, persons2)
	// modification only affects persons2, not persons
	persons2[0].age = 100
	fmt.Printf("Persons: %v; Persons2 %v\n", persons, persons2)

	// Comments 2
	// Only copies the slice data, but not the underlying array the slice refers to
	// both person2 and persons refers to the same underlying array
	// Therefore, modification affects both
	persons2 = persons
	persons2[0].age = 100
	fmt.Printf("Persons: %v; Persons2 %v\n", persons, persons2)

	vals := []int{1, 2, 5, 6}
	var vals1 []int
	// Comments 3
	// Note that vals1 is nil, so the copy doesn't copy anything
	copy(vals1, vals)
	fmt.Printf("vals1: %v; vals: %v\n", vals1, vals)

	// Same as Comments 2
	vals1 = vals
	vals1[2] = 100
	fmt.Printf("vals1: %v; vals: %v\n", vals1, vals)
}
