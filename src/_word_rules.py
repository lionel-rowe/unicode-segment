from _regex_builder import RegexBuilder

regex_builder = RegexBuilder("Word_Break", ["Extend", "Format", "ZWJ"])
b = regex_builder.b
bx = regex_builder.bx

# macros
AHLetter = ("ALetter", "Hebrew_Letter")
MidNumLetQ = ("MidNumLet", "Single_Quote")

# "÷" = break opportunity; "×" = no break opportunity
rules = [
    # WB1	sot	÷	Any
    r"(?<!.)(?<WB1>)(?=.)",
    # WB2	Any	÷	eot
    r"(?<=.)(?<WB2>)(?!.)",
    # WB3	CR	×	LF
    rf"(?<={b('CR')})(?<WB3>)(?={b('LF')})",
    # WB3a	(Newline | CR | LF)	÷
    rf"(?<={b('Newline', 'CR', 'LF')})(?<WB3a>)",
    # WB3b	 	÷	(Newline | CR | LF)
    rf"(?<WB3b>)(?={b('Newline', 'CR', 'LF')})",
    # WB3c	ZWJ	×	\p{Extended_Pictographic}
    rf"(?<={b('ZWJ')})(?<WB3c>)(?=\p{{Extended_Pictographic}})",
    # WB3d	WSegSpace	×	WSegSpace
    rf"(?<={b('WSegSpace')})(?<WB3d>)(?={b('WSegSpace')})",
    # WB4	X (Extend | Format | ZWJ)*	→	X
    rf"(?<WB4>)(?={b('Extend', 'Format', 'ZWJ')})",
    # WB5	AHLetter	×	AHLetter
    rf"(?<={bx(*AHLetter)})(?<WB5>)(?={b(*AHLetter)})",
    # WB6	AHLetter	×	(MidLetter | MidNumLetQ) AHLetter
    rf"(?<={bx(*AHLetter)})(?<WB6>)(?={bx('MidLetter', *MidNumLetQ)}{b(*AHLetter)})",
    # WB7	AHLetter (MidLetter | MidNumLetQ)	×	AHLetter
    rf"(?<={bx(*AHLetter)}{bx('MidLetter', *MidNumLetQ)})(?<WB7>)(?={b(*AHLetter)})",
    # WB7a	Hebrew_Letter	×	Single_Quote
    rf"(?<={bx('Hebrew_Letter')})(?<WB7a>)(?={b('Single_Quote')})",
    # WB7b	Hebrew_Letter	×	Double_Quote Hebrew_Letter
    rf"(?<={bx('Hebrew_Letter')})(?<WB7b>)(?={bx('Double_Quote')}{b('Hebrew_Letter')})",
    # WB7c	Hebrew_Letter Double_Quote	×	Hebrew_Letter
    rf"(?<={bx('Hebrew_Letter')}{bx('Double_Quote')})(?<WB7c>)(?={b('Hebrew_Letter')})",
    # WB8	Numeric	×	Numeric
    rf"(?<={bx('Numeric')})(?<WB8>)(?={b('Numeric')})",
    # WB9	AHLetter	×	Numeric
    rf"(?<={bx(*AHLetter)})(?<WB9>)(?={b('Numeric')})",
    # WB10	Numeric	×	AHLetter
    rf"(?<={bx('Numeric')})(?<WB10>)(?={b(*AHLetter)})",
    # WB11	Numeric (MidNum | MidNumLetQ)	×	Numeric
    rf"(?<={bx('Numeric')}{bx('MidNum', *MidNumLetQ)})(?<WB11>)(?={b('Numeric')})",
    # WB12	Numeric	×	(MidNum | MidNumLetQ) Numeric
    rf"(?<={bx('Numeric')})(?<WB12>)(?={bx('MidNum', *MidNumLetQ)}{b('Numeric')})",
    # WB13	Katakana	×	Katakana
    rf"(?<={bx('Katakana')})(?<WB13>)(?={b('Katakana')})",
    # WB13a	(AHLetter | Numeric | Katakana | ExtendNumLet)	×	ExtendNumLet
    rf"(?<={bx(*AHLetter, 'Numeric', 'Katakana', 'ExtendNumLet')})(?<WB13a>)(?={b('ExtendNumLet')})",
    # WB13b	ExtendNumLet	×	(AHLetter | Numeric | Katakana)
    rf"(?<={bx('ExtendNumLet')})(?<WB13b>)(?={b(*AHLetter, 'Numeric', 'Katakana')})",
    # WB15	sot (RI RI)* RI	×	RI
    rf"(?<=(?<!.)(?:{bx('RI')}{{2}})*{bx('RI')})(?<WB15>)(?={b('RI')})",
    # WB16	[^RI] (RI RI)* RI	×	RI
    rf"(?<=(?<!{bx('RI')})(?:{bx('RI')}{{2}})*{bx('RI')})(?<WB16>)(?={b('RI')})",
    # WB999	Any	÷	Any
    r"(?<=.)(?<WB999>)(?=.)",
]

break_matcher = regex_builder.build(rules)

# "÷" = break opportunity; "×" = no break opportunity
break_rule_keys = ["WB1", "WB2", "WB3a", "WB3b", "WB999"]
