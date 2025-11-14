# Unicode Segment

Segment text with Unicode [TR29](https://www.unicode.org/reports/tr29/)-compliant segmenters.

## Usage

```py
from unicode_segment import SentenceSegmenter

text = """This, that, the other thing, etc. Another sentence... A, b, c, \
etc., and more. D, e, f, etc. and more. One, i. e. two. Three, i. e., four. \
Five, i.e. six. You have 4.2 messages. Property access: `a.b.c`."""

segmenter = SentenceSegmenter()
sentences = segmenter.split(text)

assert sentences == [
    "This, that, the other thing, etc. ",
    "Another sentence... ",
    "A, b, c, etc., and more. ",
    "D, e, f, etc. and more. ",
    "One, i. e. two. ",
    "Three, i. e., four. ",
    "Five, i.e. six. ",
    "You have 4.2 messages. ",
    "Property access: `a.b.c`.",
]
```
