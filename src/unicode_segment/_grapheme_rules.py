from unicode_segment._regex_builder import RegexBuilder

regex_builder = RegexBuilder("Grapheme_Cluster_Break", {*()})
b = regex_builder.b
bx = regex_builder.bx

# "÷" = break opportunity; "×" = no break opportunity
rules = [
    # GB1	sot	÷	Any
    r"(?<!.)(?<GB1>)(?=.)",
    # GB2	Any	÷	eot
    r"(?<=.)(?<GB2>)(?!.)",
    # GB3	CR	×	LF
    rf"(?<={b('CR')})(?<GB3>)(?={b('LF')})",
    # GB4	(Control | CR | LF)	÷
    rf"(?<={b('Control', 'CR', 'LF')})(?<GB4>)",
    # GB5		÷	(Control | CR | LF)
    rf"(?<GB5>)(?={b('Control', 'CR', 'LF')})",
    # GB6	L	×	(L | V | LV | LVT)
    rf"(?<={b('L')})(?<GB6>)(?={b('L', 'V', 'LV', 'LVT')})",
    # GB7	(LV | V)	×	(V | T)
    rf"(?<={b('LV', 'V')})(?<GB7>)(?={b('V', 'T')})",
    # GB8	(LVT | T)	×	T
    rf"(?<={b('LVT', 'T')})(?<GB8>)(?={b('T')})",
    # GB9	 	×	(Extend | ZWJ)
    rf"(?<GB9>)(?={b('Extend', 'ZWJ')})",
    # GB9a	 	×	SpacingMark
    rf"(?<GB9a>)(?={b('SpacingMark')})",
    # GB9b	Prepend	×
    rf"(?<={b('Prepend')})(?<GB9b>)",
    # GB9c	\p{InCB=Consonant} [ \p{InCB=Extend} \p{InCB=Linker} ]* \p{InCB=Linker} [ \p{InCB=Extend} \p{InCB=Linker} ]*	×	\p{InCB=Consonant}
    r"(?<=\p{InCB=Consonant}[\p{InCB=Extend}\p{InCB=Linker}]*\p{InCB=Linker}[\p{InCB=Extend}\p{InCB=Linker}]*)(?<GB9c>)(?=\p{InCB=Consonant})",
    # GB11	\p{Extended_Pictographic} Extend* ZWJ	×	\p{Extended_Pictographic}
    rf"(?<=\p{{Extended_Pictographic}}{b('Extend')}*{b('ZWJ')})(?<GB11>)(?=\p{{Extended_Pictographic}})",
    # GB12	sot (RI RI)* RI	×	RI
    rf"(?<=(?<!.)(?:{b('RI')}{{2}})*{b('RI')})(?<GB12>)(?={b('RI')})",
    # GB13	[^RI] (RI RI)* RI	×	RI
    rf"(?<=(?<!{b('RI')})(?:{b('RI')}{{2}})*{b('RI')})(?<GB13>)(?={b('RI')})",
    # GB999	Any	÷	Any
    r"(?<=.)(?<GB999>)(?=.)",
]

break_matcher = regex_builder.build(rules)

break_rule_keys = {"GB1", "GB2", "GB4", "GB5", "GB999"}
