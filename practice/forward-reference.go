package main

import (
	"fmt"
	"time"
)

// Forward reference to Entry and anonymous
type File struct {
	Entry
	contents string
	size     int
}

// Forward reference to Directory
type Entry struct {
	parent       *Directory
	created      time.Time
	lastUpdated  time.Time
	lastAccessed time.Time
	name         string
}

type Directory struct {
	Entry
	entries []*Entry
}

func main() {
	dir := &Directory{
		Entry{nil, time.Now(), time.Now(), time.Now(), "/"}, make([]*Entry, 0)}

	// Can't have "mixture of field:value and value initializers"
	// such as in below
	/*
		dlDir := &Directory{
			Entry{
				parent:       dir,
				created:      time.Now(),
				lastUpdated:  time.Now(),
				lastAccessed: time.Now(),
				name:         "Downloads",
			},
			entries: make([]*Entry, 0),
		}
	*/
	dlDir := &Directory{
		Entry{
			parent:       dir,
			created:      time.Now(),
			lastUpdated:  time.Now(),
			lastAccessed: time.Now(),
			name:         "Downloads",
		},
		make([]*Entry, 0),
	}

	docDir := &Directory{
		Entry{
			parent:       dir,
			created:      time.Now(),
			lastUpdated:  time.Now(),
			lastAccessed: time.Now(),
			name:         "Documents",
		},
		make([]*Entry, 0),
	}

	file := &File{
		Entry{
			parent:       dlDir,
			created:      time.Now(),
			lastUpdated:  time.Now(),
			lastAccessed: time.Now(),
			name:         "hello.txt",
		},
		"Hello, how are you doing today?", 0,
	}

	file1 := &File{
		Entry{
			parent:       docDir,
			created:      time.Now(),
			lastUpdated:  time.Now(),
			lastAccessed: time.Now(),
			name:         "REAME.md",
		},
		"This is a sample of using anonymous field and forward reference", 0,
	}
	fmt.Printf("%v\n", file)
	fmt.Printf("%v\n", file1)
}
