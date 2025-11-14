from src.grapheme import GraphemeSegmenter
from tests._run_segmenter_tests import run_segmenter_unicode_break_tests

segmenter = GraphemeSegmenter()


def test_grapheme_segmenter_unicode_break_tests():
    run_segmenter_unicode_break_tests(segmenter, "GraphemeBreakTest.txt")
