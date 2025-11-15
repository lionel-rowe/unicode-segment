from ._segmenter import Segmenter
from ._word_rules import _config


class WordSegmenter(Segmenter):
    """
    [Unicode TR29](https://www.unicode.org/reports/tr29/#Word_Boundaries)
    compliant word segmenter
    """

    _config = _config
