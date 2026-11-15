// wordutil: a tiny text-statistics CLI for the Jenkins Go release lab.
//
// Usage:
//   wordutil                 counts text piped from stdin
//   wordutil file.txt [...]  counts one or more files
//
// Output is a JSON object with line/word/character counts.
package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"strings"
)

// Stats holds the text measurements produced by Analyse.
type Stats struct {
	Files  int    `json:"files"`
	Lines  int    `json:"lines"`
	Words  int    `json:"words"`
	Chars  int    `json:"chars"`
	Source string `json:"source"`
}

// Analyse streams text and returns line/word/character counts.
func Analyse(r io.Reader, source string) (Stats, error) {
	st := Stats{Source: source}
	sc := bufio.NewScanner(r)
	sc.Buffer(make([]byte, 0, 64*1024), 1024*1024)
	for sc.Scan() {
		line := sc.Text()
		st.Lines++
		st.Chars += len(line) + 1 // +1 counts the newline
		st.Words += len(strings.Fields(line))
	}
	return st, sc.Err()
}

func run() error {
	if len(os.Args) > 1 {
		total := Stats{Source: fmt.Sprintf("%d file(s)", len(os.Args)-1)}
		for _, path := range os.Args[1:] {
			f, err := os.Open(path)
			if err != nil {
				return err
			}
			st, err := Analyse(f, path)
			_ = f.Close()
			if err != nil {
				return err
			}
			total.Files++
			total.Lines += st.Lines
			total.Words += st.Words
			total.Chars += st.Chars
		}
		return printJSON(total)
	}

	st, err := Analyse(os.Stdin, "stdin")
	if err != nil {
		return err
	}
	return printJSON(st)
}

func printJSON(st Stats) error {
	out, err := json.MarshalIndent(st, "", "  ")
	if err != nil {
		return err
	}
	fmt.Println(string(out))
	return nil
}

func main() {
	if err := run(); err != nil {
		fmt.Fprintln(os.Stderr, "wordutil:", err)
		os.Exit(1)
	}
}
