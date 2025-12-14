.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: pre-commit-install-hooks
pre-commit-install-hooks: ## Install hooks and run on all files.
	uv run pre-commit install --config .pre-commit-config.yaml

.PHONY: pre-commit-run-hooks
pre-commit-run-hooks: ## Run hooks on all files.
	uv run pre-commit run --all-files

.PHONY: pre-commit-clean-hooks
pre-commit-clean-hooks: ## Uninstall hooks and clean pre-commit cache.
	uv run pre-commit uninstall
	uv run pre-commit clean

.PHONY: install
env-install: ## Install dev environment.
	uv sync --locked --dev
	@$(MAKE) pre-commit-install-hooks
	@$(MAKE) pre-commit-run-hooks

.PHONY: uninstall
env-uninstall: ## Uninstall dev environment.
	@$(MAKE) pre-commit-clean-hooks
	rm -rf .venv

.PHONY: env-reboot
env-reboot: ## Start a fresh environment setup.
	@$(MAKE) env-uninstall
	@$(MAKE) env-install

.PHONY: run-mypy
run-mypy: ## Run mypy on src/ and tests/ .
	uv run mypy --config-file=pyproject.toml src/ tests/

.PHONY: run-pytest
run-pytest: ## Run pytest on the entire project
	uv run pytest -vv

.PHONY: db-select-all-tasks
db-select-all-tasks: ## Select all Tasks in the CLI Sqlite database. [sqlite3 required]
	sqlite3 -header -column ~/.todocli/todo.db "SELECT * FROM task;"
