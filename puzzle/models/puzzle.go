package models

import (
	"fmt"
	"log"
	"sort"
)

type Puzzle[T string | uint | int] struct {
	Pending []Node[T]
	Visited map[string]*Node[T]
}

func (p *Puzzle[T]) Solve(start, target [][]T, cursor T) error {
	startNode := Node[T]{
		Values: start,
		Level:  0,
		Cost:   0,
		Move:   Origin,
		Cursor: cursor,
	}

	cost, err := startNode.ComputeDiffValuesWith(target)

	if err != nil {
		return err
	}

	startNode.Cost = cost
	p.Pending = append(p.Pending, startNode)

	for {
		if len(p.Pending) == 0 {
			log.Println("not found nothing to do")
			return nil
		}

		current := p.Pending[0]

		fmt.Println("Value and cost", current.Values, current.Cost)

		val, err := current.ComputeDiffValuesWith(target)
		log.Println("DIFERENCIA EN VALOR   ", val)

		if err != nil {
			log.Println(err)
			break
		}

		if val == 0 {
			log.Println("we found it pal !!!")
			break
		}

		nextChildren := current.ExpandChildren()
		if len(nextChildren) == 0 {
			log.Println("no more children to expend skipping")
			continue
		}

		for _, next := range nextChildren {
			log.Println("hijo calculado", next)

			_, ok := p.Visited[next.String()]

			if ok {
				log.Println("already visited skipping")
				continue
			}
			localCost, err := next.ComputeDiffValuesWith(target)

			if err != nil {
				log.Println(err)
				continue
			}

			next.Cost = localCost + int(next.Level)

			p.Pending = append(p.Pending, next)
		}

		if len(p.Pending) <= 1 {
			// resetting
			p.Pending = []Node[T]{}
		} else {
			// remove the last one
			p.Pending = p.Pending[1:]
		}

		sort.Slice(
			p.Pending, func(x, y int) bool {
				return p.Pending[x].Cost < p.Pending[y].Cost
			},
		)

		log.Println("aqui", len(p.Pending))

		p.Visited[current.String()] = &current

	}

	return nil
}
