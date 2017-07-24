.PHONY: build
build:
	python compiler.py

.PHONY: clean
clean:
	rm -r posts/*.html

dev:
	python -m SimpleHTTPServer 5000
