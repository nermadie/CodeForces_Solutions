// A. The 67th Integer Problem
package main

import "fmt"

func solve(x int) int{
	return x;
}

func main(){
	var n int
	fmt.Scanln(&n)
	for i := 0; i < n; i++ {
		var x int
		fmt.Scanln(&x)
		fmt.Println(solve(x))
	}
}