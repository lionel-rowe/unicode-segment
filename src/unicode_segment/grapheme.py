from ._segmenter import Segmenter
from ._grapheme_rules import _config


class GraphemeSegmenter(Segmenter):
    """
    [Unicode TR29](https://www.unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries)
    compliant grapheme segmenter
    """

    _config = _config
