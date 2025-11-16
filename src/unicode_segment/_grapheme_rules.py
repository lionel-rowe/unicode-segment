from unicode_segment._config_builder import ConfigBuilder

config_builder = ConfigBuilder("Grapheme_Cluster_Break", {*()}, True)
b = config_builder.b
bx = config_builder.bx

# "÷" = break opportunity; "×" = no break opportunity
rules = [
    # GB1	sot	÷	Any
    (True, "GB1", r"(?<!.)(?<GB1>)(?=.)"),
    # GB2	Any	÷	eot
    (True, "GB2", r"(?<=.)(?<GB2>)(?!.)"),
    # GB3	CR	×	LF
    (False, "GB3", rf"(?<={b('CR')})(?<GB3>)(?={b('LF')})"),
    # GB4	(Control | CR | LF)	÷
    (True, "GB4", rf"(?<={b('Control', 'CR', 'LF')})(?<GB4>)"),
    # GB5		÷	(Control | CR | LF)
    (True, "GB5", rf"(?<GB5>)(?={b('Control', 'CR', 'LF')})"),
    # GB6	L	×	(L | V | LV | LVT)
    (False, "GB6", rf"(?<={b('L')})(?<GB6>)(?={b('L', 'V', 'LV', 'LVT')})"),
    # GB7	(LV | V)	×	(V | T)
    (False, "GB7", rf"(?<={b('LV', 'V')})(?<GB7>)(?={b('V', 'T')})"),
    # GB8	(LVT | T)	×	T
    (False, "GB8", rf"(?<={b('LVT', 'T')})(?<GB8>)(?={b('T')})"),
    # GB9	 	×	(Extend | ZWJ)
    (False, "GB9", rf"(?<GB9>)(?={b('Extend', 'ZWJ')})"),
    # GB9a	 	×	SpacingMark
    (False, "GB9a", rf"(?<GB9a>)(?={b('SpacingMark')})"),
    # GB9b	Prepend	×
    (False, "GB9b", rf"(?<={b('Prepend')})(?<GB9b>)"),
    # GB9c	\p{InCB=Consonant} [ \p{InCB=Extend} \p{InCB=Linker} ]* \p{InCB=Linker} [ \p{InCB=Extend} \p{InCB=Linker} ]*	×	\p{InCB=Consonant}
    (
        False,
        "GB9c",
        r"(?<=\p{InCB=Consonant}[\p{InCB=Extend}\p{InCB=Linker}]*\p{InCB=Linker}[\p{InCB=Extend}\p{InCB=Linker}]*)(?<GB9c>)(?=\p{InCB=Consonant})",
    ),
    # GB11	\p{Extended_Pictographic} Extend* ZWJ	×	\p{Extended_Pictographic}
    (
        False,
        "GB11",
        rf"(?<=\p{{Extended_Pictographic}}{b('Extend')}*{b('ZWJ')})(?<GB11>)(?=\p{{Extended_Pictographic}})",
    ),
    # GB12	sot (RI RI)* RI	×	RI
    (False, "GB12", rf"(?<=(?<!.)(?:{b('RI')}{{2}})*{b('RI')})(?<GB12>)(?={b('RI')})"),
    # GB13	[^RI] (RI RI)* RI	×	RI
    (
        False,
        "GB13",
        rf"(?<=(?<!{b('RI')})(?:{b('RI')}{{2}})*{b('RI')})(?<GB13>)(?={b('RI')})",
    ),
    # GB999	Any	÷	Any
    (True, "GB999", r"(?<=.)(?<GB999>)(?=.)"),
]

_config = config_builder.build(rules)
