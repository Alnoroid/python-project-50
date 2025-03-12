install:
	uv sync

build:
	uv build

gendiff:
	uv run gendiff

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --reinstall dist/*.whl

lint:
	uv run ruff check gendiff

lint_fix:
	uv run ruff check gendiff --fix