from unicode_segment import SentenceSegmenter, WordSegmenter, GraphemeSegmenter
from unicode_segment._segmenter import Segmenter
from faker import Faker

SEED = 16070459220457221183


def run_benchmark(benchmark, segmenter: Segmenter):
    faker = Faker()
    faker.seed_instance(SEED)

    with open(
        f".benchmarks/regexes/{segmenter.__class__.__name__}.txt", "w", encoding="utf-8"
    ) as f:
        f.write(f"{segmenter._break_matcher.pattern}\n")

    def run_test(text: str):
        list(segmenter.segment(text))

    def setup():
        text = faker.text(500)
        # return (args, kwargs) for `run_test`
        return (text,), {}

    benchmark.pedantic(run_test, setup=setup, rounds=100)


def test_sentence_segmenter_benchmark(benchmark):
    run_benchmark(benchmark, SentenceSegmenter())


def test_word_segmenter_benchmark(benchmark):
    run_benchmark(benchmark, WordSegmenter())


def test_grapheme_segmenter_benchmark(benchmark):
    run_benchmark(benchmark, GraphemeSegmenter())
