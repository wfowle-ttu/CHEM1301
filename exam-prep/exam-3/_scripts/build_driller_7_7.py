"""Build driller-7-7: reaction types (acid–base, redox, classification), 15 questions.

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_driller_7_7.py
"""
from rxndrill import (AB, AB_PRAC, C7, CLS, CLS_PRAC, HW16_BASE, HW16_RX, HW16_SALT, HW17_CLS, HW17_COMB, HW17_WORDS, RX,
                      RX_PRAC, T, balanced, build, num)

balanced([(2, "HNO3"), (1, "Ca(OH)2")], [(1, "Ca(NO3)2"), (2, "H2O")])
balanced([(3, "HNO3"), (1, "Al(OH)3")], [(1, "Al(NO3)3"), (3, "H2O")])
balanced([(4, "Na"), (1, "O2")], [(2, "Na2O")])
balanced([(6, "Li"), (1, "N2")], [(2, "Li3N")])
balanced([(1, "C7H16"), (11, "O2")], [(7, "CO2"), (8, "H2O")])
balanced([(1, "C2H5OH"), (3, "O2")], [(2, "CO2"), (3, "H2O")])

Q = [
    # ------------------------------------------------------------ 7.6 acid–base
    dict(title="Strong acid", short="Ch 7 sl. 21, 24",
         stem="According to the course, a **strong acid** is a substance that:",
         correct=T("completely dissociates (ionizes) in water, each molecule breaking into an H^+^ ion and an anion"),
         wrong=[T("only partially dissociates in water", "Partial dissociation is what makes an acid **weak**."),
                T("is very concentrated", "\"Strong\" is about complete dissociation, not concentration."),
                T("produces [[OH^-^]] ions in water", "That's a base (slide 22)."),
                T("forms a precipitate with any metal ion", "Strong acids are about ionizing, not precipitating.")],
         cite=f"{C7}, slide 24 (principle 2: a strong acid completely dissociates), slide 21", hw=HW16_BASE,
         covers="Course definition of a strong acid.",
         sol="Slide 24, principle 2: a strong acid is a substance that **completely dissociates (ionizes)** in water: each molecule "
             "breaks up into an H^+^ ion plus an anion. Because strong acids are strong electrolytes that produce H^+^ (slide 21), "
             "they are called strong acids."),
    dict(title="Not a strong acid or base", short="Ch 7 sl. 24–25",
         stem="Which substance is **neither** a strong acid **nor** a strong base?",
         correct=T("[[HNO2]]"),
         wrong=[T("[[HNO3]]", "Nitric acid is one of the three strong acids."),
                T("HCl", "Hydrochloric acid is one of the three strong acids."),
                T("KOH", "KOH is one of the two common strong bases."),
                T("NaOH", "NaOH is one of the two common strong bases.")],
         cite=f"{C7}, slides 24–25 (principles 1 and 3: HCl, HNO~3~, H~2~SO~4~; NaOH and KOH), slide 28 (HNO~2~)", hw=HW16_BASE,
         covers="Memorized lists: strong acids HCl, HNO~3~, H~2~SO~4~; strong bases NaOH, KOH.",
         sol="Strong acids (slide 24): **HCl, HNO~3~, H~2~SO~4~**. Strong bases (slide 25): **NaOH, KOH**. HNO~2~ (nitrous acid, "
             "with **2** O) is on neither list. Watch HNO~2~ vs HNO~3~."),
    dict(title="The salt formed", short="Ch 7 sl. 23, 26",
         stem="What **salt** forms when nitric acid neutralizes aluminum hydroxide? "
              "3[[HNO3]](aq) + [[Al(OH)3]](s) → ? + 3[[H2O]](l)",
         correct=T("[[Al(NO3)3]]"),
         wrong=[T("[[AlNO3]]", "Al^3+^ is +3, so it needs three NO~3~^−^."),
                T("[[Al3NO3]]", "That has charge 3(+3) − 1 = +8. A salt must be neutral."),
                T("[[Al(OH)3]]", "That's the base, a reactant."),
                T("[[H2O]]", "Water is the other product. The salt is the ionic compound.")],
         cite=f"{C7}, slide 23 (the second product is a salt), slide 26 (principle 5)", hw=HW16_SALT,
         covers="Building the salt from the base's cation and the acid's anion, with charges balanced.",
         sol="H^+^ (from HNO~3~) and OH^−^ (from Al(OH)~3~) form water. The salt is the leftover cation, Al^3+^, with the leftover "
             "anion, NO~3~^−^. To cancel +3 you need three −1 ions: **Al(NO~3~)~3~**."),
    dict(title="Spectator ions in an acid–base reaction", short="Ch 7 sl. 17, 23",
         stem="In the reaction [[HNO3]](aq) + NaOH(aq) → [[NaNO3]](aq) + [[H2O]](l), which ions are **spectator ions**?",
         correct=T("Na^+^ and [[NO3^-^]]"),
         wrong=[T("H^+^ and [[OH^-^]]", "Those combine to form water, so they **do** take part."),
                T("Na^+^ and [[OH^-^]]", "OH^−^ ends up in water, so it isn't a spectator."),
                T("H^+^ and [[NO3^-^]]", "H^+^ ends up in water, so it isn't a spectator."),
                T("There are no spectator ions in an acid–base reaction", "Na^+^ and NO~3~^−^ stay dissolved and unchanged.")],
         cite=f"{C7}, slide 17 (spectator ions), slide 23 (acid–base net ionic equation), slide 26 (the salt stays dissolved)",
         hw=HW16_BASE, covers="In an acid–base reaction the salt's ions are spectators; H^+^ and OH^−^ form water.",
         sol="""Complete ionic: H^+^ + NO~3~^−^ + Na^+^ + OH^−^ → Na^+^ + NO~3~^−^ + H~2~O(l). **Na^+^ and NO~3~^−^** appear unchanged
on both sides, so they are the spectators (slide 17). What's left is the net ionic equation, H^+^ + OH^−^ → H~2~O (slide 23).
The salt, NaNO~3~, stays dissolved (slide 26)."""),
    dict(title="Balancing an acid–base equation", short="Ch 7 sl. 27",
         stem="When the equation below is balanced with the smallest whole-number coefficients, what is the coefficient of water?\n\n"
              "\\_\\_ [[HNO3]](aq) + \\_\\_ [[Ca(OH)2]](aq) → \\_\\_ [[Ca(NO3)2]](aq) + \\_\\_ [[H2O]](l)",
         **num(2, [(1, "Leaves H and O unbalanced: 2 H^+^ and 2 OH^−^ make 2 H~2~O."),
                   (3, "There are only 2 OH^−^ in one Ca(OH)~2~."),
                   (4, "Doubled. Use the smallest whole numbers."),
                   (6, "No balanced form needs 6 H~2~O.")]),
         cite=f"{AB_PRAC.split(',')[0]}, slide 27 (balancing an acid–base reaction)", hw=HW17_COMB,
         covers="Balancing: each H^+^ meets one OH^−^ to make one H~2~O.",
         sol="""**Step 1: NO~3~.** Ca(NO~3~)~2~ has 2 NO~3~, so **2**HNO~3~. **Step 2: Ca.** 1 = 1.

**Step 3: water.** 2 H^+^ + 2 OH^−^ → **2**H~2~O. 2HNO~3~ + Ca(OH)~2~ → Ca(NO~3~)~2~ + 2H~2~O."""),
    # ------------------------------------------------------------ 7.7 oxidation–reduction
    dict(title="Which reaction transfers electrons?", short="Ch 7 sl. 30–32",
         stem="Which reaction involves a **transfer of electrons**?",
         correct=T("[[N2]](g) + [[O2]](g) → 2NO(g)"),
         wrong=[T("NaOH(aq) + HCl(aq) → NaCl(aq) + [[H2O]](l)", "Acid–base: H^+^ and OH^−^ form water; no charges change."),
                T("[[K2CO3]](aq) + 2HCl(aq) → 2KCl(aq) + [[H2O]](l) + [[CO2]](g)", "Gas evolution / acid–base; every ion keeps its charge."),
                T("[[AgNO3]](aq) + KCl(aq) → AgCl(s) + [[KNO3]](aq)", "Precipitation: ions swap partners."),
                T("[[MgCO3]](s) → MgO(s) + [[CO2]](g)", "Decomposition with no element formed and no O~2~; Mg stays +2 and CO~3~ splits into O^2−^ and CO~2~.")],
         cite=f"{RX.split(',')[0]}, slide 32 (principle 2: two nonmetals; look for O~2~), slide 30", hw=HW17_CLS,
         covers="Two nonmetals reacting with O~2~ present is redox (principle 2).",
         sol="N~2~ + O~2~ → 2NO is two **nonmetals** reacting with **O~2~ as a reactant**. Slide 32: that's how the course recognizes "
             "nonmetal–nonmetal redox. The others only swap ions, form water or gas, or break apart without any element changing "
             "its charge."),
    dict(title="Electrons per atom", short="Ch 7 sl. 31, 38",
         stem="In the reaction 4Na(s) + [[O2]](g) → 2[[Na2O]](s), how many electrons does **each sodium atom** lose?",
         **num(1, [(0, "Metal + nonmetal is always redox (slide 31), so electrons do move."),
                   (2, "That is what each **O** atom gains (O → O^2−^)."),
                   (3, "That would make Na^3+^. Na~2~O has 2 Na^+^ for every O^2−^."),
                   (4, "That's the total gained by one O~2~ molecule (2 O × 2), not per Na atom.")]),
         cite=f"{RX_PRAC.split(',')[0]}, slide 38 (2Li + F~2~: each Li loses one electron), slide 31", hw=HW16_RX,
         covers="Electrons lost per metal atom = the cation's charge.",
         sol="""**Step 1: ions.** Na~2~O: 2 Na^+^ and 1 O^2−^ (2(+1) − 2 = 0).

**Step 2:** each Na goes 0 → +1, so it **loses 1 electron**, just like each Li in 2Li + F~2~ (slide 38).

**Check:** 4 Na × 1 = 4 lost; 2 O × 2 = 4 gained."""),
    dict(title="Which species gains electrons?", short="Ch 7 sl. 34, 40",
         stem="In Zn(s) + [[CuSO4]](aq) → [[ZnSO4]](aq) + Cu(s), which species **gains** electrons?",
         correct=T("Cu^2+^"),
         wrong=[T("Zn", "Zn goes from 0 to +2, so it **loses** 2 electrons."),
                T("[[SO4^2-^]]", "Sulfate is −2 before and after; it's a spectator."),
                T("Zn^2+^", "Zn^2+^ is the product of Zn losing electrons; it doesn't gain any."),
                T("No species; no electrons are transferred", "A metal replaces another metal's ion, so it's single replacement, which is redox.")],
         cite=f"{RX_PRAC.split(',')[0]}, slide 34 (Cu + FeCl~2~), slide 40 (single replacement is redox)", hw=HW16_RX,
         covers="Identifying the species that gains electrons in a single replacement.",
         sol="Charges: Zn 0 → +2 (loses 2 e^−^). Cu +2 (in CuSO~4~) → 0 (**gains 2 e^−^**). SO~4~^2−^ doesn't change. The species "
             "that gains electrons is **Cu^2+^**: the mirror image of slide 34, where Fe^2+^ gains electrons from Cu."),
    dict(title="Electron transfer in Na + Cl2", short="Ch 7 sl. 29, 31",
         stem="When sodium reacts with chlorine, 2Na(s) + [[Cl2]](g) → 2NaCl(s), what happens?",
         correct=T("Each Na atom transfers one electron to a Cl atom, forming Na^+^ and Cl^−^ ions"),
         wrong=[T("Each Cl atom transfers one electron to a Na atom", "Backwards: the metal loses electrons and becomes the cation."),
                T("Na and Cl share electrons equally and form NaCl molecules",
                  "A metal + nonmetal forms an **ionic** compound by transfer, not sharing."),
                T("Each Na atom loses two electrons", "Na becomes Na^+^, which is one electron."),
                T("No electrons move; the atoms just combine", "Electron transfer is exactly what happens (slide 29).")],
         cite=f"{RX.split(',')[0]}, slide 29 (when a sodium atom reacts with a chlorine atom an electron is transferred), slide 31",
         hw=HW16_RX, covers="The picture of electron transfer behind redox principle 1.",
         sol="Slide 29: when a sodium atom reacts with a chlorine atom, **an electron is transferred**. Na loses one electron "
             "(becoming Na^+^) and Cl gains one (becoming Cl^−^). Metal + nonmetal → ionic compound, always redox (slide 31)."),
    # ------------------------------------------------------------ 7.8 classification
    dict(title="Classifying a reaction", short="Ch 7 sl. 35–37",
         stem="Classify [[AgNO3]](aq) + HCl(aq) → AgCl(s) + [[HNO3]](aq).",
         correct=T("precipitation (double-displacement)"),
         wrong=[T("acid–base", "HCl is an acid, but its H^+^ doesn't end up in water; it stays as H^+^ in HNO~3~."),
                T("oxidation–reduction", "Ag stays +1 and Cl stays −1. No electrons move."),
                T("gas evolution", "No gas forms."),
                T("single-replacement", "Two anions swap partners, so it's double, not single.")],
         cite=f"{CLS.split(',')[0]}, slide 35 (precipitation), slide 36 (double-displacement), slide 37 (acid–base clue)", hw=HW17_CLS,
         covers="An acid can take part in a precipitation without the reaction being acid–base.",
         sol="""* **Precipitation:** AgCl is a solid (rule 3 exception). The anions NO~3~^−^ and Cl^−^ exchange partners, which is
  double-displacement (slide 36).
* **Not acid–base:** slide 37's clue is H^+^ ending up in **water**. Here no water forms.
* **Not redox:** every ion keeps its charge."""),
    dict(title="Recognizing combustion", short="Ch 7 sl. 41",
         stem="Which reaction is a **combustion** reaction?",
         correct=T("[[C2H5OH]](l) + 3[[O2]](g) → 2[[CO2]](g) + 3[[H2O]](g)"),
         wrong=[T("2[[H2O]](l) → 2[[H2]](g) + [[O2]](g)", "O~2~ is a **product** here: this is decomposition by electric current (slide 43)."),
                T("[[N2]](g) + 3[[H2]](g) → 2[[NH3]](g)", "Synthesis; no O~2~ reacts (slide 44)."),
                T("CaO(s) + [[CO2]](g) → [[CaCO3]](s)", "Synthesis from two compounds; no O~2~, no flame."),
                T("HCl(aq) + NaOH(aq) → NaCl(aq) + [[H2O]](l)", "Acid–base.")],
         cite=f"{CLS.split(',')[0]}, slide 41 (Combustion Reactions), slides 43–44", hw=HW17_COMB,
         covers="Combustion: a substance reacting **with** O~2~, releasing energy fast enough to give a flame.",
         sol="Slide 41: reactions involving oxygen that release energy so rapidly that a **flame** results are **combustion** "
             "reactions. Ethanol burning in O~2~ fits. In 2H~2~O → 2H~2~ + O~2~, O~2~ is made rather than consumed, so it's "
             "decomposition, not combustion."),
    dict(title="A reaction in several classes", short="Ch 7 sl. 41–42",
         stem="Hydrogen burns: 2[[H2]](g) + [[O2]](g) → 2[[H2O]](l). Which classes apply?",
         correct=T("synthesis, combustion, and oxidation–reduction"),
         wrong=[T("acid–base, because water forms", "No acid or base reacts. Forming water alone isn't acid–base."),
                T("synthesis only", "It burns in O~2~ with a flame (combustion), and O~2~ means redox."),
                T("decomposition and oxidation–reduction", "Two elements combine; nothing breaks apart."),
                T("combustion only", "One compound forms from two elements (synthesis), and O~2~ means redox.")],
         cite=f"{CLS.split(',')[0]}, slides 41–42 (combustion; synthesis), slide 32 (O~2~ signals redox)", hw=HW17_CLS,
         covers="One reaction can belong to several classes.",
         sol="""* **Synthesis:** one compound (H~2~O) from simpler materials (H~2~ and O~2~).
* **Combustion:** reacts with O~2~, releasing energy fast enough for a flame.
* **Oxidation–reduction:** O~2~ is a reactant (slide 32).
* **Not acid–base:** no acid's H^+^ meets a base's OH^−^."""),
    dict(title="Decomposition conditions", short="Ch 7 sl. 43",
         stem="According to the course, **decomposition** reactions are usually brought about by:",
         correct=T("heating or applying an electric current"),
         wrong=[T("mixing two aqueous solutions", "That's how precipitation reactions start."),
                T("adding a strong acid", "Acids drive acid–base and gas evolution reactions."),
                T("reacting the compound with oxygen", "That's combustion."),
                T("adding a more reactive metal", "That's single replacement.")],
         cite=f"{CLS.split(',')[0]}, slide 43 (Decomposition: usually by heating or the application of an electric current)",
         hw=HW17_WORDS, covers="Course definition of decomposition and how it's carried out.",
         sol="Slide 43: a compound can be broken down into simpler compounds or all the way to its elements. This is usually done by "
             "**heating** (2HgO → 2Hg + O~2~) or by **an electric current** (2H~2~O → 2H~2~ + O~2~)."),
    dict(title="Balancing from words", short="Ch 7 sl. 42",
         stem="Lithium metal combines with nitrogen gas, [[N2]], to form lithium nitride, [[Li3N]]. In the balanced equation with the "
              "smallest whole-number coefficients, what is the coefficient of Li?",
         **num(6, [(1, "Li + N~2~ → Li~3~N isn't balanced: 2 N on the left, 1 on the right."),
                   (2, "That is the coefficient of Li~3~N."),
                   (3, "That balances Li for **one** Li~3~N, but N~2~ makes two."),
                   (9, "Overshoots: 2Li~3~N contain only 6 Li.")]),
         cite=f"{CLS_PRAC.split(',')[0]}, slide 42 (synthesis), slide 33 (a metal + N~2~)", hw=HW17_WORDS,
         covers="Writing a synthesis from words and balancing N~2~ first.",
         sol="""**Step 1: formulas.** Li + N~2~ → Li~3~N.

**Step 2: N.** N~2~ gives 2 N, so **2**Li~3~N.

**Step 3: Li.** 2Li~3~N contain 6 Li, so **6**Li: **6Li + N~2~ → 2Li~3~N**."""),
    dict(title="Balancing a combustion", short="Ch 7 sl. 41",
         stem="Heptane burns completely: \\_\\_ [[C7H16]] + \\_\\_ [[O2]] → \\_\\_ [[CO2]] + \\_\\_ [[H2O]]. With the smallest "
              "whole-number coefficients, what is the coefficient of [[O2]]?",
         **num(11, [(7, "That is the coefficient of CO~2~."), (8, "That is the coefficient of H~2~O."),
                    (15, "Counted 7 + 8 = 15 molecules, not O atoms. The O atoms are 7(2) + 8(1) = 22."),
                    (22, "22 is the number of O **atoms**; O~2~ supplies them in pairs.")]),
         cite=f"{CLS.split(',')[0]}, slide 41 (Combustion)", hw=HW17_COMB,
         covers="Balancing combustion: C, then H, then O last.",
         sol="""**Step 1: C.** 7 C → **7**CO~2~. **Step 2: H.** 16 H → **8**H~2~O.

**Step 3: O.** 7(2) + 8(1) = 22 O atoms → 22 ÷ 2 = **11**O~2~. C~7~H~16~ + 11O~2~ → 7CO~2~ + 8H~2~O."""),
]

if __name__ == "__main__":
    build(7, Q)
