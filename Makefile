test:
ifneq (,$(findstring --watch,$(args)))
	deno run -A ./tests/watch.ts --args "$(args)"
else
	uv run pytest --mypy --ruff $(args)
endif

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
