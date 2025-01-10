build:
	uv build

install:
	uv sync

brain-games:
	uv run brain-games

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime