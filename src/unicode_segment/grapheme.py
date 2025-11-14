from ._segmenter import Segmenter
from ._grapheme_rules import break_rule_keys, break_matcher


class GraphemeSegmenter(Segmenter):
    """
    [Unicode TR29](https://www.unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries)
    compliant grapheme segmenter
    """

    _break_rule_keys = break_rule_keys
    _break_matcher = break_matcher
