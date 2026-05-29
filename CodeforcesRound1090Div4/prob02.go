package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(arr []int) int {
	max := arr[0]
	totalSum := -arr[0]
	for i := 1; i < len(arr); i++ {
		if arr[i] > max {
			max = arr[i]
		}
		totalSum -= arr[i]
	}
	return totalSum + max * 2
}

func main(){
	reader := bufio.NewReader(os.Stdin)

	var t int
	fmt.Fscan(reader, &t)

	for i := 0; i < t; i++ {
		arr := make([]int, 7)

		for j := 0; j < 7; j++ {
			fmt.Fscan(reader, &arr[j])
		}
		fmt.Println(solve(arr))
	}
}