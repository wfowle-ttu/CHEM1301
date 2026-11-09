"""Build driller-9-4: section 8.7 + Chapter 9, 15 questions (same layout as build_driller_9_2.py).

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_driller_9_4.py
"""
from collections import Counter

from build_driller_9_2 import BANDS, SCOPE
from drillib import (C8, C9, T, check, q_bridge, q_empirical, q_limit, q_mass, q_molecular, q_percent, q_yield)
from examlib import build_driller

Q = []

# ================================================================ section 8.7
Q.append(dict(
    ch=8, kind="concept", title="A result that isn't a whole number", short="Ch 8 sl. 43",
    stem="While finding an empirical formula, you divide by the smallest mole value and get C 1.00, H 1.33, O 1.00. "
         "What should you do next?",
    correct=T("Multiply every element's result by 3, giving [[C3H4O3]]"),
    wrong=[T("Round H to 1, giving CHO", "Only results within about 0.1 of a whole number may be rounded. 1.33 is 0.33 away."),
           T("Multiply only the H result by 3, giving [[CH4O]]",
             "That changes the ratio. The same multiplier goes on **every** element."),
           T("Multiply every result by 2, giving [[C2H3O2]]",
             "1.33 × 2 = 2.67, still not whole. A .33 means thirds, so multiply by 3."),
           T("Divide every result by 1.33 again",
             "That would make C and O fractions (0.75). Step 4 multiplies; it never divides again.")],
    cite=f"{C8}, slide 43 (step 4: multiply by the smallest integer that gives whole numbers), slides 42, 46",
    hw="HW21 — hw21ex2.png (empirical formula from percent composition)",
    covers="Step 4 of the empirical-formula method: .33 means thirds, multiply **every** element by 3.",
    sol="""**Step 1: is 1.33 a whole number?** "Whole" means within about 0.1 of an integer. 1.33 is 0.33 away from 1, so it is **not**
whole, and you must not round it.

**Step 2: which multiplier?** A decimal near .33 (or .67) is a third, so multiply by **3**: 1.33 × 3 = 3.99 ≈ 4.

**Step 3: apply it to every element.** C 1.00 × 3 = 3, H 1.33 × 3 = 4, O 1.00 × 3 = 3, giving **C~3~H~4~O~3~**. This is the
vitamin C example in study guide 8.7 (Type B, example C).""",
))

Q.append(dict(
    ch=8, kind="calc", title="Molecular to empirical formula", short="Ch 8 sl. 39–40",
    stem="Erythrose has the molecular formula [[C4H8O4]]. What is its empirical formula?",
    correct=T("[[CH2O]]"),
    wrong=[T("[[C2H4O2]]", "Divided by 2, but 2, 4, and 2 can still all be divided by 2. Use the **largest** common divisor, 4."),
           T("[[C4H8O4]]", "That is the molecular formula; 4, 8, and 4 share a factor of 4."),
           T("[[CHO]]", "Divided H by 8 instead of 4. Every subscript is divided by the **same** number."),
           T("[[CH4O]]", "Divided C and O by 4 but H only by 2.")],
    cite=f"{C8}, slide 39 (empirical formula = smallest whole-number ratio), slide 40",
    hw="HW21 — hw21ex3.png (relating empirical and molecular formulas)",
    covers="Type A (study guide 8.7): use the **largest** common divisor, not just 2.",
    sol="""**Step 1: list the subscripts.** C 4, H 8, O 4.

**Step 2: find the largest number that divides all three evenly.** 4 ÷ 4 = 1, 8 ÷ 4 = 2, 4 ÷ 4 = 1. Nothing larger than 4
divides 4, so the divisor is **4**. (Dividing by 2 gives C~2~H~4~O~2~, which can still be reduced, so it isn't the
smallest ratio.)

**Step 3: divide every subscript by 4.** **CH~2~O**.""",
))

q, r = q_empirical(
    "Percent composition to empirical formula (×4)", "Ch 8 sl. 42–43",
    "Aspirin is 60.00% C, 4.48% H, and 35.52% O by mass. What is its empirical formula?",
    ["C", "H", "O"], [60.00, 4.48, 35.52], "percent",
    f"{C8}, slides 42–43 (Steps for Determining the Empirical Formula; step 4: multiply when not whole)",
    "HW21 — hw21ex2.png (empirical formula from percent composition)")
assert r["formula"] == "C9H8O4"
Q.append(q)

q, r = q_empirical(
    "Percent composition to empirical formula (×2)", "Ch 8 sl. 35–38, 42–43",
    "An orange salt is 26.58% K, 35.35% Cr, and 38.07% O by mass. What is its empirical formula?",
    ["K", "Cr", "O"], [26.58, 35.35, 38.07], "percent",
    f"{C8}, slides 42–43 (step 4: multiply when not whole), slides 35–38",
    "HW21 — hw21ex2.png (three-element percent compositions: MgSO~4~, SiCl~2~Br~2~)")
assert r["formula"] == "K2Cr2O7"
Q.append(q)

q, r = q_empirical(
    "Grams to empirical formula", "Ch 8 sl. 45–46",
    "A sample of a sodium salt contains 2.30 g of Na, 1.60 g of S, and 2.40 g of O. What is its empirical formula?",
    ["Na", "S", "O"], [2.30, 1.60, 2.40], "grams",
    f"{C8}, slides 45–46 (empirical formula from masses), slide 42",
    "HW21 — empirical formula from composition data")
assert r["formula"] == "Na2SO3"
Q.append(q)

Q.append(q_molecular(
    "Empirical to molecular formula", "Ch 8 sl. 47–49",
    "A hydrocarbon has the empirical formula [[C3H4]] and a molar mass of 120.19 g/mol. What is its molecular formula?",
    "C3H4", 120.19,
    f"{C8}, slide 48 (molecular formula = (empirical formula)~n~), slide 49 (LA Practice), slide 47",
    "HW21 — hw21ex3.png (empirical formula + molar mass → molecular formula)"))

q, res = q_bridge(
    "From percent composition to a mole ratio", "Ch 8 sl. 42–49; Ch 9 sl. 9–11",
    "A liquid fuel is 52.14% C, 13.13% H, and 34.73% O by mass, and its molar mass is 46.07 g/mol. It burns completely in "
    "[[O2]] to form [[CO2]] and [[H2O]]. How many moles of [[O2]] are needed to burn 0.200 mol of the fuel?",
    ["C", "H", "O"], [52.14, 13.13, 34.73], 46.07,
    "Combustion of C~2~H~6~O: C first (2CO~2~), then H (3H~2~O, 6 H). The right side has 2(2) + 3(1) = 7 O. The fuel "
    "already supplies **1** O, so O~2~ must supply 6 O: 3O~2~. **C~2~H~6~O + 3O~2~ $\\rightarrow$ 2CO~2~ + 3H~2~O**.",
    "C2H6O", 1, "O2", 3, 0.200,
    [(0.200 * 3.5, "Balanced O without counting the O already in the fuel (3.5 O~2~ instead of 3)."),
     (0.200 * 6, "Assumed n = 2 (C~4~H~12~O~2~). Here n = 46.07 ÷ 46.07 = 1."),
     (0.200, "Assumed 1 : 1. O~2~'s coefficient is 3."),
     (0.200 * 2, "Used CO~2~'s coefficient (2) instead of O~2~'s (3)."),
     (0.200 / 3, "Ratio upside down: × 1/3 instead of × 3/1.")],
    f"{C8}, slides 42–49 (empirical then molecular formula); {C9}, slide 9 (balancing a combustion), slides 10–11",
    "HW21 — hw21ex3.png; HW22 — hw22ex3.png (CH~3~CH~2~OH + O~2~ equations)")
check(7, res, 0.600, 0.0005)
Q.append(q)

# ================================================================ Chapter 9
Q.append(dict(
    ch=9, kind="concept", title="What a mole–mole conversion needs", short="Ch 9 sl. 5–7, 10",
    stem="To convert **moles of A** into **moles of B** for a reaction, which information do you need?",
    correct=T("The coefficients of A and B in the balanced equation"),
    wrong=[T("The molar masses of A and B", "Molar masses convert grams ↔ moles of the **same** substance, not A to B."),
           T("Avogadro's number", "That converts moles ↔ particles. It doesn't relate two different substances."),
           T("The subscripts in the formulas of A and B", "Subscripts count atoms within one formula. The ratio between substances comes from the coefficients."),
           T("The masses of A and B present", "Masses are needed to find moles, but the link from A to B is the mole ratio.")],
    cite=f"{C9}, slides 5–7 (mole ratios from the balanced equation), slide 10 (Mole–Mole Conversions)",
    hw="HW22 — hw22ex2.png (choosing the mole ratio from the coefficients)",
    covers="The mole ratio comes only from the coefficients of a balanced equation.",
    sol=r"""The **mole ratio** (slides 5–7) is the only conversion factor that connects two different substances, and it comes from the
**coefficients** of the balanced equation:

$$\text{mol B} = \text{mol A}\times\frac{\text{coefficient of B}}{\text{coefficient of A}}$$""",
))

q, res = q_mass(
    "Mole–mole conversion", "Ch 9 sl. 10–11",
    "For 4[[NH3]](g) + 3[[O2]](g) → 2[[N2]](g) + 6[[H2O]](g), how many moles of [[N2]] form from 2.40 mol of [[NH3]]?",
    "NH3", 4, "N2", 2, 2.40, "mol", "mol",
    f"{C9}, slides 10–11 (Mole–Mole Conversions Practice)",
    "HW22 — hw22ex3.png (moles of product from moles of another substance)",
    others=[("O2", 3), ("H2O", 6)])
check(9, res, 1.20, 0.005)
Q.append(q)

q, res = q_mass(
    "Grams to moles of another substance", "Ch 9 sl. 14, 18",
    "For [[CS2]](l) + 3[[O2]](g) → [[CO2]](g) + 2[[SO2]](g), how many moles of [[SO2]] form from 15.2 g of [[CS2]] with "
    "excess [[O2]]?",
    "CS2", 1, "SO2", 2, 15.2, "g", "mol",
    f"{C9}, slide 18 (Stoichiometry Practice 2: moles of H~2~SO~4~ from 19.9 g KOH), slide 14",
    "HW22 — hw22ex3.png (moles needed from grams: 0.206 g Al → mol Br~2~)", others=[("O2", 3)])
check(10, res, 0.399, 0.0005)
Q.append(q)

q, res = q_mass(
    "Grams to grams", "Ch 9 sl. 14, 19–20",
    "Copper displaces silver: Cu(s) + 2[[AgNO3]](aq) → [[Cu(NO3)2]](aq) + 2Ag(s). What mass of Ag forms when 5.00 g of Cu "
    "reacts with excess [[AgNO3]]?",
    "Cu", 1, "Ag", 2, 5.00, "g", "g",
    f"{C9}, slides 19–20 (Stoichiometry Practice: g → mol → mol → g), slide 14",
    "HW23 — hw23ex1.png (grams of product from grams of reactant)", others=[("Cu(NO3)2", 1)])
check(11, res, 17.0, 0.05)
Q.append(q)

q, res = q_mass(
    "Balance first, then grams to grams", "Ch 9 sl. 14, 16, 19",
    "Potassium burns according to the **unbalanced** equation K(s) + [[O2]](g) → [[K2O]](s). What mass of [[K2O]] forms from "
    "7.82 g of K with excess [[O2]]?",
    "K", 4, "K2O", 2, 7.82, "g", "g",
    f"{C9}, slide 16 (balance before using coefficients), slide 14, slide 19",
    "HW22 — hw22ex1.png (balance with the lowest whole-number coefficients); HW23 — hw23ex3.png",
    balance="K~2~O has 1 O, and O~2~ supplies 2 O, so make **2**K~2~O. That has 4 K: **4K + O~2~ $\\rightarrow$ 2K~2~O**.",
    others=[("O2", 1)], drop=("upside down",))
check(12, res, 9.42, 0.005)
Q.append(q)

q, (L, left) = q_limit(
    "Limiting reactant and leftover", "Ch 9 sl. 21–24",
    "Zinc sulfide is roasted: 2ZnS(s) + 3[[O2]](g) → 2ZnO(s) + 2[[SO2]](g). A mixture of 50.0 g of ZnS and 20.0 g of [[O2]] "
    "reacts. Which statement is correct?",
    "ZnS", 2, 50.0, "O2", 3, 20.0,
    f"{C9}, slide 24 (limiting reactant from two masses), slides 21–23",
    "HW23 — hw23ex2.png (5.65 g of each reactant: which is limiting?)")
assert L == "O2"
Q.append(q)

q, (L, res) = q_yield(
    "Theoretical yield from two masses", "Ch 9 sl. 24–27",
    "For 2Al(s) + 3[[CuSO4]](aq) → [[Al2(SO4)3]](aq) + 3Cu(s), 5.40 g of Al reacts with 40.0 g of [[CuSO4]]. What is the "
    "theoretical yield of Cu?",
    "Al", 2, 5.40, "CuSO4", 3, 40.0, "Cu", 3,
    f"{C9}, slide 27 (theoretical yield when both masses are given), slide 25, slide 24",
    "HW23 — hw23ex3.png (limiting reactant, then mass of product); HW24 — hw24ex2.png")
assert L == "CuSO4"
check(14, res, 15.9, 0.05)
Q.append(q)

q, res = q_percent(
    "Percent yield", "Ch 9 sl. 28–32",
    "Magnesium burns: 2Mg(s) + [[O2]](g) → 2MgO(s). Burning 4.86 g of Mg in excess [[O2]] gives 7.10 g of MgO. What is the "
    "percent yield?",
    "Mg", 2, 4.86, "MgO", 2, 7.10,
    f"{C9}, slide 30 (percent yield formula), slides 31–32, slide 28",
    "HW24 — hw24ex1.png (percent yield of magnesium oxide)",
    excess_note="[[O2]] is in excess, so **Mg is limiting** and the theoretical yield is calculated from it.")
check(15, res, 88.1, 0.05)
Q.append(q)

if __name__ == "__main__":
    assert len(Q) == 15, len(Q)
    build_driller(9, 4, Q, seed=94, scope=SCOPE, bands=BANDS)
    dist = Counter(q["ans"] for q in Q)
    assert all(dist[L] == 3 for L in "abcde"), dist
