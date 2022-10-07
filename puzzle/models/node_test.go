package models

import (
	"fmt"
	"testing"
)

func TestCreateNode(t *testing.T) {
	node := Node[uint]{
		Values: [][]uint{
			{1, 2, 3},
			{4, 5, 6},
			{7, 0, 8},
		},
		Level:  0,
		Cost:   0,
		Move:   Left,
		Cursor: uint(Origin),
	}
	fmt.Println(node)

	_, _, err := node.FindValue(uint(100))

	if err == nil {
		fmt.Println("unexpected behavior value found , it supposed to no exists")
		t.Failed()
	}

	i, j, err := node.FindValue(uint(6)) // (0,1)

	if err != nil {
		t.Fatalf("finding value %s", err)
	}

	if i != 0 || j != 1 {
		fmt.Println("invalid coordinates, expecting 0,1")
	}

	fmt.Println(i, j)
	fmt.Println("all good")
}

func TestShuffle(t *testing.T) {
	node := Node[uint]{
		Values: [][]uint{
			{1, 2, 3},
			{4, 5, 6},
			{7, 0, 8},
		},
		Level:  0,
		Cost:   0,
		Move:   Left,
		Cursor: uint(Origin),
	}

	target := node.CopyAndShuffle(Point{0, 0}, Point{0, 2})
	fmt.Println(target)

}
