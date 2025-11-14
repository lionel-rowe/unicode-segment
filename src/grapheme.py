from _segmenter import Segmenter
import _grapheme_rules


class GraphemeSegmenter(Segmenter):
    """
    [Unicode TR29](https://www.unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries)
    compliant grapheme segmenter
    """

    _break_rule_keys = _grapheme_rules.break_rule_keys
    _break_matcher = _grapheme_rules.break_matcher
