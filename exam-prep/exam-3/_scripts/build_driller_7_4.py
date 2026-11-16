"""Build driller-7-4: solubility rules and precipitation (15 questions, layout in soldrill.py).

No question prints the solubility rules in its choices (no "which rule explains" questions).
Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_driller_7_4.py
"""
from soldrill import build
from solib import C7, T

SPEC = dict(
    concept1=dict(
        ch=7, kind="concept", title="Naming the reaction type", short="Ch 7 sl. 3, 14",
        stem="What is the name for a reaction in aqueous solution that results in the formation of a solid?",
        correct=T("A precipitation reaction"),
        wrong=[T("A neutralization (acid–base) reaction", "Acid–base reactions are driven by forming **water** (slide 3)."),
               T("An oxidation–reduction reaction", "Redox reactions are driven by **electron transfer** (slide 3)."),
               T("A combustion reaction", "Combustion is a reaction with O~2~ that produces energy, usually as a flame."),
               T("A decomposition reaction", "Decomposition breaks one compound into simpler substances.")],
        cite=f"{C7}, slide 3 (Driving Forces: formation of a solid), slide 14 (predicting precipitates)",
        hw="HW14 — hw14ex1.png (name for a reaction that forms a solid: precipitation)",
        covers="Driving force 1 (formation of a solid) and its name.",
        sol="""Formation of a solid is driving force #1 on slide 3. The solid is a **precipitate**, and the reaction is a **precipitation**
reaction. The other driving forces match the other names: formation of water (acid–base), transfer of electrons
(oxidation–reduction), and formation of a gas.""",
    ),
    insol=[("Cr", "SO4"), ("Ni", "NO3"), ("K", "PO4"), ("Ba", "Cl"), ("Zn", "OH")],
    sol=[("Mn", "S"), ("Pb", "CO3"), ("Ba", "PO4"), ("Fe2", "OH"), ("NH4", "S")],
    names_sol=[("Ca", "PO4"), ("Co", "CO3"), ("Pb", "SO4"), ("Ni", "S"), ("Fe3", "NO3")],
    net2=(("Mg", "NO3"), ("K", "OH")),
    count=[("Al", "Cl"), ("Ag", "CO3"), ("NH4", "NO3"), ("Pb", "S"), ("Mn", "SO4")],
    names=[("Ba", "NO3"), ("Fe3", "Cl"), ("Ag", "S"), ("Na", "PO4"), ("Zn", "SO4")],
    mix=(("Cu", "Cl"), ("K", "CO3")),
    mix_wrong=("[[Cu2CO3]]", "Cu^2+^ (+2) and CO~3~^2−^ (−2) already cancel 1 : 1: CuCO~3~."),
    mol=(("Ni", "NO3"), ("Na", "PO4")),
    pairs_nr=[(("Cr", "Cl"), ("K", "NO3")), (("Ba", "NO3"), ("Na", "SO4")), (("Ag", "NO3"), ("NH4", "Cl")),
              (("Co", "SO4"), ("K", "OH")), (("Pb", "NO3"), ("K", "CO3"))],
    pairs_ppt=[(("Zn", "Cl"), ("Na", "OH")), (("Fe3", "SO4"), ("Na", "Cl")), (("Ba", "Cl"), ("NH4", "NO3")),
               (("Cu", "SO4"), ("K", "Cl")), (("Al", "NO3"), ("Na", "Cl"))],
    net=(("Hg2", "NO3"), ("K", "Cl")),
    spect=(("Ca", "Cl"), ("K", "PO4")),
    select=("Ca", "Zn", [("Na", "SO4"), ("Na", "CO3"), ("Na", "PO4"), ("Na", "Cl"), ("NH4", "NO3")]),
    concept2=dict(
        ch=7, kind="concept", title="Why some mixtures give no reaction", short="Ch 7 sl. 3, 14",
        stem="When aqueous [[KNO3]] and NaCl are mixed, no reaction occurs. Which statement explains why?",
        correct=T("Both possible products are soluble, so no solid forms and the ions simply stay dissolved"),
        wrong=[T("KNO~3~ and NaCl are both insoluble, so they can't react",
                 "Both are soluble; they're in solution as separated ions."),
               T("Ions with the same charge can't react with each other",
                 "Every one of these ions has a charge of ±1. That isn't why. The products are what matter."),
               T("A precipitate forms, but it redissolves immediately",
                 "No precipitate forms at all. Both possible products are soluble."),
               T("Nitrate ions always react to form a gas", "Nitrates are spectators here and never form a gas in these mixtures.")],
        cite=f"{C7}, slide 14 (step 3: use the rules to decide whether a solid forms), slide 3 (driving forces)",
        hw="HW15 — hw15ex3.png (KNO~3~ + Na~2~S: NR)",
        covers="NR: with no insoluble product (and no water, gas, or electron transfer), there is no driving force.",
        sol="""**Step 1: ions.** K^+^, NO~3~^−^, Na^+^, Cl^−^.

**Step 2: exchange the anions.** The possible products are KCl and NaNO~3~.

**Step 3: rules.** KCl contains K^+^ and NaNO~3~ contains Na^+^ and NO~3~^−^, so both are soluble (rules 1 and 2). No solid
forms, and none of the other driving forces (water, gas, electron transfer) applies, so the answer is **NR**: the four
ions just stay dissolved.""",
    ),
)

if __name__ == "__main__":
    build(4, SPEC)
