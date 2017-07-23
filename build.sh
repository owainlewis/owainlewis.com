#!/bin/bash

for path in _posts/*.md; do
file=${path##*/}
filename="${file%.*}"
pandoc \
-H static/html/header.html \
-A static/html/footer.html \
${path} \
-o posts/${filename}.html
done
