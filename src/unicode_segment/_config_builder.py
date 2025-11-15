import regex
from regex import Pattern


class Config:
    def __init__(
        self,
        break_rules: set[str],
        break_opportunities_pattern: Pattern,
        all_rules_pattern: Pattern,
    ):
        self.break_rules = break_rules
        self.break_opportunities_pattern = break_opportunities_pattern
        self.all_rules_pattern = all_rules_pattern


class ConfigBuilder:
    def __init__(self, prop_name: str, skip: set[str]):
        self.prop_name = prop_name
        self.skip = skip

    def build_break_opportunities_pattern(
        self, rules: list[tuple[bool, str, str]]
    ) -> Pattern:
        return regex.compile(
            "|".join([rule for is_break, _, rule in rules if is_break]),
            regex.V1 | regex.DOTALL,
        )

    def build_all_rules_pattern(self, rules: list[tuple[bool, str, str]]) -> Pattern:
        return regex.compile(
            "|".join([rule for _, _, rule in rules]), regex.V1 | regex.DOTALL
        )

    def get_break_rules(self, rules: list[tuple[bool, str, str]]):
        return set([name for is_break, name, _ in rules if is_break])

    def build(self, rules: list[tuple[bool, str, str]]) -> Config:
        return Config(
            break_rules=self.get_break_rules(rules),
            break_opportunities_pattern=self.build_break_opportunities_pattern(rules),
            all_rules_pattern=self.build_all_rules_pattern(rules),
        )

    def b(self, *names: str, negate=False) -> str:
        inner = "".join([rf"\p{{{self.prop_name}={name}}}" for name in names])
        return rf"[{'^' if negate else ''}{inner}]"

    # https://www.unicode.org/reports/tr29/#Grapheme_Cluster_and_Format_Rules
    def bx(self, *names: str, negate=False) -> str:
        if negate or not self.skip:
            return self.b(*names, negate=negate)

        return rf"(?:{self.b(*names, negate=negate)}{self.b(*self.skip)}*)"
