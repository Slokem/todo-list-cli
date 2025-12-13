.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean-pre-commit-hooks
clean-pre-commit-hooks: ## Uninstall hooks and clean pre-commit cache
	uv run pre-commit uninstall
	uv run pre-commit clean

uninstall: ## Uninstall python environment
	@$(MAKE) clean-pre-commit-hooks
	rm -rf .venv

install: ## Install python environment
	uv sync --locked --dev
	uv run pre-commit install --config .pre-commit-config.yaml

env-reboot: ## Start a fresh environment setup
	@$(MAKE) uninstall
	@$(MAKE) install
