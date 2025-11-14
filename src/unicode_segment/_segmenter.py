import regex
from abc import ABC, abstractmethod


class Segmenter(ABC):
    def split(self, text: str) -> str:
        """
        Split into the relevant type of segments at every break opportunity
        """
        sentences = []
        prev_break = 0
        for i in self._find_breaks(text):
            if i == 0:
                continue
            t = text[prev_break:i]
            if not t:
                continue
            sentences.append(t)
            prev_break = i

        return sentences

    @property
    @abstractmethod
    def _break_rule_keys(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def _break_matcher(self) -> regex.Pattern[str]:
        pass

    def _find_breaks(self, text: str) -> list[int]:
        return [
            i
            for i, x in enumerate(self._get_matched_rules(text))
            if x in self._break_rule_keys
        ]

    def _get_matched_rules(self, text: str) -> list[str]:
        return [
            next(x for x in match.groupdict().items() if x[1] != None)[0]
            for match in self._break_matcher.finditer(text)
        ]
