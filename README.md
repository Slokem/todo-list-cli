# ✔️todo-cli

> CLI tool to maintain a personal todo list directly from the terminal

## Development Setup

### Pre-requisites

#### uv

This project is using `uv`. Please start by installing it by following
[official documentation](https://docs.astral.sh/uv/getting-started/installation/)

Compatible `uv` version: **0.8.0 or higher**

#### sqlite3 (optional but recommended)

Optionally, if you want to explore from the terminal the database built by this
project the installation of sqlite3 is recommended.
If you are on Debian/Ubuntu you can run:

```bash
sudo apt-get update
sudo apt-get install sqlite3
```

Otherwise please follow the [official documentation](https://sqlite.org/).

Compatible with `sqlite3` version: **3.45.0 or higher**

### Environment Setup

#### Create Python virtual environment and install dependencies with `uv`

This project contains the following files that define and ensure the
reproducibility of the python version and the python dependencies.
> [`.python-version`, `pyproject.toml`, `uv.lock`]

In one command `uv` will:

- Install the right python version is it is not already done.
- Create a virtual environment `.venv` if it does not exists in this folder.
- Install/update dependencies in the `.venv` environment.

```bash
# Please run the command at the root of the repository
uv sync --locked --dev
```

⚠️ `--locked` is primordial to ensure the use of `uv.lock` if there is no plan
to update dependencies while developing.
ℹ️ `--dev` ensures that additional dependencies are installed in you virtual
environment for development (e,g, `pre-commit`, `mypy`, `pytest`, ...)

#### Pre-commit setup

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

## Development How To Guides

### Using Editable mode

When you develop you will need to edit and run the code in editable mode so
that import can be resolved. Please run:

```bash
uv pip install -e .
```

### Testing Suites

This project is using `pytest` to configure and run test. Please take a look at
the [official documentation](https://docs.pytest.org/en/stable/).

Since the tests suite is fast, `pre-commit` hook has been configured to
run them. However you can also manually run them by suing the below command:

```bash
make run-pytest
```

## Updating Project Dependencies

If you need to update dependencies on the project please follow the below
instructions:

- Update the dependencies requirements and the version of the project in the `pyproject.toml`.
- Run the command `uv sync`. This will generate an updated version of `uv.lock`.
- Run and pass all tests.
- Open a PR.
