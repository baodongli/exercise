package shellsort

import "fmt"

func ShellSort(ary []int) {
    interval := 1
    for interval < len(ary) / 3 {
        interval = interval * 3 + 1
    }
    fmt.Printf("interval: %v\n", interval)
    for interval > 0 {
        for outer := interval; outer < len(ary); outer++ {
	    valueToInsert := ary[outer]
	    inner := outer
	    for inner > interval - 1 && ary[inner - interval] > valueToInsert {
	        ary[inner] = ary[inner - interval]
	        inner -= interval
	    }
	    ary[inner] = valueToInsert
        }
	interval = (interval - 1) / 3
    }
}
