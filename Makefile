all: build

.PHONY: server
server: build
	@python3 -m http.server 8000

.PHONY: clean
clean:
	@rm -rf posts/*.html

.PHONY: build
build: clean
	@./compile.sh
