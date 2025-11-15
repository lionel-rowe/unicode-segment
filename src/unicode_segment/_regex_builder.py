import regex


class RegexBuilder:
    def __init__(self, prop_name: str, skip: set[str]):
        self.prop_name = prop_name
        self.skip = skip

    def build(self, rules) -> regex.Pattern:
        return regex.compile("|".join(rules), regex.V1 | regex.DOTALL)

    def b(self, *names: str, negate=False) -> str:
        inner = "".join([rf"\p{{{self.prop_name}={name}}}" for name in names])
        return rf"[{'^' if negate else ''}{inner}]"

    # https://www.unicode.org/reports/tr29/#Grapheme_Cluster_and_Format_Rules
    def bx(self, *names: str, negate=False) -> str:
        if negate or not self.skip:
            return self.b(*names, negate=negate)

        return rf"(?:{self.b(*names, negate=negate)}{self.b(*self.skip)}*)"
