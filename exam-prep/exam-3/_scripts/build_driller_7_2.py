"""Build driller-7-2: solubility rules and precipitation (15 questions, layout in soldrill.py).

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_driller_7_2.py
"""
from soldrill import build
from solib import C7, T

SPEC = dict(
    concept1=dict(
        ch=7, kind="concept", title="What a dissolved salt looks like", short="Ch 7 sl. 6–9",
        stem="Which best describes an aqueous solution of barium nitrate, Ba([[NO3]])~2~(aq)?",
        correct=T("Separated Ba^2+^ and [[NO3^-^]] ions, with two [[NO3^-^]] ions for every Ba^2+^ ion, moving independently"),
        wrong=[T("Intact Ba([[NO3]])~2~ units dissolved in water",
                 "When an ionic solid dissolves, its ions separate. There are no intact units in solution."),
               T("Separated Ba^2+^ and [[NO3^-^]] ions in a 1 : 1 ratio",
                 "Each formula unit has **two** nitrate ions, so the ratio is 1 Ba^2+^ : 2 NO~3~^−^."),
               T("Ba atoms and NO~3~ molecules with no charge",
                 "Dissolving doesn't neutralize the ions. They stay charged, which is why the solution conducts."),
               T("A solid suspended in water, because barium salts are insoluble",
                 "It's a nitrate, so it's soluble (rule 1). Only some barium salts, like BaSO~4~, are insoluble.")],
        cite=f"{C7}, slides 6–9 (ions separate and move independently when an ionic solid dissolves; strong electrolytes)",
        hw="HW14 — hw14ex1.png (reactions in aqueous solution)",
        covers="Strong electrolytes: a soluble ionic compound exists in water as separated ions.",
        sol="""Slides 6–9: when an ionic solid dissolves, **the ions separate and move around independently**. Ba(NO~3~)~2~ is
soluble (rule 1), so the solution contains Ba^2+^ ions and NO~3~^−^ ions, two NO~3~^−^ for every Ba^2+^, not Ba(NO~3~)~2~
units. That is also why step 1 of predicting precipitates (slide 14) is writing the reactants as separated ions.""",
    ),
    insol=[("Mg", "SO4"), ("Fe3", "Cl"), ("Na", "PO4"), ("Al", "NO3"), ("Ca", "SO4")],
    sol=[("K", "S"), ("Cu", "OH"), ("Ag", "Cl"), ("Ni", "CO3"), ("Zn", "PO4")],
    rule_sol=("NH4", "CO3"), rule_sol_others=[6, 1, 4, 5],
    rule_ins=("Ba", "SO4"), rule_ins_others=[1, 2, 3, 6],
    count=[("Na", "OH"), ("Pb", "Cl"), ("Ca", "NO3"), ("K", "CO3"), ("NH4", "PO4")],
    names=[("Ni", "SO4"), ("K", "PO4"), ("Mn", "CO3"), ("Cr", "NO3"), ("Cu", "Cl")],
    mix=(("Pb", "NO3"), ("Na", "SO4")),
    mix_wrong=("[[Pb2SO4]]", "Pb^2+^ (+2) and SO~4~^2−^ (−2) already cancel in a 1 : 1 ratio: PbSO~4~."),
    mol=(("Mg", "Cl"), ("K", "PO4")),
    pairs_nr=[(("K", "SO4"), ("Zn", "Cl")), (("Ag", "NO3"), ("K", "Cl")), (("Ca", "Cl"), ("Na", "CO3")),
              (("Cu", "NO3"), ("Na", "OH")), (("Ba", "Cl"), ("Na", "PO4"))],
    pairs_ppt=[(("Fe2", "SO4"), ("Na", "S")), (("NH4", "Cl"), ("Cu", "NO3")), (("K", "OH"), ("Na", "NO3")),
               (("Mg", "SO4"), ("Na", "Cl")), (("Zn", "NO3"), ("K", "SO4"))],
    net=(("Pb", "NO3"), ("K", "Cl")),
    spect=(("Ba", "NO3"), ("Na", "CO3")),
    select=("Ag", "Zn", [("Na", "Cl"), ("Na", "CO3"), ("Na", "S"), ("Na", "PO4"), ("K", "NO3")]),
    concept2=dict(
        ch=7, kind="concept", title="Spectator ions", short="Ch 7 sl. 17–18",
        stem="In a precipitation reaction, **spectator ions** are ions that:",
        correct=T("are present in solution but do not participate directly in the reaction, so they are left out of the net ionic equation"),
        wrong=[T("combine to form the precipitate", "Those ions are the ones that **do** participate. They stay in the net ionic equation."),
               T("appear only in the net ionic equation", "Backwards: spectators are exactly the ions the net ionic equation leaves out."),
               T("are always Na^+^ and [[NO3^-^]]",
                 "They are often rule-1 and rule-2 ions, but not always. Any ion that stays dissolved and unchanged is a spectator."),
               T("change their charge during the reaction",
                 "Spectators are unchanged. They appear identically on both sides of the complete ionic equation.")],
        cite=f"{C7}, slide 17 (spectator ions do not participate directly), slide 18 (Types of Equations)",
        hw="HW15 — hw15ex1.png (what the net ionic equation shows)",
        covers="Course definition of spectator ions and how they relate to the net ionic equation.",
        sol="""Slide 17: ions that **do not participate directly** in a reaction in solution are **spectator ions**. They appear unchanged on
both sides of the complete ionic equation, so they cancel, and the net ionic equation (slide 18) includes only the
components that change.""",
    ),
)

if __name__ == "__main__":
    build(2, SPEC)
