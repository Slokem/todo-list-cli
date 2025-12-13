# ✔️todo-list-cli

> CLI tool to maintain a personal todo list directly from the terminal

## Development Setup

### Pre-requisites

This project is using `uv`. Please start by installing it by following
[official documentation](https://docs.astral.sh/uv/getting-started/installation/)

Compatible `uv` version: **0.8.0 or higher**

### Environment Setup

#### Create Python virtual environment and install dependencies with `uv`

This project contains the following files that define and ensure the
reproducibility of the python version and the python dependencies.
> [`.python-version`, `pyproject.toml`, `uv.lock`]

In one command `uv` will:

- install the right python version is it is not already done
- create a virtual environment `.venv` if it does not exists in this folder
- install/update dependencies in the `.venv` environment

```bash
# Please run the command at the root of the repository
uv sync --locked --dev
```

⚠️ `--locked` is primordial to ensure the use of `uv.lock` if there is no plan
to update dependencies while developing.
ℹ️ `--dev` ensures that additional dependencies are installed in you virtual
environment for development (e,g, `pre-commit`, `mypy`, `pytest`, ...)

#### Pre-commit Setup

This project already included in the dev dependencies `pre-commit` (see
[official documentation](https://pre-commit.com/)). Three is thus no need to
install manually installed pre-commit. However you will need to install the
hooks via the bewlo command:

```bash
uv run pre-commit install --config pre-commit-config.yaml
```

#### Rebooting the environment

In case you had to pull or rebase your work it is important that your local
setup is aligned with the project setup.

The below command will in one go:

- Clean any existing `pre-commit` configuration
- Delete and recreate the python virtual environment `.venv`
- Re-configure `pre-commit` hooks

```bash
make env-reboot
```
