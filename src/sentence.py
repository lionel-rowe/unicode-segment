from _segmenter import Segmenter
import _sentence_rules


class SentenceSegmenter(Segmenter):
    """
    [Unicode TR29](https://www.unicode.org/reports/tr29/#Sentence_Boundaries)
    compliant sentence segmenter
    """

    _break_rule_keys = _sentence_rules.break_rule_keys
    _break_matcher = _sentence_rules.break_matcher
