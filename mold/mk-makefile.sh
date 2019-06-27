#!/usr/bin/env

cat >Makefile <<EOF
.PHONY: all
all:
	latexmk -file-line-error -pdf $PAPER

.PHONY: watch
watch:
	latexmk -halt-on-error -file-line-error -pdf -pvc $PAPER

.PHONY: clean
clean:
	latexmk -pdf -pvc -c $PAPER
EOF
