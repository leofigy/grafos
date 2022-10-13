package models

import "fmt"

type PuzzleProcessError struct {
	msg string
}

func (e *PuzzleProcessError) Error() string {
	return fmt.Sprintf("Puzzle process error %s", e.msg)
}
