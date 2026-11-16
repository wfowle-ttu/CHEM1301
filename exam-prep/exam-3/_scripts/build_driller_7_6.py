"""Build driller-7-6: reaction types (acid–base, redox, classification), 15 questions.

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_driller_7_6.py
"""
from rxndrill import (AB, AB_PRAC, C7, CLS, CLS_PRAC, HW16_BASE, HW16_RX, HW16_SALT, HW17_CLS, HW17_COMB, HW17_WORDS, RX,
                      RX_PRAC, T, balanced, build, num)

balanced([(1, "H3PO4"), (3, "KOH")], [(1, "K3PO4"), (3, "H2O")])
balanced([(3, "Ca"), (1, "N2")], [(1, "Ca3N2")])
balanced([(2, "Na"), (2, "H2O")], [(2, "NaOH"), (1, "H2")])
balanced([(2, "C6H14"), (19, "O2")], [(12, "CO2"), (14, "H2O")])
balanced([(2, "HNO3"), (1, "Ca(OH)2")], [(1, "Ca(NO3)2"), (2, "H2O")])
balanced([(1, "Cu"), (2, "AgNO3")], [(1, "Cu(NO3)2"), (2, "Ag")])

Q = [
    # ------------------------------------------------------------ 7.6 acid–base
    dict(title="Arrhenius base", short="Ch 7 sl. 22",
         stem="According to the Arrhenius definition used in this course, a **base** is a substance that:",
         correct=T("produces hydroxide ions ([[OH^-^]]) when it is dissolved in water"),
         wrong=[T("produces H^+^ ions when it is dissolved in water", "That is an Arrhenius **acid** (slide 21)."),
                T("always contains a metal", "Not part of the definition. The definition is about producing OH^−^ in water."),
                T("loses electrons to a nonmetal", "Losing electrons is oxidation (redox), not the definition of a base."),
                T("is always insoluble in water", "The strong bases NaOH and KOH are **very** soluble (slide 25).")],
         cite=f"{C7}, slide 22 (Arrhenius Bases)", hw=HW16_BASE, covers="Course definition of an Arrhenius base.",
         sol="Slide 22: Arrhenius defined a **base** as a substance that **produces hydroxide ions (OH^−^) in water**. Hydroxide "
             "compounds that are strong electrolytes are called **strong bases**."),
    dict(title="Identifying a strong base", short="Ch 7 sl. 22, 25",
         stem="Which compound is a **strong base**?",
         correct=T("KOH"),
         wrong=[T("[[Mg(OH)2]]", "Most hydroxides are only slightly soluble (rule 5). A strong base must be **very** soluble."),
                T("[[NH3]]", "NH~3~ isn't a metal hydroxide."),
                T("[[Fe(OH)3]]", "Insoluble hydroxide (rule 5), so it can't be a strong base."),
                T("HCl", "HCl is a strong **acid**.")],
         cite=f"{C7}, slide 25 (principle 3: a strong base is a very soluble metal hydroxide; NaOH and KOH)", hw=HW16_BASE,
         covers="Strong bases: very soluble metal hydroxides (NaOH, KOH) that break completely into ions.",
         sol="Slide 25, principle 3: a **strong base** is a metal hydroxide that is **very soluble** in water. The most common are "
             "**NaOH and KOH**, which break completely into separated ions. Mg(OH)~2~ and Fe(OH)~3~ are hydroxides but only slightly "
             "soluble (rule 5), so they aren't strong bases."),
    dict(title="The salt formed", short="Ch 7 sl. 23, 26",
         stem="What **salt** forms when nitric acid reacts completely with calcium hydroxide? "
              "2[[HNO3]](aq) + [[Ca(OH)2]](aq) → ? + 2[[H2O]](l)",
         correct=T("[[Ca(NO3)2]]"),
         wrong=[T("[[CaNO3]]", "Ca^2+^ is +2 and NO~3~^−^ is −1, so two nitrates are needed."),
                T("[[Ca2NO3]]", "That has charge 2(+2) − 1 = +3. A salt must be neutral."),
                T("[[Ca(OH)2]]", "That's the base, a reactant."),
                T("[[H2O]]", "Water is the other product. The salt is the ionic compound.")],
         cite=f"{C7}, slide 23 (the second product is a salt), slide 26 (principle 5)", hw=HW16_SALT,
         covers="Building the salt: the base's cation with the acid's anion, charges balanced.",
         sol="""**Step 1: ions.** HNO~3~ gives H^+^ and NO~3~^−^; Ca(OH)~2~ gives Ca^2+^ and OH^−^.

**Step 2:** H^+^ + OH^−^ → H~2~O. What remains, Ca^2+^ with NO~3~^−^, is the salt.

**Step 3: neutral formula.** +2 needs two −1 ions: **Ca(NO~3~)~2~**."""),
    dict(title="Net ionic equation for an acid–base reaction", short="Ch 7 sl. 23–26",
         stem="Sulfuric acid reacts with sodium hydroxide: [[H2SO4]](aq) + 2NaOH(aq) → [[Na2SO4]](aq) + 2[[H2O]](l). "
              "What is the **net ionic** equation (smallest whole-number coefficients)?",
         correct=T("H^+^(aq) + [[OH^-^]](aq) → [[H2O]](l)"),
         wrong=[T("2H^+^(aq) + 2[[OH^-^]](aq) → 2[[H2O]](l)", "Right species, but not the smallest whole numbers. Divide by 2."),
                T("2Na^+^(aq) + [[SO4^2-^]](aq) → [[Na2SO4]](s)", "Na~2~SO~4~ is soluble (rules 2 and 4); those ions are spectators."),
                T("[[H2SO4]](aq) + 2[[OH^-^]](aq) → [[SO4^2-^]](aq) + 2[[H2O]](l)",
                  "H~2~SO~4~ is a strong acid: it completely dissociates (slide 24), so write it as ions; SO~4~^2−^ then cancels."),
                T("2H^+^(aq) + [[SO4^2-^]](aq) + 2Na^+^(aq) + 2[[OH^-^]](aq) → 2Na^+^(aq) + [[SO4^2-^]](aq) + 2[[H2O]](l)",
                  "That's the **complete** ionic equation. Cancel the spectators.")],
         cite=f"{C7}, slide 23 (the net ionic equation shows water forming), slide 25 (principle 4), slides 24–26",
         hw=HW16_BASE, covers="Acid–base net ionic equation, reduced to the smallest whole-number coefficients.",
         sol="""**Step 1: complete ionic.** 2H^+^ + SO~4~^2−^ + 2Na^+^ + 2OH^−^ → 2Na^+^ + SO~4~^2−^ + 2H~2~O(l)

**Step 2: cancel the spectators** Na^+^ and SO~4~^2−^: 2H^+^ + 2OH^−^ → 2H~2~O.

**Step 3: smallest whole numbers.** Divide every coefficient by 2: **H^+^(aq) + OH^−^(aq) → H~2~O(l)** (slide 23)."""),
    dict(title="Balancing an acid–base equation", short="Ch 7 sl. 27",
         stem="When the equation below is balanced with the smallest whole-number coefficients, what is the **sum** of all four "
              "coefficients?\n\n\\_\\_ [[H3PO4]](aq) + \\_\\_ KOH(aq) → \\_\\_ [[K3PO4]](aq) + \\_\\_ [[H2O]](l)",
         **num(8, [(4, "That treats the equation as balanced with all 1's. K and H don't balance that way."),
                   (6, "Balanced K (3 KOH) but forgot that 3 OH^−^ make 3 H~2~O."),
                   (10, "Added a coefficient that isn't needed; the smallest set is 1, 3, 1, 3."),
                   (12, "Doubled every coefficient. Use the smallest whole numbers.")]),
         cite=f"{AB_PRAC.split(',')[0]}, slide 27 (balance H~3~PO~4~ + Ca(OH)~2~)", hw=HW17_COMB,
         covers="Balancing a polyprotic acid with a hydroxide: each H^+^ meets one OH^−^.",
         sol="""**Step 1: K.** K~3~PO~4~ has 3 K, so **3**KOH.

**Step 2: PO~4~.** 1 on each side: **1** H~3~PO~4~, **1** K~3~PO~4~.

**Step 3: water.** 3 H^+^ (from H~3~PO~4~) + 3 OH^−^ (from 3 KOH) make **3**H~2~O.

1 + 3 + 1 + 3 = **8**."""),
    # ------------------------------------------------------------ 7.7 oxidation–reduction
    dict(title="Which reaction is NOT redox?", short="Ch 7 sl. 30–32",
         stem="Which reaction is **not** an oxidation–reduction reaction?",
         correct=T("[[Pb(NO3)2]](aq) + 2NaCl(aq) → [[PbCl2]](s) + 2[[NaNO3]](aq)"),
         wrong=[T("2Na(s) + [[Cl2]](g) → 2NaCl(s)", "Metal + nonmetal is always redox (slide 31)."),
                T("Zn(s) + 2HCl(aq) → [[ZnCl2]](aq) + [[H2]](g)", "Single replacement is redox (slide 40): Zn 0 → +2."),
                T("[[CH4]](g) + 2[[O2]](g) → [[CO2]](g) + 2[[H2O]](g)", "O~2~ is a reactant, the course's clue for redox (slide 32)."),
                T("[[N2]](g) + [[O2]](g) → 2NO(g)", "O~2~ is a reactant, so it's redox between two nonmetals (slide 32).")],
         cite=f"{RX.split(',')[0]}, slides 30–32 (electron transfer; principles 1 and 2), slide 40", hw=HW17_CLS,
         covers="Recognizing redox (metal + nonmetal, single replacement, O~2~) versus ion-swapping reactions.",
         sol="""The precipitation reaction Pb(NO~3~)~2~ + 2NaCl → PbCl~2~ + 2NaNO~3~ only swaps partners. Pb stays +2, Na stays +1, NO~3~
stays −1, and Cl stays −1, so **no electrons move**.

The others are all redox: a metal + a nonmetal (Na + Cl~2~), a single replacement (Zn + HCl), or O~2~ as a reactant
(CH~4~ combustion, N~2~ + O~2~)."""),
    dict(title="Electrons per atom", short="Ch 7 sl. 31, 33",
         stem="In the reaction 3Ca(s) + [[N2]](g) → [[Ca3N2]](s), how many electrons does **each nitrogen atom** gain?",
         **num(3, [(1, "That would make N^−^. In Ca~3~N~2~ nitrogen is N^3−^ (3 Ca^2+^ balance 2 N^3−^)."),
                   (2, "That is what each **Ca** atom loses (Ca → Ca^2+^)."),
                   (5, "5 is nitrogen's number of valence electrons; it **gains** 3 to become N^3−^."),
                   (6, "That counts both N atoms from one N~2~ molecule. The question asks per atom.")]),
         cite=f"{RX_PRAC.split(',')[0]}, slide 33 (2Al + N~2~ → 2AlN), slide 31", hw=HW16_RX,
         covers="Electrons gained per nonmetal atom = the size of its ion's charge.",
         sol="""**Step 1: ions.** Ca~3~N~2~ is ionic: Ca^2+^ and N^3−^. Check: 3(+2) + 2(−3) = 0.

**Step 2:** each N atom goes 0 → −3, so it **gains 3 electrons**. (Each Ca loses 2.)

**Check:** 3 Ca × 2 = 6 lost; 2 N × 3 = 6 gained."""),
    dict(title="Electrons in a single replacement", short="Ch 7 sl. 34, 40",
         stem="For Cu(s) + 2[[AgNO3]](aq) → [[Cu(NO3)2]](aq) + 2Ag(s), which statement is correct?",
         correct=T("Each Cu atom loses 2 electrons and each Ag^+^ ion gains 1 electron"),
         wrong=[T("Each Cu atom loses 2 electrons and each Ag^+^ ion gains 2 electrons",
                  "Ag^+^ goes from +1 to 0, which is one electron. That's why the equation needs **2** Ag^+^ for each Cu."),
                T("Each Cu atom gains 2 electrons", "Cu goes from 0 to +2, so it **loses** electrons."),
                T("The [[NO3^-^]] ions transfer electrons to silver", "Nitrate is −1 before and after; it's a spectator."),
                T("No electrons transfer; the anions simply swap partners", "Only NO~3~^−^ moves, and Cu and Ag change charge. That's redox.")],
         cite=f"{RX_PRAC.split(',')[0]}, slide 34 (Cu + FeCl~2~: electrons lost or gained by each species), slide 40", hw=HW16_RX,
         covers="Per-atom electron counts when the two metal ions have different charges.",
         sol="""**Charges:** Cu 0 → +2 (loses **2 e^−^**). Ag +1 → 0 (gains **1 e^−^**). NO~3~^−^ unchanged (spectator).

The 2 electrons lost by one Cu are picked up by **two** Ag^+^ ions, one each. That's why the balanced equation has 2AgNO~3~
and 2Ag."""),
    dict(title="Metal + nonmetal", short="Ch 7 sl. 29, 31",
         stem="According to the course, what happens when a **metal** reacts with a **nonmetal**?",
         correct=T("An ionic compound forms as the metal transfers electrons to the nonmetal, so the reaction is always redox"),
         wrong=[T("The nonmetal transfers electrons to the metal",
                  "Backwards: the metal becomes the cation by **losing** electrons."),
                T("A molecular (non-ionic) compound forms by sharing electrons",
                  "That describes two **nonmetals** (slide 32). Metal + nonmetal gives an ionic compound."),
                T("It is redox only if [[O2]] is one of the reactants",
                  "The O~2~ clue is for two nonmetals. A metal + nonmetal is **always** redox."),
                T("No electrons transfer, so it is classified as a synthesis only",
                  "It may also be synthesis, but it is always redox too.")],
         cite=f"{RX.split(',')[0]}, slide 29 (Na + Cl: an electron is transferred), slide 31 (principle 1)", hw=HW16_RX,
         covers="Redox principle 1.",
         sol="Slide 31, principle 1: when a metal reacts with a nonmetal, an **ionic compound** forms. The metal **transfers one or "
             "more electrons to the nonmetal**: the metal atom becomes a cation and the nonmetal atom becomes an anion. So a "
             "metal–nonmetal reaction can **always** be assumed to be oxidation–reduction."),
    # ------------------------------------------------------------ 7.8 classification
    dict(title="Classifying a reaction", short="Ch 7 sl. 37–40",
         stem="Classify Ni(s) + 2HCl(aq) → [[NiCl2]](aq) + [[H2]](g).",
         correct=T("oxidation–reduction and single-replacement"),
         wrong=[T("acid–base only", "HCl is an acid, but its H^+^ becomes H~2~ gas, not water. No base is involved."),
                T("precipitation", "Nothing solid forms; NiCl~2~ is soluble (rule 3)."),
                T("double-displacement", "Only one anion (Cl^−^) moves, from H^+^ to Ni^2+^. That's single replacement."),
                T("decomposition", "Two reactants combine and exchange; nothing breaks apart.")],
         cite=f"{CLS.split(',')[0]}, slide 40 (Single-Replacement: Zn + 2HCl; also redox), slide 37", hw=HW17_CLS,
         covers="Metal + acid: single replacement and redox, not acid–base.",
         sol="""* **Single replacement:** one type of anion (Cl^−^) moves from H^+^ to Ni^2+^, the same pattern as Zn + 2HCl on slide 40.
* **Oxidation–reduction:** Ni goes 0 → +2 (loses 2 e^−^) and H goes +1 → 0 in H~2~ (gains).
* **Not acid–base:** the H^+^ ends up as H~2~ gas, not in water (slide 37's clue)."""),
    dict(title="Classifying by type", short="Ch 7 sl. 42",
         stem="[[SO3]](g) + [[H2O]](l) → [[H2SO4]](aq) is best classified as:",
         correct=T("synthesis (combination)"),
         wrong=[T("decomposition", "Two substances combine into one; nothing breaks apart."),
                T("combustion", "No O~2~ reacts and there's no flame."),
                T("single-replacement", "No element replaces another."),
                T("double-displacement", "There are no two salts swapping anions.")],
         cite=f"{CLS.split(',')[0]}, slide 42 (Synthesis: a compound formed from simpler materials)", hw=HW17_WORDS,
         covers="Synthesis: one compound formed from simpler materials (which can be compounds, not just elements).",
         sol="Two simpler substances (SO~3~ and H~2~O) combine into **one** compound, H~2~SO~4~. Slide 42: when a compound is formed "
             "from simpler materials, it's a **synthesis (combination)** reaction."),
    dict(title="A reaction in several classes", short="Ch 7 sl. 37, 41",
         stem="Methane burns in a gas stove: [[CH4]](g) + 2[[O2]](g) → [[CO2]](g) + 2[[H2O]](g). Which classes apply?",
         correct=T("combustion and oxidation–reduction"),
         wrong=[T("acid–base, because water is a product",
                  "Acid–base means H^+^ from an acid ends up in water. CH~4~ isn't an acid and no OH^−^ is involved."),
                T("combustion only", "Combustion with O~2~ is also redox (O~2~ is the course's clue)."),
                T("synthesis and combustion", "Two products form, not one compound from simpler materials."),
                T("decomposition and oxidation–reduction", "CH~4~ reacts with O~2~; it doesn't break apart on its own.")],
         cite=f"{CLS.split(',')[0]}, slide 41 (Combustion: CH~4~ + 2O~2~), slide 32 (O~2~ signals redox)", hw=HW17_COMB,
         covers="Combustion is also redox; water as a product doesn't make it acid–base.",
         sol="""* **Combustion:** a reaction with oxygen that releases energy so fast that a flame results (slide 41); this exact
  reaction is the slide's example.
* **Oxidation–reduction:** O~2~ is a reactant (slide 32).
* **Not acid–base:** forming water isn't enough. Acid–base needs an acid's H^+^ combining with a base's OH^−^."""),
    dict(title="Single replacement", short="Ch 7 sl. 40",
         stem="According to the course, a **single-replacement** reaction is one in which:",
         correct=T("a single type of anion is exchanged between two cations, as Cl^−^ moves from H^+^ to Zn^2+^ in Zn + 2HCl"),
         wrong=[T("two anions exchange cation partners", "That's double displacement (slide 36)."),
                T("a single compound breaks into two elements", "That's decomposition (slide 43)."),
                T("a single substance reacts with oxygen", "That's combustion (slide 41)."),
                T("no electrons are transferred", "Single replacement is always oxidation–reduction (slide 40).")],
         cite=f"{CLS.split(',')[0]}, slide 40 (Single-Replacement Reactions)", hw=HW17_CLS,
         covers="Course definition of single replacement, and that it is also redox.",
         sol="Slide 40: Zn + 2HCl → ZnCl~2~ + H~2~ is a single-replacement reaction because **a single type of anion (Cl^−^) was "
             "exchanged between H^+^ and Zn^2+^**. It is also an oxidation–reduction reaction."),
    dict(title="Balancing from words", short="Ch 7 sl. 40",
         stem="Sodium metal reacts with water to form sodium hydroxide and hydrogen gas. In the balanced equation with the smallest "
              "whole-number coefficients, what is the coefficient of water?",
         **num(2, [(1, "Na + H~2~O → NaOH + H~2~ has 2 H on the left but 3 on the right."),
                   (3, "Doesn't balance H: try 2Na + 2H~2~O → 2NaOH + H~2~."),
                   (4, "Doubled the correct coefficients. Use the smallest whole numbers."),
                   (6, "No balanced form needs 6 H~2~O.")]),
         cite=f"{CLS_PRAC.split(',')[0]}, slide 40 (single replacement), slide 31 (metal reacting)", hw=HW17_WORDS,
         covers="Writing an equation from words and balancing H with a diatomic product.",
         sol="""**Step 1: formulas.** Na + H~2~O → NaOH + H~2~.

**Step 2: H.** Left: 2 per H~2~O. Right: 1 in NaOH + 2 in H~2~. With 2H~2~O (4 H): 2NaOH (2 H) + H~2~ (2 H) = 4 H.

**Step 3: Na and O.** 2NaOH needs **2Na**; O: 2 = 2.

**2Na + 2H~2~O → 2NaOH + H~2~**: water's coefficient is **2**."""),
    dict(title="Balancing a combustion", short="Ch 7 sl. 9, 41",
         stem="Hexane burns completely: \\_\\_ [[C6H14]] + \\_\\_ [[O2]] → \\_\\_ [[CO2]] + \\_\\_ [[H2O]]. With the smallest "
              "whole-number coefficients, what is the coefficient of [[O2]]?",
         **num(19, [(7, "That is the H~2~O coefficient before doubling."), (12, "That is the coefficient of CO~2~."),
                    (14, "That is the coefficient of H~2~O."),
                    (38, "38 is the number of O **atoms**; O~2~ supplies them in pairs.")]),
         cite=f"{C7}, slide 41 (Combustion); Chapter 9 post, slide 9 (doubling to clear a fractional O~2~)", hw=HW17_COMB,
         covers="Combustion balancing that needs doubling to clear a fraction.",
         sol="""**Step 1: C.** 6 C → 6CO~2~. **Step 2: H.** 14 H → 7H~2~O.

**Step 3: O.** 6(2) + 7(1) = 19 O atoms → 19/2 O~2~. That isn't whole, so **double everything**:
2C~6~H~14~ + **19**O~2~ → 12CO~2~ + 14H~2~O. Check O: 38 = 24 + 14."""),
]

if __name__ == "__main__":
    build(6, Q)
