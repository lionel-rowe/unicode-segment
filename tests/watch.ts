import { debounce } from 'jsr:@std/async@1.0.15/debounce'
import { globToRegExp } from 'jsr:@std/path@1.1.2'

const DEBOUNCE_MS = 200

const excludeGlobs = [
	'**/venv/**',
	'**/__pycache__/**',
	'**/*.pyc',
	'**/*.egg-info/**',
].map((g) => globToRegExp(g))
const includeGlobs = [
	'**/*.py',
	'**/*.txt',
].map((g) => globToRegExp(g))

const test = debounce(async () => {
	await new Deno.Command(
		'uv',
		{
			args: ['run', 'pytest', '--mypy', '--ruff'],
		},
	).spawn().output()

	console.info('Test run complete, watching for changes...')
}, DEBOUNCE_MS)

test()
await watch()

async function watch() {
	for await (const event of Deno.watchFs(['tests', 'src'])) {
		if (
			event.kind === 'modify'
			&& event.paths.some((path) => {
				return includeGlobs.some((rgx) => rgx.test(path))
					&& !excludeGlobs.some((rgx) => rgx.test(path))
			})
		) {
			test()
		}
	}
}
