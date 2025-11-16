from __future__ import annotations
import regex
from regex import Pattern

flags = regex.V1 | regex.DOTALL


class Config:
    def __init__(
        self,
        break_rules: set[str],
        pattern: Pattern,
        debug_pattern: Pattern,
        break_candidates_pattern: Pattern | None,
    ):
        self.break_rules = break_rules
        self.pattern = pattern
        self.debug_pattern = debug_pattern
        self.break_candidates_pattern = break_candidates_pattern


class ConfigBuilder:
    def __init__(self, prop_name: str, skip: set[str], break_any: bool):
        self.prop_name = prop_name
        self.skip = skip
        self.break_any = break_any

    def _build_break_candidates_pattern(
        self, rules: list[tuple[bool, str, str]]
    ) -> Pattern | None:
        if self.break_any:
            return None

        return regex.compile(
            "|".join([rule for is_break, _, rule in rules if is_break]),
            flags,
        )

    def _build_debug_pattern(self, rules: list[tuple[bool, str, str]]) -> Pattern:
        return regex.compile("|".join([rule for _, _, rule in rules]), flags)

    def _build_pattern(self, rules: list[tuple[bool, str, str]]) -> Pattern:
        # return regex.compile("|".join([rule for _, _, rule in rules]), flags)
        pattern = ""
        group_depth = 0

        prev_is_break = True

        for is_break, _, rule in rules:
            if pattern and prev_is_break:
                pattern += "|"

            if is_break:
                pattern += rule
            else:
                group_depth += 1
                pattern += rf"(?!{rule})"
                pattern += "(?:"

            prev_is_break = is_break

        pattern += ")" * group_depth

        pattern = regex.sub(r"\(\?<\w+>\)", "", pattern)

        return regex.compile(pattern, flags)

    def _get_break_rules(self, rules: list[tuple[bool, str, str]]):
        return set([name for is_break, name, _ in rules if is_break])

    def build(self, rules: list[tuple[bool, str, str]]) -> Config:
        return Config(
            break_rules=self._get_break_rules(rules),
            pattern=self._build_pattern(rules),
            debug_pattern=self._build_debug_pattern(rules),
            break_candidates_pattern=self._build_break_candidates_pattern(rules),
        )

    def b(self, *names: str, negate=False) -> str:
        inner = "".join([rf"\p{{{self.prop_name}={name}}}" for name in names])
        return rf"[{'^' if negate else ''}{inner}]"

    # https://www.unicode.org/reports/tr29/#Grapheme_Cluster_and_Format_Rules
    def bx(self, *names: str, negate=False) -> str:
        if negate or not self.skip:
            return self.b(*names, negate=negate)

        return rf"(?:{self.b(*names, negate=negate)}{self.b(*self.skip)}*)"
