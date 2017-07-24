.PHONY: build
build:
	scripts/build.sh

.PHONY: clean
clean:
	rm -r posts/*.html
