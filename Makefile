.PHONY: help new-%

help:
	@echo "Usage:"
	@echo "  make new-<name>    Create a directory named <name> with main.py and README.md"


# パターンルール
new-%: # new-<name> 形式を受け付けるターゲット
	@mkdir -p $*
	@echo "# Main script for $*" > $*/main.py
	@echo "# README for $*" > $*/README.md
	@echo "Directory '$*' with main.py and README.md created."
