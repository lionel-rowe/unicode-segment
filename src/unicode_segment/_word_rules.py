from unicode_segment._config_builder import ConfigBuilder

config_builder = ConfigBuilder("Word_Break", {"Extend", "Format", "ZWJ"}, True)
b = config_builder.b
bx = config_builder.bx

# macros
AHLetter = ("ALetter", "Hebrew_Letter")
MidNumLetQ = ("MidNumLet", "Single_Quote")

# "÷" = break opportunity; "×" = no break opportunity
rules = [
    # WB1	sot	÷	Any
    (True, "WB1", r"(?<!.)(?<WB1>)(?=.)"),
    # WB2	Any	÷	eot
    (True, "WB2", r"(?<=.)(?<WB2>)(?!.)"),
    # WB3	CR	×	LF
    (False, "WB3", rf"(?<={b('CR')})(?<WB3>)(?={b('LF')})"),
    # WB3a	(Newline | CR | LF)	÷
    (True, "WB3a", rf"(?<={b('Newline', 'CR', 'LF')})(?<WB3a>)"),
    # WB3b	 	÷	(Newline | CR | LF)
    (True, "WB3b", rf"(?<WB3b>)(?={b('Newline', 'CR', 'LF')})"),
    # WB3c	ZWJ	×	\p{Extended_Pictographic}
    (False, "WB3c", rf"(?<={b('ZWJ')})(?<WB3c>)(?=\p{{Extended_Pictographic}})"),
    # WB3d	WSegSpace	×	WSegSpace
    (False, "WB3d", rf"(?<={b('WSegSpace')})(?<WB3d>)(?={b('WSegSpace')})"),
    # WB4	X (Extend | Format | ZWJ)*	→	X
    (False, "WB4", rf"(?<WB4>)(?={b('Extend', 'Format', 'ZWJ')})"),
    # WB5	AHLetter	×	AHLetter
    (False, "WB5", rf"(?<={bx(*AHLetter)})(?<WB5>)(?={b(*AHLetter)})"),
    # WB6	AHLetter	×	(MidLetter | MidNumLetQ) AHLetter
    (
        False,
        "WB6",
        rf"(?<={bx(*AHLetter)})(?<WB6>)(?={bx('MidLetter', *MidNumLetQ)}{b(*AHLetter)})",
    ),
    # WB7	AHLetter (MidLetter | MidNumLetQ)	×	AHLetter
    (
        False,
        "WB7",
        rf"(?<={bx(*AHLetter)}{bx('MidLetter', *MidNumLetQ)})(?<WB7>)(?={b(*AHLetter)})",
    ),
    # WB7a	Hebrew_Letter	×	Single_Quote
    (False, "WB7a", rf"(?<={bx('Hebrew_Letter')})(?<WB7a>)(?={b('Single_Quote')})"),
    # WB7b	Hebrew_Letter	×	Double_Quote Hebrew_Letter
    (
        False,
        "WB7b",
        rf"(?<={bx('Hebrew_Letter')})(?<WB7b>)(?={bx('Double_Quote')}{b('Hebrew_Letter')})",
    ),
    # WB7c	Hebrew_Letter Double_Quote	×	Hebrew_Letter
    (
        False,
        "WB7c",
        rf"(?<={bx('Hebrew_Letter')}{bx('Double_Quote')})(?<WB7c>)(?={b('Hebrew_Letter')})",
    ),
    # WB8	Numeric	×	Numeric
    (False, "WB8", rf"(?<={bx('Numeric')})(?<WB8>)(?={b('Numeric')})"),
    # WB9	AHLetter	×	Numeric
    (False, "WB9", rf"(?<={bx(*AHLetter)})(?<WB9>)(?={b('Numeric')})"),
    # WB10	Numeric	×	AHLetter
    (False, "WB10", rf"(?<={bx('Numeric')})(?<WB10>)(?={b(*AHLetter)})"),
    # WB11	Numeric (MidNum | MidNumLetQ)	×	Numeric
    (
        False,
        "WB11",
        rf"(?<={bx('Numeric')}{bx('MidNum', *MidNumLetQ)})(?<WB11>)(?={b('Numeric')})",
    ),
    # WB12	Numeric	×	(MidNum | MidNumLetQ) Numeric
    (
        False,
        "WB12",
        rf"(?<={bx('Numeric')})(?<WB12>)(?={bx('MidNum', *MidNumLetQ)}{b('Numeric')})",
    ),
    # WB13	Katakana	×	Katakana
    (False, "WB13", rf"(?<={bx('Katakana')})(?<WB13>)(?={b('Katakana')})"),
    # WB13a	(AHLetter | Numeric | Katakana | ExtendNumLet)	×	ExtendNumLet
    (
        False,
        "WB13a",
        rf"(?<={bx(*AHLetter, 'Numeric', 'Katakana', 'ExtendNumLet')})(?<WB13a>)(?={b('ExtendNumLet')})",
    ),
    # WB13b	ExtendNumLet	×	(AHLetter | Numeric | Katakana)
    (
        False,
        "WB13b",
        rf"(?<={bx('ExtendNumLet')})(?<WB13b>)(?={b(*AHLetter, 'Numeric', 'Katakana')})",
    ),
    # WB15	sot (RI RI)* RI	×	RI
    (
        False,
        "WB15",
        rf"(?<=(?<!.)(?:{bx('RI')}{{2}})*{bx('RI')})(?<WB15>)(?={b('RI')})",
    ),
    # WB16	[^RI] (RI RI)* RI	×	RI
    (
        False,
        "WB16",
        rf"(?<=(?<!{bx('RI')})(?:{bx('RI')}{{2}})*{bx('RI')})(?<WB16>)(?={b('RI')})",
    ),
    # WB999	Any	÷	Any
    (True, "WB999", r"(?<=.)(?<WB999>)(?=.)"),
]

_config = config_builder.build(rules)
