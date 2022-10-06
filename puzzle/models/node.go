package models

type Direction uint8

const (
	Origin Direction = iota
	Right
	Left
	Down
	Up
)

type Node[T string | uint | int] struct {
	Values [][]T
	Level  uint
	Cost   int
	Move   Direction
	Cursor T
}

type Point struct {
	X int
	Y int
}

func (n *Node[T]) FindValue(value T) (int, int, error) {
	for i := 0; i < len(n.Values); i++ {
		for j := 0; j < len(n.Values[i]); j++ {
			if n.Values[i][j] == value {
				return i, j, nil
			}
		}
	}
	return -1, -1, &PuzzleProcessError{"unable to find directions for the value in the puzzle"}
}
