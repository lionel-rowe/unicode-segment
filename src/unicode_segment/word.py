from ._segmenter import Segmenter
from ._word_rules import break_rule_keys, break_matcher


class WordSegmenter(Segmenter):
    """
    [Unicode TR29](https://www.unicode.org/reports/tr29/#Word_Boundaries)
    compliant word segmenter
    """

    _break_rule_keys = break_rule_keys
    _break_matcher = break_matcher
