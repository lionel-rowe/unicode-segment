from ._segmenter import Segmenter
from ._sentence_rules import break_rule_keys, break_matcher


class SentenceSegmenter(Segmenter):
    """
    [Unicode TR29](https://www.unicode.org/reports/tr29/#Sentence_Boundaries)
    compliant sentence segmenter
    """

    _break_rule_keys = break_rule_keys
    _break_matcher = break_matcher
