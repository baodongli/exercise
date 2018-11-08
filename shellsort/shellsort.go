package main

import (
        "fmt"
        "math/rand"
        "os"
        "strconv"
        "time"

        "lib/shellsort"
)

func main() {
   lenArg := os.Args[1] 
   length, _ := strconv.Atoi(lenArg)
   
   A := make([]int, length)
   
   rand.Seed(time.Now().Unix())
   for i := 0; i < length; i++ {
       A[i] = rand.Int() % 1000
   }
   
   fmt.Println("before sort: %v", A)
   shellsort.ShellSort(A)
   fmt.Println("after sort: %v", A)
}
