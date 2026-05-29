// C. The 67th Permutation Problem
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func solve(n int){
	var arr []string = make([]string, 3*n)
	for i := 0; i < n; i++ {
		arr[i * 3] = fmt.Sprintf("%d", i+1)
		arr[i * 3 + 1] = fmt.Sprintf("%d", n+i*2+1)
		arr[i * 3 + 2] = fmt.Sprintf("%d", n+i*2+2)
	}
	fmt.Println(strings.Join(arr, " "))
}

func main(){
	reader := bufio.NewReader(os.Stdin)
	var t int
	fmt.Fscan(reader, &t)

	for i := 0; i < t; i++ {
		var n int
		fmt.Fscan(reader, &n)
		solve(n)
	}
}