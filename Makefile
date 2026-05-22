.PHONY: install install-dev test clean build help

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install the package
	pip install -e .

install-dev: ## Install with development dependencies
	pip install -e ".[dev]"

test: ## Run tests
	python test_cli.py

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean ## Build the package
	python -m build

format: ## Format code with black
	black src/

lint: ## Lint code with ruff
	ruff check src/

publish: build ## Build and publish to PyPI (requires credentials
	twine upload dist/*

# Convenience targets for testing commands
stock-history: ## Test stock history command
	efinance-cli stock history 600519 --limit 10

stock-realtime: ## Test stock realtime command
	efinance-cli stock realtime --limit 10

fund-history: ## Test fund history command
	efinance-cli fund history 161725 --limit 10

bond-realtime: ## Test bond realtime command
	efinance-cli bond realtime --limit 10

futures-info: ## Test futures info command
	efinance-cli futures info --limit 10
