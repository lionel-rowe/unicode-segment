test:
	uv run pytest --mypy --benchmark-autosave

publish:
	rm dist/* 2>/dev/null || true \
		&& uv build \
		&& twine upload dist/*

fmt:
	dprint fmt

benchmark-compare:
	uv run pytest-benchmark compare --group-by func
