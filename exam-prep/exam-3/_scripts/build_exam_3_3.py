"""Build practice-exam-3-3 and its key, checking every numeric answer.

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_exam_3_3.py
Same blueprint as 3-1 and 3-2 (Ch 7: 13, Ch 8: 13, Ch 9: 9; 18 concept / 17 calc; 7 answers per letter),
with new compounds and numbers. Generated questions come from solib (Ch 7 solubility) and drillib
(Ch 8.7 and Ch 9); their key solutions name every step and label every conversion factor.
No question lists the solubility rules as choices; electron counts are asked per atom.
"""
from collections import Counter

from drillib import C8, C9, EQ, F, Steps, T, q_empirical, q_limit, q_mass, q_molecular, q_percent, q_yield, sig
from examlib import NA, build, check, mm, sci
from solib import C7, q_mix, q_net, q_pair, q_pick, q_spect

Q = []
CL = f"{C7}, slide 11 (Table 7.1), slide 12 (Solubility Practice)"
PRED = f"{C7}, slide 14 (How to Predict Precipitates), slide 11"
HW14 = "HW14 — hw14ex5.png (classify compounds as soluble or not soluble)"
HW15 = "HW15 — hw15ex3.png (does a reaction occur? NR or net ionic)"


def nq(ch, title, short, stem, correct, wrong, cite, hw, covers, sol, unit="", fmt=None):
    """Numeric question: correct/wrong values are formatted with `fmt` (default 3 sig figs) plus `unit`."""
    fmt = fmt or (lambda v: sig(v))
    return dict(ch=ch, kind="calc", numeric=True, title=title, short=short, stem=stem,
                correct=(correct, fmt(correct) + unit, ""), wrong=[(v, fmt(v) + unit, w) for v, w in wrong],
                cite=cite, hw=hw, covers=covers, sol=sol)


# ================================================================ Chapter 7 (13)
Q.append(dict(
    ch=7, kind="concept", title="Driving force of a precipitation", short="Ch 7 sl. 3, 35",
    stem="When aqueous [[K2CrO4]] and Ba([[NO3]])~2~ are mixed, yellow [[BaCrO4]](s) forms. Which driving force makes this "
         "reaction occur?",
    correct=T("Formation of a solid"),
    wrong=[T("Formation of water", "No H^+^ or OH^−^ is involved, so no water forms."),
           T("Formation of a gas", "No gas is produced."),
           T("Transfer of electrons", "Every ion keeps its charge (Ba stays +2, CrO~4~ stays −2)."),
           T("Formation of a strong acid", "Not one of the four driving forces.")],
    cite=f"{C7}, slide 3 (Driving Forces), slide 35 (Precipitation Reaction: BaCrO~4~)",
    hw="HW14 — hw14ex1.png (a reaction that forms a solid is a precipitation)",
    covers="Matching a reaction to its driving force: precipitation ↔ formation of a solid.",
    sol="Slide 3 lists four driving forces: formation of a solid, of water, or of a gas, and transfer of electrons. Here a solid, "
        "BaCrO~4~, forms from two solutions, so the driving force is **formation of a solid** (slide 35 calls this a "
        "precipitation reaction)."))

Q.append(q_pick("Which compound is insoluble?", "Ch 7 sl. 11–12", "On the basis of the solubility rules, which compound is "
                "**insoluble** in water?", [("Cu", "NO3"), ("NH4", "CO3"), ("Mg", "Cl"), ("Zn", "SO4"), ("Pb", "S")],
                False, CL, HW14))
Q.append(q_pick("Which compound is soluble?", "Ch 7 sl. 11–12", "Which compound is expected to be **soluble** in water?",
                [("K", "PO4"), ("Ca", "SO4"), ("Ni", "OH"), ("Ag", "Cl"), ("Ba", "CO3")], True, CL, HW14))
Q.append(q_mix("Predicting the precipitate", "Ch 7 sl. 14", ("Fe3", "Cl"), ("Na", "OH"), PRED, HW15,
               ("[[Fe(OH)2]]", "Fe^3+^ needs **three** OH^−^ to be neutral: Fe(OH)~3~.")))
Q.append(q_net("Net ionic equation", "Ch 7 sl. 16–20", ("Ba", "NO3"), ("Na", "SO4"),
               f"{C7}, slides 16–17 (complete and net ionic equations), slides 19–20, slide 11",
               "HW15 — hw15ex2.png (net ionic equations for precipitations)"))

Q.append(dict(
    ch=7, kind="calc", numeric=True, title="Balancing an acid–base neutralization", short="Ch 7 sl. 27",
    stem="When the equation below is balanced with the smallest whole-number coefficients, what is the **sum** of all four "
         "coefficients?\n\n\\_\\_ [[H3PO4]](aq) + \\_\\_ [[Ba(OH)2]](aq) → \\_\\_ [[Ba3(PO4)2]](s) + \\_\\_ [[H2O]](l)",
    correct=(12, "12", ""),
    wrong=[(4, "4", "All coefficients 1 doesn't balance Ba, PO~4~, H, or O."),
           (8, "8", "Balanced Ba and PO~4~ (3 and 2) but used 2 H~2~O; 6 H^+^ + 6 OH^−^ make 6 H~2~O."),
           (10, "10", "Off by two: check the water. 2 H~3~PO~4~ supply 6 H^+^."),
           (14, "14", "One coefficient too large; the smallest set is 2, 3, 1, 6.")],
    cite=f"{C7}, slide 27 (Practice: balance H~3~PO~4~ + Ca(OH)~2~ → Ca~3~(PO~4~)~2~ + H~2~O)",
    hw="HW17 — hw17ex2.png (balance with the lowest whole-number coefficients)",
    covers="Balancing a neutralization: metal first, the polyatomic ion as a unit, then water.",
    sol="""**Step 1: Ba.** Ba~3~(PO~4~)~2~ has 3 Ba, so **3**Ba(OH)~2~.

**Step 2: PO~4~ as a unit.** Ba~3~(PO~4~)~2~ has 2 PO~4~, so **2**H~3~PO~4~.

**Step 3: water.** 2 H~3~PO~4~ give 6 H^+^ and 3 Ba(OH)~2~ give 6 OH^−^, so **6**H~2~O. Check H: 6 + 6 = 12 = 6 × 2.

2H~3~PO~4~ + 3Ba(OH)~2~ → Ba~3~(PO~4~)~2~ + 6H~2~O. Sum: 2 + 3 + 1 + 6 = **12**."""))

Q.append(q_pair("Mixing with no reaction", "Ch 7 sl. 14",
                [(("K", "NO3"), ("Mg", "SO4")), (("Ag", "NO3"), ("Na", "PO4")), (("Pb", "NO3"), ("K", "Cl")),
                 (("Cu", "Cl"), ("Na", "S")), (("Ca", "Cl"), ("K", "CO3"))], False, PRED, HW15))

Q.append(dict(
    ch=7, kind="concept", title="Net ionic equation for an acid–base reaction", short="Ch 7 sl. 23–26",
    stem="Nitric acid reacts with potassium hydroxide: [[HNO3]](aq) + KOH(aq) → [[KNO3]](aq) + [[H2O]](l). "
         "What is the **net ionic** equation?",
    correct=T("H^+^(aq) + [[OH^-^]](aq) → [[H2O]](l)"),
    wrong=[T("K^+^(aq) + [[NO3^-^]](aq) → [[KNO3]](s)", "KNO~3~ is soluble (rules 1 and 2); K^+^ and NO~3~^−^ are spectators."),
           T("[[HNO3]](aq) + [[OH^-^]](aq) → [[NO3^-^]](aq) + [[H2O]](l)",
             "HNO~3~ is a strong acid: it completely dissociates (slide 24), so it is written as H^+^ and NO~3~^−^, and "
             "NO~3~^−^ then cancels."),
           T("H^+^(aq) + [[NO3^-^]](aq) + K^+^(aq) + [[OH^-^]](aq) → K^+^(aq) + [[NO3^-^]](aq) + [[H2O]](l)",
             "That's the **complete** ionic equation. Cancel the spectators K^+^ and NO~3~^−^."),
           T("[[HNO3]](aq) + KOH(aq) → [[KNO3]](aq) + [[H2O]](l)", "That's the **molecular** equation.")],
    cite=f"{C7}, slide 23 (HNO~3~ + KOH: the net ionic equation shows water forming), slide 25 (principle 4), slide 26",
    hw="HW16 — hw16ex1.png (the same net ionic process for any strong acid and strong base)",
    covers="Acid–base net ionic equation: H^+^ + OH^−^ → H~2~O, with the salt's ions as spectators.",
    sol="""**Step 1: write the strong electrolytes as ions** (slides 24–25). HNO~3~ → H^+^ + NO~3~^−^; KOH → K^+^ + OH^−^;
KNO~3~ (soluble) → K^+^ + NO~3~^−^. Water stays H~2~O(l).

**Step 2: complete ionic.** H^+^(aq) + NO~3~^−^(aq) + K^+^(aq) + OH^−^(aq) → K^+^(aq) + NO~3~^−^(aq) + H~2~O(l)

**Step 3: cancel the spectators** K^+^ and NO~3~^−^ (unchanged on both sides).

**Net ionic:** **H^+^(aq) + OH^−^(aq) → H~2~O(l)**. Slide 23 uses this exact reaction: the net ionic equation shows water
being formed."""))

Q.append(dict(
    ch=7, kind="concept", title="The strong acids", short="Ch 7 sl. 21, 24",
    stem="Which list contains **only** the strong acids named in the course?",
    correct=T("HCl, [[HNO3]], [[H2SO4]]"),
    wrong=[T("HCl, HF, [[HNO3]]", "HF isn't on the course's strong-acid list (slide 24)."),
           T("[[HNO3]], [[HNO2]], [[H2SO4]]", "HNO~2~ (nitrous acid, 2 O) isn't on the list. Don't confuse it with HNO~3~."),
           T("HCl, [[H3PO4]], [[H2SO4]]", "H~3~PO~4~ isn't on the course's strong-acid list."),
           T("HCl, [[HNO3]], [[HC2H3O2]]", "Acetic acid, HC~2~H~3~O~2~, isn't on the course's strong-acid list.")],
    cite=f"{C7}, slide 21 (HCl, HNO~3~, H~2~SO~4~ are strong acids), slide 24 (principle 1)",
    hw="HW16 — hw16ex2.png (strong acid / strong base reactions)",
    covers="The course's strong-acid list: HCl, HNO~3~, H~2~SO~4~.",
    sol="Slide 24, principle 1: the common strong acids are aqueous solutions of **HCl, HNO~3~, and H~2~SO~4~** (also slide 21). "
        "Each other list swaps one of them for an acid that isn't on the course's list."))

Q.append(q_spect("Spectator ions", "Ch 7 sl. 17–18", ("Ni", "Cl"), ("K", "CO3"),
                 f"{C7}, slide 17 (spectator ions), slide 18, slide 14", "HW15 — hw15ex1.png (what a net ionic equation shows)"))

Q.append(dict(
    ch=7, kind="calc", numeric=True, title="Electrons transferred per atom", short="Ch 7 sl. 31, 33",
    stem="In the reaction 3Mg(s) + [[N2]](g) → [[Mg3N2]](s), how many electrons does **each magnesium atom** lose?",
    correct=(2, "2", ""),
    wrong=[(1, "1", "That would make Mg^+^. In Mg~3~N~2~ magnesium is Mg^2+^."),
           (3, "3", "That is what each **N** atom gains (N → N^3−^)."),
           (5, "5", "Nitrogen has 5 valence electrons; that isn't a count of electrons transferred."),
           (6, "6", "That is the total for one Mg~3~N~2~ formula unit (3 Mg × 2), not per Mg atom.")],
    cite=f"{C7}, slide 33 (Practice: electrons transferred from each Al atom in 2Al + N~2~), slide 31",
    hw="HW16 — hw16ex3.png (Ba + Cl~2~: electrons lost and gained)",
    covers="Electrons lost per metal atom = the cation's charge.",
    sol="""**Step 1: ions.** Mg~3~N~2~ is ionic: Mg^2+^ and N^3−^. Check: 3(+2) + 2(−3) = 0.

**Step 2:** each Mg goes 0 → +2, so it **loses 2 electrons**.

**Check:** 3 Mg × 2 = 6 lost; 2 N × 3 = 6 gained."""))

Q.append(dict(
    ch=7, kind="concept", title="Classifying a metal + salt reaction", short="Ch 7 sl. 34, 40",
    stem="The reaction Fe(s) + [[CuSO4]](aq) → [[FeSO4]](aq) + Cu(s) is best classified as:",
    correct=T("oxidation–reduction and single-replacement"),
    wrong=[T("precipitation and double-displacement", "Cu(s) is an element, not a precipitate of two ions, and only one anion moves."),
           T("acid–base", "No acid, base, or water."),
           T("decomposition", "Two reactants exchange; nothing breaks apart."),
           T("combustion", "No O~2~ and no flame.")],
    cite=f"{C7}, slide 40 (Single-Replacement: one anion moves; also redox), slide 34 (Cu + FeCl~2~)",
    hw="HW17 — hw17ex1.png (classify: precipitation, acid–base, oxidation–reduction)",
    covers="Metal + ionic compound: single replacement, always redox.",
    sol="""* **Single replacement:** one anion (SO~4~^2−^) moves from Cu^2+^ to Fe^2+^ (the pattern of slide 40).
* **Oxidation–reduction:** Fe goes 0 → +2 (loses 2 e^−^) and Cu goes +2 → 0 (gains 2 e^−^), like slide 34 in reverse."""))

Q.append(dict(
    ch=7, kind="concept", title="A reaction in several classes", short="Ch 7 sl. 41–42",
    stem="A magnesium ribbon burns in air with a bright flame: 2Mg(s) + [[O2]](g) → 2MgO(s). Which classes apply?",
    correct=T("synthesis, combustion, and oxidation–reduction"),
    wrong=[T("synthesis only", "It also burns in O~2~ with a flame (combustion), and a metal + nonmetal is always redox."),
           T("decomposition and oxidation–reduction", "Two elements combine; nothing breaks apart."),
           T("combustion only", "One compound forms from two elements (synthesis), and it's also redox."),
           T("precipitation", "No solutions are mixed; MgO forms directly from the elements.")],
    cite=f"{C7}, slides 41–42 (combustion; synthesis), slide 31 (metal + nonmetal is redox)",
    hw="HW17 — hw17ex2.png (definition of combustion: reacts with oxygen, flame, heat energy)",
    covers="One reaction can belong to several classes.",
    sol="""* **Synthesis:** one compound (MgO) from simpler materials (Mg and O~2~) (slide 42).
* **Combustion:** reacts with oxygen and releases energy fast enough to give a flame (slide 41).
* **Oxidation–reduction:** metal + nonmetal (slide 31); each Mg loses 2 e^−^ and each O gains 2 e^−^."""))

# ================================================================ Chapter 8 (13)
fe_atom = mm("Fe") * 1.66e-24
check(14, fe_atom, 9.27e-23, 0.005e-23)
Q.append(nq(8, "Mass of one atom", "Ch 8 sl. 5",
            "Using 1 amu = 1.66 × 10^−24^ g, what is the mass in grams of **one** iron atom (average atomic mass 55.85 amu)?",
            fe_atom, [(1.66e-24, "That is the mass of 1 amu, not 55.85 amu."),
                      (fe_atom * 10, "Decimal slip: check the exponent."),
                      (55.85, "That is the mass of one **mole** of Fe atoms."),
                      (55.85 / 1.66e-24, "Divided by 1.66 × 10^−24^ instead of multiplying.")],
            f"{C8}, slide 5 (Atomic Mass Units: 1 amu = 1.66 × 10^−24^ g; Table 8.1)", "HW18 — average atomic masses",
            "Average atomic mass is the mass of **one** atom in amu; convert to grams with 1 amu = 1.66 × 10^−24^ g.",
            "The average atomic mass of Fe, 55.85 amu, is the mass of **one** Fe atom (study guide 8.1). Convert amu to grams:\n\n"
            + EQ("55.85", "amu", [F("1.66\\times10^{-24}", "g", 1, "amu", "definition of the amu (slide 5)")],
                 "9.27\\times10^{-23}", "g", final=True),
            unit=" g", fmt=lambda v: "55.85" if v == 55.85 else sci(v)))

Q.append(dict(
    ch=8, kind="concept", title="Same number of atoms", short="Ch 8 sl. 6, 9",
    stem="Which sample contains the **same number of atoms** as 32.07 g of sulfur?",
    correct=T("26.98 g of aluminum"),
    wrong=[T("32.07 g of aluminum", "Same mass isn't the same number of atoms; Al atoms are lighter than S atoms."),
           T("16.04 g of sulfur", "That is half a mole of S, so half as many atoms."),
           T("1.00 g of hydrogen atoms (H)", "1.00 g H is 0.992 mol, slightly less than 1 mol."),
           T("6.022 g of carbon", "Avogadro's **number** isn't a mass. 6.022 g C is only 0.501 mol.")],
    cite=f"{C8}, slide 6 (same mass ratio as atomic masses gives the same number of atoms), slide 9 (Table 8.2: 1-mole samples)",
    hw="HW18 — comparing samples (which contains more atoms?)",
    covers="1 mole of any element = its atomic mass in grams = 6.022 × 10^23^ atoms.",
    sol="32.07 g S is exactly **1 mol** of S (atomic mass 32.07), which is 6.022 × 10^23^ atoms. Any element's atomic mass in grams "
        "is also 1 mol (Table 8.2, slide 9), so **26.98 g Al = 1 mol Al** has the same number of atoms. Slide 6 makes the same "
        "point with 26.98 g Al and 63.55 g Cu."))

mg_mol = 12.5 / mm("Mg")
check(16, mg_mol, 0.514, 0.0005)
Q.append(nq(8, "Grams to moles", "Ch 8 sl. 11–12", "How many moles of magnesium are in 12.5 g of Mg?",
            mg_mol, [(mg_mol / 10, "Decimal slip (off by 10)."),
                     (mm("Mg") / 12.5, "Inverted: 24.31 ÷ 12.5."),
                     (12.5 * mm("Mg"), "Multiplied by the molar mass instead of dividing."),
                     (mg_mol * NA, "That is the number of **atoms**, not moles.")],
            f"{C8}, slides 11–12 (Mole Conversion Practice: 3.60 g Al, 544 g Ca)", "HW18 — hw18ex1.png (moles from grams)",
            "Grams → moles: multiply by (1 mol / atomic mass in g).",
            "Atomic mass of Mg = 24.31, so 1 mol Mg = 24.31 g. You have grams, so grams goes on the bottom:\n\n"
            + EQ("12.5", "g Mg", [F(1, "mol Mg", "24.31", "g Mg", "atomic mass of Mg")], "0.514", "mol Mg", final=True),
            unit=" mol", fmt=lambda v: sci(v) if v > 1e6 else sig(v)))

zn_atoms = 0.250 * NA
check(17, zn_atoms, 1.51e23, 0.006e23)
Q.append(nq(8, "Moles to atoms", "Ch 8 sl. 13–14", "How many zinc atoms are in 0.250 mol of Zn?",
            zn_atoms, [(0.250 / NA, "Divided by Avogadro's number instead of multiplying."),
                       (0.250 * mm("Zn"), "That is the mass in **grams** (0.250 × 65.38)."),
                       (zn_atoms / 10, "Exponent slip."),
                       (0.250 * mm("Zn") * NA, "Multiplied by the molar mass too; moles → atoms needs only Avogadro's number.")],
            f"{C8}, slides 13–14 (Atom Conversion Practice: 0.133 mol Al, 13.6 mol Ca)", "HW18 — hw18ex3.png (atoms from moles)",
            "Moles → atoms: multiply by 6.022 × 10^23^. The molar mass isn't needed.",
            EQ("0.250", "mol Zn", [F("6.022\\times10^{23}", "Zn atoms", 1, "mol Zn", "Avogadro's number")],
               "1.51\\times10^{23}", "Zn atoms", final=True),
            unit=" atoms", fmt=lambda v: sci(v) if (v > 1e6 or v < 1e-3) else sig(v)))

ag_mol = 3.01e23 / NA
ag_g = ag_mol * mm("Ag")
check(18, ag_g, 53.9, 0.05)
Q.append(nq(8, "Atoms to grams", "Ch 8 sl. 15", "What is the mass of 3.01 × 10^23^ silver atoms?",
            ag_g, [(ag_mol, "That is the number of **moles**; one more step (× molar mass) is needed."),
                   (ag_mol / mm("Ag"), "Divided by the molar mass instead of multiplying."),
                   (mm("Ag") / ag_mol, "Inverted the last factor: 107.87 ÷ 0.500."),
                   (3.01e23 * mm("Ag"), "Never divided by Avogadro's number.")],
            f"{C8}, slide 15 (Convert atoms to grams: 2.31 × 10^22^ atoms of gold)",
            "HW18 — atoms → grams setup ((1 mol / 6.022 × 10^23^ atoms)(g / 1 mol))",
            "Atoms → moles (÷ N~A~) → grams (× molar mass).",
            "**Step 1: atoms to moles** (Avogadro's number flipped, atoms on the bottom):\n\n"
            + EQ("3.01\\times10^{23}", "Ag atoms", [F(1, "mol Ag", "6.022\\times10^{23}", "Ag atoms", "Avogadro's number, flipped")],
                 sig(ag_mol, 4), "mol Ag")
            + "\n\n**Step 2: moles to grams** (atomic mass of Ag = 107.87):\n\n"
            + EQ(sig(ag_mol, 4), "mol Ag", [F("107.87", "g Ag", 1, "mol Ag", "atomic mass of Ag")], "53.9", "g Ag", final=True),
            unit=" g", fmt=lambda v: sci(v) if (v > 1e6 or v < 1e-2) else sig(v)))

al2so43 = mm("Al2(SO4)3")
check(19, al2so43, 342.2, 0.05)
Q.append(nq(8, "Molar mass with parentheses", "Ch 8 sl. 22–26", "What is the molar mass of aluminum sulfate, [[Al2(SO4)3]]?",
            al2so43, [(mm("AlSO4"), "Ignored every subscript outside the parentheses."),
                      (mm("Al2SO4"), "Dropped the 3 outside the parentheses."),
                      (mm("Al2S3O4"), "Applied the 3 to S but not to O."),
                      (mm("Al(SO4)3"), "Dropped the 2 on Al.")],
            f"{C8}, slide 26 (LA problem: Ba(OH)~2~, a subscript outside parentheses), slides 22–25", "HW19 — hw19ex1.png (formula and molar mass)",
            "Counting atoms when a subscript multiplies a polyatomic ion.",
            """**Step 1: count atoms.** Al 2; the 3 outside (SO~4~) multiplies everything inside: S 1 × 3 = 3, O 4 × 3 = 12.

**Step 2: (count × atomic mass), added:** 2(26.98) + 3(32.07) + 12(16.00) = 53.96 + 96.21 + 192.00 = **342.17 ≈ 342.2 g/mol**.""",
            unit=" g/mol", fmt=lambda v: f"{v:.1f}"))

gluc_g = 0.420 * mm("C6H12O6")
check(20, gluc_g, 75.7, 0.05)
Q.append(nq(8, "Moles to grams", "Ch 8 sl. 25, 27", "What is the mass of 0.420 mol of glucose, [[C6H12O6]]?",
            gluc_g, [(0.420 / mm("C6H12O6"), "Divided by the molar mass instead of multiplying."),
                     (0.420 * mm("CH2O"), "Used the empirical formula CH~2~O (30.03 g/mol) instead of C~6~H~12~O~6~."),
                     (mm("C6H12O6") / 0.420, "Divided the molar mass by the moles."),
                     (0.420 * NA, "That is the number of molecules.")],
            f"{C8}, slide 27 (Calculating Mass from Moles: 7.89 mol NaOH), slide 25 (molar mass of C~6~H~12~O~6~)",
            "HW18 — hw18ex2.png (mass in grams from moles)", "Moles → grams: multiply by the molar mass.",
            "**Step 1: molar mass** (slide 25): 6(12.01) + 12(1.008) + 6(16.00) = 180.16 g/mol.\n\n"
            "**Step 2: moles to grams** (grams on top):\n\n"
            + EQ("0.420", "mol C6H12O6", [F("180.16", "g C6H12O6", 1, "mol C6H12O6", "molar mass of C6H12O6")],
                 "75.7", "g C6H12O6", final=True),
            unit=" g", fmt=lambda v: sci(v) if (v > 1e6 or v < 1e-2) else sig(v)))

h2o_mol = 9.00 / mm("H2O")
h2o_molec = h2o_mol * NA
check(21, h2o_molec, 3.01e23, 0.006e23)
Q.append(nq(8, "Grams to molecules", "Ch 8 sl. 10–15, 28", "How many water molecules are in 9.00 g of [[H2O]]?",
            h2o_molec, [(h2o_mol, "That is the number of **moles**. Multiply by Avogadro's number."),
                        (h2o_molec / 10, "Exponent slip."),
                        (h2o_molec * 3, "That counts **atoms** (3 per molecule), not molecules."),
                        (9.00 * NA, "Skipped grams → moles: multiplied the grams by Avogadro's number.")],
            f"{C8}, slide 28 (grams → moles), slides 13–14 (moles → particles)", "HW19 — number of molecules from a mass",
            "Grams → moles → molecules; moles are always the middle step.",
            "**Step 1: molar mass of H~2~O** = 2(1.008) + 16.00 = 18.02 g/mol.\n\n**Step 2: grams to moles.**\n\n"
            + EQ("9.00", "g H2O", [F(1, "mol H2O", "18.02", "g H2O", "molar mass of H2O")], sig(h2o_mol, 4), "mol H2O")
            + "\n\n**Step 3: moles to molecules.**\n\n"
            + EQ(sig(h2o_mol, 4), "mol H2O", [F("6.022\\times10^{23}", "molecules", 1, "mol H2O", "Avogadro's number")],
                 "3.01\\times10^{23}", "molecules", final=True),
            unit=" molecules", fmt=lambda v: sci(v) if (v > 1e6 or v < 1e-2) else sig(v)))

pct_o = 6 * 16.00 / mm("Ca(NO3)2") * 100
check(22, pct_o, 58.50, 0.005)
Q.append(nq(8, "Mass percent", "Ch 8 sl. 30–33", "What is the mass percent of **oxygen** in calcium nitrate, [[Ca(NO3)2]]?",
            pct_o, [(16.00 / mm("Ca(NO3)2") * 100, "Counted only one O atom. There are 6."),
                    (2 * 14.01 / mm("Ca(NO3)2") * 100, "That is the percent of **N**."),
                    (40.08 / mm("Ca(NO3)2") * 100, "That is the percent of **Ca**."),
                    (3 * 16.00 / mm("Ca(NO3)2") * 100, "Counted 3 O (one nitrate). The subscript 2 doubles it to 6.")],
            f"{C8}, slide 30 (Mass Percent), slides 31–33 (ethanol, H~3~PO~4~, Mg(IO~2~)~2~)",
            "HW20 — hw20ex2.png (percent by mass of an element)",
            "Mass percent: (atoms of the element × atomic mass) ÷ molar mass × 100, counting through parentheses.",
            """**Step 1: count atoms.** Ca 1, N 1 × 2 = 2, O 3 × 2 = **6**.

**Step 2: molar mass.** 40.08 + 2(14.01) + 6(16.00) = 164.10 g/mol.

**Step 3: mass percent.**
$$\\%\\,\\text{O}=\\frac{6(16.00)\\ \\text{g O}}{164.10\\ \\text{g Ca(NO}_3)_2}\\times100\\%=\\frac{96.00}{164.10}\\times100\\% = \\boxed{58.50\\%}$$""",
            unit="%", fmt=lambda v: f"{v:.2f}"))

Q.append(dict(
    ch=8, kind="concept", title="Molecular to empirical formula", short="Ch 8 sl. 39–40",
    stem="Styrene has the molecular formula [[C8H8]]. What is its empirical formula?",
    correct=T("CH"),
    wrong=[T("[[C8H8]]", "8 and 8 share a factor of 8, so it isn't the smallest ratio."),
           T("[[C4H4]]", "Divided by 2, but 4 and 4 can still be divided. Use the **largest** common divisor, 8."),
           T("[[C2H2]]", "Divided by 4; it can still be reduced to CH."),
           T("[[CH2]]", "C and H are equal (8 : 8), so the ratio is 1 : 1.")],
    cite=f"{C8}, slide 39 (empirical formula = smallest whole-number ratio), slide 40",
    hw="HW21 — hw21ex3.png (CH with molar mass ≈ 26 is C~2~H~2~)",
    covers="Type A (study guide 8.7): divide every subscript by the largest common divisor.",
    sol="Subscripts: C 8, H 8. The largest number dividing both is **8**: 8 ÷ 8 = 1 and 8 ÷ 8 = 1. Empirical formula: **CH** "
        "(the same as benzene and acetylene; slide 39's point that different compounds can share an empirical formula)."))

q, r = q_empirical("Percent composition to empirical formula", "Ch 8 sl. 42–43",
                   "A chromium oxide is 68.42% Cr and 31.58% O by mass. What is its empirical formula?",
                   ["Cr", "O"], [68.42, 31.58], "percent",
                   f"{C8}, slides 42–43 (Steps for Determining the Empirical Formula; step 4)",
                   "HW21 — hw21ex2.png (empirical formula from percent composition)")
assert r["formula"] == "Cr2O3"
Q.append(q)

Q.append(q_molecular("Empirical to molecular formula", "Ch 8 sl. 47–49",
                     "A compound has the empirical formula [[C2H4O]] and a molar mass of 88.11 g/mol. What is its molecular formula?",
                     "C2H4O", 88.11, f"{C8}, slide 48 ((empirical formula)~n~), slide 49 (LA Practice), slide 47",
                     "HW21 — hw21ex3.png (C~3~H~7~NO, molar mass 145–150 → C~6~H~14~N~2~O~2~)"))

Q.append(dict(
    ch=8, kind="concept", title="Why the molecular formula", short="Ch 8 sl. 39, 50",
    stem="Why is the **molecular** formula of a compound more informative than its empirical formula?",
    correct=T("It gives the actual number of each kind of atom in one molecule"),
    wrong=[T("It always has smaller subscripts", "The molecular formula has subscripts equal to or **larger** than the empirical formula's."),
           T("It can be found from percent composition alone", "Percent composition gives only the empirical formula; you also need the molar mass (slide 47)."),
           T("It shows the mass percent of each element", "Both formulas give the same mass percents."),
           T("It is always different from the empirical formula", "They can be the same (n = 1), as for H~2~O.")],
    cite=f"{C8}, slide 50 (why the molecular formula is more useful), slide 39, slide 47",
    hw="HW21 — hw21ex1.png (what evidence is needed for empirical vs molecular formulas)",
    covers="Empirical = ratio only; molecular = actual atom counts.",
    sol="The empirical formula gives only the **smallest whole-number ratio** of atoms; many compounds share one (C~2~H~2~ and "
        "C~6~H~6~ are both CH). The molecular formula gives the **actual number of atoms** in one molecule (slide 50). Getting it "
        "needs the molar mass as well as the composition (slide 47)."))

# ================================================================ Chapter 9 (9)
Q.append(dict(
    ch=9, kind="concept", title="What a balanced equation conserves", short="Ch 9 sl. 2–4, 16",
    stem="In a correctly balanced chemical equation, which quantity is always the **same** on both sides?",
    correct=T("The number of atoms of each element"),
    wrong=[T("The number of molecules", "2H~2~ + O~2~ → 2H~2~O has 3 molecules on the left and 2 on the right."),
           T("The number of moles of substances", "Moles of molecules can change (3 mol → 2 mol in the same example)."),
           T("The sum of the coefficients", "The coefficient sums usually differ (3 vs 2 above)."),
           T("The number of different compounds", "Reactions change which compounds are present.")],
    cite=f"{C9}, slide 2 (balanced equation: identities and amounts), slides 3–4, slide 16 (why balance first)",
    hw="HW22 — hw22ex1.png (balancing with whole-number coefficients)",
    covers="Balancing conserves atoms (and total mass), not molecules or moles.",
    sol="Balancing makes the **number of atoms of each element** equal on both sides, because atoms are only rearranged. Molecules "
        "and moles of molecules can change: 2H~2~ + O~2~ → 2H~2~O turns 3 molecules into 2, yet has 4 H and 2 O on each side."))

Q.append(dict(
    ch=9, kind="concept", title="Choosing the mole ratio", short="Ch 9 sl. 5–9",
    stem="For 2[[C2H6]](g) + 7[[O2]](g) → 4[[CO2]](g) + 6[[H2O]](g), which conversion factor converts **moles of [[O2]]** into "
         "**moles of [[H2O]]**?",
    correct=T(r"$\rule[-2.2ex]{0pt}{5.8ex}\dfrac{6\ \text{mol H}_2\text{O}}{7\ \text{mol O}_2}$"),
    wrong=[T(r"$\rule[-2.2ex]{0pt}{5.8ex}\dfrac{7\ \text{mol O}_2}{6\ \text{mol H}_2\text{O}}$", "Upside down: the unit you have (mol O~2~) goes on the bottom."),
           T(r"$\rule[-2.2ex]{0pt}{5.8ex}\dfrac{6\ \text{mol H}_2\text{O}}{2\ \text{mol C}_2\text{H}_6}$", "That starts from C~2~H~6~, not O~2~."),
           T(r"$\rule[-2.2ex]{0pt}{5.8ex}\dfrac{4\ \text{mol CO}_2}{7\ \text{mol O}_2}$", "That gives moles of CO~2~, not H~2~O."),
           T(r"$\rule[-2.2ex]{0pt}{5.8ex}\dfrac{18.02\ \text{g H}_2\text{O}}{1\ \text{mol H}_2\text{O}}$", "That's a molar mass (moles ↔ grams of the same substance).")],
    cite=f"{C9}, slides 5–8 (mole ratios from coefficients), slide 9 (ethane combustion), slide 11",
    hw="HW22 — hw22ex2.png (choose the mole ratio)",
    covers="Mole ratio from two coefficients, oriented want-over-have.",
    sol="Have O~2~ (coefficient **7**), want H~2~O (coefficient **6**). So 7 mol O~2~ produce 6 mol H~2~O, and with the wanted unit "
        "on top: **6 mol H~2~O / 7 mol O~2~**."))

q, res = q_mass("Mole–mole conversion", "Ch 9 sl. 10–11",
                "For 4Al(s) + 3[[O2]](g) → 2[[Al2O3]](s), how many moles of [[Al2O3]] form from 1.80 mol of Al?",
                "Al", 4, "Al2O3", 2, 1.80, "mol", "mol", f"{C9}, slides 10–11 (Mole–Mole Conversions)",
                "HW22 — hw22ex3.png (moles of product from moles of reactant)", others=[("O2", 3)])
check(29, res, 0.900, 0.0005)
Q.append(q)

Q.append(dict(
    ch=9, kind="concept", title="Actual yield", short="Ch 9 sl. 28, 30",
    stem="In a percent-yield calculation, which quantity is found by **measuring** the product in the lab?",
    correct=T("The actual yield"),
    wrong=[T("The theoretical yield", "The theoretical yield is **calculated** from the limiting reactant (slide 25)."),
           T("The mole ratio", "Mole ratios come from the balanced equation's coefficients."),
           T("The molar mass of the product", "Molar masses come from the periodic table."),
           T("The limiting reactant", "The limiting reactant is identified by calculation (need vs have).")],
    cite=f"{C9}, slide 28 (Actual Yield: the amount actually produced), slide 30 (percent yield), slide 25",
    hw="HW24 — hw24ex1.png (theoretical yield calculated; actual yield weighed)",
    covers="Actual (measured) vs theoretical (calculated) yield.",
    sol="The **actual yield** is the amount of product **actually produced and measured** (slide 28). The theoretical yield is "
        "**calculated** from the limiting reactant (slide 25). Percent yield = actual ÷ theoretical × 100% (slide 30)."))

q, res = q_mass("Grams to grams", "Ch 9 sl. 14, 19–20",
                "Hydrazine burns: [[N2H4]](l) + [[O2]](g) → [[N2]](g) + 2[[H2O]](g). What mass of [[H2O]] forms from 8.00 g of "
                "[[N2H4]] with excess [[O2]]?",
                "N2H4", 1, "H2O", 2, 8.00, "g", "g", f"{C9}, slides 19–20 (Stoichiometry Practice), slide 14 (steps)",
                "HW23 — hw23ex1.png (grams of product from grams of reactant)", others=[("N2", 1)])
check(31, res, 8.99, 0.005)
Q.append(q)

q, (L, left) = q_limit("Limiting reactant and leftover", "Ch 9 sl. 21–24",
                       "For 2Fe(s) + 3[[Cl2]](g) → 2[[FeCl3]](s), 10.0 g of Fe reacts with 10.0 g of [[Cl2]]. Which statement is correct?",
                       "Fe", 2, 10.0, "Cl2", 3, 10.0, f"{C9}, slide 24 (limiting reactant from two masses), slides 21–23",
                       "HW23 — hw23ex2.png (equal masses of each reactant: which is limiting?)")
assert L == "Cl2"
Q.append(q)

q, (L, res) = q_yield("Theoretical yield with a limiting reactant", "Ch 9 sl. 24–27",
                      "For 2[[H2]](g) + [[O2]](g) → 2[[H2O]](l), 4.00 g of [[H2]] reacts with 16.0 g of [[O2]]. What is the theoretical "
                      "yield of [[H2O]]?",
                      "H2", 2, 4.00, "O2", 1, 16.0, "H2O", 2,
                      f"{C9}, slide 27 (theoretical yield with two masses), slide 25, slide 24",
                      "HW24 — hw24ex2.png (theoretical yield of XeF~4~ from two masses)")
assert L == "O2"
check(33, res, 18.0, 0.05)
Q.append(q)

q, res = q_percent("Percent yield", "Ch 9 sl. 28–32",
                   "For 2[[SO2]](g) + [[O2]](g) → 2[[SO3]](g), 48.0 g of [[SO2]] reacts with excess [[O2]] and 52.5 g of [[SO3]] is "
                   "collected. What is the percent yield?",
                   "SO2", 2, 48.0, "SO3", 2, 52.5, f"{C9}, slide 30 (percent yield formula), slides 31–32, slide 28",
                   "HW24 — hw24ex1.png (percent yield)",
                   excess_note="[[O2]] is in excess, so **[[SO2]] is limiting** and the theoretical yield comes from it.")
check(34, res, 87.5, 0.05)
Q.append(q)

Q.append(dict(
    ch=9, kind="concept", title="The limiting reactant", short="Ch 9 sl. 21, 25",
    stem="Which statement about the **limiting reactant** is correct?",
    correct=T("It is completely used up, and the theoretical yield is calculated from it"),
    wrong=[T("It is always the reactant with the smaller mass", "Mass doesn't decide it; compare moles through the mole ratio."),
           T("It is the reactant left over when the reaction stops", "That is the **excess** reactant."),
           T("It is always the reactant with the smaller coefficient", "Coefficients alone don't decide it; the amounts present matter too."),
           T("Its amount has no effect on how much product forms", "It's exactly what limits how much product forms.")],
    cite=f"{C9}, slide 21 (Limiting Reactants: runs out first), slide 25 (theoretical yield from the limiting reactant)",
    hw="HW23 — hw23ex2.png (limiting reactant)",
    covers="Role of the limiting reactant.",
    sol="The limiting reactant **runs out first** and so **limits the amount of product** (slide 21). The theoretical yield is "
        "the amount of product **calculated from the limiting reactant** (slide 25). The other reactant is in excess, and some "
        "of it is left over."))

if __name__ == "__main__":
    assert len(Q) == 35, len(Q)
    kinds = Counter(q["kind"] for q in Q)
    chs = Counter(q["ch"] for q in Q)
    assert chs == {7: 13, 8: 13, 9: 9}, chs
    assert kinds == {"concept": 18, "calc": 17}, kinds
    build(3, Q, seed=33)
    dist = Counter(q["ans"] for q in Q)
    assert all(dist[L] == 7 for L in "abcde"), dist
