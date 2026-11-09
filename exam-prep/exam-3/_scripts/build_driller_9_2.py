"""Build driller-9-2: section 8.7 (empirical/molecular formulas) + Chapter 9, 15 questions.

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_driller_9_2.py
Layout (same for 9-2, 9-3, 9-4): 7 from section 8.7 (concept, molecular->empirical, three
percent/grams->empirical, empirical+molar mass->molecular, an 8.7->9 bridge) and 8 from Chapter 9
(concept, mole-mole, mol<->g, g->g, balance-first g->g, limiting + leftover, theoretical yield,
percent yield). Answers balanced 3 per letter. Compounds are new to this driller set.
"""
from collections import Counter

from drillib import (C8, C9, T, check, q_bridge, q_empirical, q_limit, q_mass, q_molecular, q_percent, q_yield)
from examlib import build_driller

Q = []
SCOPE = "Section 8.7 (empirical and molecular formulas) + Chapter 9"
BANDS = ("14–15 solid on 8.7 and Chapter 9 · 11–13 rework the study guide sections cited for the questions you missed ·\n"
         "10 or below go back through study guide sections 8.7 and 9.2–9.7 before the next driller.")

# ================================================================ section 8.7
Q.append(dict(
    ch=8, kind="concept", title="Empirical vs molecular formula", short="Ch 8 sl. 39–40, 48, 50",
    stem="Which statement about empirical and molecular formulas is correct?",
    correct=T("The molecular formula is always a whole-number multiple of the empirical formula"),
    wrong=[T("The empirical formula is always different from the molecular formula",
             "They can be the same. For H~2~O, n = 1, so the empirical and molecular formulas are both H~2~O."),
           T("The empirical formula gives the actual number of atoms in one molecule",
             "That is the **molecular** formula (slide 50). The empirical formula only gives the smallest ratio."),
           T("Two different compounds can never have the same empirical formula",
             "They can: C~2~H~2~ and C~6~H~6~ are both CH (slide 39)."),
           T("An empirical formula may contain fractional subscripts such as CH~1.5~",
             "Empirical formulas use the smallest **whole-number** ratio. A .5 means multiply every subscript by 2.")],
    cite=f"{C8}, slide 39 (empirical vs molecular formulas), slide 48 (molecular = (empirical)~n~), slide 50",
    hw="HW21 — hw21ex3.png (CH with molar mass ≈ 26 gives C~2~H~2~)",
    covers="Course definitions: empirical = smallest whole-number ratio; molecular = (empirical)~n~, n a whole number.",
    sol="""**Definitions (study guide 8.7).** The empirical formula is the **smallest whole-number ratio** of atoms. The molecular
formula is the **actual** number of atoms in one molecule. They are linked by **molecular = (empirical)~n~**, where n is a
whole number (1, 2, 3, ...), as slide 48 states.

So the molecular formula is always the empirical formula times a whole number. When n = 1 the two formulas are the same
(H~2~O, CO~2~).""",
))

Q.append(dict(
    ch=8, kind="calc", title="Molecular to empirical formula", short="Ch 8 sl. 39–40",
    stem="Hexane has the molecular formula [[C6H14]]. What is its empirical formula?",
    correct=T("[[C3H7]]"),
    wrong=[T("[[C6H14]]", "That is the molecular formula. 6 and 14 are both divisible by 2, so it isn't the smallest ratio."),
           T("[[CH2]]", "That reduces C~6~H~12~, not C~6~H~14~. 14 isn't divisible by 6."),
           T("[[C2H5]]", "Divided C by 3, but 14 ÷ 3 isn't a whole number. Every subscript must be divided by the **same** number."),
           T("[[C3H8]]", "C was divided by 2, but 14 ÷ 2 = 7, not 8.")],
    cite=f"{C8}, slide 39 (empirical formula = smallest whole-number ratio), slide 40",
    hw="HW21 — hw21ex3.png (relating empirical and molecular formulas)",
    covers="Type A (study guide 8.7): divide every subscript by their largest common divisor.",
    sol="""**Step 1: list the subscripts.** C 6, H 14.

**Step 2: find the largest number that divides both evenly.** 6 ÷ 2 = 3 and 14 ÷ 2 = 7. No larger number divides both
(3 doesn't divide 14, and 7 doesn't divide 6), so the divisor is **2**.

**Step 3: divide every subscript by 2.** C 6 ÷ 2 = 3, H 14 ÷ 2 = 7. Empirical formula: **C~3~H~7~**.""",
))

q, r = q_empirical(
    "Percent composition to empirical formula (×2)", "Ch 8 sl. 35–38, 42–43",
    "A nitrogen oxide contains 25.94% N and 74.06% O by mass. What is its empirical formula?",
    ["N", "O"], [25.94, 74.06], "percent",
    f"{C8}, slides 42–43 (Steps for Determining the Empirical Formula; step 4: multiply when not whole), slides 35–38",
    "HW21 — hw21ex2.png (empirical formula from percent composition: MgSO~4~, SiCl~2~Br~2~)")
assert r["formula"] == "N2O5"
Q.append(q)

q, r = q_empirical(
    "Percent composition to empirical formula", "Ch 8 sl. 35–38, 42",
    "Ethylene glycol is 38.70% C, 9.74% H, and 51.56% O by mass. What is its empirical formula?",
    ["C", "H", "O"], [38.70, 9.74, 51.56], "percent",
    f"{C8}, slides 35–37 (four-element example: percent → grams → moles → ratio), slide 42",
    "HW21 — hw21ex2.png (empirical formula from percent composition)")
assert r["formula"] == "CH3O"
Q.append(q)

q, r = q_empirical(
    "Grams to empirical formula", "Ch 8 sl. 45–46",
    "A 5.00 g sample of a sulfur oxide contains 2.00 g of sulfur; the rest is oxygen. What is its empirical formula?",
    ["S", "O"], [2.00, 3.00], "grams",
    f"{C8}, slides 45–46 (empirical formula from masses: 1.198 g C + 0.302 g H), slide 42",
    "HW21 — empirical formula from composition data",
    grams_note="Sulfur: 2.00 g (given). Oxygen is the rest of the sample: 5.00 g − 2.00 g = **3.00 g O**.")
assert r["formula"] == "SO3"
Q.append(q)

Q.append(q_molecular(
    "Empirical to molecular formula", "Ch 8 sl. 47–49",
    "Butane has the empirical formula [[C2H5]] and a molar mass of 58.12 g/mol. What is its molecular formula?",
    "C2H5", 58.12,
    f"{C8}, slide 48 (molecular formula = (empirical formula)~n~), slide 49 (LA Practice), slide 47",
    "HW21 — hw21ex3.png (CH, molar mass ≈ 26 → C~2~H~2~; C~3~H~7~NO → C~6~H~14~N~2~O~2~)"))

q, res = q_bridge(
    "From percent composition to a mole ratio", "Ch 8 sl. 42–49; Ch 9 sl. 9–11",
    "A gaseous hydrocarbon is 85.63% C and 14.37% H by mass, and its molar mass is 28.05 g/mol. It burns completely in "
    "[[O2]] to form [[CO2]] and [[H2O]]. How many moles of [[O2]] are needed to burn 0.500 mol of the hydrocarbon?",
    ["C", "H"], [85.63, 14.37], 28.05,
    "Combustion of C~2~H~4~: balance C first (2CO~2~), then H (2H~2~O, 4 H), then O: the right side has 2(2) + 2(1) = 6 O, "
    "so 3O~2~. **C~2~H~4~ + 3O~2~ $\\rightarrow$ 2CO~2~ + 2H~2~O**.",
    "C2H4", 1, "O2", 3, 0.500,
    [(0.500 * 1.5, "Used the empirical formula CH~2~ (CH~2~ + 1.5O~2~), which is half a molecule."),
     (0.500, "Assumed 1 : 1. O~2~'s coefficient is 3."),
     (0.500 / 3, "Ratio upside down: × 1/3 instead of × 3/1."),
     (0.500 * 2, "Used CO~2~'s coefficient (2) instead of O~2~'s (3).")],
    f"{C8}, slides 42–49 (empirical then molecular formula); {C9}, slide 9 (balancing a combustion), slides 10–11",
    "HW21 — hw21ex3.png (empirical + molar mass → molecular); HW22 — hw22ex3.png (moles of one substance from another)")
check(6, res, 1.50, 0.005)
Q.append(q)

# ================================================================ Chapter 9
Q.append(dict(
    ch=9, kind="concept", title="Definition of the limiting reactant", short="Ch 9 sl. 21–22",
    stem="The **limiting reactant** in a chemical reaction is the reactant that:",
    correct=T("is completely used up first and so determines how much product can form"),
    wrong=[T("has the smallest mass", "Mass alone doesn't decide it. A reactant with a smaller mass can be in excess."),
           T("has the smallest coefficient in the balanced equation",
             "Coefficients alone don't decide it. You need the actual moles present compared through the ratio."),
           T("has the fewest moles present",
             "Raw moles don't decide it either. 3Mg + N~2~ on slide 23 has more moles of Mg, yet Mg is limiting."),
           T("is left over when the reaction stops", "That is the **excess** reactant.")],
    cite=f"{C9}, slide 21 (Limiting Reactants: the reactant that runs out first), slide 22, slide 23",
    hw="HW23 — hw23ex2.png (determine which reactant is limiting)",
    covers="Course definition of the limiting reactant, and why mass, coefficients, or raw moles can't identify it.",
    sol="""Slide 21: the limiting reactant is the reactant that **runs out first**, and it **limits the amount of product** that can
form. The other reactant is in excess and some of it is left over.

To find it, compare what one reactant **needs** of the other (through the mole ratio) with what is actually **available**
(study guide 9.5).""",
))

q, res = q_mass(
    "Mole–mole conversion", "Ch 9 sl. 10–11",
    "Air bags inflate by the reaction 2[[NaN3]](s) → 2Na(s) + 3[[N2]](g). How many moles of [[N2]] form from 1.50 mol of [[NaN3]]?",
    "NaN3", 2, "N2", 3, 1.50, "mol", "mol",
    f"{C9}, slides 10–11 (Mole–Mole Conversions Practice)",
    "HW22 — hw22ex3.png (moles of product from moles of another substance)", others=[("Na", 2)],
    covers="One step: moles given × (coefficient wanted / coefficient given).")
check(9, res, 2.25, 0.005)
Q.append(q)

q, res = q_mass(
    "Moles to grams of product", "Ch 9 sl. 12, 14, 17",
    "For [[N2]](g) + [[O2]](g) → 2NO(g), what mass of NO forms from 0.750 mol of [[N2]] with excess [[O2]]?",
    "N2", 1, "NO", 2, 0.750, "mol", "g",
    f"{C9}, slide 17 (Stoichiometry Practice 1: grams of SO~3~ from 2.33 mol O~2~), slide 8 (N~2~ + O~2~ → 2NO), slide 14",
    "HW23 — mass of product from an amount of reactant", others=[("O2", 1)])
check(10, res, 45.0, 0.05)
Q.append(q)

q, res = q_mass(
    "Grams to grams", "Ch 9 sl. 14, 18–20",
    "Zinc dissolves in acid: Zn(s) + 2HCl(aq) → [[ZnCl2]](aq) + [[H2]](g). What mass of [[H2]] forms when 10.0 g of Zn "
    "reacts with excess HCl?",
    "Zn", 1, "H2", 1, 10.0, "g", "g",
    f"{C9}, slides 19–20 (Stoichiometry Practice: g → mol → mol → g), slide 14 (steps)",
    "HW23 — hw23ex1.png (grams of C~2~H~2~ from 3.25 g CaC~2~)", others=[("HCl", 2)])
check(11, res, 0.308, 0.0005)
Q.append(q)

q, res = q_mass(
    "Balance first, then grams to grams", "Ch 9 sl. 14, 16, 19",
    "Silicon reacts with chlorine according to the **unbalanced** equation Si(s) + [[Cl2]](g) → [[SiCl4]](l). What mass of "
    "[[Cl2]] is needed to react completely with 7.00 g of Si?",
    "Si", 1, "Cl2", 2, 7.00, "g", "g",
    f"{C9}, slide 16 (why the equation must be balanced first), slide 14, slide 19",
    "HW22 — hw22ex3.png (unbalanced equations: balance, then convert)",
    balance="SiCl~4~ has 4 Cl and Cl~2~ supplies Cl in pairs, so use **2**Cl~2~ (4 Cl). Si is already 1 = 1: "
            "**Si + 2Cl~2~ $\\rightarrow$ SiCl~4~**.",
    others=[("SiCl4", 1)])
check(12, res, 35.3, 0.05)
Q.append(q)

q, (L, left) = q_limit(
    "Limiting reactant and leftover", "Ch 9 sl. 21–24",
    "Methane burns: [[CH4]](g) + 2[[O2]](g) → [[CO2]](g) + 2[[H2O]](g). A mixture of 8.00 g of [[CH4]] and 24.0 g of [[O2]] "
    "reacts. Which statement is correct?",
    "CH4", 1, 8.00, "O2", 2, 24.0,
    f"{C9}, slide 24 (limiting reactant from two masses), slides 21–23",
    "HW23 — hw23ex2.png (5.65 g of each reactant: which is limiting?)")
assert L == "O2"
Q.append(q)

q, (L, res) = q_yield(
    "Theoretical yield from two masses", "Ch 9 sl. 24–27",
    "For 2NO(g) + [[O2]](g) → 2[[NO2]](g), 15.0 g of NO reacts with 10.0 g of [[O2]]. What is the theoretical yield of [[NO2]]?",
    "NO", 2, 15.0, "O2", 1, 10.0, "NO2", 2,
    f"{C9}, slide 27 (theoretical yield when both masses are given), slide 25 (definition), slide 24",
    "HW23 — hw23ex3.png (find the limiting reactant, then the mass of product); HW24 — hw24ex2.png")
assert L == "NO"
check(14, res, 23.0, 0.05)
Q.append(q)

q, res = q_percent(
    "Percent yield", "Ch 9 sl. 28–32",
    "Baking soda decomposes when heated: 2[[NaHCO3]](s) → [[Na2CO3]](s) + [[H2O]](g) + [[CO2]](g). Heating 16.8 g of "
    "[[NaHCO3]] gives 9.85 g of [[Na2CO3]]. What is the percent yield?",
    "NaHCO3", 2, 16.8, "Na2CO3", 1, 9.85,
    f"{C9}, slide 30 (percent yield formula), slide 32 (2KClO~3~ decomposition), slide 28 (actual vs theoretical)",
    "HW24 — hw24ex1.png (percent yield from theoretical and actual masses)")
check(15, res, 92.9, 0.05)
Q.append(q)

if __name__ == "__main__":
    assert len(Q) == 15, len(Q)
    build_driller(9, 2, Q, seed=92, scope=SCOPE, bands=BANDS)
    dist = Counter(q["ans"] for q in Q)
    assert all(dist[L] == 3 for L in "abcde"), dist
