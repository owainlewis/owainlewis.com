PANDOC=pandoc
INPUT = content/algebraic-data-types.md

INPUT_DIR = content
OUTPUT_DIR = posts

TEMPLATE = static/templates/template.html

FLAGS = --standalone --toc --toc-depth=2 --highlight-style tango

all:
	@for f in $(shell ls ${INPUT_DIR}); do $${f%%.*}; done

build:
	$(PANDOC) --template $(TEMPLATE) -s $(INPUT) -t html $(FLAGS) -o $(OUTPUT_DIR)/algebraic-data-types.html
