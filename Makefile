.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: pre-commit-clean-hooks
pre-commit-clean-hooks: ## Uninstall hooks and clean pre-commit cache.
	uv run pre-commit uninstall
	uv run pre-commit clean

.PHONY: install-and-run
pre-commit-install-run-hooks: ## Install hooks and run on all files.
	uv run pre-commit install --config .pre-commit-config.yaml
	uv run pre-commit run --all-files

.PHONY: install
install: ## Install dev environment.
	uv sync --locked --dev
	@$(MAKE) pre-commit-install-run-hooks

.PHONY: uninstall
uninstall: ## Uninstall dev environment.
	@$(MAKE) pre-commit-clean-hooks
	rm -rf .venv

.PHONY: env-reboot
env-reboot: ## Start a fresh environment setup.
	@$(MAKE) uninstall
	@$(MAKE) install
