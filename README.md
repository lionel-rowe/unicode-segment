# Unicode Segment

Segment text with Unicode [TR29](https://www.unicode.org/reports/tr29/)-compliant segmenters.

## Usage

```py
from unicode_segment import SentenceSegmenter

text = """This, that, the other thing, etc. Another sentence... A, b, c, \
etc., and more. D, e, f, etc. and more. One, i. e. two. Three, i. e., four. \
Five, i.e. six. You have 4.2 messages. Property access: `a.b.c`."""

segmenter = SentenceSegmenter()
segments = segmenter.segment(text)

assert list(segments) == [
    (0, "This, that, the other thing, etc. "),
    (34, "Another sentence... "),
    (54, "A, b, c, etc., and more. "),
    (79, "D, e, f, etc. and more. "),
    (103, "One, i. e. two. "),
    (119, "Three, i. e., four. "),
    (139, "Five, i.e. six. "),
    (155, "You have 4.2 messages. "),
    (178, "Property access: `a.b.c`."),
]
```
