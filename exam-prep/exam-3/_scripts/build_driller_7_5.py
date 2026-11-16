"""Build driller-7-5: reaction types (acid–base, redox, classification), 15 questions.

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_driller_7_5.py
"""
from rxndrill import (AB, AB_PRAC, CLS, CLS_PRAC, HW16_BASE, HW16_RX, HW16_SALT, HW17_CLS, HW17_COMB, HW17_WORDS, RX,
                      RX_PRAC, T, balanced, build, num)

balanced([(3, "H2SO4"), (2, "Al(OH)3")], [(1, "Al2(SO4)3"), (6, "H2O")])
balanced([(2, "Al"), (3, "S")], [(1, "Al2S3")])
balanced([(2, "Al"), (3, "Br2")], [(2, "AlBr3")])
balanced([(1, "C5H12"), (8, "O2")], [(5, "CO2"), (6, "H2O")])
balanced([(1, "H2SO4"), (2, "KOH")], [(1, "K2SO4"), (2, "H2O")])

Q = [
    # ------------------------------------------------------------ 7.6 acid–base
    dict(title="Arrhenius acid", short="Ch 7 sl. 21",
         stem="According to the Arrhenius definition used in this course, an **acid** is a substance that:",
         correct=T("produces H^+^ ions (protons) when it is dissolved in water"),
         wrong=[T("produces hydroxide ions ([[OH^-^]]) when it is dissolved in water", "That is an Arrhenius **base** (slide 22)."),
                T("forms a precipitate when mixed with a base",
                  "Acid–base reactions form water and a salt; the salt usually stays dissolved (slide 23)."),
                T("always contains oxygen", "HCl has no oxygen and is a strong acid."),
                T("gains electrons from a metal", "Electron transfer defines oxidation–reduction, not acids.")],
         cite=f"{AB.split(',')[0]}, slide 21 (Arrhenius Acids)", hw=HW16_BASE,
         covers="Course definition of an Arrhenius acid.",
         sol="Slide 21: Arrhenius proposed that an **acid** is a substance that **produces H^+^ ions (protons) when dissolved in "
             "water**. Its partner definition (slide 22): a **base** produces OH^−^ ions in water."),
    dict(title="Strong acids", short="Ch 7 sl. 21, 24",
         stem="Which pair contains **only** strong acids?",
         correct=T("HCl and [[H2SO4]]"),
         wrong=[T("[[HNO3]] and [[HNO2]]", "HNO~3~ is strong, but HNO~2~ (nitrous acid, 2 O) isn't on the course's list."),
                T("HF and HCl", "HCl is strong, but HF isn't one of the strong acids."),
                T("[[H3PO4]] and [[H2SO4]]", "H~2~SO~4~ is strong, but H~3~PO~4~ isn't on the course's list."),
                T("[[HC2H3O2]] and [[HNO3]]", "HNO~3~ is strong, but acetic acid, HC~2~H~3~O~2~, isn't.")],
         cite=f"{AB.split(',')[0]}, slide 21 (HCl, HNO~3~, H~2~SO~4~ are strong acids), slide 24 (principle 1)", hw=HW16_BASE,
         covers="The course's strong-acid list: HCl, HNO~3~, H~2~SO~4~.",
         sol="Slide 24, principle 1: the common strong acids are **HCl, HNO~3~, and H~2~SO~4~**. Only one choice has two acids "
             "from that list: **HCl and H~2~SO~4~**. Every other pair includes an acid not on the list (HNO~2~, HF, H~3~PO~4~, "
             "HC~2~H~3~O~2~)."),
    dict(title="The salt formed", short="Ch 7 sl. 23, 26",
         stem="What **salt** forms when sulfuric acid reacts completely with potassium hydroxide? "
              "[[H2SO4]](aq) + 2KOH(aq) → ? + 2[[H2O]](l)",
         correct=T("[[K2SO4]]"),
         wrong=[T("[[KSO4]]", "K^+^ is +1 and SO~4~^2−^ is −2, so two K^+^ are needed: K~2~SO~4~."),
                T("[[K(SO4)2]]", "That would have charge +1 + 2(−2) = −3. A salt must be neutral."),
                T("[[H2O]]", "Water is the **other** product. The salt is the ionic compound."),
                T("KOH", "KOH is the base, a reactant.")],
         cite=f"{AB.split(',')[0]}, slide 23 (the second product is a salt), slide 26 (principle 5)", hw=HW16_SALT,
         covers="Building the salt: the base's cation with the acid's anion, charges balanced.",
         sol="""**Step 1: find the ions.** The acid gives H^+^ and SO~4~^2−^; the base gives K^+^ and OH^−^.

**Step 2: H^+^ + OH^−^ make water** (slide 23). What remains, K^+^ with SO~4~^2−^, is the salt.

**Step 3: write it neutral.** K^+^ is +1 and SO~4~^2−^ is −2, so you need 2 K^+^: **K~2~SO~4~**. The balanced equation is
H~2~SO~4~ + 2KOH → K~2~SO~4~ + 2H~2~O."""),
    dict(title="Net ionic equation for an acid–base reaction", short="Ch 7 sl. 23–26",
         stem="Hydrochloric acid reacts with potassium hydroxide: HCl(aq) + KOH(aq) → KCl(aq) + [[H2O]](l). "
              "What is the **net ionic** equation?",
         correct=T("H^+^(aq) + [[OH^-^]](aq) → [[H2O]](l)"),
         wrong=[T("HCl(aq) + [[OH^-^]](aq) → Cl^−^(aq) + [[H2O]](l)",
                  "HCl is a strong acid: it completely dissociates (slide 24), so write it as H^+^ and Cl^−^; Cl^−^ then cancels."),
                T("K^+^(aq) + Cl^−^(aq) → KCl(s)", "KCl is soluble (rules 2 and 3). K^+^ and Cl^−^ are spectators."),
                T("H^+^(aq) + Cl^−^(aq) + K^+^(aq) + [[OH^-^]](aq) → K^+^(aq) + Cl^−^(aq) + [[H2O]](l)",
                  "That's the **complete** ionic equation. Cancel the spectators."),
                T("HCl(aq) + KOH(aq) → KCl(aq) + [[H2O]](l)", "That's the **molecular** equation.")],
         cite=f"{AB.split(',')[0]}, slide 23 (HCl + NaOH: the net ionic equation shows water forming), slide 25 (principle 4)",
         hw="HW16 — hw16ex1.png (the same net ionic process for any strong acid and strong base)",
         covers="Acid–base net ionic equation: H^+^ + OH^−^ → H~2~O; the salt's ions are spectators.",
         sol="""**Step 1: strong electrolytes as ions.** HCl → H^+^ + Cl^−^ (strong acid, slide 24); KOH → K^+^ + OH^−^ (strong base);
KCl (soluble) → K^+^ + Cl^−^.

**Step 2: complete ionic.** H^+^ + Cl^−^ + K^+^ + OH^−^ → K^+^ + Cl^−^ + H~2~O(l)

**Step 3: cancel K^+^ and Cl^−^.** **H^+^(aq) + OH^−^(aq) → H~2~O(l)**, the net ionic equation slide 23 shows for every
acid–base reaction."""),
    dict(title="Balancing an acid–base equation", short="Ch 7 sl. 27",
         stem="When the equation below is balanced with the smallest whole-number coefficients, what is the coefficient of water?\n\n"
              "\\_\\_ [[H2SO4]](aq) + \\_\\_ [[Al(OH)3]](s) → \\_\\_ [[Al2(SO4)3]](aq) + \\_\\_ [[H2O]](l)",
         **num(6, [(2, "That is the coefficient of Al(OH)~3~."), (3, "That is the coefficient of H~2~SO~4~."),
                   (4, "Doesn't balance H: 3H~2~SO~4~ + 2Al(OH)~3~ have 12 H, which make 6 H~2~O."),
                   (12, "12 is the number of H **atoms**; each H~2~O uses 2 of them.")]),
         cite=f"{AB_PRAC.split(',')[0]}, slide 27 (balance H~3~PO~4~ + Ca(OH)~2~ → Ca~3~(PO~4~)~2~ + H~2~O)",
         hw="HW17 — hw17ex2.png (balancing with the lowest whole-number coefficients)",
         covers="Balancing an acid–base reaction: metal first, then the polyatomic ion as a unit, then H and O.",
         sol="""**Step 1: balance Al.** Al~2~(SO~4~)~3~ has 2 Al, so put **2** in front of Al(OH)~3~.

**Step 2: balance SO~4~ as a unit.** Al~2~(SO~4~)~3~ has 3 SO~4~, so put **3** in front of H~2~SO~4~.

**Step 3: balance H and O with water.** Left: 3 H~2~SO~4~ give 6 H^+^, and 2 Al(OH)~3~ give 6 OH^−^. Each H^+^ + OH^−^ makes
one H~2~O, so **6 H~2~O**. Check H: 6 + 6 = 12 left, 6 × 2 = 12 right. O (outside sulfate): 6 left, 6 right.

3H~2~SO~4~ + 2Al(OH)~3~ → Al~2~(SO~4~)~3~ + **6**H~2~O."""),
    # ------------------------------------------------------------ 7.7 oxidation–reduction
    dict(title="Which reaction is redox?", short="Ch 7 sl. 30–32",
         stem="Which reaction is an **oxidation–reduction** reaction?",
         correct=T("2Mg(s) + [[O2]](g) → 2MgO(s)"),
         wrong=[T("[[AgNO3]](aq) + NaCl(aq) → AgCl(s) + [[NaNO3]](aq)", "Precipitation: ions swap partners, and every ion keeps its charge."),
                T("HCl(aq) + NaOH(aq) → NaCl(aq) + [[H2O]](l)", "Acid–base: H^+^ ends up in water. No electrons move."),
                T("[[CaCO3]](s) + 2HCl(aq) → [[CaCl2]](aq) + [[H2O]](l) + [[CO2]](g)",
                  "Gas evolution / acid–base. Every ion keeps its charge."),
                T("[[BaCl2]](aq) + [[Na2SO4]](aq) → [[BaSO4]](s) + 2NaCl(aq)", "Precipitation (double-displacement); no electron transfer.")],
         cite=f"{RX.split(',')[0]}, slide 30 (redox = transfer of electrons), slide 31 (principle 1: metal + nonmetal), slide 32", hw=HW17_CLS,
         covers="Spotting redox: a metal + nonmetal (both elements), or O~2~ as a reactant or product.",
         sol="""A redox reaction transfers electrons (slide 30). The two clues from slides 31–32 are a **metal reacting with a nonmetal**
(always redox) and **O~2~ appearing** as a reactant or product.

2Mg + O~2~ → 2MgO has both: Mg (a metal) reacts with O~2~ (a nonmetal). Each Mg atom loses 2 electrons to become Mg^2+^,
and each O atom gains 2 to become O^2−^. In the other four, every ion keeps its charge; they only swap partners or form
water or gas."""),
    dict(title="Electrons per atom", short="Ch 7 sl. 31, 33",
         stem="In the reaction 2Al(s) + 3S(s) → [[Al2S3]](s), how many electrons does **each sulfur atom** gain?",
         **num(2, [(1, "That would make S^−^. In Al~2~S~3~, sulfur is S^2−^ (2 Al^3+^ balance 3 S^2−^)."),
                   (3, "That is what each **Al** atom loses (Al → Al^3+^)."),
                   (4, "No ion here has a charge of 4."),
                   (6, "That is the total for one Al~2~S~3~ formula unit (3 S × 2), not per S atom.")]),
         cite=f"{RX_PRAC.split(',')[0]}, slide 33 (electrons from each Al atom: 2Al + N~2~), slide 31, slide 38", hw=HW16_RX,
         covers="Electrons gained per nonmetal atom = the size of its ion's charge.",
         sol="""**Step 1: find the ions.** Al~2~S~3~ is ionic (metal + nonmetal), made of Al^3+^ and S^2−^. Check: 2(+3) + 3(−2) = 0.

**Step 2: read the electrons.** Each S atom goes from 0 to −2, so it **gains 2 electrons**. (Each Al goes 0 → +3 and loses 3.)

**Check:** 2 Al × 3 = 6 lost and 3 S × 2 = 6 gained."""),
    dict(title="Electrons in a single replacement", short="Ch 7 sl. 34, 40",
         stem="For Mg(s) + [[CuCl2]](aq) → [[MgCl2]](aq) + Cu(s), which statement is correct?",
         correct=T("Each Mg atom loses 2 electrons and each Cu^2+^ ion gains 2 electrons; Cl^−^ is unchanged"),
         wrong=[T("Each Mg atom gains 2 electrons and each Cu^2+^ ion loses 2 electrons",
                  "Backwards. Mg goes from 0 to +2 (loses); Cu^2+^ goes from +2 to 0 (gains)."),
                T("The Cl^−^ ions lose electrons to the magnesium", "Cl^−^ is −1 before and after. It's a spectator."),
                T("No electrons are transferred; this is a double-displacement reaction",
                  "Only one anion (Cl^−^) moves, from Cu^2+^ to Mg^2+^: single replacement, which is always redox."),
                T("Each Mg atom loses 1 electron and each Cu^2+^ ion gains 1 electron", "Mg becomes Mg^2+^, so the count is 2, not 1.")],
         cite=f"{RX_PRAC.split(',')[0]}, slide 34 (Cu + FeCl~2~: electrons lost or gained by each species), slide 40 (single replacement)",
         hw="HW17 — hw17ex1.png (HCl + Fe: oxidation–reduction)",
         covers="Tracking charges in a single replacement: the metal loses electrons, the metal ion gains them.",
         sol="""**Step 1: charges before and after.** Mg: 0 → +2 (in MgCl~2~). Cu: +2 (in CuCl~2~) → 0. Cl: −1 → −1.

**Step 2: electrons.** Going from 0 to +2 means **Mg loses 2 e^−^**; going from +2 to 0 means **Cu^2+^ gains 2 e^−^**. Cl^−^
doesn't change, so it is a spectator. This is the same pattern as slide 34 (Cu + FeCl~2~)."""),
    dict(title="Redox between two nonmetals", short="Ch 7 sl. 32",
         stem="Two **nonmetals** react. According to the course, how can you tell at this point that the reaction is an "
              "oxidation–reduction reaction?",
         correct=T("[[O2]] appears as a reactant or a product"),
         wrong=[T("An ionic compound forms", "When two nonmetals react, the compound formed is **not** ionic (slide 32)."),
                T("A precipitate forms", "A solid forming signals precipitation, not redox."),
                T("Water is one of the products", "Forming water is the acid–base clue."),
                T("All the coefficients in the balanced equation are 1", "Coefficients have nothing to do with electron transfer.")],
         cite=f"{RX.split(',')[0]}, slide 32 (principle 2: two nonmetals; recognize by O~2~ as a reactant or product)", hw=HW17_CLS,
         covers="Redox principle 2 and how the course recognizes nonmetal–nonmetal redox.",
         sol="Slide 32, principle 2: two nonmetals can also undergo oxidation–reduction. **At this point, we recognize these cases "
             "only by looking for O~2~ as a reactant or product.** When two nonmetals react, the compound formed is not ionic."),
    # ------------------------------------------------------------ 7.8 classification
    dict(title="Classifying a reaction", short="Ch 7 sl. 35–39",
         stem="Classify [[H2SO4]](aq) + 2KOH(aq) → [[K2SO4]](aq) + 2[[H2O]](l).",
         correct=T("acid–base only"),
         wrong=[T("precipitation only", "No solid forms; K~2~SO~4~ is soluble (rule 2)."),
                T("oxidation–reduction only", "Every ion keeps its charge; no electrons move."),
                T("acid–base and precipitation", "Acid–base yes, but nothing precipitates."),
                T("acid–base and oxidation–reduction", "No electron transfer; H^+^ and OH^−^ just form water.")],
         cite=f"{CLS.split(',')[0]}, slide 37 (acid–base: H^+^ ends up in water), slides 35, 38", hw=HW17_CLS,
         covers="HW17-style classification: precipitation, acid–base, and/or oxidation–reduction.",
         sol="""Check each class:

* **Acid–base?** Yes. H~2~SO~4~ is an acid, and its H^+^ ends up in **water** (slide 37).
* **Precipitation?** No. All products are (aq) or (l); K~2~SO~4~ is soluble.
* **Oxidation–reduction?** No. K stays +1, SO~4~ stays −2, H stays +1. No electrons move."""),
    dict(title="Classifying by type", short="Ch 7 sl. 41–44",
         stem="Heating limestone gives [[CaCO3]](s) → CaO(s) + [[CO2]](g). This is best classified as:",
         correct=T("decomposition"),
         wrong=[T("synthesis", "Synthesis builds one compound from simpler materials; here one compound breaks apart."),
                T("combustion", "Combustion needs O~2~ as a reactant and gives a flame."),
                T("single-replacement", "No element replaces another."),
                T("acid–base", "No acid, no base, no water formed.")],
         cite=f"{CLS.split(',')[0]}, slide 43 (decomposition, usually by heating or electric current), slide 44", hw=HW17_WORDS,
         covers="Decomposition: one compound → simpler substances, usually with heat or electric current.",
         sol="One reactant, **CaCO~3~**, breaks into two simpler substances, CaO and CO~2~, when heated. Slide 43: a compound broken down "
             "into simpler compounds or elements, usually by **heating** or an electric current, is a **decomposition** reaction."),
    dict(title="A reaction in several classes", short="Ch 7 sl. 38, 41–42",
         stem="Sulfur burns in air: S(s) + [[O2]](g) → [[SO2]](g), releasing heat and a flame. Which classes apply?",
         correct=T("synthesis, combustion, and oxidation–reduction"),
         wrong=[T("synthesis only", "It also reacts with O~2~ with a flame (combustion), and O~2~ means redox."),
                T("combustion only", "One compound forms from two elements, which is also synthesis, and O~2~ means redox."),
                T("decomposition and oxidation–reduction", "Two elements combine; nothing breaks apart."),
                T("synthesis and acid–base", "No acid, base, or water.")],
         cite=f"{CLS.split(',')[0]}, slide 41 (combustion), slide 42 (synthesis), slide 32 (O~2~ signals redox)", hw=HW17_CLS,
         covers="One reaction can belong to several classes.",
         sol="""* **Synthesis:** one compound (SO~2~) forms from simpler materials (S and O~2~) (slide 42).
* **Combustion:** a reaction with **oxygen** that releases energy so fast a **flame** results (slide 41).
* **Oxidation–reduction:** O~2~ is a reactant, which is the course's clue for nonmetal redox (slide 32).

All three apply."""),
    dict(title="Double-displacement", short="Ch 7 sl. 36",
         stem="A **double-displacement** (double-exchange) reaction is one in which:",
         correct=T("two anions exchange their cation partners"),
         wrong=[T("one element replaces another element in a compound", "That's **single** replacement (slide 40)."),
                T("one compound breaks into simpler substances", "That's decomposition (slide 43)."),
                T("a substance reacts with oxygen and produces a flame", "That's combustion (slide 41)."),
                T("electrons move from a metal to a nonmetal", "That's oxidation–reduction (slide 31).")],
         cite=f"{CLS.split(',')[0]}, slide 36 (Double-Displacement Reactions: the anions NO~3~^−^ and CrO~4~^2−^ exchange)",
         hw=HW17_CLS, covers="Course definition of double-displacement.",
         sol="Slide 36: in K~2~CrO~4~ + Ba(NO~3~)~2~ → BaCrO~4~ + 2KNO~3~, the two anions (NO~3~^−^ and CrO~4~^2−^) are simply "
             "**exchanged**: NO~3~^−^ starts with Ba^2+^ and ends with K^+^. Because of this double exchange, it's called a "
             "**double-exchange** or **double-displacement** reaction."),
    dict(title="Balancing from words", short="Ch 7 sl. 42",
         stem="Aluminum metal combines with bromine, [[Br2]], to form aluminum bromide, [[AlBr3]]. In the balanced equation with "
              "the smallest whole-number coefficients, what is the coefficient of [[Br2]]?",
         **num(3, [(1, "Al + Br~2~ → AlBr~3~ isn't balanced: 2 Br on the left, 3 on the right."),
                   (2, "That is the coefficient of Al and of AlBr~3~."),
                   (4, "4 Br~2~ would give 8 Br, which can't match AlBr~3~ in whole numbers with the smallest coefficients."),
                   (6, "6 is the number of Br **atoms**; Br~2~ supplies them in pairs.")]),
         cite=f"{CLS_PRAC.split(',')[0]}, slide 42 (synthesis: 2Na + Cl~2~ → 2NaCl, Mg + F~2~ → MgF~2~)", hw=HW17_WORDS,
         covers="Writing a synthesis from words and balancing a diatomic element.",
         sol="""**Step 1: write the formulas.** Al + Br~2~ → AlBr~3~ (bromine is diatomic, Br~2~).

**Step 2: balance Br.** The left has Br in pairs (2) and the right has 3 per AlBr~3~. The smallest common multiple is 6, so use
**3**Br~2~ and **2**AlBr~3~.

**Step 3: balance Al.** 2AlBr~3~ has 2 Al, so 2Al: **2Al + 3Br~2~ → 2AlBr~3~**."""),
    dict(title="Balancing a combustion", short="Ch 7 sl. 41",
         stem="Pentane burns completely: \\_\\_ [[C5H12]] + \\_\\_ [[O2]] → \\_\\_ [[CO2]] + \\_\\_ [[H2O]]. With the smallest "
              "whole-number coefficients, what is the coefficient of [[O2]]?",
         **num(8, [(5, "That is the coefficient of CO~2~."), (6, "That is the coefficient of H~2~O."),
                   (11, "Counted the O atoms needed (16) wrong; 5 CO~2~ have 10 O and 6 H~2~O have 6 O."),
                   (16, "16 is the number of O **atoms**; O~2~ supplies them in pairs, so 16 ÷ 2 = 8.")]),
         cite=f"{CLS.split(',')[0]}, slide 41 (Combustion: CH~4~ + 2O~2~ → CO~2~ + 2H~2~O)", hw=HW17_COMB,
         covers="Balancing combustion: C first, then H, then O last.",
         sol="""**Step 1: C.** 5 C on the left → **5**CO~2~.

**Step 2: H.** 12 H on the left → **6**H~2~O (6 × 2 = 12).

**Step 3: O.** The right now has 5(2) + 6(1) = 16 O atoms. O~2~ supplies 2 each, so 16 ÷ 2 = **8**O~2~.

C~5~H~12~ + **8**O~2~ → 5CO~2~ + 6H~2~O."""),
]

if __name__ == "__main__":
    build(5, Q)
