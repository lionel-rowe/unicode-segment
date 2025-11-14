from _regex_builder import RegexBuilder

regex_builder = RegexBuilder("Sentence_Break", ["Extend", "Format"])
b = regex_builder.b
bx = regex_builder.bx

# macros
ParaSep = ("Sep", "CR", "LF")
SATerm = ("STerm", "ATerm")

# "÷" = break opportunity; "×" = no break opportunity
rules = [
    # SB1	sot	÷	Any
    r"(?<!.)(?<SB1>)(?=.)",
    # SB2	Any	÷	eot
    r"(?<=.)(?<SB2>)(?!.)",
    # SB3	CR	×	LF
    rf"(?<={b('CR')})(?<SB3>)(?={b('LF')})",
    # SB4	ParaSep	÷
    rf"(?<={b(*ParaSep)})(?<SB4>)",
    # SB5	X (Extend | Format)*	→	X
    rf"(?<SB5>)(?={b('Extend', 'Format')})",
    # SB6	ATerm	×	Numeric
    rf"(?<={bx('ATerm')})(?<SB6>)(?={b('Numeric')})",
    # SB7	(Upper | Lower) ATerm	×	Upper
    rf"(?<={bx('Upper', 'Lower')}{bx('ATerm')})(?<SB7>)(?={b('Upper')})",
    # SB8	ATerm Close* Sp*	×	[^ OLetter Upper Lower ParaSep SATerm]* Lower
    rf"(?<={bx('ATerm')}{bx('Close')}*{bx('Sp')}*)(?<SB8>)(?={bx('OLetter', 'Upper', 'Lower', *ParaSep, *SATerm, negate=True)}*{b('Lower')})",
    # SB8a	SATerm Close* Sp*	×	(SContinue | SATerm)
    rf"(?<={bx(*SATerm)}{bx('Close')}*{bx('Sp')}*)(?<SB8a>)(?={b('SContinue', *SATerm)})",
    # SB9	SATerm Close*	×	( Close | Sp | ParaSep )
    rf"(?<={bx(*SATerm)}{bx('Close')}*)(?<SB9>)(?={b('Close', 'Sp', *ParaSep)})",
    # SB10	SATerm Close* Sp*	×	( Sp | ParaSep )
    rf"(?<={bx(*SATerm)}{bx('Close')}*{bx('Sp')}*)(?<SB10>)(?={b('Sp', *ParaSep)})",
    # SB11	SATerm Close* Sp* ParaSep?	÷
    rf"(?<={bx(*SATerm)}{bx('Close')}*{bx('Sp')}*{b(*ParaSep)}?)(?<SB11>)",
    # SB998		×	Any
    r"(?<=.)(?<SB998>)(?=.)",
]

break_matcher = regex_builder.build(rules)

# "÷" = break opportunity; "×" = no break opportunity
break_rule_keys = ["SB1", "SB2", "SB4", "SB11"]
