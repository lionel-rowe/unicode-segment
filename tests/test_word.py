from src.word import WordSegmenter
from tests._run_segmenter_tests import run_segmenter_unicode_break_tests

segmenter = WordSegmenter()


def test_word_segmenter_unicode_break_tests():
    run_segmenter_unicode_break_tests(segmenter, "WordBreakTest.txt")
