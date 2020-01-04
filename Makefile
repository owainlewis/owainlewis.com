all: dev

.PHONY: build
build:
	python compiler.py

.PHONY: clean
clean:
	rm -r posts/*.html

dev: clean build
	python -m SimpleHTTPServer 5000
