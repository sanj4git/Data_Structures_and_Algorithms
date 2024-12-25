package main

import (
	"fmt"
	"math/rand"
)

type Node struct {
	value int
	level int     // Store the level of each node.
	next  []*Node // This allows each node in the skip list to have multiple pointers to other nodes
} 				  // at different levels, supporting the layered structure of the skip list.

type skipList struct {
	head         *Node
	maxNoOfLevel int
}

func coinToss(maxNoOfLevel int) int {
	level := 0
	for level < maxNoOfLevel && rand.Intn(2) == 1 {
		level++
	}
	return level
}

func newSkipList(maxNoOfLevel int) *skipList {
	head := &Node{
		value: 0,
		level: maxNoOfLevel,
		next:  make([]*Node, maxNoOfLevel), // Initialize with maxNoOfLevel levels.
	}

	return &skipList{
		head:         head,
		maxNoOfLevel: maxNoOfLevel, // Set the maximum number of levels.
	}
}

func (sl *skipList) insert(value int) {
	newLevel := coinToss(sl.maxNoOfLevel)

	newNode := &Node{
		value: value,
		level: newLevel,
		next:  make([]*Node, newLevel+1),
	}

	current := sl.head
	update := make([]*Node, len(sl.head.next))
	for i := len(sl.head.next) - 1; i >= 0; i-- {
		for current.next[i] != nil && current.next[i].value < value {
			current = current.next[i]
		}
		update[i] = current
	}

	for i := 0; i <= newLevel; i++ {
		newNode.next[i] = update[i].next[i]
		update[i].next[i] = newNode
	}
}

func (sl *skipList) remove(value int) {
	current := sl.head
	update := make([]*Node, sl.maxNoOfLevel)

	// Traverse the list to find the position of the node to be deleted.
	for i := sl.maxNoOfLevel - 1; i >= 0; i-- {
		for current.next[i] != nil && current.next[i].value < value {
			current = current.next[i]
		}
		update[i] = current
	}

	current = current.next[0] // Clear the reference to the current node.

	if current != nil && current.value == value {
		for i := 0; i < len(current.next); i++ {
			update[i].next[i] = current.next[i]
		}

		for sl.maxNoOfLevel > 0 && sl.head.next[sl.maxNoOfLevel-1] == nil {
			sl.maxNoOfLevel--
		}
		fmt.Println("Element", value, "deleted successfully.")
	} else {
		fmt.Println("Element:", value, "does not exist!")
	}
}

func (sl *skipList) search(value int) bool {
	current := sl.head

	for i := len(sl.head.next) - 1; i >= 0; i-- {
		// Keep moving forward at the current level
		//if the next node's value is less than the search value.
		for current.next[i] != nil && current.next[i].value < value {
			current = current.next[i]
		}
	}

	current = current.next[0]

	if current != nil && current.value == value {
		fmt.Println("Element", value, "found.")
		return true
	} else {
		fmt.Println("Element", value, "not found.")
		return false
	}
}

func (sl *skipList) display() {
	fmt.Println("Skip List:")

	for i := len(sl.head.next) - 1; i >= 0; i-- {
		current := sl.head.next[i]

		fmt.Printf("Level %d: ", i)

		for current != nil {
			fmt.Printf("%d ", current.value)
			current = current.next[i]
		}
		fmt.Println()
	}
}

func main() {
	maxLevels := 10
	skipList := newSkipList(maxLevels)

	skipList.insert(10)
	skipList.insert(20)
	skipList.insert(30)
	skipList.insert(40)
	skipList.insert(50)

	skipList.display()

	skipList.search(20)
	skipList.search(40)

	skipList.remove(20)
	skipList.remove(40)

	skipList.display()
}
