#! /bin/bash

PANDOC=pandoc
INPUT=content/algebraic-data-types.md
INPUT_DIR=content
OUTPUT_DIR=posts
TEMPLATE=static/templates/template.html
FLAGS="--standalone --toc --toc-depth=2 --highlight-style tango"

for f in $(ls ${INPUT_DIR}) ; do
    echo "Compiling ${f%%.*}" ;
    $PANDOC --template $TEMPLATE \
    -s $INPUT_DIR/$f \
    -t html \
    --standalone --toc --toc-depth=2 --highlight-style tango \
    -o $OUTPUT_DIR/${f%%.*}.html ;
done
