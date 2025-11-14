from _segmenter import Segmenter
import _word_rules


class WordSegmenter(Segmenter):
    """
    [Unicode TR29](https://www.unicode.org/reports/tr29/#Word_Boundaries)
    compliant word segmenter
    """

    _break_rule_keys = _word_rules.break_rule_keys
    _break_matcher = _word_rules.break_matcher

print(
    WordSegmenter()._break_matcher.pattern
)
