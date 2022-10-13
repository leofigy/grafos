package main

import (
	"log"
	"puzzle/models"
)

func main() {
	log.Println("puzzle solver")
	myPuzzle := models.Puzzle[int]{
		Pending: []models.Node[int]{},
		Visited: map[string]*models.Node[int]{},
	}

	log.Println(myPuzzle)

	initial := [][]int{
		{2, 1, 6},
		{4, -1, 8},
		{7, 5, 3},
	}

	target := [][]int{
		{1, 2, 3},
		{8, -1, 4},
		{7, 6, 5},
	}

	err := myPuzzle.Solve(initial, target, -1)

	if err != nil {
		log.Fatalln(err)
	}

}
