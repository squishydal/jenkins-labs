package main

import (
	"strings"
	"testing"
)

func TestAnalyseCounts(t *testing.T) {
	input := "hello jenkins world\nsecond line here\n"
	st, err := Analyse(strings.NewReader(input), "test")
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if st.Lines != 2 {
		t.Errorf("Lines = %d, want 2", st.Lines)
	}
	if st.Words != 6 {
		t.Errorf("Words = %d, want 6", st.Words)
	}
	if st.Chars != len(input) {
		t.Errorf("Chars = %d, want %d", st.Chars, len(input))
	}
}

func TestAnalyseEmptyInput(t *testing.T) {
	st, err := Analyse(strings.NewReader(""), "empty")
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if st.Lines != 0 || st.Words != 0 || st.Chars != 0 {
		t.Errorf("expected zeros, got %+v", st)
	}
}

func TestAnalyseSingleLineNoTrailingNewline(t *testing.T) {
	st, err := Analyse(strings.NewReader("one two three"), "test")
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if st.Lines != 1 || st.Words != 3 {
		t.Errorf("Lines/Words = %d/%d, want 1/3", st.Lines, st.Words)
	}
}
