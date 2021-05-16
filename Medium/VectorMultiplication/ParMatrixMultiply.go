package main

import (
	"fmt"
)

func main() {
	matrix := [][]int{
		{1, 2, 3, 4, 5},
		{6, 7, 8, 9, 10},
		{11, 12, 13, 14, 15},
		{16, 17, 18, 19, 20},
		{21, 22, 23, 24, 25},
	}
	vector := []int{10, 20, 30, 40, 50}

	product := multiply(matrix, vector)

	for _, row := range product {
		fmt.Printf("%v\n", row)
	}
}

func multiply(matrix [][]int, vector []int) [][]int {
	product_matrix := make([][]int, len(matrix))
	channels := make([]chan []int, len(matrix))

	for i := range matrix {
		channels[i] = make(chan []int)
		go vector_multiply(matrix[i], vector, channels[i])
	}

	for i := range matrix {
		product_matrix[i] = <-channels[i]
	}

	return product_matrix
}

func vector_multiply(vector_a []int, vector_b []int, c chan<- []int) {
	product_vector := make([]int, len(vector_a))

	for i := range vector_a {
		product_vector[i] = vector_a[i] * vector_b[i]
	}

	c <- product_vector
	close(c)
}
