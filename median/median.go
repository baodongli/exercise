package main

import (
        "fmt"
	"math/rand"
        "os"
        "strconv"
        "time"

	"lib/quicksort"
)

type aryPos struct {
    ary   []int
    right int
    which int
}

func findPos(fromAry, inAry *aryPos) int {
    foundValue := fromAry.ary[fromAry.right]
    left := 0
    if foundValue <= inAry.ary[left] {
        return left
    }
    right := inAry.right
    for right - left > 1 {
        midIndex := (left + right) / 2
	if foundValue >= inAry.ary[midIndex] {
	    left = midIndex
	} else {
	    right = midIndex
	}
    }
    fmt.Printf("Find Pos %v in Array %v\n", right, inAry.which)
    return right
}

func locate(ary1, ary2 *aryPos, locateFn func(*aryPos, *aryPos)(bool, int)) int {
    for {
        if ary1.ary[ary1.right] >= ary2.ary[ary2.right] {
	    if found, median := locateFn(ary2, ary1); found {
	        return median
	    }
	} else {
	    if found, median := locateFn(ary1, ary2); found {
	        return median
	    }
	}
    }
}

func FindMedian(A1, A2 []int) int {
    ary1Len := len(A1)
    ary2Len := len(A2)

    ta := [2]aryPos {{A1, ary1Len - 1, 1},
		    {A2, ary2Len - 1, 2},
	      }

    a1Median := A1[ary1Len / 2]
    a2Median := A2[ary2Len / 2]

    if a1Median <= a2Median {
	ta[1].right = ary2Len / 2
    } else {
        ta[0].right = ary1Len / 2
    }
    
    medianIndex := (ary1Len + ary2Len) / 2
    return locate(&ta[0], &ta[1], func(fromAry, inAry *aryPos) (found bool, median int){
        pos := findPos(fromAry, inAry)
	leftCount := fromAry.right + pos

	fmt.Printf("Leftcount %v\n", leftCount)
	if medianIndex >= leftCount {
	    if medianIndex == leftCount {
	        median = fromAry.ary[fromAry.right]
		fmt.Printf("Median value found in array %v: %v\n", fromAry.which, median)
		found = true
	    } else {
		pos += (medianIndex - leftCount) - 1  
		median = inAry.ary[pos]
		fmt.Printf("Median value found in array %v: %v\n", inAry.which, inAry.ary[pos])
		found = true
	    }
	} else {
	    if pos >= 1 {
		inAry.right = pos - 1
		fromAry.right--
		found = false
	    } else {
		// array fromAry [0-right] can be prepended in front of array inAry
		// and the median is in between 0 and fromAry.right
		fromAry.right--
		median = fromAry.ary[medianIndex]
		fmt.Printf("Median value found in array %v: %v\n", fromAry.which, median)
		found = true
	    }
	}
	return
    })
}

func oddEvenArray(ary1Len, ary2Len int) {
    A1 := make([]int, ary1Len)
    A2 := make([]int, ary2Len)
    A3 := make([]int, ary1Len + ary2Len)

    for i := 0; i < ary1Len; i++ {
        A1[i] = i * 2 + 1
	A3[i] = A1[i]
    }

    for i := 0; i < ary2Len; i++ {
        A2[i] = i * 2 + 2
	A3[i + ary1Len] = A2[i]
    }

    fmt.Printf("Array 1: %v\n", A1)
    fmt.Printf("Array 2: %v\n", A2)
    quicksort.Sort(A3)
    medianIndex := (ary1Len + ary2Len) / 2
    fmt.Printf("Combined Array: %v with Median %v at %v\n", A3, A3[medianIndex], medianIndex)
    median := FindMedian(A1, A2)
    if median != A3[medianIndex] {
        panic(fmt.Sprintf("Found median %v not equal to %v\n", median, A3[medianIndex]))
    }
}

func randArray(ary1Len, ary2Len int) {
    rand.Seed(time.Now().Unix())

    A1 := make([]int, ary1Len)
    A2 := make([]int, ary2Len)
    A3 := make([]int, ary1Len + ary2Len)

    for i := 0; i < ary1Len; i++ {
        A1[i] = rand.Intn(1000)
	A3[i] = A1[i]
    }
    
    for i := 0; i < ary2Len; i++ {
        A2[i] = rand.Intn(1000)
	A3[i + ary1Len] = A2[i]
    }

    quicksort.Sort(A1)
    fmt.Printf("Array 1: %v\n", A1)
    quicksort.Sort(A2)
    fmt.Printf("Array 2: %v\n", A2)
    quicksort.Sort(A3)
    medianIndex := (ary1Len + ary2Len) / 2
    fmt.Printf("Combined Array: %v with Median %v at %v\n", A3, A3[medianIndex], medianIndex)
    median := FindMedian(A1, A2)
    if median != A3[medianIndex] {
        panic(fmt.Sprintf("Found median %v not equal to %v\n", median, A3[medianIndex]))
    }
}

func main() {
    ary1Len, _ := strconv.Atoi(os.Args[1])
    ary2Len, _ := strconv.Atoi(os.Args[2])
    randArray(ary1Len, ary2Len)

    // oddEvenArray(ary1Len, ary2Len)
}
