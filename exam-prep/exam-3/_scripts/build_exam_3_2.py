"""Build practice-exam-3-2 and its key, checking every numeric answer.

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_exam_3_2.py
Same topic blueprint as 3-1 (Ch 7: 13, Ch 8: 13, Ch 9: 9) with new problems.
Choice tuples are (value, text, why-wrong); value is None for text choices.
"""
from examlib import NA, build, check, mm, sci

C7, C8, C9 = "Chapter 7 post", "Chapter 8 post", "Chapter 9 post"
Q = []


def T(text, why=""):
    return (None, text, why)


# ---------------------------------------------------------------- Chapter 7
Q.append(dict(
    ch=7, kind="concept", title="Driving force of a neutralization", short="Ch 7 sl. 3, 37",
    stem="The reaction HCl(aq) + KOH(aq) → [[H2O]](l) + KCl(aq) occurs mainly because of which driving force?",
    correct=T("Formation of water"),
    wrong=[T("Formation of a solid", "KCl is soluble (rules 2, 3). Nothing precipitates."),
           T("Formation of a gas", "No gas is produced."),
           T("Transfer of electrons", "No electrons move. H^+^ + OH^−^ → H~2~O is acid–base, not redox."),
           T("An increase in the number of ions in solution", "Not one of the four driving forces. Ions are actually used up.")],
    cite=f"{C7}, slide 3 (Driving Forces), slide 37 (Acid–Base Reactions: HCl + KOH)",
    hw="HW16 — hw16ex2.png (the same net ionic process, H^+^ + OH^−^ → H~2~O, for any strong acid/strong base)",
    covers="Matching each reaction type to its driving force (acid–base ↔ formation of water).",
    sol="""Slide 37 uses this exact reaction: "You can recognize this as an acid–base reaction because it involves an H^+^ ion that
ends up in the product water." Forming water is driving force #2 on slide 3.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Solubility rules: insoluble salt", short="Ch 7 sl. 11",
    stem="On the basis of the general solubility rules, which compound is **insoluble** in water?",
    correct=T("[[BaSO4]]"),
    wrong=[T("[[CaCl2]]", "Rule 3: most chlorides are soluble, and Ca isn't a chloride exception (only Ag, Pb, Hg~2~ are)."),
           T("[[K2CO3]]", "Rule 2 beats rule 6: K^+^ salts are soluble."),
           T("[[NH4NO3]]", "Rules 1 and 2: both ions make it soluble."),
           T("[[Na3PO4]]", "Rule 2 beats rule 6: Na^+^ salts are soluble.")],
    cite=f"{C7}, slide 11 (Solubility Rules, Table 7.1), rule 4",
    hw="HW14 — hw14ex2.png (choose the substance not likely to be soluble)",
    covers="The named sulfate exceptions (BaSO~4~, PbSO~4~, CaSO~4~), and rule 2 overriding rule 6.",
    sol="""Rule 4: most sulfates are soluble; **notable exceptions are BaSO~4~, PbSO~4~, and CaSO~4~.** Ca shows up as a
*sulfate* exception, not a chloride exception, so CaCl~2~ is soluble but CaSO~4~ is not.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Solubility rules: cation rule wins", short="Ch 7 sl. 11",
    stem="Which of the following compounds is expected to be **soluble** in water?",
    correct=T("[[K2S]]"),
    wrong=[T("[[PbSO4]]", "Rule 4 exception."),
           T("[[AgCl]]", "Rule 3 exception."),
           T("[[Fe(OH)3]]", "Rule 5: only NaOH and KOH are listed as soluble hydroxides."),
           T("[[Ca3(PO4)2]]", "Rule 6: phosphates are only slightly soluble, and Ca^2+^ isn't a rule-2 cation.")],
    cite=f"{C7}, slide 11 (Solubility Rules), rules 2 and 6",
    hw="HW14 — hw14ex3.png / hw14ex4.png (which rule explains solubility, e.g. K~3~PO~4~, ammonium sulfide)",
    covers="Rule 2 (Na^+^, K^+^, NH~4~^+^ salts soluble) overrides the 'slightly soluble' anion rule 6.",
    sol="""Sulfides are normally only slightly soluble (rule 6), but **most salts of K^+^ are soluble** (rule 2), and the cation
rule wins. K~2~S is soluble. Every other choice is either a named exception or falls under rule 5 or 6 with a non-rule-2 cation.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Predicting the precipitate", short="Ch 7 sl. 11, 14",
    stem="Aqueous solutions of lead(II) nitrate, [[Pb(NO3)2]], and sodium sulfate, [[Na2SO4]], are mixed. What is the precipitate?",
    correct=T("[[PbSO4]]"),
    wrong=[T("[[NaNO3]]", "Rules 1 and 2: soluble."),
           T("[[Pb(SO4)2]]", "Pb^2+^ and SO~4~^2−^ combine 1 : 1. This formula isn't neutral."),
           T("[[NaPb]]", "Two cations can't form a solid (slide 10)."),
           T("No precipitate forms", "PbSO~4~ is a rule-4 exception, so a solid does form.")],
    cite=f"{C7}, slide 14 (How to Predict Precipitates), slide 11 (rule 4 exception), slide 10",
    hw="HW15 — hw15ex4.png (molecular equations for precipitation reactions)",
    covers="Swapping anions, then checking both products against the rules, including the exception lists.",
    sol="""The ions present are Pb^2+^, NO~3~^−^, Na^+^, SO~4~^2−^. Swapping anions gives PbSO~4~ and NaNO~3~. NaNO~3~ is soluble.
PbSO~4~ is a rule-4 exception, so **PbSO~4~ precipitates**:

Pb(NO~3~)~2~(aq) + Na~2~SO~4~(aq) → PbSO~4~(s) + 2NaNO~3~(aq)""",
))

Q.append(dict(
    ch=7, kind="concept", title="Net ionic equation", short="Ch 7 sl. 17–18",
    stem="Which is the correct **net ionic equation** for the reaction of aqueous barium chloride with aqueous potassium sulfate?",
    correct=T("[[Ba^2+^]](aq) + [[SO4^2-^]](aq) → [[BaSO4]](s)"),
    wrong=[T("[[BaCl2]](aq) + [[K2SO4]](aq) → [[BaSO4]](s) + 2KCl(aq)", "Molecular equation."),
           T("[[Ba^2+^]](aq) + 2[[Cl^-^]](aq) + 2[[K^+^]](aq) + [[SO4^2-^]](aq) → [[BaSO4]](s) + 2[[K^+^]](aq) + 2[[Cl^-^]](aq)",
             "Complete ionic equation. It still has the spectators K^+^ and Cl^−^."),
           T("[[K^+^]](aq) + [[Cl^-^]](aq) → KCl(s)", "KCl is soluble, so these ions are spectators."),
           T("[[Ba^2+^]](aq) + [[SO4^2-^]](aq) → [[BaSO4]](aq)", "BaSO~4~ precipitates, so it must be (s).")],
    cite=f"{C7}, slides 15–18 (molecular / complete ionic / net ionic equations), slide 11 (rule 4)",
    hw="HW15 — hw15ex1.png (what a net ionic equation shows) and hw15ex2.png (write the net ionic equation)",
    covers="Writing the net ionic equation by cancelling spectator ions, with the precipitate written as (s).",
    sol="""Molecular: BaCl~2~(aq) + K~2~SO~4~(aq) → BaSO~4~(s) + 2KCl(aq). Write every soluble strong electrolyte as ions. K^+^ and Cl^−^
appear unchanged on both sides, so cancel them: **Ba^2+^(aq) + SO~4~^2−^(aq) → BaSO~4~(s)**.""",
))

Q.append(dict(
    ch=7, kind="calc", numeric=True, title="Balancing a neutralization", short="Ch 7 sl. 27",
    stem="When the equation below is balanced with the smallest whole-number coefficients, what is the **sum of all the coefficients**?\n\n"
         "\\_\\_ [[H2SO4]](aq) + \\_\\_ [[Al(OH)3]](s) → \\_\\_ [[Al2(SO4)3]](aq) + \\_\\_ [[H2O]](l)",
    correct=(12, "12", ""),
    wrong=[(4, "4", "Leaves every coefficient as 1 (unbalanced)."),
           (6, "6", "That is the coefficient of H~2~O alone."),
           (8, "8", "Balanced Al and SO~4~ but left H~2~O at 2."),
           (11, "11", "Gives H~2~SO~4~ a coefficient of 2 instead of 3.")],
    cite=f"{C7}, slide 27 (Practice: balancing H~3~PO~4~ + Ca(OH)~2~ → Ca~3~(PO~4~)~2~ + H~2~O)",
    hw="HW22 — balancing with the lowest whole-number coefficients (2Al + 3H~2~SO~4~ → Al~2~(SO~4~)~3~ + 3H~2~)",
    covers="Balancing an acid–base reaction: polyatomic ions first as units, then H and O, then add up the coefficients.",
    sol="""Balance Al: 2 Al(OH)~3~. Balance SO~4~ as a unit: 3 H~2~SO~4~. H^+^ from the acid = 6 and OH^−^ from the base = 6, so 6 H~2~O.

$$3\\,\\text{H}_2\\text{SO}_4 + 2\\,\\text{Al(OH)}_3 \\rightarrow \\text{Al}_2(\\text{SO}_4)_3 + 6\\,\\text{H}_2\\text{O}$$

Sum = 3 + 2 + 1 + 6 = **12**. Check O: 12 + 6 = 18 on the left, 12 + 6 = 18 on the right.""",
))
check(6, 3 + 2 + 1 + 6, 12, 0)

Q.append(dict(
    ch=7, kind="concept", title="Spectator ions", short="Ch 7 sl. 15–17",
    stem="In the reaction [[K2CrO4]](aq) + [[Ba(NO3)2]](aq) → [[BaCrO4]](s) + 2[[KNO3]](aq), the spectator ions are:",
    correct=T("[[K^+^]] and [[NO3^-^]]"),
    wrong=[T("[[Ba^2+^]] and [[CrO4^2-^]]", "These form the solid, so they are directly involved."),
           T("[[K^+^]] and [[Ba^2+^]]", "Ba^2+^ ends up in the precipitate."),
           T("[[NO3^-^]] and [[CrO4^2-^]]", "CrO~4~^2−^ ends up in the precipitate."),
           T("There are no spectator ions", "K^+^ and NO~3~^−^ are unchanged on both sides.")],
    cite=f"{C7}, slides 15–17 (molecular → complete ionic → net ionic for K~2~CrO~4~ + Ba(NO~3~)~2~)",
    hw="HW15 — hw15ex1.png (spectator ions are left out of the net ionic equation)",
    covers="Course definition: spectator ions do not participate directly in the reaction.",
    sol="""Complete ionic: 2K^+^ + CrO~4~^2−^ + Ba^2+^ + 2NO~3~^−^ → BaCrO~4~(s) + 2K^+^ + 2NO~3~^−^. The ions that appear unchanged on both
sides are **K^+^ and NO~3~^−^**. The net ionic equation on slide 17 is Ba^2+^ + CrO~4~^2−^ → BaCrO~4~(s).""",
))

Q.append(dict(
    ch=7, kind="concept", title="Products of strong acid + strong base", short="Ch 7 sl. 23, 26",
    stem="What are the products when aqueous nitric acid reacts with aqueous potassium hydroxide?",
    correct=T("[[KNO3]](aq) and [[H2O]](l)"),
    wrong=[T("[[KNO3]](s) and [[H2O]](l)", "KNO~3~ is soluble (rules 1, 2). The salt stays dissolved (slide 26, principle 5)."),
           T("[[KNO2]](aq) and [[H2O]](l)", "Nitric acid is HNO~3~, so the anion is NO~3~^−^, not NO~2~^−^."),
           T("[[KH]](aq) and [[NO3OH]](aq)", "The acid's H^+^ joins OH^−^ to make water. These formulas aren't real."),
           T("[[K2O]](s) and [[HNO3]](aq)", "Acid + base makes a salt + water.")],
    cite=f"{C7}, slide 23 (Acid–Base Reactions: HNO~3~ + KOH), slide 26 (principle 5: water + a dissolved salt)",
    hw="HW16 — hw16ex2.png (what salt forms: HI + NaOH → NaI, NaOH + HNO~3~ → NaNO~3~)",
    covers="Strong acid + strong base gives water + a salt (base cation + acid anion), and the salt stays dissolved.",
    sol="""HNO~3~(aq) + KOH(aq) → **KNO~3~(aq) + H~2~O(l)**. The salt takes K^+^ from the base and NO~3~^−^ from the acid. Slide 26, principle 5:
the other product "is always an ionic compound called a salt, which remains dissolved in the water." """,
))

Q.append(dict(
    ch=7, kind="concept", title="Identifying strong bases", short="Ch 7 sl. 25",
    stem="Which pair contains **only** the most common strong bases named in this course?",
    correct=T("[[NaOH]] and [[KOH]]"),
    wrong=[T("[[Mg(OH)2]] and [[Fe(OH)3]]", "Only slightly soluble hydroxides (rule 5), so they aren't strong bases."),
           T("[[Ca(OH)2]] and [[Al(OH)3]]", "Ca(OH)~2~ is only moderately soluble and Al(OH)~3~ is only slightly soluble."),
           T("[[HCl]] and [[NaOH]]", "HCl is a strong *acid*."),
           T("[[KOH]] and [[HNO3]]", "HNO~3~ is a strong *acid*.")],
    cite=f"{C7}, slide 25 (principle 3: 'The most common strong bases are NaOH and KOH'), slide 11 (rule 5)",
    hw="HW16 — hw16ex1.png (what is meant by a strong base)",
    covers="The course's strong-base list, and the link to solubility rule 5 (NaOH and KOH are the soluble hydroxides).",
    sol="""Slide 25: a strong base is a metal hydroxide that is very soluble in water, and "the most common strong bases are **NaOH and
KOH**." These are also the two hydroxides rule 5 names as soluble, which is no coincidence. A hydroxide that barely dissolves
can't release much OH^−^.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Ions in solution", short="Ch 7 sl. 6–7",
    stem="An aqueous solution of barium nitrate, [[Ba(NO3)2]](aq), contains:",
    correct=T("separated [[Ba^2+^]] and [[NO3^-^]] ions, two [[NO3^-^]] for every [[Ba^2+^]]"),
    wrong=[T("intact [[Ba(NO3)2]] units", "Slide 6: Ba(NO~3~)~2~(aq) does *not* contain Ba(NO~3~)~2~ units."),
           T("separated [[Ba^2+^]] and [[NO3^-^]] ions, one [[NO3^-^]] for every [[Ba^2+^]]", "Charge balance needs two NO~3~^−^ per Ba^2+^."),
           T("[[Ba^2+^]], [[N^3-^]], and [[O^2-^]] ions", "Polyatomic ions such as NO~3~^−^ stay together."),
           T("neutral Ba atoms and [[NO3]] molecules", "Dissolving an ionic solid releases ions, not neutral atoms. That's why the solution conducts.")],
    cite=f"{C7}, slide 6 (Ionic Compounds in Water: the Ba(NO~3~)~2~ example), slide 7 (Strong Electrolytes)",
    hw="HW15 — complete vs net ionic equations (strong electrolytes written as ions)",
    covers="Soluble ionic compounds are strong electrolytes that break into separated ions in the formula ratio.",
    sol="""Slide 6: "Ba(NO~3~)~2~(aq) does not contain Ba(NO~3~)~2~ units. Rather, it contains separated Ba^2+^ and NO~3~^−^ ions ...
two NO~3~^−^ ions for every Ba^2+^ ion." The ions are why the solution conducts electricity (slide 7).""",
))

Q.append(dict(
    ch=7, kind="calc", numeric=True, title="Electrons gained per molecule", short="Ch 7 sl. 31–33",
    stem="In the reaction 4Al(s) + 3[[O2]](g) → 2[[Al2O3]](s), how many electrons does **each [[O2]] molecule** gain?",
    correct=(4, "4", ""),
    wrong=[(1, "1", "Neither ion has a charge of 1."),
           (2, "2", "That is per O *atom* (O^2−^). Each O~2~ molecule has two O atoms."),
           (3, "3", "That is the electrons lost per Al atom (Al^3+^)."),
           (6, "6", "That is the total for one Al~2~O~3~ formula unit, not per O~2~.")],
    cite=f"{C7}, slide 31 (metal + nonmetal = redox), slide 33 (electrons per atom: 2Al + N~2~), slide 38 (2Li + F~2~)",
    hw="HW16 — hw16ex3.png (Ba + Cl~2~: Ba loses two electrons, Cl~2~ gains two)",
    covers="Electrons per species from the ion charges, counting per molecule versus per atom.",
    sol="""Al~2~O~3~ is ionic, made of Al^3+^ and O^2−^. Each O atom gains 2 e^−^, and an O~2~ molecule has 2 O atoms, so **each O~2~ gains 4 e^−^**.
Check the totals: 4 Al × 3 e^−^ lost = 12 lost, and 3 O~2~ × 4 e^−^ gained = 12 gained.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Classifying a carbonate + acid reaction", short="Ch 7 sl. 39",
    stem="The reaction 2HCl(aq) + [[Na2CO3]](aq) → [[CO2]](g) + [[H2O]](l) + 2NaCl(aq) is best classified as:",
    correct=T("gas evolution and acid–base"),
    wrong=[T("precipitation only", "No solid forms; NaCl is soluble."),
           T("oxidation–reduction and single-replacement", "No electrons are transferred; every ion keeps its charge."),
           T("combustion", "No O~2~ and no flame."),
           T("decomposition", "Two reactants combine. This isn't one compound breaking apart.")],
    cite=f"{C7}, slide 39 (Gas Evolution Reactions: the same equation, 'also an acid–base reaction'), slide 45",
    hw="HW17 — hw17ex1.png (classify each reaction as precipitation, acid–base, and/or oxidation–reduction)",
    covers="Gas evolution as a class, and a reaction belonging to two classes at once.",
    sol="""Slide 39 uses this exact equation: "In this reaction carbon dioxide gas is formed. This reaction is also an acid–base reaction."
The H^+^ from HCl ends up in H~2~O, and CO~2~(g) forms, so it is both **gas evolution and acid–base**.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Recognizing decomposition", short="Ch 7 sl. 43",
    stem="When heated, potassium chlorate reacts: 2[[KClO3]](s) → 2KCl(s) + 3[[O2]](g). This is best classified as a:",
    correct=T("decomposition reaction"),
    wrong=[T("synthesis reaction", "Synthesis makes one compound from simpler materials. This is the reverse."),
           T("combustion reaction", "O~2~ is a product here, not a reactant burning something."),
           T("double-displacement reaction", "There is only one reactant, so there are no anions to swap."),
           T("acid–base reaction", "No H^+^ or OH^−^ is involved.")],
    cite=f"{C7}, slide 43 (Decomposition: a compound broken into simpler substances, usually by heat or current), slide 42",
    hw="HW17 — decomposition reactions (ammonium nitrite → N~2~ + H~2~O; HBr → H~2~ + Br~2~)",
    covers="Decomposition: one compound breaks into simpler compounds or elements, usually by heating.",
    sol="""One compound, KClO~3~, breaks into simpler substances (KCl and O~2~) when heated. That matches slide 43's definition of
**decomposition** (compare 2HgO → 2Hg + O~2~ on the same slide). Ch 9 slide 32 uses this same reaction for percent yield.""",
))

# ---------------------------------------------------------------- Chapter 8
Q.append(dict(
    ch=8, kind="concept", title="Atomic mass units", short="Ch 8 sl. 5, 7",
    stem="The average mass of a single carbon atom is:",
    correct=T("12.01 amu"),
    wrong=[T("12.01 g", "12.01 g is the mass of one *mole* of C atoms."),
           T("6.022 × 10^23^ g", "That is Avogadro's *number*, not a mass."),
           T("1.66 × 10^−24^ amu", "1 amu = 1.66 × 10^−24^ **g**. The units are mixed up."),
           T("1 amu", "1 amu is about the mass of one H atom (1.008 amu).")],
    cite=f"{C8}, slide 5 (Atomic Mass Units, Table 8.1: C = 12.01 amu), slide 7 (The Mole: 12.01 g of C)",
    hw="HW18 — 'use the average atomic masses' conversions",
    covers="Average atomic mass in amu (one atom) versus molar mass in g (one mole).",
    sol="""Table 8.1 gives carbon's average atomic mass as **12.01 amu** for one atom. One *mole* of C atoms has a mass of 12.01 g
(slide 7). The same number, but different units and different amounts.""",
))

Q.append(dict(
    ch=8, kind="concept", title="Comparing numbers of atoms", short="Ch 8 sl. 6, 9",
    stem="Which 10.0 g sample contains the **greatest number of atoms**?",
    correct=T("boron (10.81 g/mol)"),
    wrong=[T("aluminum (26.98 g/mol)", "Heavier atoms, so fewer of them in 10.0 g."),
           T("iron (55.85 g/mol)", "Heavier atoms, so fewer of them."),
           T("xenon (131.3 g/mol)", "Heavier atoms, so fewer of them."),
           T("gold (196.97 g/mol)", "Heaviest atoms here, so the *fewest* atoms.")],
    cite=f"{C8}, slide 9 (Table 8.2: 1-mole samples of Al, Au, Fe, S, B, Xe), slide 6, slide 2 (counting by weighing)",
    hw="HW18 — comparing samples (which contains the greater number of atoms?)",
    covers="For equal masses, moles = mass / molar mass, so the lightest atoms give the most atoms.",
    sol="""Moles = 10.0 g ÷ molar mass, and atoms = moles × N~A~. The smallest molar mass gives the most moles and so the most atoms:
B: 10.0 / 10.81 = 0.925 mol, compared with Au: 10.0 / 196.97 = 0.0508 mol. **Boron** wins.""",
))

fe = 25.0 / mm("Fe")
check(16, fe, 0.448, 0.0005)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Grams to moles", short="Ch 8 sl. 11–12",
    stem="How many moles of iron are in 25.0 g of Fe?",
    correct=(0.448, "0.448 mol", ""),
    wrong=[(25.0 * mm("Fe"), f"{25.0 * mm('Fe'):.0f} mol", "Multiplied by the molar mass."),
           (mm("Fe") / 25.0, f"{mm('Fe') / 25.0:.2f} mol", "Inverted: 55.85 / 25.0."),
           (fe * NA, f"{sci(fe * NA)} mol", "That is the number of atoms."),
           (4.48, "4.48 mol", "Decimal slip (off by 10).")],
    cite=f"{C8}, slides 11–12 (Mole Conversion Practice: 3.60 g Al, 544 g Ca)",
    hw="HW18 — hw18ex1.png (moles of element from grams); 45.9 g Ge → mol",
    covers="Grams → moles: divide by the molar mass.",
    sol="""$$25.0\\ \\text{g Fe}\\times\\frac{1\\ \\text{mol}}{55.85\\ \\text{g}} = 0.448\\ \\text{mol Fe}$$""",
))

ca_atoms = 2.75 * NA
check(17, ca_atoms, 1.66e24, 0.006e24)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Moles to atoms", short="Ch 8 sl. 13–14",
    stem="How many atoms are in 2.75 mol of calcium?",
    correct=(ca_atoms, f"{sci(ca_atoms)} atoms", ""),
    wrong=[(2.75 / NA, f"{sci(2.75 / NA)} atoms", "Divided by Avogadro's number instead of multiplying."),
           (2.75 / mm("Ca") * NA, f"{sci(2.75 / mm('Ca') * NA)} atoms", "Treated 2.75 mol as 2.75 g and divided by the molar mass first."),
           (ca_atoms / 10, f"{sci(ca_atoms / 10)} atoms", "Exponent slip."),
           (2.75 * mm("Ca") * NA, f"{sci(2.75 * mm('Ca') * NA)} atoms", "Multiplied by the molar mass too. You don't need it for mol → atoms.")],
    cite=f"{C8}, slides 13–14 (Atom Conversion Practice: 0.133 mol Al, 13.6 mol Ca), slide 7",
    hw="HW18 — hw18ex3.png (number of atoms from 0.00580 mol Cu)",
    covers="Moles → atoms uses only Avogadro's number. The molar mass isn't needed.",
    sol="""$$2.75\\ \\text{mol}\\times\\frac{6.022\\times10^{23}\\ \\text{atoms}}{1\\ \\text{mol}} = 1.66\\times10^{24}\\ \\text{atoms Ca}$$""",
))

cu_mol = 5.00e21 / NA
cu_g = cu_mol * mm("Cu")
check(18, cu_g, 0.528, 0.0005)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Atoms to grams", short="Ch 8 sl. 15",
    stem="What is the mass of 5.00 × 10^21^ atoms of copper?",
    correct=(0.528, "0.528 g", ""),
    wrong=[(cu_mol / mm("Cu"), f"{sci(cu_mol / mm('Cu'))} g", "Divided by the molar mass instead of multiplying."),
           (cu_mol, f"{sci(cu_mol)} g", "Stopped at moles."),
           (mm("Cu") / cu_mol, f"{sci(mm('Cu') / cu_mol)} g", "Inverted: 63.55 / mol."),
           (5.00e21 * mm("Cu"), f"{sci(5.00e21 * mm('Cu'))} g", "Never divided by Avogadro's number.")],
    cite=f"{C8}, slide 15 (Convert atoms to grams: 2.31 × 10^22^ atoms of gold)",
    hw="HW18 — atoms → grams setup ((1 mol / 6.022 × 10^23^ atoms)(g / 1 mol))",
    covers="Atoms → moles (÷ N~A~) → grams (× molar mass).",
    sol="""$$5.00\\times10^{21}\\ \\text{atoms}\\times\\frac{1\\ \\text{mol}}{6.022\\times10^{23}} = 8.30\\times10^{-3}\\ \\text{mol};\\quad 8.30\\times10^{-3}\\times63.55 = 0.528\\ \\text{g Cu}$$""",
))

cap = mm("Ca3(PO4)2")
check(19, cap, 310.2, 0.05)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Molar mass with parentheses", short="Ch 8 sl. 22, 26",
    stem="What is the molar mass of calcium phosphate, [[Ca3(PO4)2]]?",
    correct=(310.2, "310.2 g/mol", ""),
    wrong=[(mm("CaPO4"), f"{mm('CaPO4'):.1f} g/mol", "Ignored every subscript outside the parentheses."),
           (mm("Ca3PO4"), f"{mm('Ca3PO4'):.1f} g/mol", "Dropped the 2 outside the parentheses."),
           (mm("Ca(PO4)2"), f"{mm('Ca(PO4)2'):.1f} g/mol", "Dropped the 3 on Ca."),
           (mm("Ca3P2O4"), f"{mm('Ca3P2O4'):.1f} g/mol", "Applied the 2 to P but not to O.")],
    cite=f"{C8}, slide 22 (Molar Mass), slide 26 (LA problem: Ba(OH)~2~, parentheses)",
    hw="HW19 — hw19ex1.png (formula and molar mass)",
    covers="Counting atoms when a subscript multiplies a polyatomic ion.",
    sol="""Atom count: 3 Ca, 2 P, 8 O.

$$3(40.08) + 2(30.97) + 8(16.00) = 120.24 + 61.94 + 128.00 = 310.18 \\approx 310.2\\ \\text{g/mol}$$""",
))

h2so4 = 0.350 * mm("H2SO4")
check(20, h2so4, 34.3, 0.05)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Moles to grams", short="Ch 8 sl. 24, 27",
    stem="What is the mass of 0.350 mol of sulfuric acid, [[H2SO4]]?",
    correct=(34.3, "34.3 g", ""),
    wrong=[(0.350 / mm("H2SO4"), f"{sci(0.350 / mm('H2SO4'))} g", "Divided by the molar mass."),
           (mm("H2SO4") / 0.350, f"{mm('H2SO4') / 0.350:.0f} g", "Divided the molar mass by the moles."),
           (0.350 * mm("S"), f"{0.350 * mm('S'):.1f} g", "Used only the mass of S."),
           (0.350 * mm("H2SO3"), f"{0.350 * mm('H2SO3'):.1f} g", "Wrong formula: H~2~SO~3~ (sulfurous acid) has 3 O.")],
    cite=f"{C8}, slide 24 (molar mass of H~2~SO~4~), slide 27 (Calculating Mass from Moles)",
    hw="HW18 — hw18ex2.png (mass in grams from moles)",
    covers="Moles → grams: multiply by the molar mass.",
    sol="""Molar mass H~2~SO~4~ = 2(1.008) + 32.07 + 4(16.00) = 98.09 g/mol.

$$0.350\\ \\text{mol}\\times98.09\\ \\tfrac{\\text{g}}{\\text{mol}} = 34.3\\ \\text{g}$$""",
))

no2 = 125e-3 / mm("NO2")
check(21, no2, 2.72e-3, 0.005e-3)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Milligrams to moles", short="Ch 8 sl. 28–29",
    stem="How many moles of nitrogen dioxide, [[NO2]], are in 125 mg of the gas?",
    correct=(no2, f"{sci(no2)} mol", ""),
    wrong=[(125 / mm("NO2"), f"{125 / mm('NO2'):.2f} mol", "Didn't convert mg to g."),
           (125e-3 / mm("NO"), f"{sci(125e-3 / mm('NO'))} mol", "Used the molar mass of NO (30.01) instead of NO~2~."),
           (125e-3 * mm("NO2"), f"{125e-3 * mm('NO2'):.2f} mol", "Multiplied by the molar mass."),
           (no2 * NA, f"{sci(no2 * NA)} mol", "That is the number of molecules.")],
    cite=f"{C8}, slide 29 (LA problem 1: 9.43 mg of calcium chloride), slide 28",
    hw="HW19 — hw19ex2.png (moles in 21.9 mg of nitrogen dioxide)",
    covers="Convert mg → g before dividing by the molar mass, and write the formula correctly from the name.",
    sol="""NO~2~: 14.01 + 2(16.00) = 46.01 g/mol. 125 mg = 0.125 g.

$$\\frac{0.125\\ \\text{g}}{46.01\\ \\text{g/mol}} = 2.72\\times10^{-3}\\ \\text{mol}$$""",
))

amsulf = mm("(NH4)2SO4")
pct_n = 2 * mm("N") / amsulf * 100
check(22, pct_n, 21.20, 0.005)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Mass percent", short="Ch 8 sl. 30–32",
    stem="What is the mass percent of nitrogen in ammonium sulfate, [[(NH4)2SO4]]?",
    correct=(21.20, "21.20%", ""),
    wrong=[(mm("N") / amsulf * 100, f"{mm('N') / amsulf * 100:.2f}%", "Counted only one N; the formula has 2."),
           (2 / 15 * 100, f"{2 / 15 * 100:.2f}%", "Atom fraction (2 N of 15 atoms), not mass."),
           (mm("S") / amsulf * 100, f"{mm('S') / amsulf * 100:.2f}%", "That is % S."),
           (64.00 / amsulf * 100, f"{64.00 / amsulf * 100:.2f}%", "That is % O.")],
    cite=f"{C8}, slide 30 (Mass Percent), slide 31 (ethanol example), slide 32 (H~3~PO~4~ practice)",
    hw="HW20 — hw20ex2.png (percent by mass of the first element listed, e.g. KNO~2~, theobromine)",
    covers="Mass percent with a subscript outside the parentheses (2 N atoms).",
    sol="""Molar mass: 2(14.01) + 8(1.008) + 32.07 + 4(16.00) = 132.15 g/mol. Mass of N in 1 mol = 2(14.01) = 28.02 g.

$$\\%\\text{N} = \\frac{28.02}{132.15}\\times100\\% = 21.20\\%$$""",
))

Q.append(dict(
    ch=8, kind="concept", title="Same empirical formula", short="Ch 8 sl. 39",
    stem="Which pair of compounds has the **same empirical formula**?",
    correct=T("[[C2H2]] and [[C6H6]]"),
    wrong=[T("CO and [[CO2]]", "Empirical formulas CO and CO~2~ differ."),
           T("[[H2O]] and [[H2O2]]", "Empirical formulas H~2~O and HO differ."),
           T("[[C2H4]] and [[C2H6]]", "Empirical formulas CH~2~ and CH~3~ differ."),
           T("NO and [[NO2]]", "Empirical formulas NO and NO~2~ differ.")],
    cite=f"{C8}, slide 39 (Empirical and Molecular Formulas: C~6~H~12~O~6~ and CH~2~O-type compounds share an empirical formula), slide 40",
    hw="HW21 — CH has a molar mass of about 26, so C~2~H~2~",
    covers="Reducing molecular formulas to the smallest whole-number ratio and comparing them.",
    sol="""C~2~H~2~ ÷ 2 = **CH**, and C~6~H~6~ ÷ 6 = **CH**. Both have the empirical formula CH. They are different compounds (different
molar masses) with the same ratio of atoms, which is slide 39's point.""",
))

pfe, po = 69.94 / mm("Fe"), 30.06 / mm("O")
r = po / pfe
check(24, r, 1.5, 0.01)
Q.append(dict(
    ch=8, kind="calc", title="Empirical formula needing a multiplier", short="Ch 8 sl. 42–43",
    stem="An iron oxide is 69.94% Fe and 30.06% O by mass. What is its empirical formula?",
    correct=T("[[Fe2O3]]"),
    wrong=[T("FeO", "Rounded 1.5 down to 1. Multiply instead (slide 43, step 4)."),
           T("[[FeO2]]", "Rounded 1.5 up to 2."),
           T("[[Fe3O4]]", "Mole ratio 1 : 1.33. That doesn't match 1 : 1.5."),
           T("[[Fe3O2]]", "Inverted ratio; there is more O than Fe in moles.")],
    cite=f"{C8}, slides 42–43 (Steps for Determining the Empirical Formula, step 4: multiply by the smallest integer), slides 35–37",
    hw="HW21 — empirical formula from percent composition",
    covers="Step 4 of the empirical-formula method: clearing a .5 ratio by multiplying by 2.",
    sol="""Per 100 g: Fe 69.94 / 55.85 = 1.252 mol and O 30.06 / 16.00 = 1.879 mol. Divide by the smallest: Fe 1.00, O 1.50.
1.50 isn't a whole number, so multiply both by 2: Fe 2, O 3. The formula is **Fe~2~O~3~**.""",
))

nn = 92.02 / mm("NO2")
check(25, nn, 2, 0.01)
Q.append(dict(
    ch=8, kind="calc", title="Empirical to molecular formula", short="Ch 8 sl. 47–49",
    stem="A compound has the empirical formula [[NO2]] and a molar mass of 92.02 g/mol. What is its molecular formula?",
    correct=T("[[N2O4]]"),
    wrong=[T("[[NO2]]", "n = 1 would give a molar mass of 46.01."),
           T("[[N3O6]]", "n = 3 would give 138."),
           T("[[N4O8]]", "n = 4 would give 184."),
           T("[[NO4]]", "Multiplied only the O subscript by 2.")],
    cite=f"{C8}, slide 48 ((empirical formula)~n~ = molecular formula), slide 49 (LA Practice), slide 47",
    hw="HW21 — molecular formula from empirical formula + molar mass",
    covers="n = molar mass / empirical mass, and every subscript gets multiplied by n.",
    sol="""Empirical mass NO~2~ = 14.01 + 2(16.00) = 46.01. n = 92.02 / 46.01 = 2, so (NO~2~)~2~ = **N~2~O~4~**.""",
))

Q.append(dict(
    ch=8, kind="concept", title="Combustion analysis", short="Ch 8 sl. 44",
    stem="In **combustion analysis**, a carbon-containing sample is:",
    correct=T("burned in excess oxygen so it fully converts to products, giving the percent C (and other elements) and so the empirical formula"),
    wrong=[T("heated with an electric current until it decomposes into its elements", "That describes a decomposition reaction (slide 43)."),
           T("dissolved in water to see whether it conducts electricity", "That tests for electrolytes (slide 7)."),
           T("burned in a limited amount of oxygen to measure its molar mass directly", "Combustion analysis uses *excess* O~2~ and gives composition, not molar mass."),
           T("weighed to determine its molecular formula without any other data", "Mass alone gives no formula. The molecular formula needs composition plus molar mass.")],
    cite=f"{C8}, slide 44 (Combustion analysis), slide 47",
    hw="HW21 — hw21ex1.png (what evidence is needed for empirical vs molecular formulas)",
    covers="What combustion analysis does and what it produces (composition, leading to the empirical formula).",
    sol="""Slide 44: combustion analysis "works by burning the sample in excess oxygen so that it fully converts to products. ... we can
find the percent of carbon and the other elements which leads us to the empirical formula." To go further to the molecular
formula, you would still need the molar mass (slide 47).""",
))

# ---------------------------------------------------------------- Chapter 9
Q.append(dict(
    ch=9, kind="concept", title="Why balance first", short="Ch 9 sl. 14, 16",
    stem="Why must a chemical equation be balanced before it is used in a stoichiometry calculation?",
    correct=T("The mole ratios used in the calculation come from the coefficients of the balanced equation"),
    wrong=[T("Balancing makes the total mass of the reactants equal the mass of each product", "Mass is conserved in total, not per substance."),
           T("Balancing converts the coefficients from grams into moles", "Coefficients are always mole/particle ratios. They are never grams."),
           T("An unbalanced equation has no limiting reactant", "Limiting reactants exist either way. You just can't find them without the correct ratio."),
           T("Balancing is needed only so the molar masses can be calculated", "Molar masses come from the formulas, not the coefficients.")],
    cite=f"{C9}, slide 16 (Think, Pair, Share 9.3: why balance before stoichiometry?), slide 14 (step 1: balance), slide 2",
    hw="HW22 — balancing before mole-ratio problems ('for each of the following unbalanced equations ...')",
    covers="The reason behind step 1 of slide 14: coefficients give the mole ratios.",
    sol="""Slide 2: "The coefficients in a balanced equation give us the relative numbers of molecules." Every stoichiometry problem
uses a mole ratio (slide 14, step 3). With wrong coefficients, every ratio, and every answer, is wrong.""",
))

o2 = 6 * 3 / 2
check(28, o2, 9, 0)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Counting molecules from coefficients", short="Ch 9 sl. 3–4",
    stem="For 2[[Al2O3]] → 4Al + 3[[O2]], how many molecules of [[O2]] are formed from 6 formula units of [[Al2O3]]?",
    correct=(9, "9", ""),
    wrong=[(3, "3", "That is the coefficient, not scaled to 6 units of Al~2~O~3~."),
           (4, "4", "Inverted the ratio: 6 × 2/3."),
           (12, "12", "That is the number of Al atoms produced."),
           (18, "18", "Multiplied by 3 without dividing by 2.")],
    cite=f"{C9}, slide 4 (Chemical Equation Practice: 2Al~2~O~3~ → 4Al + 3O~2~), slide 3 (Table 9.1)",
    hw="HW22 — interpreting a balanced equation in molecules and moles (H~2~ + F~2~ → 2HF)",
    covers="Coefficients as particle ratios, scaled to a given number of particles.",
    sol="""2 Al~2~O~3~ ⇔ 3 O~2~, so 6 Al~2~O~3~ × (3 O~2~ / 2 Al~2~O~3~) = **9 O~2~ molecules** (and 12 Al atoms).""",
))

co2 = 0.750 * 4 / 7
check(29, co2, 0.429, 0.0005)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Mole–mole conversion", short="Ch 9 sl. 9, 11",
    stem="Ethane burns according to 2[[C2H6]] + 7[[O2]] → 4[[CO2]] + 6[[H2O]]. How many moles of [[CO2]] form when 0.750 mol of [[O2]] reacts completely?",
    correct=(0.429, "0.429 mol", ""),
    wrong=[(0.750 * 7 / 4, f"{0.750 * 7 / 4:.2f} mol", "Inverted ratio (7/4)."),
           (0.750 * 2 / 7, f"{0.750 * 2 / 7:.3f} mol", "Used the C~2~H~6~ coefficient (2) instead of CO~2~ (4)."),
           (0.750, "0.750 mol", "Assumed 1 : 1."),
           (1.50, "1.50 mol", "Multiplied by 2.")],
    cite=f"{C9}, slide 11 (Mole–Mole Conversions Practice 2: 2C~2~H~6~ + 7O~2~ → 4CO~2~ + 6H~2~O), slide 9 (ethane combustion)",
    hw="HW22 — moles of product from moles (e.g. KO~2~ + H~2~O: mol O~2~ from 0.480 mol KOH)",
    covers="Picking the right two coefficients from a four-substance equation.",
    sol="""$$0.750\\ \\text{mol O}_2\\times\\frac{4\\ \\text{mol CO}_2}{7\\ \\text{mol O}_2} = 0.429\\ \\text{mol CO}_2$$""",
))

Q.append(dict(
    ch=9, kind="concept", title="Why actual yield is lower", short="Ch 9 sl. 28",
    stem="According to the course, one reason the actual yield of a reaction is usually **less** than the theoretical yield is:",
    correct=T("side reactions consume some of the reactants or products"),
    wrong=[T("the excess reactant also turns into product", "The excess reactant is left over. It doesn't add product."),
           T("the theoretical yield is calculated from the excess reactant", "The theoretical yield comes from the *limiting* reactant (slide 25)."),
           T("the limiting reactant is never used up", "By definition, the limiting reactant runs out first."),
           T("mass is not conserved in most chemical reactions", "Mass is always conserved.")],
    cite=f"{C9}, slide 28 (Actual Yield: 'One reason for this is the presence of side reactions'), slide 25",
    hw="HW24 — percent yield problems (actual is less than theoretical)",
    covers="Course definition of actual yield and the reason it falls short.",
    sol="""Slide 28: "the amount of product predicted (the theoretical yield) is seldom obtained. One reason for this is the presence of
**side reactions** (other reactions that consume one or more of the reactants or products)." """,
))

koh = 25.0 / mm("KOH")
k2so4 = koh / 2 * mm("K2SO4")
check(31, k2so4, 38.8, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Grams to grams", short="Ch 9 sl. 14, 18",
    stem="For [[H2SO4]] + 2KOH → [[K2SO4]] + 2[[H2O]], what mass of [[K2SO4]] is produced from 25.0 g of KOH with excess [[H2SO4]]?",
    correct=(38.8, "38.8 g", ""),
    wrong=[(koh / 2, f"{koh / 2:.3f} g", "That is the moles of K~2~SO~4~."),
           (koh / 2 * mm("H2SO4"), f"{koh / 2 * mm('H2SO4'):.1f} g", "Used the molar mass of H~2~SO~4~ instead of K~2~SO~4~."),
           (koh * mm("K2SO4"), f"{koh * mm('K2SO4'):.1f} g", "Assumed 1 : 1 (forgot the 2 KOH)."),
           (25.0, "25.0 g", "Assumed the product mass equals the reactant mass.")],
    cite=f"{C9}, slide 18 (Stoichiometry Practice 2: H~2~SO~4~ + 2KOH), slide 14 (steps)",
    hw="HW23 — mass of product from mass of reactant (CaC~2~ → C~2~H~2~)",
    covers="g → mol → mol ratio → g, with a 2 : 1 ratio.",
    sol="""$$25.0\\ \\text{g KOH}\\div56.11 = 0.4456\\ \\text{mol};\\quad\\times\\tfrac{1}{2} = 0.2228\\ \\text{mol K}_2\\text{SO}_4;\\quad\\times174.27 = 38.8\\ \\text{g}$$""",
))

mg, n2 = 0.600, 0.250
prod = min(mg / 3, n2) * mm("Mg3N2")
check(32, prod, 20.2, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Limiting reactant, then product mass", short="Ch 9 sl. 22–23",
    stem="For 3Mg + [[N2]] → [[Mg3N2]], 0.600 mol of Mg reacts with 0.250 mol of [[N2]]. What mass of [[Mg3N2]] can form?",
    correct=(20.2, "20.2 g", ""),
    wrong=[(n2 * mm("Mg3N2"), f"{n2 * mm('Mg3N2'):.1f} g", "Treated N~2~ as limiting. It is in excess (Mg needs only 0.200 mol N~2~)."),
           (mg * mm("Mg3N2"), f"{mg * mm('Mg3N2'):.1f} g", "Assumed 1 mol Mg gives 1 mol Mg~3~N~2~."),
           (mg / 3, f"{mg / 3:.3f} g", "That is the moles of Mg~3~N~2~."),
           (mg * mm("Mg") + n2 * mm("N2"), f"{mg * mm('Mg') + n2 * mm('N2'):.1f} g", "Added the reactant masses, ignoring the excess N~2~.")],
    cite=f"{C9}, slide 23 (Limiting Reactants Practice: 3Mg + N~2~ → Mg~3~N~2~), slides 21–22, 25",
    hw="HW23 — limiting reactant then product mass (5.65 g of each reactant; Fe + O~2~)",
    covers="Find the limiting reactant from moles, then calculate the product from it.",
    sol="""Mg needs 0.600 / 3 = 0.200 mol N~2~. 0.250 mol is available, so N~2~ is in excess and **Mg is limiting**.

$$0.600\\ \\text{mol Mg}\\times\\frac{1\\ \\text{mol Mg}_3\\text{N}_2}{3\\ \\text{mol Mg}}\\times100.95\\ \\tfrac{\\text{g}}{\\text{mol}} = 20.2\\ \\text{g}$$""",
))

nacl = 10.0 / mm("NaCl")
pbcl2 = nacl / 2 * mm("PbCl2")
check(33, pbcl2, 23.8, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Theoretical yield with excess reactant", short="Ch 9 sl. 25–26",
    stem="For [[Pb(NO3)2]] + 2NaCl → [[PbCl2]] + 2[[NaNO3]], what is the theoretical yield of [[PbCl2]] when 10.0 g of NaCl reacts with excess [[Pb(NO3)2]]?",
    correct=(23.8, "23.8 g", ""),
    wrong=[(nacl * mm("PbCl2"), f"{nacl * mm('PbCl2'):.1f} g", "Assumed 1 : 1 (forgot the 2 NaCl)."),
           (nacl / 2, f"{nacl / 2:.4f} g", "That is the moles of PbCl~2~."),
           (nacl / 2 * mm("Pb(NO3)2"), f"{nacl / 2 * mm('Pb(NO3)2'):.1f} g", "Used the molar mass of Pb(NO~3~)~2~."),
           (10.0, "10.0 g", "Assumed the product mass equals the reactant mass.")],
    cite=f"{C9}, slide 26 (Theoretical Yield Practice: 237 g NaCl + excess Pb(NO~3~)~2~), slide 25",
    hw="HW24 — theoretical yield calculations (XeF~4~; Na~2~S~2~O~3~·5H~2~O)",
    covers="'Excess' tells you which reactant is limiting, so calculate the yield from it.",
    sol="""$$10.0\\ \\text{g NaCl}\\div58.44 = 0.1711\\ \\text{mol};\\quad\\times\\tfrac{1}{2} = 0.08556\\ \\text{mol PbCl}_2;\\quad\\times278.1 = 23.8\\ \\text{g}$$""",
))

n2m, h2m = 14.0 / mm("N2"), 6.00 / mm("H2")
nh3_theo = min(n2m, h2m / 3) * 2 * mm("NH3")
pct = 12.5 / nh3_theo * 100
check(34, pct, 73.4, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Percent yield with a limiting reactant", short="Ch 9 sl. 27, 30",
    stem="For [[N2]] + 3[[H2]] → 2[[NH3]], 14.0 g of [[N2]] reacts with 6.00 g of [[H2]], and 12.5 g of [[NH3]] is collected. What is the percent yield?",
    correct=(73.4, "73.4%", ""),
    wrong=[(12.5 / (h2m / 3 * 2 * mm("NH3")) * 100, f"{12.5 / (h2m / 3 * 2 * mm('NH3')) * 100:.1f}%", "Used H~2~ as limiting. It is in excess."),
           (12.5 / 20.0 * 100, f"{12.5 / 20.0 * 100:.1f}%", "Divided by the total reactant mass."),
           (12.5 / 14.0 * 100, f"{12.5 / 14.0 * 100:.1f}%", "Divided by the mass of N~2~."),
           (nh3_theo / 12.5 * 100, f"{nh3_theo / 12.5 * 100:.0f}%", "Upside down: theoretical / actual.")],
    cite=f"{C9}, slide 27 (theoretical yield with two given masses), slide 30 (Percent Yield formula), slides 31–32",
    hw="HW24 — hw24ex2.png (theoretical yield of XeF~4~ from two masses, then percent yield)",
    covers="The full chain: limiting reactant → theoretical yield → percent yield.",
    sol="""N~2~: 14.0 / 28.02 = 0.4996 mol. H~2~: 6.00 / 2.016 = 2.976 mol. N~2~ needs 3 × 0.4996 = 1.499 mol H~2~, which is less than
2.976, so **N~2~ is limiting**.

$$\\text{NH}_3\\ \\text{theoretical} = 0.4996\\times2\\times17.03 = 17.02\\ \\text{g};\\qquad \\%\\ \\text{yield} = \\frac{12.5}{17.02}\\times100 = 73.4\\%$$""",
))

Q.append(dict(
    ch=9, kind="concept", title="A yield above 100%", short="Ch 9 sl. 28–29",
    stem="A student reports a percent yield of 112%. Which statement is correct?",
    correct=T("Something is wrong, such as a wet or impure product or a calculation error, because the theoretical yield is the maximum possible"),
    wrong=[T("Side reactions produced extra product beyond the theoretical yield", "Side reactions *lower* the yield (slide 28)."),
           T("The excess reactant was converted into additional product", "The theoretical yield already accounts for the limiting reactant. The excess can't react further."),
           T("Yields above 100% are normal whenever the reaction is fast", "The theoretical yield is the maximum, regardless of speed."),
           T("The theoretical yield must have been calculated from the limiting reactant", "That is the correct way to calculate it. It doesn't explain the error.")],
    cite=f"{C9}, slide 29 (Think, Pair, Share 9.6: can the actual yield exceed the theoretical?), slide 28 (theoretical yield = maximum)",
    hw="HW24 — percent yield",
    covers="The theoretical yield is a ceiling. Percent yield can't truly exceed 100%.",
    sol="""Slide 28 defines the theoretical yield as "the **maximum** amount of product that can be produced." A measured result over 100%
means extra mass (water or impurities in the product) or a mistake. It can't be real product.""",
))

if __name__ == "__main__":
    assert len(Q) == 35, len(Q)
    build(2, Q, seed=32)
