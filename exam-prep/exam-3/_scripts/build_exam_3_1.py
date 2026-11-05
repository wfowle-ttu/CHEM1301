"""Build practice-exam-3-1 and its key, checking every numeric answer.

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_exam_3_1.py
Choice tuples are (value, text, why-wrong); value is None for text choices.
"""
from examlib import NA, build, check, mm, sci

C7, C8, C9 = "Chapter 7 post", "Chapter 8 post", "Chapter 9 post"
Q = []


def T(text, why=""):
    return (None, text, why)


# ---------------------------------------------------------------- Chapter 7
Q.append(dict(
    ch=7, kind="concept", title="Driving forces", short="Ch 7 sl. 3",
    stem="Which of the following is **NOT** one of the four driving forces that tend to make a chemical reaction occur?",
    correct=T("An increase in the total mass of the products"),
    wrong=[T("Formation of a solid", "listed driving force #1."),
           T("Formation of water", "listed driving force #2."),
           T("Transfer of electrons", "listed driving force #3."),
           T("Formation of a gas", "listed driving force #4.")],
    cite=f"{C7}, slide 3 (Driving Forces); slide 2 (Predicting Whether a Reaction Will Occur)",
    hw="HW14 — hw14ex1.png (naming the reaction type driven by forming a solid)",
    covers="Recalling the course's four driving forces: solid, water, electron transfer, gas.",
    sol="""Slide 3 lists exactly four driving forces: (1) formation of a solid, (2) formation of water,
(3) transfer of electrons, (4) formation of a gas. Mass is conserved in every reaction, so "an increase in the
total mass of the products" is not a driving force; it can't happen at all.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Solubility rules: insoluble salt", short="Ch 7 sl. 11",
    stem="On the basis of the general solubility rules, which compound is **insoluble** (only slightly soluble) in water?",
    correct=T("[[PbCl2]]"),
    wrong=[T("[[KNO3]]", "Rules 1 and 2: nitrates and K^+^ salts are soluble."),
           T("[[Na2SO4]]", "Rules 2 and 4: Na^+^ salts and most sulfates are soluble."),
           T("[[NH4Cl]]", "Rules 2 and 3: NH~4~^+^ salts and most chlorides are soluble."),
           T("[[Ba(NO3)2]]", "Rule 1: nitrates are soluble. (BaSO~4~ is the barium exception, not the nitrate.)")],
    cite=f"{C7}, slide 11 (Solubility Rules, Table 7.1), rule 3",
    hw="HW14 — hw14ex2.png (choose the substance not likely to be soluble)",
    covers="Memorized Table 7.1, especially the named exceptions to the chloride and sulfate rules.",
    sol="""Rule 3: most chloride salts are soluble. **Notable exceptions are AgCl, PbCl~2~, and Hg~2~Cl~2~.**
PbCl~2~ is one of the three named exceptions, so it is insoluble. The exceptions are the most likely thing to be tested here.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Solubility rules: which rule wins", short="Ch 7 sl. 11",
    stem="Which of the following compounds is expected to be **soluble** in water?",
    correct=T("[[(NH4)3PO4]]"),
    wrong=[T("[[CaCO3]]", "Rule 6: carbonates are only slightly soluble, and Ca^2+^ isn't a rule-2 cation."),
           T("[[BaSO4]]", "Rule 4 exception: BaSO~4~ is insoluble."),
           T("[[Mg(OH)2]]", "Rule 5: most hydroxides are only slightly soluble (only NaOH and KOH are listed as soluble)."),
           T("[[Ag2S]]", "Rule 6: sulfides are only slightly soluble.")],
    cite=f"{C7}, slide 11 (Solubility Rules), rules 2 and 6",
    hw="HW14 — hw14ex3.png / hw14ex4.png (which rule explains solubility, e.g. ammonium sulfide)",
    covers="Applying rule 2 (Na^+^, K^+^, NH~4~^+^ salts are soluble) even when the anion is a rule-6 'insoluble' anion.",
    sol="""Phosphates are normally only slightly soluble (rule 6), **but** rule 2 says most salts of Na^+^, K^+^,
and NH~4~^+^ are soluble. The cation rule wins, so (NH~4~)~3~PO~4~ is soluble. HW14 does the same thing with
ammonium sulfide and ammonium carbonate, where the answer is "most salts of NH~4~^+^ are soluble." """,
))

Q.append(dict(
    ch=7, kind="concept", title="Predicting the precipitate", short="Ch 7 sl. 11, 14",
    stem="Aqueous solutions of calcium nitrate, [[Ca(NO3)2]], and sodium carbonate, [[Na2CO3]], are mixed. What is the precipitate?",
    correct=T("[[CaCO3]]"),
    wrong=[T("[[NaNO3]]", "Rules 1 and 2: NaNO~3~ is soluble and stays as Na^+^ and NO~3~^−^ ions."),
           T("[[Na(NO3)2]]", "Not a valid neutral formula, and it isn't what you get from swapping anions."),
           T("[[CaNa2]]", "Two cations can't combine. A solid must contain both a cation and an anion (slide 10)."),
           T("No precipitate forms", "CaCO~3~ is only slightly soluble (rule 6), so a solid does form.")],
    cite=f"{C7}, slide 14 (How to Predict Precipitates), slide 11 (rules 1, 2, 6), slide 10 (a solid must contain cations and anions)",
    hw="HW15 — hw15ex4.png (molecular equations for precipitation, e.g. K~2~CO~3~ + MgCl~2~ → MgCO~3~(s))",
    covers="The three-step method: write the ions, swap the anions, check each possible product against the solubility rules.",
    sol="""Step 1: the ions present are Ca^2+^, NO~3~^−^, Na^+^, CO~3~^2−^. Step 2: swapping anions gives the possible solids
CaCO~3~ and NaNO~3~. Step 3: NaNO~3~ is soluble (rules 1, 2), and CaCO~3~ is only slightly soluble (rule 6), so the solid is **CaCO~3~**.

Ca(NO~3~)~2~(aq) + Na~2~CO~3~(aq) → CaCO~3~(s) + 2NaNO~3~(aq)""",
))

Q.append(dict(
    ch=7, kind="concept", title="Net ionic equation", short="Ch 7 sl. 17, 20",
    stem="Which is the correct **net ionic equation** for the reaction of aqueous sodium chloride with aqueous silver nitrate?",
    correct=T("[[Ag^+^]](aq) + [[Cl^-^]](aq) → [[AgCl]](s)"),
    wrong=[T("[[NaCl]](aq) + [[AgNO3]](aq) → [[AgCl]](s) + [[NaNO3]](aq)", "This is the molecular equation (slide 15)."),
           T("[[Ag^+^]](aq) + [[Cl^-^]](aq) + [[Na^+^]](aq) + [[NO3^-^]](aq) → [[AgCl]](s) + [[Na^+^]](aq) + [[NO3^-^]](aq)",
             "This is the complete ionic equation. It still has the spectator ions."),
           T("[[Na^+^]](aq) + [[NO3^-^]](aq) → [[NaNO3]](s)", "NaNO~3~ is soluble (rules 1, 2), so these are spectator ions."),
           T("[[Ag^+^]](aq) + [[Cl^-^]](aq) → [[AgCl]](aq)", "AgCl is an exception to rule 3. It precipitates, so its state is (s).")],
    cite=f"{C7}, slide 20 (Practice: NaCl + AgNO~3~), slides 15–18 (molecular / complete ionic / net ionic)",
    hw="HW15 — hw15ex1.png (definition of net ionic equation) and hw15ex2.png (Sr^2+^ + CrO~4~^2−^ net ionic)",
    covers="Telling the three equation types apart; a net ionic equation leaves out the spectator ions.",
    sol="""Molecular: NaCl(aq) + AgNO~3~(aq) → AgCl(s) + NaNO~3~(aq).
Complete ionic: write every strong electrolyte as ions. Na^+^ and NO~3~^−^ appear unchanged on both sides, so they are
spectator ions. Cancel them to get the net ionic equation: **Ag^+^(aq) + Cl^−^(aq) → AgCl(s)** (slide 17: "only those
components that are directly involved").""",
))

h2o = 6
Q.append(dict(
    ch=7, kind="calc", numeric=True, title="Balancing an acid–base neutralization", short="Ch 7 sl. 27",
    stem="When the equation below is balanced with the smallest whole-number coefficients, what is the coefficient of water?\n\n"
         "\\_\\_ [[H3PO4]](aq) + \\_\\_ [[Ca(OH)2]](aq) → \\_\\_ [[Ca3(PO4)2]](s) + \\_\\_ [[H2O]](l)",
    correct=(6, "6", ""),
    wrong=[(1, "1", "Leaves the equation unbalanced."),
           (2, "2", "This is the coefficient of H~3~PO~4~."),
           (3, "3", "This is the coefficient of Ca(OH)~2~."),
           (4, "4", "Doesn't balance H or O.")],
    cite=f"{C7}, slide 27 (Practice: H~3~PO~4~ + Ca(OH)~2~ → Ca~3~(PO~4~)~2~ + H~2~O)",
    hw="HW22 — balancing equations with lowest whole-number coefficients (KrF~2~ + H~2~O; Al + H~2~SO~4~)",
    covers="Balancing an acid–base reaction: polyatomic ions go first as units, then H and O.",
    sol="""Balance Ca first: 3 Ca(OH)~2~. Balance PO~4~ as a unit: 2 H~3~PO~4~. Now count H and O outside PO~4~:
6 H from the acid + 6 OH from the base make **6 H~2~O**.

$$2\\,\\text{H}_3\\text{PO}_4 + 3\\,\\text{Ca(OH)}_2 \\rightarrow \\text{Ca}_3(\\text{PO}_4)_2 + 6\\,\\text{H}_2\\text{O}$$

Check: H is 6 + 6 = 12 on the left and 12 on the right. O is 8 + 6 = 14 on the left and 8 + 6 = 14 on the right.""",
))
check(6, 2 * 3 + 3 * 2, 2 * h2o, 0)  # H atoms: 2*3 (acid) + 3*2 (base) = 2*6 (water)

Q.append(dict(
    ch=7, kind="concept", title="Mixing with no reaction", short="Ch 7 sl. 11, 14",
    stem="Which pair of aqueous solutions will **NOT** form a precipitate when mixed?",
    correct=T("[[KNO3]] and [[Na2S]]"),
    wrong=[T("[[AgNO3]] and [[NaCl]]", "Forms AgCl(s) (rule 3 exception)."),
           T("[[BaCl2]] and [[Na2SO4]]", "Forms BaSO~4~(s) (rule 4 exception)."),
           T("[[MgCl2]] and [[K2CO3]]", "Forms MgCO~3~(s) (rule 6)."),
           T("[[AlCl3]] and [[KOH]]", "Forms Al(OH)~3~(s) (rule 5).")],
    cite=f"{C7}, slide 14 (How to Predict Precipitates), slide 11 (Solubility Rules)",
    hw="HW15 — hw15ex3.png (does a reaction occur: potassium nitrate + sodium sulfide → NR; aluminum chloride + potassium hydroxide)",
    covers="Swapping anions and checking both possible products. If both are soluble, there is no reaction (NR).",
    sol="""KNO~3~ + Na~2~S: the possible products from swapping anions are K~2~S and NaNO~3~. K~2~S is soluble because K^+^ salts
are soluble (rule 2), and NaNO~3~ is soluble (rules 1, 2). Nothing precipitates, so the answer is **NR**. Every other pair makes one
insoluble product.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Strong acid + strong base net ionic", short="Ch 7 sl. 23, 25",
    stem="The net ionic equation for the reaction of **any** strong acid with **any** strong base is:",
    correct=T("[[H^+^]](aq) + [[OH^-^]](aq) → [[H2O]](l)"),
    wrong=[T("[[HCl]](aq) + [[NaOH]](aq) → [[NaCl]](aq) + [[H2O]](l)", "A molecular equation for one specific acid and base."),
           T("[[Na^+^]](aq) + [[Cl^-^]](aq) → [[NaCl]](s)", "The salt stays dissolved (slide 26, principle 5), so Na^+^ and Cl^−^ are spectators."),
           T("[[H^+^]](aq) + [[Cl^-^]](aq) → [[HCl]](aq)", "Strong acids completely dissociate. They don't re-form."),
           T("2[[H^+^]](aq) + [[O^2-^]](aq) → [[H2O]](l)", "Strong bases release OH^−^, not O^2−^.")],
    cite=f"{C7}, slide 23 (Acid–Base Reactions), slide 25 (principle 4), slide 26 (principles 5–6)",
    hw="HW16 — hw16ex2.png (the same net ionic process for any strong acid/strong base)",
    covers="The net ionic equation for every strong acid + strong base reaction is the formation of water.",
    sol="""Slide 25, principle 4: "The net ionic equation for the reaction of a strong acid and a strong base ... is always the
same: it shows the production of water." The cation of the base and the anion of the acid are spectators, so the equation is
**H^+^(aq) + OH^−^(aq) → H~2~O(l)**.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Identifying a strong acid", short="Ch 7 sl. 21, 24",
    stem="Which of the following is one of the common **strong acids** named in this course?",
    correct=T("[[H2SO4]]"),
    wrong=[T("[[HNO2]]", "Nitrous acid (slide 28) is not on the strong-acid list. Don't mix it up with HNO~3~."),
           T("[[HC2H3O2]]", "Acetic acid is not on the strong-acid list."),
           T("[[HF]]", "Not on the strong-acid list. HCl is the strong hydrogen halide."),
           T("[[H3PO4]]", "Phosphoric acid (slide 27) is not on the strong-acid list.")],
    cite=f"{C7}, slide 24 (Summary of Strong Acids and Strong Bases, principle 1), slide 21 (Arrhenius Acids)",
    hw="HW16 — hw16ex2.png (salts formed by strong acid/strong base reactions: HI, HNO~3~, HCl)",
    covers="Memorizing the course's list of strong acids (HCl, HNO~3~, H~2~SO~4~) and the definition of a strong acid.",
    sol="""Slide 24, principle 1: "The common strong acids are aqueous solutions of **HCl, HNO~3~, and H~2~SO~4~**." A strong acid
completely dissociates (ionizes) in water (principle 2). Watch HNO~2~ (nitrous) versus HNO~3~ (nitric). Only nitric is strong.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Definition of a strong base", short="Ch 7 sl. 22, 25",
    stem="According to the course, which statement best describes a **strong base**?",
    correct=T("A metal hydroxide that is very soluble in water and completely breaks up into separated ions, so it is a strong electrolyte"),
    wrong=[T("A substance that produces [[H^+^]] ions when dissolved in water", "That is an Arrhenius acid (slide 21)."),
           T("Any compound containing [[OH]], whether or not it dissolves", "Most hydroxides are only slightly soluble (rule 5). Those aren't strong bases."),
           T("A metal hydroxide that produces [[OH^-^]] ions but is not a strong electrolyte", "Strong bases are strong electrolytes (HW16)."),
           T("A substance that accepts electrons from a metal", "That describes the nonmetal in a redox reaction (slide 31).")],
    cite=f"{C7}, slide 25 (principle 3), slide 22 (Arrhenius Bases), slide 7 (Strong Electrolytes)",
    hw="HW16 — hw16ex1.png (what is a strong base; are strong bases strong electrolytes?)",
    covers="Course definitions: Arrhenius base, strong base, strong electrolyte.",
    sol="""Slide 25, principle 3: "A strong base is a metal hydroxide compound that is very soluble in water. The most common
strong bases are NaOH and KOH, which completely break up into separated ions." Because every unit gives separated ions,
strong bases are **strong electrolytes** (slide 7 definition).""",
))

Q.append(dict(
    ch=7, kind="calc", numeric=True, title="Electrons transferred per atom", short="Ch 7 sl. 33",
    stem="In the oxidation–reduction reaction 2Al(s) + [[N2]](g) → 2AlN(s), how many electrons are transferred **from each Al atom**?",
    correct=(3, "3", ""),
    wrong=[(1, "1", "That would give Al^+^, but AlN needs Al^3+^ to balance N^3−^."),
           (2, "2", "The subscript on N~2~ has nothing to do with the charge."),
           (4, "4", "No combination of the ion charges gives 4."),
           (6, "6", "That is the total for 2 Al atoms, not per atom.")],
    cite=f"{C7}, slide 33 (Oxidation–Reduction Reactions Practice: 2Al + N~2~ → 2AlN), slides 30–31",
    hw="HW16 — hw16ex3.png (Ba + Cl~2~ → BaCl~2~: Ba loses two electrons)",
    covers="Metal + nonmetal is always redox. Get the ion charges from the ionic product.",
    sol="""Metal + nonmetal makes an ionic compound, so this is redox (slide 31). In AlN, nitrogen forms N^3−^ (group 15 gains 3),
so aluminum must be Al^3+^ for the compound to be neutral. Each Al atom **loses 3 electrons**, and each N atom gains 3.
Total electrons moved per equation = 2 × 3 = 6.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Classifying Zn + HCl", short="Ch 7 sl. 40",
    stem="The reaction Zn(s) + 2HCl(aq) → [[ZnCl2]](aq) + [[H2]](g) is best classified as:",
    correct=T("oxidation–reduction and single-replacement"),
    wrong=[T("precipitation and double-displacement", "No solid forms, and only one anion (Cl^−^) changes partners."),
           T("acid–base only", "No OH^−^ is involved, and H^+^ ends up in H~2~, not in water."),
           T("decomposition", "Two reactants combine into new products. Nothing is broken down."),
           T("combustion and synthesis", "No O~2~ is involved, and it doesn't make one compound from simpler ones.")],
    cite=f"{C7}, slide 40 (Single-Replacement Reactions), slide 45 (Summary of Classes of Reactions)",
    hw="HW17 — hw17ex1.png (classify HCl(aq) + Fe(s) → H~2~(g) + FeCl~2~(aq) as oxidation–reduction)",
    covers="A reaction can be in more than one class. A single-replacement reaction is always redox.",
    sol="""Zn goes from a neutral atom to Zn^2+^ (loses 2 e^−^), and H^+^ becomes H~2~ (gains electrons), so this is **redox**.
One anion (Cl^−^) is passed from H^+^ to Zn^2+^, which is the slide 40 definition of a **single-replacement** reaction.""",
))

Q.append(dict(
    ch=7, kind="concept", title="Synthesis that is redox but not combustion", short="Ch 7 sl. 41–43",
    stem="Which reaction is a **synthesis** reaction that is also an oxidation–reduction reaction but is **not** a combustion reaction?",
    correct=T("2Fe(s) + 3[[Cl2]](g) → 2[[FeCl3]](s)"),
    wrong=[T("C(s) + [[O2]](g) → [[CO2]](g)", "Synthesis and redox, but it burns in O~2~, so it is also combustion."),
           T("[[CH4]](g) + 2[[O2]](g) → [[CO2]](g) + 2[[H2O]](g)", "Combustion, not synthesis. It makes two products."),
           T("2HgO(s) → 2Hg(l) + [[O2]](g)", "Decomposition (slide 43)."),
           T("[[NaOH]](aq) + [[HCl]](aq) → [[NaCl]](aq) + [[H2O]](l)", "Acid–base, with no electron transfer.")],
    cite=f"{C7}, slide 42 (Synthesis), slide 41 (Combustion), slide 43 (Decomposition), slide 31 (metal + nonmetal = redox)",
    hw="HW17 — hw17ex3.png (synthesis also combustion vs. synthesis also redox but not combustion)",
    covers="Telling synthesis, combustion, and decomposition apart, and seeing that one reaction can belong to several classes.",
    sol="""Synthesis makes one compound from simpler materials (slide 42). Fe + Cl~2~ → FeCl~3~ qualifies, and it is metal +
nonmetal, so it is redox (slide 31). No O~2~ is involved, so it is not combustion (slide 41). C + O~2~ is also a synthesis, but it
burns in oxygen, so it counts as combustion.""",
))

# ---------------------------------------------------------------- Chapter 8
Q.append(dict(
    ch=8, kind="concept", title="Definition of the mole", short="Ch 8 sl. 7",
    stem="The mole is defined in this course as:",
    correct=T("the number of carbon atoms in exactly 12.01 g of carbon, 6.022 × 10^23^"),
    wrong=[T("the mass of one atom of carbon, 12.01 g", "12.01 g is the mass of a *mole* of C. One atom is 12.01 amu."),
           T("1.66 × 10^−24^ g", "That is 1 amu (slide 5)."),
           T("the number of atoms in 1.000 g of any element", "Different elements have different atomic masses, so 1 g contains different numbers of atoms."),
           T("the number of molecules in 1 L of any substance", "That isn't how the mole is defined.")],
    cite=f"{C8}, slide 7 (The Mole); slide 5 (Atomic Mass Units)",
    hw="HW18 — the atoms → grams conversion factor (1 mol / 6.022 × 10^23^ atoms)",
    covers="The course's wording of the mole and Avogadro's number, and how they differ from the amu.",
    sol="""Slide 7: "The mole (mol) can be defined as the number equal to the number of carbon atoms in 12.01 grams of carbon ...
6.022 × 10^23^. This number is called Avogadro's number." """,
))

Q.append(dict(
    ch=8, kind="concept", title="Same number of atoms", short="Ch 8 sl. 6",
    stem="Which sample contains the **same number of atoms** as 26.98 g of aluminum?",
    correct=T("24.31 g of magnesium"),
    wrong=[T("26.98 g of magnesium", "Equal masses of different elements do NOT have equal numbers of atoms."),
           T("13.49 g of copper", "This is half the Al mass. Equal atoms needs 63.55 g Cu (slide 6)."),
           T("12.01 g of magnesium", "12.01 g is 1 mol of *carbon*, not magnesium."),
           T("6.022 g of hydrogen", "1 mol of H is 1.008 g, so 6.022 g H is about 6 mol.")],
    cite=f"{C8}, slide 6 (Elements: 26.98 g Al vs 63.55 g Cu), slide 9 (Table 8.2, 1-mole samples)",
    hw="HW18 — comparing samples (Co atoms vs Mn moles: which contains more atoms?)",
    covers="Samples whose masses are in the same ratio as their atomic masses contain the same number of atoms.",
    sol="""26.98 g Al = 1 mol Al = 6.022 × 10^23^ atoms. The same number of Mg atoms is 1 mol Mg = **24.31 g**. Slide 6:
"samples in which the ratio of the masses is the same as the ratio of the masses of the individual atoms always contain the same
number of atoms." """,
))

al = 3.60 / mm("Al")
check(16, al, 0.133, 0.0005)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Grams to moles", short="Ch 8 sl. 11",
    stem="How many moles of aluminum are in 3.60 g of Al?",
    correct=(0.133, "0.133 mol", ""),
    wrong=[(97.1, "97.1 mol", "Multiplied by the molar mass instead of dividing."),
           (7.49, "7.49 mol", "Inverted: 26.98 / 3.60."),
           (8.04e22, f"{sci(al * NA)} mol", "That is the number of atoms, not moles."),
           (1.33, "1.33 mol", "Decimal slip (off by 10).")],
    cite=f"{C8}, slide 11 (Mole Conversion Practice: 3.60 g Al)",
    hw="HW18 — hw18ex1.png (moles from mass: neon, silver, uranium)",
    covers="Grams → moles: divide by the molar mass from the periodic table.",
    sol="""$$3.60\\ \\text{g Al}\\times\\frac{1\\ \\text{mol Al}}{26.98\\ \\text{g Al}} = 0.133\\ \\text{mol Al}$$""",
))

au_mol = 2.31e22 / NA
au_g = au_mol * mm("Au")
check(17, au_g, 7.56, 0.005)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Atoms to grams", short="Ch 8 sl. 15",
    stem="What is the mass of 2.31 × 10^22^ atoms of gold?",
    correct=(7.56, "7.56 g", ""),
    wrong=[(au_mol / mm("Au"), f"{sci(au_mol / mm('Au'))} g", "Divided by the molar mass instead of multiplying."),
           (0.0384, "0.0384 g", "Stopped at moles (0.0384 mol)."),
           (mm("Au") / au_mol, f"{sci(mm('Au') / au_mol)} g", "Inverted the mole value: 196.97 / 0.0384."),
           (2.31e22 * mm("Au"), f"{sci(2.31e22 * mm('Au'))} g", "Multiplied atoms by molar mass without dividing by Avogadro's number.")],
    cite=f"{C8}, slide 15 (Convert atoms to grams: 2.31 × 10^22^ atoms of gold), slide 10 (Mole Conversion Example)",
    hw="HW18 — atoms → grams setup ((1 mol / 6.022 × 10^23^ atoms) × (g / 1 mol))",
    covers="Atoms → moles (÷ Avogadro's number) → grams (× molar mass).",
    sol="""$$2.31\\times10^{22}\\ \\text{atoms}\\times\\frac{1\\ \\text{mol}}{6.022\\times10^{23}\\ \\text{atoms}}\\times\\frac{196.97\\ \\text{g}}{1\\ \\text{mol}} = 0.03836\\ \\text{mol}\\times196.97 = 7.56\\ \\text{g Au}$$""",
))

mg_atoms = 4.25 / mm("Mg") * NA
check(18, mg_atoms, 1.05e23, 0.006e23)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Grams to atoms", short="Ch 8 sl. 10, 13",
    stem="How many atoms are present in 4.25 g of magnesium?",
    correct=(mg_atoms, f"{sci(mg_atoms)} atoms", ""),
    wrong=[(mg_atoms / 10, f"{sci(mg_atoms / 10)} atoms", "Exponent slip: 10^23^ is right, not 10^22^."),
           (4.25 * NA, f"{sci(4.25 * NA)} atoms", "Skipped the grams → moles step (treated 4.25 g as 4.25 mol)."),
           (mm("Mg") / 4.25 * NA, f"{sci(mm('Mg') / 4.25 * NA)} atoms", "Inverted the mole step: 24.31 / 4.25."),
           (4.25 * mm("Mg") * NA, f"{sci(4.25 * mm('Mg') * NA)} atoms", "Multiplied by the molar mass instead of dividing.")],
    cite=f"{C8}, slide 10 (Mole Conversion Example: 0.500 g H → atoms), slides 13–14 (Atom Conversion Practice)",
    hw="HW18 — hw18ex3.png (number of atoms in 3.00 g Ag, 6.50 kg Mg, ...)",
    covers="Grams → moles → atoms, following slide 10's two-step pattern.",
    sol="""$$4.25\\ \\text{g Mg}\\times\\frac{1\\ \\text{mol}}{24.31\\ \\text{g}} = 0.1748\\ \\text{mol};\\quad 0.1748\\ \\text{mol}\\times6.022\\times10^{23}\\ \\tfrac{\\text{atoms}}{\\text{mol}} = 1.05\\times10^{23}\\ \\text{atoms}$$""",
))

alsulf = mm("Al2(SO4)3")
check(19, alsulf, 342.2, 0.05)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Molar mass with parentheses", short="Ch 8 sl. 22, 26",
    stem="What is the molar mass of aluminum sulfate, [[Al2(SO4)3]]?",
    correct=(342.2, "342.2 g/mol", ""),
    wrong=[(mm("AlSO4"), f"{mm('AlSO4'):.1f} g/mol", "Ignored every subscript outside the parentheses (AlSO~4~)."),
           (mm("Al2SO4"), f"{mm('Al2SO4'):.1f} g/mol", "Dropped the 3 outside the parentheses (Al~2~SO~4~)."),
           (mm("Al2S3O4"), f"{mm('Al2S3O4'):.1f} g/mol", "Applied the 3 to S only, not to O."),
           (mm("Al(SO4)3"), f"{mm('Al(SO4)3'):.1f} g/mol", "Dropped the 2 on Al.")],
    cite=f"{C8}, slide 22 (Molar Mass: sum of component atoms), slide 26 (LA problem: Ba(OH)~2~ with parentheses)",
    hw="HW19 — hw19ex1.png (write formula and molar mass: iron(II) chloride, copper(II) sulfate, rubidium chloride)",
    covers="Molar mass = sum of atomic masses × subscripts. A subscript outside parentheses multiplies everything inside.",
    sol="""Atom count: 2 Al, 3 S, 12 O.

$$2(26.98) + 3(32.07) + 12(16.00) = 53.96 + 96.21 + 192.00 = 342.17 \\approx 342.2\\ \\text{g/mol}$$""",
))

naoh = 2.45 * mm("NaOH")
check(20, naoh, 98.0, 0.05)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Moles to grams", short="Ch 8 sl. 27",
    stem="What is the mass of 2.45 mol of sodium hydroxide, [[NaOH]]?",
    correct=(98.0, "98.0 g", ""),
    wrong=[(2.45 / mm("NaOH"), f"{2.45 / mm('NaOH'):.4f} g", "Divided by the molar mass instead of multiplying."),
           (mm("NaOH") / 2.45, f"{mm('NaOH') / 2.45:.1f} g", "Divided the molar mass by the moles."),
           (2.45 * mm("Na"), f"{2.45 * mm('Na'):.1f} g", "Used only the mass of Na (22.99) as the molar mass."),
           (2.45 * mm("NaCl"), f"{2.45 * mm('NaCl'):.0f} g", "Used the molar mass of NaCl (58.44).")],
    cite=f"{C8}, slide 27 (Calculating Mass from Moles Practice: NaOH)",
    hw="HW18 — hw18ex2.png (mass in grams from moles: Li, Al, Pb)",
    covers="Moles → grams: multiply by the molar mass.",
    sol="""Molar mass NaOH = 22.99 + 16.00 + 1.008 = 40.00 g/mol.

$$2.45\\ \\text{mol}\\times40.00\\ \\tfrac{\\text{g}}{\\text{mol}} = 98.0\\ \\text{g}$$""",
))

cacl2 = 9.43e-3 / mm("CaCl2")
check(21, cacl2, 8.50e-5, 0.005e-5)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Milligrams to moles", short="Ch 8 sl. 29",
    stem="How many moles of calcium chloride, [[CaCl2]], are in 9.43 mg of the compound?",
    correct=(cacl2, f"{sci(cacl2)} mol", ""),
    wrong=[(9.43 / mm("CaCl2"), f"{sci(9.43 / mm('CaCl2'))} mol", "Didn't convert mg to g (treated 9.43 mg as 9.43 g)."),
           (9.43e-3 / mm("CaCl"), f"{sci(9.43e-3 / mm('CaCl'))} mol", "Wrong formula: CaCl (forgot Ca^2+^ needs two Cl^−^)."),
           (9.43e-3 * mm("CaCl2"), f"{9.43e-3 * mm('CaCl2'):.2f} mol", "Multiplied by the molar mass."),
           (cacl2 * NA, f"{sci(cacl2 * NA)} mol", "That is the number of formula units, not moles.")],
    cite=f"{C8}, slide 29 (LA problem 1: 9.43 mg of calcium chloride), slide 28 (moles from mass)",
    hw="HW19 — hw19ex2.png (moles in 21.9 mg of nitrogen dioxide, ...)",
    covers="Unit conversion (mg → g) before the mole conversion, plus writing the correct ionic formula.",
    sol="""CaCl~2~: 40.08 + 2(35.45) = 110.98 g/mol. Convert mg to g first: 9.43 mg = 9.43 × 10^−3^ g.

$$\\frac{9.43\\times10^{-3}\\ \\text{g}}{110.98\\ \\text{g/mol}} = 8.50\\times10^{-5}\\ \\text{mol}$$""",
))

pct_p = mm("P") / mm("H3PO4") * 100
check(22, pct_p, 31.6, 0.05)
Q.append(dict(
    ch=8, kind="calc", numeric=True, title="Mass percent", short="Ch 8 sl. 30–32",
    stem="What is the mass percent of phosphorus in phosphoric acid, [[H3PO4]]?",
    correct=(31.6, "31.6%", ""),
    wrong=[(3 * mm("H") / mm("H3PO4") * 100, f"{3 * mm('H') / mm('H3PO4') * 100:.2f}%", "This is the mass percent of H."),
           (12.5, "12.5%", "1 P out of 8 atoms is an atom fraction, not a mass fraction."),
           (mm("P") / 64.00 * 100, f"{mm('P') / 64.00 * 100:.1f}%", "Divided by the mass of O only, not the whole molar mass."),
           (64.00 / mm("H3PO4") * 100, f"{64.00 / mm('H3PO4') * 100:.1f}%", "This is the mass percent of O.")],
    cite=f"{C8}, slide 30 (Mass Percent definition), slide 31 (worked ethanol example), slide 32 (Practice: H~3~PO~4~)",
    hw="HW20 — hw20ex1.png / hw20ex3.png (percent by mass of each element: HClO~2~, PCl~5~)",
    covers="Mass percent = (mass of element in 1 mol) / (molar mass) × 100%.",
    sol="""Molar mass H~3~PO~4~ = 3(1.008) + 30.97 + 4(16.00) = 97.99 g/mol.

$$\\%\\text{P} = \\frac{30.97}{97.99}\\times100\\% = 31.6\\%$$

(For a full check: H = 3.09%, O = 65.31%, and 3.09 + 31.6 + 65.31 = 100%.)""",
))

Q.append(dict(
    ch=8, kind="concept", title="Empirical formula", short="Ch 8 sl. 39–40",
    stem="What is the **empirical formula** of glucose, [[C6H12O6]]?",
    correct=T("[[CH2O]]"),
    wrong=[T("[[C6H12O6]]", "That is the molecular formula."),
           T("[[C2H4O2]]", "Same ratio but not the smallest whole numbers (÷2 only; ÷6 is possible)."),
           T("[[CHO]]", "The H:C ratio is 2:1, not 1:1."),
           T("[[C3H6O3]]", "Same ratio but not reduced to the smallest whole numbers.")],
    cite=f"{C8}, slide 39 (Empirical and Molecular Formulas: C~6~H~12~O~6~ → CH~2~O), slide 48",
    hw="HW20 — empirical formula for benzoic acid, C~7~H~6~O~2~ (already in simplest form)",
    covers="Empirical formula = smallest whole-number ratio; molecular formula = (empirical)~n~.",
    sol="""Divide every subscript by their greatest common factor, 6: C~6/6~H~12/6~O~6/6~ = **CH~2~O**. Slide 39 uses glucose
as the example: "The empirical formula for both is CH~2~O." """,
))

pc = {"C": 9.94 / mm("C"), "Cl": 58.6 / mm("Cl"), "F": 31.4 / mm("F")}
small = min(pc.values())
ratio = {k: v / small for k, v in pc.items()}
check(24, ratio["Cl"], 2, 0.05)
check(24, ratio["F"], 2, 0.05)
Q.append(dict(
    ch=8, kind="calc", title="Percent composition to empirical formula", short="Ch 8 sl. 35–38",
    stem="A compound contains 9.94% C, 58.6% Cl, and 31.4% F by mass. What is its empirical formula?",
    correct=T("[[CCl2F2]]"),
    wrong=[T("[[CClF]]", "Didn't divide by the smallest number of moles; the ratio is 1:2:2."),
           T("[[CClF2]]", "Cl moles: 58.6 / 35.45 = 1.65, which is 2× the C moles, not 1×."),
           T("[[C2Cl3F3]]", "Doesn't match the mole ratio 1 : 2 : 2."),
           T("[[CCl2F]]", "F moles (1.65) equal Cl moles, so F also gets a subscript of 2.")],
    cite=f"{C8}, slide 38 (Percent composition to formula: C 9.94%, Cl 58.6%, F 31.4%), slides 35–37 (worked steps), slides 42–43",
    hw="HW21 — empirical formula from percent composition (Mg/S/O → MgSO~4~; Si/Cl/Br → SiCl~2~Br~2~)",
    covers="The slide 35–37 procedure: % → g (100 g sample) → mol → divide by the smallest.",
    sol="""Assume 100 g, so the percentages become grams.

| | grams | ÷ molar mass | moles | ÷ smallest (0.828) |
|:-:|:-:|:-:|:-:|:-:|
| C | 9.94 | 12.01 | 0.828 | 1.00 |
| Cl | 58.6 | 35.45 | 1.653 | 2.00 |
| F | 31.4 | 19.00 | 1.653 | 2.00 |

Empirical formula **CCl~2~F~2~**.""",
))

emp = mm("C4H5N2O")
check(25, 194.14 / emp, 2, 0.01)
Q.append(dict(
    ch=8, kind="calc", title="Empirical to molecular formula", short="Ch 8 sl. 47–49",
    stem="A compound has the empirical formula [[C4H5N2O]] and a molar mass of 194.14 g/mol. What is its molecular formula?",
    correct=T("[[C8H10N4O2]]"),
    wrong=[T("[[C4H5N2O]]", "Assumes n = 1. The empirical mass is 97.10, not 194.14."),
           T("[[C12H15N6O3]]", "n = 3 would give 291 g/mol."),
           T("[[C8H10N4O]]", "Every subscript, including O, has to be multiplied by n."),
           T("[[C16H20N8O4]]", "n = 4 would give 388 g/mol.")],
    cite=f"{C8}, slide 49 (LA Practice: C~4~H~5~N~2~O, MM 194.14), slide 48 ((empirical formula)~n~ = molecular formula), slide 47",
    hw="HW21 — molecular formula from empirical formula + molar mass (CH → C~2~H~2~; C~3~H~7~NO → C~6~H~14~N~2~O~2~)",
    covers="n = molar mass / empirical formula mass; multiply every subscript by n.",
    sol="""Empirical formula mass: 4(12.01) + 5(1.008) + 2(14.01) + 16.00 = 97.10 g/mol.

$$n = \\frac{194.14}{97.10} = 2.00 \\quad\\Rightarrow\\quad (\\text{C}_4\\text{H}_5\\text{N}_2\\text{O})_2 = \\text{C}_8\\text{H}_{10}\\text{N}_4\\text{O}_2$$

(This is caffeine.)""",
))

Q.append(dict(
    ch=8, kind="concept", title="Data needed for a molecular formula", short="Ch 8 sl. 47",
    stem="What experimental information must be known to determine the **molecular** formula of a new compound?",
    correct=T("Its composition by mass **and** its molar mass"),
    wrong=[T("Its composition by mass only", "That is enough for the empirical formula only (slide 47)."),
           T("Its molar mass only", "Many formulas share a molar mass. You need the composition too."),
           T("The mass of the sample and its melting point", "Neither fixes the atom ratio."),
           T("The mass of the sample only", "Gives no information about which elements are present or in what ratio.")],
    cite=f"{C8}, slide 47 (From Empirical to Molecular Formula: 'To obtain the molecular formula we must know the molar mass')",
    hw="HW21 — hw21ex1.png (what evidence is needed for empirical vs molecular formula)",
    covers="Empirical formula needs composition; molecular formula needs composition plus molar mass.",
    sol="""Slide 47: from the masses or mass percentages "we can calculate the empirical formula but not the molecular formula.
To obtain the molecular formula we must know the molar mass." So you need both, which is exactly the HW21 select-all answer.""",
))

# ---------------------------------------------------------------- Chapter 9
Q.append(dict(
    ch=9, kind="concept", title="Meaning of coefficients", short="Ch 9 sl. 2–3",
    stem="For the balanced equation CO(g) + 2[[H2]](g) → [[CH3OH]](l), which statement is correct?",
    correct=T("1 mol of CO reacts with 2 mol of [[H2]] to produce 1 mol of [[CH3OH]]"),
    wrong=[T("1 g of CO reacts with 2 g of [[H2]] to produce 1 g of [[CH3OH]]", "Coefficients are mole (particle) ratios, not mass ratios."),
           T("1 mol of CO reacts with 1 mol of [[H2]] to produce 1 mol of [[CH3OH]]", "Ignores the coefficient 2 on H~2~."),
           T("3 g of reactants produce 1 g of product", "Mass is conserved. Coefficients don't describe grams."),
           T("1 molecule of CO reacts with 2 atoms of H to produce 1 molecule of [[CH3OH]]", "The 2 counts H~2~ *molecules* (4 H atoms).")],
    cite=f"{C9}, slide 3 (Table 9.1, Methanol Production), slide 2 (Information Given by Chemical Equations)",
    hw="HW22 — interpreting H~2~ + F~2~ → 2HF in molecules and in moles",
    covers="Coefficients give relative numbers of molecules or moles, never grams.",
    sol="""Slide 2: "The coefficients in a balanced equation give us the relative numbers of molecules." Table 9.1 reads the same
equation as 1 molecule CO + 2 molecules H~2~ → 1 molecule CH~3~OH, and equally as **1 mol CO + 2 mol H~2~ → 1 mol CH~3~OH**.""",
))

Q.append(dict(
    ch=9, kind="concept", title="Choosing the mole ratio", short="Ch 9 sl. 6–7",
    stem="For [[N2]](g) + 3[[H2]](g) → 2[[NH3]](g), which mole ratio converts **moles of [[H2]]** into **moles of [[NH3]]** produced?",
    correct=T("(2 mol [[NH3]]) / (3 mol [[H2]])"),
    wrong=[T("(3 mol [[H2]]) / (2 mol [[NH3]])", "Upside down. The unit you want (NH~3~) goes on top."),
           T("(2 mol [[NH3]]) / (1 mol [[N2]])", "This ratio starts from N~2~, not H~2~."),
           T("(1 mol [[NH3]]) / (3 mol [[H2]])", "The coefficient of NH~3~ is 2."),
           T("(17.03 g [[NH3]]) / (2.016 g [[H2]])", "That is a ratio of molar masses, not a mole ratio.")],
    cite=f"{C9}, slide 7 (Mole Ratios Practice: N~2~ + 3H~2~ → 2NH~3~), slide 6 (Mole Ratios)",
    hw="HW22 — choosing the mole ratio for 4B + 3O~2~ → 2B~2~O~3~",
    covers="Writing mole ratios from coefficients and orienting them so the units cancel.",
    sol="""From the coefficients, 3 mol H~2~ ⇔ 2 mol NH~3~. To convert *from* H~2~ *to* NH~3~, put H~2~ on the bottom so it
cancels: mol H~2~ × (2 mol NH~3~ / 3 mol H~2~).""",
))

fe = 17.5 * 2 / 3
check(29, fe, 11.7, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Mole–mole conversion", short="Ch 9 sl. 10",
    stem="For [[Fe2O3]](s) + 3CO(g) → 2Fe(s) + 3[[CO2]](g), how many moles of Fe can be produced from 17.5 mol of CO?",
    correct=(11.7, "11.7 mol", ""),
    wrong=[(5.83, "5.83 mol", "Used 1/3 (forgot the 2 on Fe)."),
           (17.5, "17.5 mol", "Assumed a 1:1 ratio."),
           (26.3, "26.3 mol", "Inverted the ratio (3/2)."),
           (35.0, "35.0 mol", "Multiplied by 2 only (forgot the 3 on CO).")],
    cite=f"{C9}, slide 10 (Mole–Mole Conversions Practice: Fe~2~O~3~ + 3CO → 2Fe + 3CO~2~, 17.5 mol CO)",
    hw="HW22 — moles of product from moles (e.g. Fe~2~O~3~ + Al: mol Fe from 0.660 mol Al~2~O~3~)",
    covers="mol given × (coefficient wanted / coefficient given).",
    sol="""$$17.5\\ \\text{mol CO}\\times\\frac{2\\ \\text{mol Fe}}{3\\ \\text{mol CO}} = 11.7\\ \\text{mol Fe}$$""",
))

Q.append(dict(
    ch=9, kind="concept", title="Definition of theoretical yield", short="Ch 9 sl. 25, 28",
    stem="The **theoretical yield** of a reaction is:",
    correct=T("the amount of product predicted from the amount of the limiting reactant"),
    wrong=[T("the amount of product actually obtained in the laboratory", "That is the actual yield (slide 28)."),
           T("(actual yield ÷ theoretical yield) × 100%", "That is the percent yield (slide 30)."),
           T("the amount of product predicted from the amount of the excess reactant", "The excess reactant doesn't run out, so it doesn't limit the product."),
           T("the total mass of all reactants added", "Reactants left in excess don't become product.")],
    cite=f"{C9}, slide 25 (Theoretical Yield), slide 28 (Actual Yield), slide 30 (Percent Yield)",
    hw="HW24 — theoretical yield vs percent yield (XeF~4~, Na~2~S~2~O~3~·5H~2~O)",
    covers="Telling theoretical, actual, and percent yield apart (course definitions).",
    sol="""Slide 25: the amount of product calculated from the limiting reactant "is called the theoretical yield ... the amount of
product predicted from the amounts of reactants used." Slide 28 calls it "the maximum amount of product that can be produced."
""",
))

so3 = 2.33 * 2 * mm("SO3")
check(31, so3, 373, 0.5)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Moles to grams of product", short="Ch 9 sl. 14, 17",
    stem="For 2[[SO2]](g) + [[O2]](g) → 2[[SO3]](g), how many grams of [[SO3]] can be produced from 2.33 mol of [[O2]]?",
    correct=(373, "373 g", ""),
    wrong=[(4.66, "4.66 g", "That is the moles of SO~3~; it still has to be converted to grams."),
           (2.33 * mm("SO2"), f"{2.33 * mm('SO2'):.0f} g", "1:1 ratio and the molar mass of SO~2~."),
           (2.33 * mm("SO3"), f"{2.33 * mm('SO3'):.0f} g", "Assumed 1:1 (forgot the 2 mol SO~3~ per mol O~2~)."),
           (4.66 * mm("SO2"), f"{4.66 * mm('SO2'):.0f} g", "Used the molar mass of SO~2~ instead of SO~3~.")],
    cite=f"{C9}, slide 17 (Stoichiometry Practice: 2SO~2~ + O~2~ → 2SO~3~, 2.33 mol O~2~), slide 14 (Steps for calculating masses)",
    hw="HW23 — mass of product from mass of reactant (CaC~2~ → C~2~H~2~; Fe + Cl~2~ → FeCl~3~)",
    covers="mol given → mol wanted (mole ratio) → grams (molar mass).",
    sol="""$$2.33\\ \\text{mol O}_2\\times\\frac{2\\ \\text{mol SO}_3}{1\\ \\text{mol O}_2}\\times\\frac{80.07\\ \\text{g SO}_3}{1\\ \\text{mol SO}_3} = 4.66\\times80.07 = 373\\ \\text{g}$$""",
))

no_mol = 54.7 / mm("NO")
o2_g = no_mol * 5 / 4 * mm("O2")
check(32, o2_g, 72.9, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Grams to grams", short="Ch 9 sl. 14, 19",
    stem="For 4[[NH3]](g) + 5[[O2]](g) → 4NO(g) + 6[[H2O]](g), how many grams of [[O2]] are needed to produce 54.7 g of NO?",
    correct=(72.9, "72.9 g", ""),
    wrong=[(no_mol * 5 / 4, f"{no_mol * 5 / 4:.2f} g", "That is the moles of O~2~, not grams."),
           (no_mol * 4 / 5 * mm("O2"), f"{no_mol * 4 / 5 * mm('O2'):.1f} g", "Inverted the mole ratio (4/5)."),
           (54.7, "54.7 g", "Assumed the grams of O~2~ equal the grams of NO."),
           (no_mol * mm("O2"), f"{no_mol * mm('O2'):.1f} g", "Assumed a 1:1 mole ratio.")],
    cite=f"{C9}, slide 19 (Stoichiometry Practice 3: 4NH~3~ + 5O~2~ → 4NO + 6H~2~O, 54.7 g NO), slide 14",
    hw="HW23 — grams of bromine from 34.0 g of bromine trifluoride",
    covers="The full g → mol → mol → g path from slide 14.",
    sol="""$$54.7\\ \\text{g NO}\\times\\frac{1\\ \\text{mol}}{30.01\\ \\text{g}} = 1.823\\ \\text{mol NO}$$

$$1.823\\ \\text{mol NO}\\times\\frac{5\\ \\text{mol O}_2}{4\\ \\text{mol NO}} = 2.278\\ \\text{mol O}_2;\\quad 2.278\\times32.00 = 72.9\\ \\text{g O}_2$$""",
))

al_mol = 17.9 / mm("Al")
o2_need = al_mol * 3 / 4
o2_have = 64 / mm("O2")
assert o2_need < o2_have
print(f"OK  Q33: Al {al_mol:.4f} mol needs {o2_need:.4f} mol O2, have {o2_have:.4f} -> Al limiting")
Q.append(dict(
    ch=9, kind="calc", title="Identifying the limiting reactant", short="Ch 9 sl. 21–24",
    stem="For 4Al(s) + 3[[O2]](g) → 2[[Al2O3]](s), 17.9 g of Al reacts with 64 g of [[O2]]. Which statement is correct?",
    correct=T("Al is the limiting reactant"),
    wrong=[T("[[O2]] is the limiting reactant", "You need only 0.498 mol O~2~ and there are 2.0 mol, so O~2~ is in excess."),
           T("Neither; the reactants are present in exactly the stoichiometric ratio", "0.663 mol Al : 2.0 mol O~2~ is not 4 : 3."),
           T("[[Al2O3]] is the limiting reactant", "A product can never be the limiting reactant."),
           T("[[O2]] is the limiting reactant because its coefficient is smaller", "Coefficients alone don't decide it. Compare moles available with moles needed.")],
    cite=f"{C9}, slide 24 (Limiting Reactants Practice 2: 4Al + 3O~2~, 17.9 g Al, 64 g O~2~), slides 21–22",
    hw="HW23 — 5.65 g of each reactant: determine the limiting reactant (S + H~2~SO~4~; MnO~2~ + H~2~SO~4~)",
    covers="Convert both reactants to moles, then use the mole ratio to see which one runs out first.",
    sol="""$$\\text{Al: } \\frac{17.9}{26.98} = 0.663\\ \\text{mol};\\qquad \\text{O}_2\\text{: } \\frac{64}{32.00} = 2.0\\ \\text{mol}$$

O~2~ needed for all the Al: 0.663 × (3/4) = 0.498 mol. That is less than the 2.0 mol available, so **Al runs out first and is
the limiting reactant**.""",
))

na_mol = 68 / mm("Na")
cl2_mol = 97 / mm("Cl2")
nacl = min(na_mol, 2 * cl2_mol) * mm("NaCl")
check(34, nacl, 160, 0.5)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Theoretical yield with a limiting reactant", short="Ch 9 sl. 25–27",
    stem="For 2Na(s) + [[Cl2]](g) → 2NaCl(s), 68 g of Na reacts with 97 g of [[Cl2]]. What is the theoretical yield of NaCl?",
    correct=(160, "160 g", ""),
    wrong=[(2 * cl2_mol, f"{2 * cl2_mol:.2f} g", "That is the moles of NaCl, not grams."),
           (cl2_mol * mm("NaCl"), f"{cl2_mol * mm('NaCl'):.0f} g", "Cl~2~ limiting but used a 1:1 ratio (forgot the 2 NaCl)."),
           (165, "165 g", "Added the reactant masses. Na is left over, so it doesn't all become product."),
           (na_mol * mm("NaCl"), f"{na_mol * mm('NaCl'):.0f} g", "Used Na as the limiting reactant (Cl~2~ actually runs out first).")],
    cite=f"{C9}, slide 27 (Theoretical Yield Practice 2: 68 g Na + 97 g Cl~2~), slides 25–26",
    hw="HW24 — hw24ex2.png (theoretical mass of XeF~4~ from 173 g Xe + 104 g F~2~)",
    covers="Find the limiting reactant, then calculate the product from it.",
    sol="""$$\\text{Na: } \\frac{68}{22.99} = 2.958\\ \\text{mol};\\qquad \\text{Cl}_2\\text{: } \\frac{97}{70.90} = 1.368\\ \\text{mol}$$

Na needed for all the Cl~2~: 1.368 × 2 = 2.736 mol. You have 2.958 mol, so Na is in excess and **Cl~2~ is limiting**.

$$1.368\\ \\text{mol Cl}_2\\times\\frac{2\\ \\text{mol NaCl}}{1\\ \\text{mol Cl}_2}\\times\\frac{58.44\\ \\text{g}}{\\text{mol}} = 160\\ \\text{g NaCl}$$""",
))

kcl_theo = 191 / mm("KClO3") * mm("KCl")
pct = 89.9 / kcl_theo * 100
check(35, pct, 77.4, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Percent yield", short="Ch 9 sl. 30–32",
    stem="For 2[[KClO3]](s) → 2KCl(s) + 3[[O2]](g), 191 g of [[KClO3]] decomposes and 89.9 g of KCl is actually collected. What is the percent yield?",
    correct=(77.4, "77.4%", ""),
    wrong=[(89.9 / 191 * 100, f"{89.9 / 191 * 100:.1f}%", "Divided by the mass of reactant, not the theoretical yield of KCl."),
           (89.9 / (kcl_theo * 1.5) * 100, f"{89.9 / (kcl_theo * 1.5) * 100:.1f}%", "Used the 3 from O~2~ in the ratio (3/2 instead of 2/2)."),
           (116, "116%", "That number is the theoretical yield in grams, not a percent."),
           (kcl_theo / 89.9 * 100, f"{kcl_theo / 89.9 * 100:.0f}%", "Upside down: theoretical / actual. Percent yield can't be over 100%.")],
    cite=f"{C9}, slide 32 (Percent Yield Practice 2: 191 g KClO~3~, 89.9 g KCl), slide 30 (formula), slide 29",
    hw="HW24 — hw24ex1.png (percent yield of magnesium oxide; Na~2~S~2~O~3~·5H~2~O)",
    covers="Theoretical yield by stoichiometry, then (actual / theoretical) × 100%.",
    sol="""$$191\\ \\text{g KClO}_3\\times\\frac{1\\ \\text{mol}}{122.55\\ \\text{g}}\\times\\frac{2\\ \\text{mol KCl}}{2\\ \\text{mol KClO}_3}\\times\\frac{74.55\\ \\text{g}}{\\text{mol}} = 116.2\\ \\text{g KCl (theoretical)}$$

$$\\%\\ \\text{yield} = \\frac{89.9}{116.2}\\times100\\% = 77.4\\%$$""",
))

if __name__ == "__main__":
    assert len(Q) == 35, len(Q)
    build(1, Q, seed=31)
