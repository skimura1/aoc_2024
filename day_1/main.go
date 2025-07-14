package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var col1 []int
	var col2 []int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		var a, b int
		_, err := fmt.Sscanf(scanner.Text(), "%d %d", &a, &b)
		if err != nil {
			fmt.Println("Failed to parse line: ", scanner.Text())
			continue
		}
		col1 = append(col1, a)
		col2 = append(col2, b)
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	fmt.Println("Part 1: ", part_1(col1, col2))
	fmt.Println("Part 2: ", part_2(col1, col2))
}

func part_1(col1, col2 []int) int {
	slices.Sort(col1)
	slices.Sort(col2)
	sum := 0

	for i := range len(col1) {
		if col1[i] > col2[i] {
			sum += col1[i] - col2[i]
		} else {
			sum += col2[i] - col1[i]
		}
	}

	return sum
}

func part_2(col1, col2 []int) int {
	freq := make(map[int]int)
	sum := 0

	for _, num1 := range col1 {
			if _, ok := freq[num1]; ok {
				continue
			}
		for _, num2 := range col2 {
			if num1 == num2 {
				freq[num1] = freq[num1] + 1
			}
		}
	}

	for _, num1 := range col1 { 
		sum += freq[num1] * num1
	}
	return sum
}
