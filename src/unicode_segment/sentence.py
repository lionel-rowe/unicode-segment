from ._segmenter import Segmenter
from ._sentence_rules import _config


class SentenceSegmenter(Segmenter):
    """
    [Unicode TR29](https://www.unicode.org/reports/tr29/#Sentence_Boundaries)
    compliant sentence segmenter
    """

    _config = _config
