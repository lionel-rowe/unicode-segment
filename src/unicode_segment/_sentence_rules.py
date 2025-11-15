from unicode_segment._config_builder import ConfigBuilder

config_builder = ConfigBuilder("Sentence_Break", {"Extend", "Format"})
b = config_builder.b
bx = config_builder.bx

# macros
ParaSep = ("Sep", "CR", "LF")
SATerm = ("STerm", "ATerm")

# "÷" = break opportunity; "×" = no break opportunity
rules = [
    # SB1	sot	÷	Any
    (True, "SB1", r"(?<!.)(?<SB1>)(?=.)"),
    # SB2	Any	÷	eot
    (True, "SB2", r"(?<=.)(?<SB2>)(?!.)"),
    # SB3	CR	×	LF
    (False, "SB3", rf"(?<={b('CR')})(?<SB3>)(?={b('LF')})"),
    # SB4	ParaSep	÷
    (True, "SB4", rf"(?<={b(*ParaSep)})(?<SB4>)"),
    # SB5	X (Extend | Format)*	→	X
    (False, "SB5", rf"(?<SB5>)(?={b('Extend', 'Format')})"),
    # SB6	ATerm	×	Numeric
    (False, "SB6", rf"(?<={bx('ATerm')})(?<SB6>)(?={b('Numeric')})"),
    # SB7	(Upper | Lower) ATerm	×	Upper
    (
        False,
        "SB7",
        rf"(?<={bx('Upper', 'Lower')}{bx('ATerm')})(?<SB7>)(?={b('Upper')})",
    ),
    # SB8	ATerm Close* Sp*	×	[^ OLetter Upper Lower ParaSep SATerm]* Lower
    (
        False,
        "SB8",
        rf"(?<={bx('ATerm')}{bx('Close')}*{bx('Sp')}*)(?<SB8>)(?={bx('OLetter', 'Upper', 'Lower', *ParaSep, *SATerm, negate=True)}*{b('Lower')})",
    ),
    # SB8a	SATerm Close* Sp*	×	(SContinue | SATerm)
    (
        False,
        "SB8a",
        rf"(?<={bx(*SATerm)}{bx('Close')}*{bx('Sp')}*)(?<SB8a>)(?={b('SContinue', *SATerm)})",
    ),
    # SB9	SATerm Close*	×	( Close | Sp | ParaSep )
    (
        False,
        "SB9",
        rf"(?<={bx(*SATerm)}{bx('Close')}*)(?<SB9>)(?={b('Close', 'Sp', *ParaSep)})",
    ),
    # SB10	SATerm Close* Sp*	×	( Sp | ParaSep )
    (
        False,
        "SB10",
        rf"(?<={bx(*SATerm)}{bx('Close')}*{bx('Sp')}*)(?<SB10>)(?={b('Sp', *ParaSep)})",
    ),
    # SB11	SATerm Close* Sp* ParaSep?	÷
    (
        True,
        "SB11",
        rf"(?<={bx(*SATerm)}{bx('Close')}*{bx('Sp')}*{b(*ParaSep)}?)(?<SB11>)",
    ),
    # SB998		×	Any
    (False, "SB998", r"(?<=.)(?<SB998>)(?=.)"),
]

_config = config_builder.build(rules)
