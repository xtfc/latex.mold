#!/usr/bin/env sh

latexmk -halt-on-error -file-line-error -pdf -pvc $PAPER
