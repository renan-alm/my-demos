package main

import (
	"fmt"
	"net/http"
)

func handleGitHub(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "GitHub Handle: your-github-handle")
}

func main() {
	http.HandleFunc("/", handleGitHub)
	fmt.Println("Server is listening on port 8080...")
	http.ListenAndServe(":8080", nil)
}
