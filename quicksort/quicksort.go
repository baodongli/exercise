package main

import (
	"baodongli/exercise/lib/quicksort"
	"fmt"
	"math/rand" //        "sort"
	"os"
	"strconv"
	"time"
)

func main() {
	lenArg := os.Args[1]
	length, _ := strconv.Atoi(lenArg)
	A := make([]int, length)
	rand.Seed(time.Now().Unix())
	for i := 0; i < length; i++ {
		A[i] = rand.Intn(1000)
	}

	fmt.Printf("Before sort: %v\n", A)
	//B := sort.IntSlice(A)
	//B.Sort()
	quicksort.Sort(A)
	fmt.Printf("After sort: %v\n", A)
}
