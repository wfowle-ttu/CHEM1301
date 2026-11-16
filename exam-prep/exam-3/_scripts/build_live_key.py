"""Build exam-3-live-answer-key.qmd: certified answer key for the real CHEM 1301 Exam 3 (fall 2026, Ver 1).

Questions were transcribed from the photos of the returned exam. Every numeric answer is recomputed below and
asserted against the printed choice. Every citation was checked against the extracted slide text of
Chapter 7/8/9 post.pptx (slide numbers match the PDFs).
Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_live_key.py
"""
from pathlib import Path

from drillib import EQ, F, sig
from examlib import AM, chem, mm

OUT = Path(__file__).resolve().parent.parent / "exam-3-live-answer-key.qmd"
NA = 6.022e23
C7, C8, C9 = "Ch 7", "Ch 8", "Ch 9"


def near(x, y, tol):
    assert abs(x - y) <= tol, (x, y)


K = []   # (num, letter, answer text, kind, citation, solution, note)


def add(n, letter, ans, cite, sol, note=""):
    K.append((n, letter, ans, cite, sol, note))


# ---------------------------------------------------------------- answers
add(1, "c", "strong electrolyte", f"{C7} slide 7 (Strong Electrolytes)",
    "Slide 7: separated ions are present when a solution is an **excellent conductor of electricity**, and a substance whose "
    "every dissolved unit produces separated ions is called a **strong electrolyte**.")

add(2, "b", "All of the samples contain the same number of atoms", f"{C8} slide 7 (The Mole), slide 9 (Table 8.2)",
    "Slide 7: one mole of something consists of 6.022 × 10^23^ units. Each sample is **1 mol**, so each has 6.022 × 10^23^ "
    "atoms (Table 8.2 on slide 9 shows equal atom counts for 1-mole samples of different elements).")

v = 1.8 * NA
near(v, 1.1e24, 0.05e24)
add(3, "b", "1.1 × 10^24^ atoms", f"{C8} slide 7 (Avogadro's number), slides 13–14 (Atom Conversion Practice)",
    EQ("1.8", "mol O", [F("6.022\\times10^{23}", "O atoms", 1, "mol O", "Avogadro's number")],
       "1.1\\times10^{24}", "O atoms", final=True))

s = 38.8 / AM["S"]
o2 = s * 3 / 2
mol = o2 * NA
near(mol, 1.09e24, 0.005e24)
add(4, "b", "1.09 × 10^24^ molecules oxygen",
    f"{C9} slide 14 (steps: g → mol → mole ratio), slides 17–20; {C8} slides 13–14 (moles → particles)",
    "**Step 1: grams S → moles S** (atomic mass of S = 32.07):\n\n"
    + EQ("38.8", "g S", [F(1, "mol S", "32.07", "g S", "atomic mass of S")], sig(s, 4), "mol S")
    + "\n\n**Step 2: moles S → moles O~2~** (2S + 3O~2~ → 2SO~3~):\n\n"
    + EQ(sig(s, 4), "mol S", [F(3, "mol O2", 2, "mol S", "coefficient of O2 / coefficient of S")], sig(o2, 4), "mol O2")
    + "\n\n**Step 3: moles O~2~ → molecules:**\n\n"
    + EQ(sig(o2, 4), "mol O2", [F("6.022\\times10^{23}", "molecules", 1, "mol O2", "Avogadro's number")],
         "1.09\\times10^{24}", "molecules O2", final=True))

add(5, "a", "produces 8.0 mol of CuO", f"{C9} slides 5–6 (mole ratios from a balanced equation)",
    "From 2Cu + O~2~ → 2CuO, the mole ratio Cu : CuO is 2 : 1... per the coefficients **2 : 2**, so 8.0 mol Cu × (2 mol CuO / "
    "2 mol Cu) = **8.0 mol CuO**. (It reacts with 8.0 × 1/2 = 4.0 mol O~2~, so choice c is wrong.)")

add(6, "c", "oxidation–reduction reaction", f"{C7} slide 31 (Principle 1: metal + nonmetal), slide 38 (2Li + F~2~ → 2LiF)",
    "K (a metal) reacts with Br~2~ (a nonmetal) to form an ionic compound. Slide 31: a metal–nonmetal reaction is **always** "
    "oxidation–reduction. It is the same pattern as slide 38 (2Li + F~2~): each K loses one electron to become K^+^. No solid "
    "forms from solutions (not precipitation), one compound doesn't break apart (not decomposition), and no ion is exchanged "
    "(not displacement).")

v = mm("Ba3(PO4)2")
near(v, 601.93, 0.01)
add(7, "a", "601.93 g/mol", f"{C8} slide 22 (Molar Mass), slide 26 (Ba(OH)~2~: subscript outside parentheses)",
    "Atoms: Ba 3, P 1 × 2 = 2, O 4 × 2 = 8.\n\n3(137.33) + 2(30.97) + 8(16.00) = 411.99 + 61.94 + 128.00 = **601.93 g/mol**.")

v = 23.5 * 4.003
near(v, 94.1, 0.05)
add(8, "d", "94.1 g", f"{C8} slide 27 (Calculating Mass from Moles)",
    EQ("23.5", "mol He", [F("4.003", "g He", 1, "mol He", "atomic mass of He")], "94.1", "g He", final=True))

v = 540.3 / AM["Ca"]
near(v, 13.48, 0.005)
add(9, "d", "13.48 mol", f"{C8} slides 11–12 (Mole Conversion Practice: 544 g Ca), slide 28",
    EQ("540.3", "g Ca", [F(1, "mol Ca", "40.08", "g Ca", "atomic mass of Ca")], "13.48", "mol Ca", final=True))

add(10, "b", "acid–base reaction", f"{C7} slide 37 (Acid–Base Reactions), slides 21–23",
    "HI is an acid (produces H^+^, slide 21) and NaOH a base (produces OH^−^, slide 22). Slide 37: you recognize an acid–base "
    "reaction because it involves an **H^+^ ion that ends up in the product water**. NaI is soluble (rule 2), so it isn't "
    "precipitation.")

s = 5.71 / AM["S"]
o2 = 10.0 / 32.00
need = s * 3 / 2
assert need < o2
so3 = s * mm("SO3")
near(so3, 14.3, 0.05)
add(11, "b", "14.3 g", f"{C9} slides 21–24 (limiting reactant), slides 25, 27 (theoretical yield from the limiting reactant)",
    "**Step 1: moles of each reactant.**\n\n"
    + EQ("5.71", "g S", [F(1, "mol S", "32.07", "g S", "atomic mass of S")], sig(s, 4), "mol S")
    + "\n\n" + EQ("10.0", "g O2", [F(1, "mol O2", "32.00", "g O2", "molar mass of O2")], sig(o2, 4), "mol O2")
    + "\n\n**Step 2: how much O~2~ does all the S need?**\n\n"
    + EQ(sig(s, 4), "mol S", [F(3, "mol O2", 2, "mol S", "coefficient of O2 / coefficient of S")], sig(need, 4), "mol O2 needed")
    + f"\n\n**Step 3: compare.** Need {sig(need, 4)} mol O~2~, have {sig(o2, 4)} mol, so O~2~ is in excess and **S is limiting**.\n\n"
    "**Step 4: SO~3~ from the limiting reactant** (molar mass SO~3~ = 32.07 + 3(16.00) = 80.07 g/mol):\n\n"
    + EQ(sig(s, 4), "mol S", [F(2, "mol SO3", 2, "mol S", "coefficient of SO3 / coefficient of S"),
                             F("80.07", "g SO3", 1, "mol SO3", "molar mass of SO3")], "14.3", "g SO3", final=True))

add(12, "b", "Both beakers A and B contain the same number of atoms because there is one mole in each",
    f"{C8} slide 6 (same mass ratio as atomic masses → same number of atoms), slides 7, 9",
    "32.07 g S is 1 mol S (atomic mass 32.07) and 74.92 g As is 1 mol As (atomic mass 74.92, periodic table). One mole of "
    "anything is 6.022 × 10^23^ units (slide 7), so the counts are equal. Slide 6 makes the same argument with 26.98 g Al and "
    "63.55 g Cu.",
    note="The atomic mass of As (74.92) comes from the periodic table provided on the exam.")

add(13, "a", "acid–base reaction", f"{C7} slide 23 (Acid–Base Reactions), slide 26 (principle 5)",
    "Slide 23: \"Besides water, **which is always a product** of the reaction of an acid with OH^−^ ...\" Slide 26 (principle 5) "
    "repeats that one product is always water.")

add(14, "a", "oxidation–reduction reaction", f"{C7} slide 40 (Single-Replacement Reactions)",
    "Slide 40 uses this exact reaction: \"This reaction is an **oxidation–reduction reaction**. This reaction is also a "
    "single-replacement reaction.\" No solid forms (not precipitation), and the H^+^ ends up in H~2~ gas, not water (not "
    "acid–base).")

pct = {f: n * 14.01 / mm(f) * 100 for f, n in [("NH3", 1), ("N2O", 2), ("HCN", 1), ("N2H4", 2), ("HNO3", 1)]}
assert min(pct, key=pct.get) == "HNO3"
add(15, "a", "HNO~3~", f"{C8} slide 30 (Mass Percent), slides 31–32",
    "Mass percent N = (N atoms × 14.01) ÷ molar mass × 100% (slide 30):\n\n"
    + "\n".join(f"* {chem('[[' + f + ']]')}: {pct[f]:.1f}%" for f in pct)
    + "\n\nThe smallest is **HNO~3~ (22.2%)**. With 100.0 g of each, the sample with the smallest percent has the least N.")

add(16, "a", "1.0 mol Zn", f"{C8} slide 9 (Table 8.2: the mass of 1 mol equals the atomic mass in grams)",
    "1 mol of an element weighs its atomic mass in grams (Table 8.2): Zn 65.38 g, Ni 58.69 g, Cr 52.00 g, Si 28.09 g. The "
    "largest is **Zn**.", note="Atomic masses from the periodic table provided on the exam.")

ch4 = 38.4 / mm("CH4")
theo = ch4 * mm("CH3Cl")
p17 = 45.0 / theo * 100
near(p17, 37.2, 0.05)
add(17, "d", "37.2%", f"{C9} slide 25 (theoretical yield), slide 30 (Percent Yield), slides 31–32",
    "CH~4~ is the limiting reactant (Cl~2~ in excess). Molar masses: CH~4~ = 12.01 + 4(1.008) = 16.04; "
    "CH~3~Cl = 12.01 + 3(1.008) + 35.45 = 50.48 g/mol.\n\n"
    + EQ("38.4", "g CH4", [F(1, "mol CH4", "16.04", "g CH4", "molar mass of CH4"),
                          F(1, "mol CH3Cl", 1, "mol CH4", "coefficients"),
                          F("50.48", "g CH3Cl", 1, "mol CH3Cl", "molar mass of CH3Cl")], sig(theo, 4), "g CH3Cl (theoretical)")
    + f"\n\n$$\\text{{percent yield}}=\\frac{{45.0\\ \\text{{g (actual)}}}}{{{sig(theo, 4)}\\ \\text{{g (theoretical)}}}}\\times100\\% = \\boxed{{37.2\\%}}$$")

c = 21.4 / mm("C6H14")
o2g = c * 19 / 2 * 32.00
near(o2g, 75.5, 0.05)
add(18, "a", "75.5 g", f"{C9} slide 14 (step 1: balance the equation), slide 16, slides 17–20; {C9} slide 9 (balancing a combustion)",
    "**Step 1: balance.** C: 6CO~2~. H: 14 H → 7H~2~O. O: 6(2) + 7 = 19 O → 19/2 O~2~, so double everything: "
    "**2C~6~H~14~ + 19O~2~ → 12CO~2~ + 14H~2~O**.\n\n"
    "**Step 2: g → mol → mol → g** (C~6~H~14~ = 6(12.01) + 14(1.008) = 86.17 g/mol):\n\n"
    + EQ("21.4", "g C6H14", [F(1, "mol C6H14", "86.17", "g C6H14", "molar mass of C6H14"),
                            F(19, "mol O2", 2, "mol C6H14", "coefficients"),
                            F("32.00", "g O2", 1, "mol O2", "molar mass of O2")], "75.5", "g O2", final=True))

add(19, "a", "2NH~4~^+^(aq)", f"{C7} slide 16 (Complete Ionic Equations), slide 14, slide 11",
    "Molecular: (NH~4~)~2~CO~3~(aq) + BaCl~2~(aq) → BaCO~3~(s) + 2NH~4~Cl(aq). BaCO~3~ is a carbonate (rule 6), so it "
    "precipitates; NH~4~Cl is soluble (rule 2).\n\nComplete ionic (strong electrolytes as ions, slide 16):\n\n"
    "**2NH~4~^+^(aq)** + CO~3~^2−^(aq) + Ba^2+^(aq) + 2Cl^−^(aq) → BaCO~3~(s) + 2NH~4~^+^(aq) + 2Cl^−^(aq)\n\n"
    "Only **2NH~4~^+^(aq)** appears among the choices with the coefficient it has in standard form. Chloride appears as "
    "2Cl^−^, not Cl^−^; barium as Ba^2+^, not 3Ba^2+^; carbonate as CO~3~^2−^, not 2CO~3~^2−^.")

C, H, Br = 12.8 / 12.01, 2.1 / 1.008, 85.1 / 79.90
m = min(C, H, Br)
assert (round(C / m), round(H / m), round(Br / m)) == (1, 2, 1)
n20 = 188 / mm("CH2Br")
assert round(n20) == 2
add(20, "d", "C~2~H~4~Br~2~", f"{C8} slides 35–37, 42–43 (empirical formula steps), slides 47–48 (molecular formula)",
    f"**Empirical formula** (100 g sample): C 12.8/12.01 = {C:.3f} mol; H 2.1/1.008 = {H:.3f} mol; Br 85.1/79.90 = {Br:.3f} mol. "
    f"Divide by the smallest ({m:.3f}): C {C/m:.2f}, H {H/m:.2f}, Br {Br/m:.2f} → **CH~2~Br**.\n\n"
    f"**Molecular formula:** empirical mass = 12.01 + 2(1.008) + 79.90 = {mm('CH2Br'):.2f} g/mol; n = 188 ÷ {mm('CH2Br'):.2f} = "
    f"{n20:.2f} ≈ 2 (slide 48), so (CH~2~Br)~2~ = **C~2~H~4~Br~2~**.")

add(21, "a", "6.022 × 10^23^ units", f"{C8} slide 7 (The Mole)",
    "Slide 7: \"One mole of something consists of **6.022 × 10^23^ units** of that substance.\"")

n2 = 9.33 / mm("N2")
h2 = n2 * 3 * mm("H2")
near(h2, 2.01, 0.005)
add(22, "c", "2.01 g", f"{C9} slide 14 (steps), slides 17–20 (Stoichiometry Practice)",
    EQ("9.33", "g N2", [F(1, "mol N2", "28.02", "g N2", "molar mass of N2"),
                       F(3, "mol H2", 1, "mol N2", "coefficients"),
                       F("2.016", "g H2", 1, "mol H2", "molar mass of H2")], "2.01", "g H2", final=True))

add(23, "b", "no precipitate forms", f"{C7} slide 14 (exchange the anions), slide 11 (Table 7.1, rule 2)",
    "Ions: K^+^, Cl^−^, Na^+^, SO~4~^2−^. Exchanging anions gives K~2~SO~4~ and NaCl. Both contain K^+^ or Na^+^, so both are "
    "soluble (rule 2): **no precipitate forms**. (Na~2~SO~4~ is a reactant, not a product.)")

add(24, "a", "BaSO~4~", f"{C7} slide 11 (Table 7.1, rule 4), slide 12 (Solubility Practice: BaSO~4~)",
    "Rule 4: most sulfates are soluble; **notable exceptions are BaSO~4~, PbSO~4~, and CaSO~4~**. FeSO~4~ and CuSO~4~ are "
    "soluble by rule 4, and Na~2~SO~4~ by rules 2 and 4. Slide 12 classifies BaSO~4~ as insoluble.")

v = mm("Ca(NO2)2")
near(v, 132.10, 0.01)
add(25, "d", "132.10 g/mol", f"{C8} slide 22 (Molar Mass), slide 26 (subscript outside parentheses)",
    "Calcium nitrite is Ca(NO~2~)~2~ (Ca^2+^ with two nitrite ions, NO~2~^−^). Atoms: Ca 1, N 2, O 4.\n\n"
    "40.08 + 2(14.01) + 4(16.00) = 40.08 + 28.02 + 64.00 = **132.10 g/mol**.",
    note="The formula of the nitrite ion (NO~2~^−^) comes from ion naming taught earlier in the course; it is not in the "
         "Chapter 7–9 slides. (Choice a, 164.10 g/mol, is calcium **nitrate**, Ca(NO~3~)~2~.)")

add(26, "b", "decomposition reaction", f"{C7} slide 43 (Decomposition Reactions)",
    "Slide 43 uses this exact reaction as its example: 2HgO(s) → 2Hg(l) + O~2~(g), with heat. A compound broken down into "
    "simpler substances (here its elements) is a **decomposition** reaction.")

C, H, O = 40.68 / 12.01, 5.12 / 1.008, 54.20 / 16.00
m = min(C, H, O)
assert abs(H / m - 1.5) < 0.01
add(27, "a", "C~2~H~3~O~2~", f"{C8} slides 42–43 (Steps for Determining the Empirical Formula, step 4), slides 35–37",
    f"**Steps 1–2** (100 g sample): C 40.68/12.01 = {C:.4f} mol; H 5.12/1.008 = {H:.4f} mol; O 54.20/16.00 = {O:.4f} mol.\n\n"
    f"**Step 3** (÷ smallest, {m:.4f}): C {C/m:.2f}, H {H/m:.2f}, O {O/m:.2f}.\n\n"
    "**Step 4** (slide 43): 1.50 isn't whole, so multiply **every** result by 2: C 2, H 3, O 2 → **C~2~H~3~O~2~**.")

add(28, "b", "precipitate", f"{C7} slide 5 (Precipitation Reactions)",
    "Slide 5: \"The solid that forms is called a **precipitate**, and the reaction is known as a precipitation reaction.\"")

tot = 3 * 112.41 + 2 * (30.97 + 64.00)
p29 = 3 * 112.41 / tot * 100
near(p29, 64.0, 0.05)
add(29, "b", "64.0%", f"{C8} slide 30 (Mass Percent), slides 31–33",
    f"Atoms: Cd 3, P 2, O 8. Molar mass = 3(112.41) + 2(30.97) + 8(16.00) = 337.23 + 61.94 + 128.00 = {tot:.2f} g/mol.\n\n"
    f"$$\\%\\,\\text{{Cd}}=\\frac{{337.23}}{{{tot:.2f}}}\\times100\\% = \\boxed{{64.0\\%}}$$",
    note="The atomic mass of Cd (112.41) comes from the periodic table provided on the exam.")

ca = 49.3 / mm("CaCO3")
th = ca * mm("H2O")
p30 = 3.65 / th * 100
near(p30, 41.1, 0.05)
add(30, "a", "41.1%", f"{C9} slide 25 (theoretical yield), slide 30 (Percent Yield), slides 31–32",
    "**Step 1: balanced equation.** CaCO~3~ + H~2~SO~4~ → CaSO~4~ + H~2~O + CO~2~ (all coefficients 1). CaCO~3~ (100.09 g/mol) "
    "is the given reactant.\n\n"
    + EQ("49.3", "g CaCO3", [F(1, "mol CaCO3", "100.09", "g CaCO3", "molar mass of CaCO3"),
                            F(1, "mol H2O", 1, "mol CaCO3", "coefficients"),
                            F("18.02", "g H2O", 1, "mol H2O", "molar mass of H2O")], sig(th, 4), "g H2O (theoretical)")
    + f"\n\n$$\\text{{percent yield}}=\\frac{{3.65\\ \\text{{g}}}}{{{sig(th, 4)}\\ \\text{{g}}}}\\times100\\% = \\boxed{{41.1\\%}}$$")

add(31, "d", "molecular equation", f"{C7} slide 15 (Molecular Equations), slide 18",
    "Slide 15: \"A molecular equation shows the **complete formulas** of all reactants and products.\" Every substance here is "
    "written as a full formula (no separated ions), so it is a **molecular equation**.")

M32 = 0.376 / 8.55e-3
mms = {f: mm(f) for f in ["C4H10", "CH4", "C2H6", "C3H8"]}
best = min(mms, key=lambda f: abs(mms[f] - M32))
assert best == "C3H8"
add(32, "d", "C~3~H~8~", f"{C8} slide 22 (Molar Mass: g per mol), slides 27–28 (mass ↔ moles)",
    f"Molar mass = mass ÷ moles = 0.376 g ÷ 8.55 × 10^−3^ mol = **{M32:.1f} g/mol**.\n\n"
    + "\n".join(f"* {chem('[[' + f + ']]')}: {v:.2f} g/mol" for f, v in mms.items())
    + "\n\nOnly **C~3~H~8~ (44.09 g/mol)** matches 44.0 g/mol.")

add(33, "b", "3", f"{C7} slide 33 (electrons transferred from each Al atom), slide 31 (Principle 1)",
    "AlF~3~ is ionic (metal + nonmetal, slide 31): Al^3+^ and F^−^ (charges: +3 + 3(−1) = 0). Each Al goes from 0 to +3, so "
    "**3 electrons** are transferred from each Al atom, the same count as slide 33's 2Al + N~2~ practice.")

add(34, "c", "Ag~2~CrO~4~", f"{C7} slide 14 (exchange the anions), slide 11 (rules 1 and 2), slides 35–36 (BaCrO~4~ precipitate)",
    "Ions: Ag^+^, NO~3~^−^, K^+^, CrO~4~^2−^. Exchanging anions gives **Ag~2~CrO~4~** (2 Ag^+^ balance CrO~4~^2−^) and KNO~3~. "
    "KNO~3~ is soluble (rules 1 and 2), and AgNO~3~ and K~2~CrO~4~ are the dissolved reactants, so the precipitate is "
    "**Ag~2~CrO~4~**.",
    note="Table 7.1 has no rule for chromates. The answer follows from the slide-14 method plus elimination (KNO~3~ is soluble "
         "by rules 1 and 2). Slides 35–36 show another chromate, BaCrO~4~, precipitating.")

v = 5.0 * 3 / 2
near(v, 7.5, 1e-9)
add(35, "d", "7.5 mol", f"{C9} slides 10–11 (Mole–Mole Conversions)",
    EQ("5.0", "mol CO2", [F(3, "mol O2", 2, "mol CO2", "coefficient of O2 / coefficient of CO2")], "7.5", "mol O2", final=True))

# fix wording slip in Q5 solution
K[4] = (5, "a", "produces 8.0 mol of CuO", f"{C9} slides 5–6 (mole ratios from a balanced equation)",
        "From 2Cu + O~2~ → 2CuO, the mole ratio Cu : CuO is **2 : 2**:\n\n"
        + EQ("8.0", "mol Cu", [F(2, "mol CuO", 2, "mol Cu", "coefficient of CuO / coefficient of Cu")], "8.0", "mol CuO", final=True)
        + "\n\nIt reacts with 8.0 × (1/2) = 4.0 mol O~2~, so choice c (8.0 mol O~2~) is wrong.", "")

assert [k[0] for k in K] == list(range(1, 36))

# ---------------------------------------------------------------- write
HEAD = """---
title: "CHEM 1301 Exam 3 (Fall 2026, Ver 1) — Certified Answer Key"
subtitle: "Answers worked from the returned exam, each checked against the course slides"
format:
  pdf:
    papersize: letter
    fontsize: 11pt
    include-in-header:
      text: |
        \\usepackage{longtable,array,colortbl,cancel}
filters:
  - _filters/tables.lua
---

**How this key was certified.** Each question was transcribed from the photos of the returned exam (Ver 1, pages 1–6).
Every numeric answer was recomputed by `_scripts/build_live_key.py` and checked against the printed choice. Every citation
was checked against the actual text of the cited slide in `Chapter 7/8/9 post.pptx` (slide numbers match the PDFs).
Atomic masses are periodic-table values. **Notes** flag any answer that relies on something outside the Chapter 7–9 slides.
The handwritten answers on the exam were not used to choose these answers.

"""
lines = [HEAD, "| Q | Answer | | Q | Answer |\n|:-:|:--|-|:-:|:--|\n"]
half = 18
for i in range(half):
    a = K[i]
    b = K[i + half] if i + half < 35 else None
    right = f"| {b[0]} | **{b[1]}**  {b[2]} |" if b else "| | |"
    lines.append(f"| {a[0]} | **{a[1]}**  {a[2]} | {right}\n")
lines.append("\n")
for n, letter, ans, cite, sol, note in K:
    lines.append(f"# {n}. **{letter})** {ans}\n\n**Course source:** {cite}\n\n{chem(sol)}\n\n")
    if note:
        lines.append(f"**Note:** {chem(note)}\n\n")
OUT.write_text("".join(lines), encoding="utf-8")
print("wrote", OUT.name, "-", "".join(k[1] for k in K))
