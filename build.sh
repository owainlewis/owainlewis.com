#!/bin/bash

for path in _posts/*.md; do
  FILE=${path##*/}
  NAME="${FILE%.*}"
  pandoc \
  -H static/html/header.html \
  -A static/html/footer.html \
  ${path} \
  -o posts/${NAME}.html
done
