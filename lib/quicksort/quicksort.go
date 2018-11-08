package quicksort

import "fmt"

func swap(index1, index2 int, ary []int) {
    v := ary[index1]
    ary[index1] = ary[index2]
    ary[index2] = v
}

func partition(left, right, pivot int, ary []int) int {
    r := right
    for {
        // left will never run over the end of the array due to '<' check
        // anything greater than pivot is swapped to the right
        for ary[left] < pivot {
	    left++
	}
	for r > 0 && ary[r] >= pivot {
	    r--
	}
        if left >= r {
	    break;
	} else {
	    swap(left, r, ary)
	}
    }
    swap(left, right, ary)
    return left
}

func quickSort(left, right int, ary []int) {
    if right <= left {
        return
    } else {
        partPoint := partition(left, right, ary[right], ary)
	quickSort(left, partPoint - 1, ary)
	quickSort(partPoint + 1, right, ary)
    }
}

func check(ary []int) {
    for i := 1; i < len(ary); i++ {
        if ary[i] < ary[i-1] {
            panic(fmt.Sprintf("array not sorted correctly at %v %v %v", i - 1, ary[i-1], ary[i]))
        }
    }
}

func Sort(ary []int) {
    quickSort(0, len(ary) - 1, ary)
    check(ary)
}
