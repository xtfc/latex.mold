#!/usr/bin/env sh

# Useful when working with overleaf.

git add -p && \
  git commit -m 'Local changes' && \
  git push origin master
