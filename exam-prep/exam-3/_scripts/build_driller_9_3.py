"""Build driller-9-3: section 8.7 + Chapter 9, 15 questions (same layout as build_driller_9_2.py).

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_driller_9_3.py
"""
from collections import Counter

from build_driller_9_2 import BANDS, SCOPE
from drillib import (C8, C9, T, check, q_bridge, q_empirical, q_limit, q_mass, q_molecular, q_percent, q_yield)
from examlib import build_driller

Q = []

# ================================================================ section 8.7
Q.append(dict(
    ch=8, kind="concept", title="Step 3 of the empirical-formula method", short="Ch 8 sl. 42–43",
    stem="When finding an empirical formula, after converting each element's mass to moles, you should next:",
    correct=T("divide every element's moles by the smallest mole value"),
    wrong=[T("divide every element's moles by the largest mole value",
             "Dividing by the largest makes the results fractions below 1. The smallest makes the smallest element exactly 1."),
           T("divide every element's moles by the molar mass of the compound",
             "The molar mass is used later, to get the **molecular** formula (n = molar mass ÷ empirical mass)."),
           T("round each mole value to the nearest whole number",
             "Mole values like 0.0998 or 1.852 aren't subscripts yet. First divide by the smallest to get the ratio."),
           T("divide each element's mass by the smallest mass",
             "Masses aren't atom counts. The ratio has to be in **moles**, and you already converted to moles.")],
    cite=f"{C8}, slide 42 (Steps for Determining the Empirical Formula, step 3), slides 35–37",
    hw="HW21 — hw21ex2.png (empirical formula from percent composition)",
    covers="The order of the empirical-formula method, aimed at its most-missed step.",
    sol="""Slide 42's steps, as in study guide 8.7 Type B:

1. Get grams of each element (assume 100 g if given percents).
2. Convert each element's grams to **moles** (÷ its atomic mass).
3. **Divide every mole value by the smallest mole value.** The smallest becomes exactly 1, and the others tell you how many
   of that atom there are per 1 of the smallest.
4. If any result isn't within 0.1 of a whole number, multiply **every** result by the same small integer.""",
))

Q.append(dict(
    ch=8, kind="calc", title="Molecular to empirical formula", short="Ch 8 sl. 39–40",
    stem="Sucrose has the molecular formula [[C12H22O11]]. What is its empirical formula?",
    correct=T("[[C12H22O11]]"),
    wrong=[T("[[C6H11O5]]", "Divided by 2, but 11 ÷ 2 isn't a whole number (5.5). You can't divide unless **every** subscript divides evenly."),
           T("[[CH2O]]", "That is the empirical formula of glucose (C~6~H~12~O~6~), not sucrose."),
           T("[[C6H11O11]]", "Divided only C and H by 2. Every subscript must be divided by the same number."),
           T("[[C12H22O]]", "Dropped the O subscript. Every element keeps its count.")],
    cite=f"{C8}, slide 39 (empirical formula = smallest whole-number ratio), slide 40",
    hw="HW20 — hw20ex2.png (formulas such as theobromine); HW21 — hw21ex3.png",
    covers="Type A (study guide 8.7) when the formula is already empirical: the only common divisor is 1.",
    sol="""**Step 1: list the subscripts.** C 12, H 22, O 11.

**Step 2: find the largest number that divides all three evenly.** 11 is prime, so the only candidates are 1 and 11.
12 ÷ 11 isn't whole, so the only common divisor is **1**. (2 divides 12 and 22 but not 11.)

**Step 3: conclusion.** Dividing by 1 changes nothing, so the formula is **already empirical**: **C~12~H~22~O~11~**.""",
))

q, r = q_empirical(
    "Grams to empirical formula (×3)", "Ch 8 sl. 42–46",
    "A 2.000 g sample of an iron oxide contains 1.447 g of iron; the rest is oxygen. What is its empirical formula?",
    ["Fe", "O"], [1.447, 0.553], "grams",
    f"{C8}, slides 45–46 (empirical formula from masses), slide 43 (step 4: multiply by the smallest integer)",
    "HW21 — empirical formula from composition data",
    grams_note="Iron: 1.447 g (given). Oxygen is the rest: 2.000 g − 1.447 g = **0.553 g O**.")
assert r["formula"] == "Fe3O4"
Q.append(q)

q, r = q_empirical(
    "Percent composition to empirical formula (four elements)", "Ch 8 sl. 35–37, 42",
    "A white powder is 39.05% K, 1.01% H, 12.00% C, and 47.94% O by mass. What is its empirical formula?",
    ["K", "H", "C", "O"], [39.05, 1.01, 12.00, 47.94], "percent",
    f"{C8}, slides 35–37 (four-element example: C~2~H~5~O~2~N), slide 42",
    "HW21 — hw21ex2.png (empirical formula from percent composition: MgSO~4~)")
assert r["formula"] == "KHCO3"
Q.append(q)

q, r = q_empirical(
    "Percent composition to empirical formula (×2)", "Ch 8 sl. 42–43",
    "A manganese oxide is 49.55% Mn and 50.45% O by mass. What is its empirical formula?",
    ["Mn", "O"], [49.55, 50.45], "percent",
    f"{C8}, slides 42–43 (Steps for Determining the Empirical Formula; step 4: multiply when not whole)",
    "HW21 — hw21ex2.png (empirical formula from percent composition)")
assert r["formula"] == "Mn2O7"
Q.append(q)

Q.append(q_molecular(
    "Empirical to molecular formula", "Ch 8 sl. 47–49",
    "Ribose has the empirical formula [[CH2O]] and a molar mass of 150.13 g/mol. What is its molecular formula?",
    "CH2O", 150.13,
    f"{C8}, slide 48 (molecular formula = (empirical formula)~n~), slide 49 (LA Practice), slide 47",
    "HW21 — hw21ex3.png (empirical formula + molar mass → molecular formula)"))

q, res = q_bridge(
    "From percent composition to a mole ratio", "Ch 8 sl. 42–49; Ch 9 sl. 9–11",
    "A liquid hydrocarbon is 92.26% C and 7.74% H by mass, and its molar mass is 78.11 g/mol. It burns completely in "
    "[[O2]] to form [[CO2]] and [[H2O]]. How many moles of [[O2]] are needed to burn 0.400 mol of the hydrocarbon?",
    ["C", "H"], [92.26, 7.74], 78.11,
    "Combustion of C~6~H~6~: C first (6CO~2~), then H (3H~2~O), then O: 6(2) + 3(1) = 15 O on the right, so 15/2 O~2~. "
    "That isn't whole, so double everything: **2C~6~H~6~ + 15O~2~ $\\rightarrow$ 12CO~2~ + 6H~2~O**.",
    "C6H6", 2, "O2", 15, 0.400,
    [(0.400 * 1.25, "Used the empirical formula CH (CH + 1.25O~2~), which is one-sixth of a molecule."),
     (0.400, "Assumed 1 : 1. The ratio is 15 O~2~ : 2 C~6~H~6~."),
     (0.400 * 15, "Used 15 but forgot to divide by C~6~H~6~'s coefficient (2)."),
     (0.400 * 12 / 2, "Used CO~2~'s coefficient (12) instead of O~2~'s (15)."),
     (0.400 * 2 / 15, "Ratio upside down: × 2/15 instead of × 15/2.")],
    f"{C8}, slides 42–49 (empirical then molecular formula); {C9}, slide 9 (balancing a combustion: double to clear 7/2), slide 11",
    "HW21 — hw21ex3.png; HW22 — hw22ex1.png (2C~6~H~6~ + 15O~2~ → 12CO~2~ + 6H~2~O)")
check(7, res, 3.00, 0.005)
Q.append(q)

# ================================================================ Chapter 9
Q.append(dict(
    ch=9, kind="concept", title="The excess reactant", short="Ch 9 sl. 21–22, 25",
    stem="Which statement about the **excess** reactant in a reaction is correct?",
    correct=T("Some of it remains unreacted after the reaction stops"),
    wrong=[T("It determines the theoretical yield", "The **limiting** reactant determines the theoretical yield (slide 25)."),
           T("It is always the reactant present in the larger mass", "Mass doesn't decide it. Only a mole comparison through the ratio does."),
           T("It is used up before the limiting reactant", "Backwards: the limiting reactant runs out first."),
           T("Its leftover amount is added to the theoretical yield", "Leftover reactant never became product, so it isn't part of the yield.")],
    cite=f"{C9}, slide 21 (Limiting Reactants), slide 22, slide 25 (theoretical yield from the limiting reactant)",
    hw="HW23 — hw23ex2.png (limiting reactant, then mass of product)",
    covers="Roles of the limiting and excess reactants.",
    sol="""The limiting reactant runs out first and fixes how much product forms (slides 21, 25). The other reactant is **in excess**: when
the limiting reactant is gone the reaction stops, and **some of the excess reactant is left over**, unreacted.""",
))

q, res = q_mass(
    "Mole–mole conversion", "Ch 9 sl. 9–11",
    "Octane burns: 2[[C8H18]](l) + 25[[O2]](g) → 16[[CO2]](g) + 18[[H2O]](g). How many moles of [[O2]] are needed to burn "
    "0.300 mol of [[C8H18]]?",
    "C8H18", 2, "O2", 25, 0.300, "mol", "mol",
    f"{C9}, slide 11 (Mole–Mole Conversions Practice 2: 2C~2~H~6~ + 7O~2~), slide 9",
    "HW22 — hw22ex1.png (2C~6~H~6~ + 15O~2~: reading mole amounts from coefficients)",
    others=[("CO2", 16), ("H2O", 18)])
check(9, res, 3.75, 0.005)
Q.append(q)

q, res = q_mass(
    "Grams to moles of another substance", "Ch 9 sl. 14, 18",
    "Mercury(II) oxide decomposes when heated: 2HgO(s) → 2Hg(l) + [[O2]](g). How many moles of [[O2]] form from 21.7 g of HgO?",
    "HgO", 2, "O2", 1, 21.7, "g", "mol",
    f"{C9}, slide 18 (Stoichiometry Practice 2: moles of H~2~SO~4~ from 19.9 g KOH), slide 14; {C8}, slide 43 (2HgO → 2Hg + O~2~)",
    "HW22 — hw22ex3.png (moles of a substance from grams of another)")
check(10, res, 0.0501, 0.00005)
Q.append(q)

q, res = q_mass(
    "Grams to grams", "Ch 9 sl. 14, 19–20",
    "The thermite reaction is [[Fe2O3]](s) + 2Al(s) → 2Fe(l) + [[Al2O3]](s). What mass of Fe forms from 40.0 g of [[Fe2O3]] "
    "with excess Al?",
    "Fe2O3", 1, "Fe", 2, 40.0, "g", "g",
    f"{C9}, slides 19–20 (Stoichiometry Practice: g → mol → mol → g), slide 14",
    "HW23 — hw23ex1.png (grams of product from grams of reactant)", others=[("Al2O3", 1)])
check(11, res, 28.0, 0.05)
Q.append(q)

q, res = q_mass(
    "Balance first, then grams to grams", "Ch 9 sl. 14, 16, 19",
    "Lithium burns according to the **unbalanced** equation Li(s) + [[O2]](g) → [[Li2O]](s). What mass of [[Li2O]] forms "
    "from 3.47 g of Li with excess [[O2]]?",
    "Li", 4, "Li2O", 2, 3.47, "g", "g",
    f"{C9}, slide 16 (balance before using coefficients), slide 14, slide 19",
    "HW22 — hw22ex1.png (balance with the lowest whole-number coefficients); HW23 — hw23ex3.png",
    balance="Li~2~O has 2 Li and 1 O. O~2~ supplies 2 O, so make **2**Li~2~O. That needs 4 Li: "
            "**4Li + O~2~ $\\rightarrow$ 2Li~2~O**.",
    others=[("O2", 1)])
check(12, res, 7.47, 0.005)
Q.append(q)

q, (L, left) = q_limit(
    "Limiting reactant and leftover", "Ch 9 sl. 21–24",
    "Silicon carbide forms by [[SiO2]](s) + 3C(s) → SiC(s) + 2CO(g). A mixture of 30.0 g of [[SiO2]] and 15.0 g of C is "
    "heated. Which statement is correct?",
    "SiO2", 1, 30.0, "C", 3, 15.0,
    f"{C9}, slide 24 (limiting reactant from two masses), slides 21–23",
    "HW23 — hw23ex2.png (determine the limiting reactant)")
assert L == "C"
Q.append(q)

q, (L, res) = q_yield(
    "Theoretical yield from two masses", "Ch 9 sl. 24–27",
    "For 3[[NO2]](g) + [[H2O]](l) → 2[[HNO3]](aq) + NO(g), 23.0 g of [[NO2]] reacts with 5.00 g of [[H2O]]. What is the "
    "theoretical yield of [[HNO3]]?",
    "NO2", 3, 23.0, "H2O", 1, 5.00, "HNO3", 2,
    f"{C9}, slide 27 (theoretical yield when both masses are given), slide 25, slide 24",
    "HW24 — hw24ex2.png (theoretical yield of XeF~4~ from two masses)")
assert L == "NO2"
check(14, res, 21.0, 0.05)
Q.append(q)

q, res = q_percent(
    "Percent yield", "Ch 9 sl. 28–32",
    "Yeast ferments glucose: [[C6H12O6]](aq) → 2[[C2H5OH]](aq) + 2[[CO2]](g). Fermenting 45.0 g of glucose gives 19.5 g of "
    "ethanol, [[C2H5OH]]. What is the percent yield?",
    "C6H12O6", 1, 45.0, "C2H5OH", 2, 19.5,
    f"{C9}, slide 30 (percent yield formula), slides 31–32 (worked percent yields), slide 28",
    "HW24 — hw24ex1.png (percent yield)")
check(15, res, 84.7, 0.05)
Q.append(q)

if __name__ == "__main__":
    assert len(Q) == 15, len(Q)
    build_driller(9, 3, Q, seed=93, scope=SCOPE, bands=BANDS)
    dist = Counter(q["ans"] for q in Q)
    assert all(dist[L] == 3 for L in "abcde"), dist
