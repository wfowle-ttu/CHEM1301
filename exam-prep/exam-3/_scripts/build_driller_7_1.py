"""Build driller-7-1: solubility rules and precipitation (15 questions, layout in soldrill.py).

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_driller_7_1.py
"""
from soldrill import build
from solib import C7, T

SPEC = dict(
    concept1=dict(
        ch=7, kind="concept", title="Insoluble vs slightly soluble", short="Ch 7 sl. 11",
        stem="Table 7.1 calls some salts \"slightly soluble.\" According to the course, how does that compare with \"insoluble\"?",
        correct=T("They mean the same thing: so little dissolves that it can't be detected with the naked eye"),
        wrong=[T("Slightly soluble salts dissolve completely if the solution is stirred",
                 "Stirring doesn't change it. Too little dissolves to see either way."),
               T("Slightly soluble salts never form precipitates",
                 "They are exactly the ones that **do** precipitate: rules 5 and 6 cover the common precipitates."),
               T("Insoluble salts are strong electrolytes; slightly soluble salts are not",
                 "Solubility and electrolyte strength aren't what the footnote compares."),
               T("Slightly soluble means more than half of the salt dissolves",
                 "No. The footnote says only a tiny amount dissolves.")],
        cite=f"{C7}, slide 11 (Table 7.1 footnote: insoluble and slightly soluble mean the same thing)",
        hw="HW14 — hw14ex5.png (soluble vs not soluble)",
        covers="Course wording: 'slightly soluble' = 'insoluble' for predicting precipitates.",
        sol="""Slide 11's footnote: the terms **insoluble** and **slightly soluble** really mean the same thing. Such a tiny amount
dissolves that you can't see it with the naked eye. So whenever a rule says "only slightly soluble" (rules 5 and 6),
treat the compound as **insoluble**: it forms a precipitate.""",
    ),
    insol=[("Zn", "SO4"), ("K", "CO3"), ("Cu", "Cl"), ("Pb", "NO3"), ("Ni", "OH")],
    sol=[("NH4", "PO4"), ("Ca", "CO3"), ("Fe2", "S"), ("Pb", "SO4"), ("Mg", "OH")],
    rule_sol=("Na", "S"), rule_sol_others=[6, 1, 3, 5],
    rule_ins=("Pb", "Cl"), rule_ins_others=[1, 2, 4, 6],
    count=[("K", "OH"), ("Ba", "SO4"), ("Cu", "NO3"), ("Ag", "Cl"), ("Zn", "CO3")],
    names=[("Fe2", "SO4"), ("Na", "CO3"), ("Co", "OH"), ("NH4", "Cl"), ("Mn", "NO3")],
    mix=(("Ca", "NO3"), ("Na", "PO4")),
    mix_wrong=("[[CaPO4]]", "The ions were just joined. Ca^2+^ and PO~4~^3−^ need a 3 : 2 ratio for zero charge: Ca~3~(PO~4~)~2~."),
    mol=(("Ba", "Cl"), ("K", "SO4")),
    pairs_nr=[(("Na", "NO3"), ("Cu", "Cl")), (("Pb", "NO3"), ("Na", "Cl")), (("Fe2", "Cl"), ("K", "OH")),
              (("Zn", "NO3"), ("Na", "S")), (("Mg", "Cl"), ("Na", "PO4"))],
    pairs_ppt=[(("K", "Cl"), ("Zn", "NO3")), (("NH4", "NO3"), ("Na", "SO4")), (("Cu", "SO4"), ("Na", "NO3")),
               (("Mg", "NO3"), ("K", "Cl")), (("Ni", "Cl"), ("Na", "CO3"))],
    net=(("Fe3", "NO3"), ("Na", "OH")),
    spect=(("Cu", "SO4"), ("Na", "S")),
    select=("Ba", "Mg", [("Na", "SO4"), ("Na", "CO3"), ("Na", "PO4"), ("Na", "Cl"), ("K", "NO3")]),
    concept2=dict(
        ch=7, kind="concept", title="What a precipitate must contain", short="Ch 7 sl. 10, 14",
        stem="When [[K2CrO4]](aq) and Ba([[NO3]])~2~(aq) are mixed, a yellow solid forms. Why can't that solid be made of "
             "only K^+^ and Ba^2+^ ions?",
        correct=T("A solid compound must have zero net charge, so it needs both a cation and an anion"),
        wrong=[T("K^+^ and Ba^2+^ have different charges, so they can't fit in one crystal",
                 "Different charges isn't the issue. Two **positive** ions can never add to zero charge."),
               T("Potassium salts are always soluble, so K^+^ can't be in a solid",
                 "True of K^+^ salts, but the real reason is charge: no anion means no neutral compound."),
               T("Only nitrate ions can form solids with Ba^2+^",
                 "Nitrates are always **soluble** (rule 1). They never form the solid."),
               T("Ba^2+^ never forms solids, so the solid must contain K^+^",
                 "Ba^2+^ does form solids: BaCrO~4~ on slides 15–17, and BaSO~4~ (rule 4).")],
        cite=f"{C7}, slide 10 (a solid must have zero net charge), slide 14 (exchange the anions), slides 15–17 (BaCrO~4~)",
        hw="HW15 — hw15ex3.png (which ions combine to form the precipitate)",
        covers="A precipitate is a neutral compound of a cation and an anion, which is why you exchange the anions.",
        sol="""A solid compound must have **zero net charge** (slide 10). K^+^ and Ba^2+^ are both positive, and CrO~4~^2−^ and NO~3~^−^ are
both negative, so a solid has to pair a cation with an anion. Exchanging the anions (slide 14) gives KNO~3~ (soluble, rules 1
and 2) and **BaCrO~4~**, the yellow solid on slides 15–17.""",
    ),
)

if __name__ == "__main__":
    build(1, SPEC)
