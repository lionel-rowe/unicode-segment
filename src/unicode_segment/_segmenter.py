from typing import Generator
import regex
from abc import ABC, abstractmethod


class Segmenter(ABC):
    def segment(self, text: str) -> Generator[tuple[int, str], None, None]:
        """
        Split into the relevant type of segments at every break opportunity
        """
        prev_break = 0
        for i in self._find_breaks(text):
            t = text[prev_break:i]
            if not t:
                continue
            yield (prev_break, t)
            prev_break = i

    @property
    @abstractmethod
    def _break_rule_keys(self) -> set[str]:
        pass

    @property
    @abstractmethod
    def _break_matcher(self) -> regex.Pattern:
        pass

    def _find_breaks(self, text: str) -> Generator[int, None, None]:
        for i, x in enumerate(self._get_matched_rules(text)):
            if x in self._break_rule_keys:
                yield i

    def _get_matched_rules(self, text: str) -> Generator[str, None, None]:
        if not text:
            return

        for i in range(len(text) + 1):
            match = self._break_matcher.match(text, i)
            assert match is not None
            yield next(x for x in match.groupdict().items() if x[1] is not None)[0]
