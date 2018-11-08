package main

import (
    "fmt"
    "math/rand"
    "os"
    "strconv"
)

const (
    NP = 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4
)

func validate3() {
    NP3 := 4 * 4 * 4
    choices := make([][3]int, NP3)
    ch := 0
    for i0 := 0; i0 < 4; i0++ {
        for i1 := 0; i1 < 4; i1++ {
            for i2 := 0; i2 < 4; i2++ {
                choices[ch] = [3]int{i0, i1, i2}
                ch++
            }
        }
    }
    good := 0
    for ch = 0; ch < NP3; ch++ {
        correctAnswer := 0
        //fmt.Printf("%v\n", choices[ch])
        for i := 0; i < 3; i++ {
            if choices[ch][i] == 1 {
                correctAnswer++
            }
        }
        if correctAnswer >= 2 {
            //fmt.Println("GOOD")
            good++
        }
    }
    fmt.Printf("good ones %v out of %v, probability %f\n", good, NP3, float32(good)/float32(NP3))
}

func validate10Binomial() {
    factorial := func(num int) int {
        f := 1
        for i := 2; i <= num; i++ {
            f = f * i
        }
        return f
    }

    power := func(p float32, n int) float32 {
        r := p
        for i := 1; i < n; i++ {
	    r = r * p
	}
        return r
    }

    cf := func(total, get int) int {
       return factorial(total) / (factorial(get) * factorial(total - get))
    }

    r := float32(0.25)
    w := float32(0.75)
    fmt.Printf("Probability %v\n", power(r, 10) + float32(cf(10, 9)) * power(r, 9) * power(w, 1) + float32(cf(10, 8)) * power(r, 8) * power(w, 2) + float32(cf(10, 7)) * power(r, 7) * power(w, 3) + float32(cf(10, 6)) * power(r, 6) * power(w, 4))
}

func validate4() {
    NP4 := 4 * 4 * 4 * 4
    choices := make([][4]int, NP4)
    ch := 0
    for i0 := 0; i0 < 4; i0++ {
        for i1 := 0; i1 < 4; i1++ {
            for i2 := 0; i2 < 4; i2++ {
                for i3 := 0; i3 < 4; i3++ {
		    choices[ch] = [4]int{i0, i1, i2, i3}
		    ch++
                }
            }
        }
    }
    good := 0
    for ch = 0; ch < NP4; ch++ {
        //fmt.Printf("%v\n", choices[ch])
        correctAnswer := 0
        for i := 0; i < 4; i++ {
            if choices[ch][i] == 1 {
                correctAnswer++
            }
        }
        if correctAnswer >= 2 {
	    //fmt.Printf("%v\n", choices[ch])
            good++
        }
    }
    fmt.Printf("good ones %v out of %v, probability %f\n", good, NP4, float32(good)/float32(NP4))
}

func validate10() {
    choices := make([][10]int, NP)
    ch := 0
    for i0 := 0; i0 < 4; i0++ {
	for i1 := 0; i1 < 4; i1++ {
	    for i2 := 0; i2 < 4; i2++ {
		for i3 := 0; i3 < 4; i3++ {
		    for i4 := 0; i4 < 4; i4++ {
			for i5 := 0; i5 < 4; i5++ {
			    for i6 := 0; i6 < 4; i6++ {
				for i7 := 0; i7 < 4; i7++ {
				    for i8 := 0; i8 < 4; i8++ {
					for i9 := 0; i9 < 4; i9++ {
					    choices[ch] = [10]int{i0, i1, i2, i3, i4, i5, i6, i7, i8, i9}    
					    ch++
					}
				    }
				}
			    }
			}
		    }
		}
	    }
	}
    }
    good := 0
    for ch = 0; ch < NP; ch++ {
	correctAnswer := 0
        for i := 0; i < 10; i++ {
	    if choices[ch][i] == 1 {
		correctAnswer++
	    }
        }
	if correctAnswer >= 6 {
            good++
	}
    }
    fmt.Printf("good ones %v out of %v, probability %f\n", good, NP, float32(good)/float32(NP))
}

func main() {
    trialCount, _ := strconv.Atoi(os.Args[1])
    goodTrial := 0
    answers := make([]int, 10)
    for i := 0; i < 10; i++ {
        answers[i] = rand.Intn(4)
    } 

    for t := 0; t < trialCount; t++ {
        correctAnswer := 0
	for i := 0; i < 10; i++ {
            a := rand.Intn(4)
	    // fmt.Printf("%v ", a)
	    if a == answers[i] {
		correctAnswer++
	    }
	}
	// fmt.Printf("\n ")
	if correctAnswer >= 6 {
            goodTrial++
	}
    }
    fmt.Printf("got good trial %v out of %v, probability %f\n", goodTrial, trialCount, float32(goodTrial)/float32(trialCount))
    validate10()
    validate4()
    validate3()
    validate10Binomial()
}
