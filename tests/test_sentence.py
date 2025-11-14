from src.unicode_segment.sentence import SentenceSegmenter
from tests._run_segmenter_tests import run_segmenter_unicode_break_tests

segmenter = SentenceSegmenter()


def test_sentence_segmenter_unicode_break_tests():
    run_segmenter_unicode_break_tests(segmenter, "SentenceBreakTest.txt")


def test_sentence_segmenter_basic():
    # Example from https://www.regular-expressions.info/unicodeboundaries.html#sentence
    text = (
        '"Dr. John works at I.B.M., doesn\'t he?", asked Alice. "Yes," replied Charlie.'
    )
    # Note that the first split is wrong, but it's a known limitation of the Unicode algorithm that it can never
    # give 100% results due to abbreviations etc.
    expected = [
        '"Dr. ',
        "John works at I.B.M., doesn't he?\", asked Alice. ",
        '"Yes," replied Charlie.',
    ]
    actual = segmenter.split(text)
    assert actual == expected


def test_sentence_segmenter_readme_example():
    text = "".join(
        [
            "This, that, the other thing, etc. Another sentence... A, b, c, etc., and ",
            "more. D, e, f, etc. and more. One, i. e. two. Three, i. e., four. Five, ",
            "i.e. six. You have 4.2 messages. Property access: `a.b.c`.",
        ]
    )

    sentences = segmenter.split(text)

    assert sentences == [
        "This, that, the other thing, etc. ",
        "Another sentence... ",
        "A, b, c, etc., and more. ",
        "D, e, f, etc. and more. ",
        "One, i. e. two. ",
        "Three, i. e., four. ",
        "Five, i.e. six. ",
        "You have 4.2 messages. ",
        "Property access: `a.b.c`.",
    ]
