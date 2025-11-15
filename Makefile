test:
	deno run -A ./tests/watch.ts

publish:
	rm dist/* 2>/dev/null || true \
		&& uv build \
		&& twine upload dist/*

fmt:
	dprint fmt

benchmark-save:
	uv run pytest --mypy --benchmark-autosave

benchmark-compare:
	uv run pytest-benchmark compare --group-by func
