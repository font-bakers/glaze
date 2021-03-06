.PHONY: help init venv venv-develop develop lint-black lint-pylint lint test check black clean
.DEFAULT_GOAL = help

PYTHON = python3
SHELL = bash
VENV_PATH = venv

help:
	@echo "Usage:"
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[1;34mmake %-10s\033[0m%s\n", $$1, $$2}'

init:
	@printf "Initializing git hooks...\n"
	find .git/hooks -type l -exec rm {} \;
	find .githooks -type f -exec ln -sf ../../{} .git/hooks/ \;
	@printf "\n\n\033[1;34mGit hooks initialized!\033[0m\n\n\n"

venv:
	@printf "Creating Python virtual environment...\n"
	rm -rf glaze.egg-info/ ${VENV_PATH}
	${SHELL} scripts/setup_venv.sh ${PYTHON} ${VENV_PATH} requirements.txt
	@printf "\n\nVirtual environment created! \033[1;34mRun \`source venv/bin/activate\` to activate it.\033[0m\n\n\n"

venv-develop:
	@printf "Creating Python virtual environment for development...\n"
	rm -rf glaze.egg-info/ ${VENV_PATH}
	${SHELL} scripts/setup_venv.sh ${PYTHON} ${VENV_PATH} requirements-dev.txt
	@printf "\n\nVirtual environment created! \033[1;34mRun \`source venv/bin/activate\` to activate it.\033[0m\n\n\n"

develop: init venv-develop  # Set up development environment.

lint-black:
	@printf "Checking code style with black...\n"
	black glaze/ --check --target-version=py35
	@printf "\033[1;34mBlack passes!\033[0m\n\n"

lint-pylint:
	@printf "Checking code style with pylint...\n"
	pylint glaze/ --rcfile=.pylintrc
	@printf "\033[1;34mPylint passes!\033[0m\n\n"

lint: lint-black lint-pylint  # Check code style with black and pylint.

test: clean  # Run tests.
	@printf "Running test script...\n"
	pytest
	${SHELL} glaze/tests/test_cli.sh
	@printf "\033[1;34mTests pass!\033[0m\n\n"

check: clean lint test  # Alias for `make clean lint test`.

black:  # Format code in-place with black.
	black glaze/ --target-version=py35

clean:  # Clean project directories.
	rm -rf dist/ site/ __pycache__/ *.log data/renders*
	find glaze/ -type d -name "__pycache__" -exec rm -rf {} +
	find glaze/ -type d -name "__pycache__" -delete
	find glaze/ -type f \( -name "*.pyc" -o -name "*.log" -o -name "*.png" \) -delete

package: clean  # Package glaze in preparation for releasing to PyPI.
	${PYTHON} setup.py sdist bdist_wheel
	twine check dist/*
	@printf "\n\n\033[1;34mTo upload to PyPI, run:\033[0m\n\n"
	@printf "\033[1;34m\ttwine upload dist/*\033[0m\n\n"
	@printf "\033[1;34mYou will need PyPI credentials.\033[0m\n\n"
