from typing import Iterator

from regex import Match
from unicode_segment._config_builder import Config
from abc import ABC, abstractmethod


class Segmenter(ABC):
    def segment(self, text: str) -> Iterator[tuple[int, str]]:
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
    def _config(self) -> Config:
        pass

    def _find_breaks(self, text: str) -> Iterator[int]:
        if not text:
            return

        for i in self._find_break_opportunities(text):
            match = self._config.all_rules_pattern.match(text, i)
            assert match is not None
            x = self._get_matched_rule(match)
            if x in self._config.break_rules:
                yield i

    def _find_break_opportunities(self, text: str) -> Iterator[int]:
        for m in self._config.break_opportunities_pattern.finditer(text):
            yield m.start()

    def _get_matched_rule(self, match: Match) -> str:
        return next(x for x in match.groupdict().items() if x[1] is not None)[0]

    # mainly for testing purposes
    def _get_all_matched_rules(self, text: str) -> Iterator[str]:
        if not text:
            return

        for i in range(len(text) + 1):
            match = self._config.all_rules_pattern.match(text, i)
            assert match is not None
            yield self._get_matched_rule(match)
