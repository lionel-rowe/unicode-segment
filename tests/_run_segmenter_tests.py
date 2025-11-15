import regex
from unicode_segment._segmenter import Segmenter

alphabet = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])
r = regex.compile(r"(?<=\[)[\d.]+(?=\])")


def get_rule_names(comment: str, initial: str) -> list[str]:
    return [f"{initial}B{remap_rule(float(n))}" for n in r.findall(comment)]


def remap_rule(n: float) -> str:
    if n == 0.2:
        return "1"
    elif n == 0.3:
        return "2"
    elif n % 1 != 0:
        return f"{int(n)}{alphabet[int(round(n % 1, 1) * 10) - 1]}"

    return str(int(n))


def run_segmenter_unicode_break_tests(segmenter: Segmenter, test_file_name: str):
    # check zero case first
    assert list(segmenter.segment("")) == []
    assert list(segmenter._find_breaks("")) == []
    assert list(segmenter._get_matched_rules("")) == []

    # https://www.unicode.org/Public/17.0.0/ucd/auxiliary/SentenceBreakTest.txt
    with open(f"tests/test_data/{test_file_name}", "r", encoding="utf-8") as f:
        lines = [
            line for line in f.readlines() if line.strip() and not line.startswith("#")
        ]

    for line in lines:
        [case, comment] = line.split("#", 1)

        expected_all = [
            "".join([chr(int(cp, 16)) for cp in part.split("×")])
            if part.strip()
            else ""
            for part in case.split("÷")
        ]

        expected = [s for s in expected_all if s]

        joined = "".join(expected)
        actual = [s for _, s in segmenter.segment(joined)]

        expected_rules = get_rule_names(comment, test_file_name[0])
        actual_rules = list(segmenter._get_matched_rules(joined))

        assert actual == expected, "\n".join(
            [
                f"\x1b[0m{line}\x1b[0m"
                for line in [
                    f"\x1b[31m{actual}\x1b[0m != \x1b[32m{expected}",
                    "Expected rules:",
                    f"-> \x1b[32m{expected_rules}",
                    "Actual rules:",
                    f"-> \x1b[31m{actual_rules}",
                    f"\x1b[90m# {case.strip()}",
                    f"\x1b[90m# {comment.strip()}",
                ]
            ]
        )

        assert actual_rules == expected_rules
