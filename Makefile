.PHONY: build
build:
	python compiler.py

.PHONY: clean
clean:
	rm -r posts/*.html
