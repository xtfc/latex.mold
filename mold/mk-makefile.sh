#!/usr/bin/env

cat >Makefile <<EOF
.PHONY: all
all:
	latexmk -file-line-error -pdf paper.tex

.PHONY: watch
watch:
	latexmk -halt-on-error -file-line-error -pdf -pvc paper.tex

.PHONY: clean
clean:
	latexmk -pdf -pvc -c paper.tex
EOF
