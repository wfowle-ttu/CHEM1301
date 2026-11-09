"""Build driller-9-1 (10 Chapter 9 questions) and its key, checking every numeric answer.

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_driller_9_1.py
Topic spread follows the Ch 9 slides: coefficients (2-5), mole ratios (5-9), mole-mole (10-12),
mass stoichiometry (13-20), limiting reactant (21-24), theoretical yield (25-27), percent yield (28-32).
Compounds and numbers are new (not used in practice exams 3-1 / 3-2).

Key solutions follow the study-guide format: every step named, every conversion factor written
want-over-have with an underbrace label saying where its numbers come from, cancelled units struck out.
"""
import re

from examlib import build_driller, check, mm

C9 = "Chapter 9 post"
Q = []


def T(text, why=""):
    return (None, text, why)


# ------------------------------------------------------------ LaTeX helpers
def U(s):
    """'mol C3H8' -> \\text{mol C}_{3}\\text{H}_{8} (formula digits become subscripts)."""
    body = re.sub(r"(?<=[A-Za-z\)])(\d+)", r"}_{\1}\\text{", s)
    return (r"\text{" + body + "}").replace(r"\text{}", "")


def X(s):
    """A unit that cancels."""
    return r"\cancel{" + U(s) + "}"


def F(top_n, top_u, bot_n, bot_u, label):
    """Labelled conversion factor; the bottom unit cancels."""
    return (r"\underbrace{\frac{" + f"{top_n}\\ " + U(top_u) + "}{" + f"{bot_n}\\ " + X(bot_u) + "}}_{"
            + U(label) + "}")


def EQ(n, unit, factors, result, runit, final=False):
    """Display equation: n unit × factors = result runit (boxed if final)."""
    right = f"{result}\\ " + U(runit)
    if final:
        right = r"\boxed{" + right + "}"
    return "$$" + f"{n}\\ " + X(unit) + r" \times " + r" \times ".join(factors) + " = " + right + "$$"


# ------------------------------------------------------------ 1. coefficients
Q.append(dict(
    ch=9, kind="concept", title="What the coefficients mean", short="Ch 9 sl. 2–5",
    stem="For the balanced equation 2[[H2]](g) + [[O2]](g) → 2[[H2O]](g), which statement is correct?",
    correct=T("2 mol of [[H2]] reacts with 1 mol of [[O2]] to form 2 mol of [[H2O]]"),
    wrong=[T("2 g of [[H2]] reacts with 1 g of [[O2]] to form 2 g of [[H2O]]",
             "Coefficients count molecules or moles, never grams (slide 2)."),
           T("1 mol of [[H2]] reacts with 2 mol of [[O2]]",
             "The ratio is flipped. H~2~'s coefficient is 2 and O~2~'s is 1 (no number written means 1)."),
           T("The mass of [[H2O]] formed equals the mass of [[H2]] used",
             "Mass is conserved for the whole reaction: mass of H~2~ + mass of O~2~ = mass of H~2~O."),
           T("2 molecules of [[H2]] react to form 1 molecule of [[H2O]]",
             "H~2~O's coefficient is 2, so 2 molecules of H~2~ form **2** molecules of H~2~O.")],
    cite=f"{C9}, slide 2 (coefficients give relative numbers of molecules), slide 3 (Table 9.1: molecules, dozens, moles), slide 5",
    hw="HW22 — hw22ex1.png (H~2~ + F~2~ → 2HF read in molecules and in moles)",
    covers="Reading a balanced equation in moles: coefficients are mole (particle) ratios, not masses.",
    sol="""**Step 1: read the coefficients.** H~2~ **2**, O~2~ **1** (nothing written means 1), H~2~O **2**.

**Step 2: say it in moles.** Slide 3 (Table 9.1) shows that the same coefficients can be read as molecules, dozens, or
moles. In moles: **2 mol H~2~ + 1 mol O~2~ → 2 mol H~2~O**.

Coefficients never mean grams. 2 mol H~2~ (4.03 g) and 1 mol O~2~ (32.00 g) have very different masses.""",
))

# ------------------------------------------------------------ 2. choosing the mole ratio
Q.append(dict(
    ch=9, kind="concept", title="Choosing the mole ratio", short="Ch 9 sl. 5–8",
    stem="For 4Fe(s) + 3[[O2]](g) → 2[[Fe2O3]](s), which conversion factor converts **moles of [[O2]]** into "
         "**moles of [[Fe2O3]]**?",
    correct=T(r"$\rule[-2.2ex]{0pt}{5.8ex}\dfrac{2\ \text{mol Fe}_2\text{O}_3}{3\ \text{mol O}_2}$"),
    wrong=[T(r"$\rule[-2.2ex]{0pt}{5.8ex}\dfrac{3\ \text{mol O}_2}{2\ \text{mol Fe}_2\text{O}_3}$",
             "Upside down. The unit you have (mol O~2~) has to be on the bottom so it cancels."),
           T(r"$\rule[-2.2ex]{0pt}{5.8ex}\dfrac{2\ \text{mol Fe}_2\text{O}_3}{4\ \text{mol Fe}}$",
             "That converts mol Fe to mol Fe~2~O~3~. The question starts from O~2~."),
           T(r"$\rule[-2.2ex]{0pt}{5.8ex}\dfrac{3\ \text{mol O}_2}{4\ \text{mol Fe}}$",
             "That relates the two reactants (O~2~ and Fe). It never reaches Fe~2~O~3~."),
           T(r"$\rule[-2.2ex]{0pt}{5.8ex}\dfrac{32.00\ \text{g O}_2}{1\ \text{mol O}_2}$",
             "That is the molar mass of O~2~. It converts moles to grams of the **same** substance, not to another substance.")],
    cite=f"{C9}, slides 5–8 (mole ratios from the coefficients: N~2~ + 3H~2~ → 2NH~3~, N~2~ + O~2~ → 2NO)",
    hw="HW22 — hw22ex2.png (which mole ratio for 4B + 3O~2~ → 2B~2~O~3~: 3 mol O~2~ / 4 mol B)",
    covers="Building a mole ratio from two coefficients and orienting it want-over-have.",
    sol=r"""**Step 1: pick the two substances.** You **have** O~2~ and **want** Fe~2~O~3~. Fe is not involved.

**Step 2: read their coefficients.** O~2~ **3**, Fe~2~O~3~ **2**. So 3 mol O~2~ makes 2 mol Fe~2~O~3~.

**Step 3: orient it want-over-have.** Fe~2~O~3~ (want) on top, O~2~ (have) on the bottom:

$$\text{mol O}_2\times\frac{2\ \text{mol Fe}_2\text{O}_3}{3\ \text{mol O}_2}\ \text{leaves mol Fe}_2\text{O}_3$$""",
))

# ------------------------------------------------------------ 3. mole-mole
c3h8 = 2.40
o2_needed = c3h8 * 5 / 1
check(3, o2_needed, 12.0, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Mole–mole conversion", short="Ch 9 sl. 10–11",
    stem="Propane burns according to [[C3H8]](g) + 5[[O2]](g) → 3[[CO2]](g) + 4[[H2O]](g). How many moles of [[O2]] are "
         "needed to burn 2.40 mol of [[C3H8]] completely?",
    correct=(12.0, "12.0 mol", ""),
    wrong=[(c3h8 / 5, f"{c3h8 / 5:.3f} mol", "Ratio upside down: 2.40 × 1/5."),
           (c3h8, "2.40 mol", "Assumed 1 : 1. O~2~'s coefficient is 5."),
           (c3h8 * 3, f"{c3h8 * 3:.2f} mol", "Used CO~2~'s coefficient (3) instead of O~2~'s (5)."),
           (c3h8 * 4, f"{c3h8 * 4:.2f} mol", "Used H~2~O's coefficient (4) instead of O~2~'s (5).")],
    cite=f"{C9}, slide 11 (Mole–Mole Conversions Practice 2: 2C~2~H~6~ + 7O~2~), slide 10",
    hw="HW22 — hw22ex3.png (moles of one substance from moles of another, e.g. mol Se from mol H~2~O)",
    covers="Picking the right two coefficients out of a four-substance equation.",
    sol="**Step 1: coefficients you need.** Have C~3~H~8~ (coefficient **1**, nothing written); want O~2~ (coefficient **5**). "
        "CO~2~ and H~2~O are not involved.\n\n"
        "**Step 2: multiply by the mole ratio (want over have).**\n\n"
        + EQ("2.40", "mol C3H8", [F(5, "mol O2", 1, "mol C3H8", "coefficient of O2 / coefficient of C3H8")],
             "12.0", "mol O2", final=True),
))

# ------------------------------------------------------------ 4. order of steps
Q.append(dict(
    ch=9, kind="concept", title="Order of the stoichiometry steps", short="Ch 9 sl. 13–14",
    stem="You are given the mass of reactant A and asked for the mass of product B. Which sequence of conversions is correct?",
    correct=T("grams A → moles A → moles B → grams B"),
    wrong=[T("grams A → grams B, using the coefficients as a mass ratio",
             "Coefficients are mole ratios, never mass ratios (slide 2)."),
           T("grams A → moles A → grams B",
             "Skips the mole ratio. Moles of A are not moles of B unless the coefficients are equal."),
           T("grams A → moles B → moles A → grams B",
             "You can't get moles of B directly from grams of A. Convert to moles of A first."),
           T("grams A → moles A → moles B → atoms B",
             "Ends in particles. The question asks for grams, so the last step multiplies by B's molar mass.")],
    cite=f"{C9}, slide 14 (Steps for Calculating the Masses of Reactants and Products), slide 13, slide 16",
    hw="HW23 — hw23ex1.png (mass of C~2~H~2~ from 3.25 g CaC~2~)",
    covers="The four-step path of slide 14: moles are always the middle step, and the coefficients act only on moles.",
    sol=r"""Slide 14's steps after balancing: convert grams to moles, use the mole ratio, then convert moles to grams.

$$\text{g A}\xrightarrow{\ \times\frac{1\ \text{mol A}}{\text{molar mass of A}}\ }\text{mol A}\xrightarrow{\ \times\frac{\text{coef. B}}{\text{coef. A}}\ }\text{mol B}\xrightarrow{\ \times\frac{\text{molar mass of B}}{1\ \text{mol B}}\ }\text{g B}$$

The mole ratio is the **only** link between A and B, and it only works on moles. So there has to be a moles step on each
side of it.""",
))

# ------------------------------------------------------------ 5. grams to grams
h2o2 = 50.0 / mm("H2O2")
o2_mol = h2o2 / 2
o2_g = o2_mol * mm("O2")
check(5, o2_g, 23.5, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Grams to grams", short="Ch 9 sl. 14, 17–19",
    stem="Hydrogen peroxide decomposes: 2[[H2O2]](aq) → 2[[H2O]](l) + [[O2]](g). What mass of [[O2]] forms when 50.0 g of "
         "[[H2O2]] decomposes completely?",
    correct=(23.5, "23.5 g", ""),
    wrong=[(o2_mol, f"{o2_mol:.3f} g", "That is the **moles** of O~2~. You stopped before the last step."),
           (o2_mol * 16.00, f"{o2_mol * 16.00:.1f} g", "Used 16.00 g/mol (one O atom) instead of 32.00 g/mol for O~2~."),
           (h2o2 * mm("O2"), f"{h2o2 * mm('O2'):.1f} g", "Assumed 1 : 1. It takes 2 H~2~O~2~ to make 1 O~2~."),
           (50.0, "50.0 g", "Assumed the product mass equals the reactant mass. Some of the mass goes to H~2~O.")],
    cite=f"{C9}, slides 17–19 (Stoichiometry Practice: g → mol → mol → g), slide 14 (steps)",
    hw="HW23 — hw23ex2.png (grams of Br~2~ from the decomposition of 34.0 g BrF~3~)",
    covers="The full g → mol → mol → g chain with a 2 : 1 ratio.",
    sol="**Step 1: molar masses.** H~2~O~2~ = 2(1.008) + 2(16.00) = 34.02 g/mol. "
        "O~2~ = 2(16.00) = 32.00 g/mol (O~2~ has two O atoms).\n\n"
        "**Step 2: grams H~2~O~2~ to moles H~2~O~2~.**\n\n"
        + EQ("50.0", "g H2O2", [F(1, "mol H2O2", "34.02", "g H2O2", "molar mass of H2O2")], f"{h2o2:.4f}", "mol H2O2")
        + "\n\n**Step 3: moles H~2~O~2~ to moles O~2~.** Have H~2~O~2~ (coefficient **2**), want O~2~ (coefficient **1**).\n\n"
        + EQ(f"{h2o2:.4f}", "mol H2O2", [F(1, "mol O2", 2, "mol H2O2", "coefficient of O2 / coefficient of H2O2")],
             f"{o2_mol:.4f}", "mol O2")
        + "\n\n**Step 4: moles O~2~ to grams O~2~.**\n\n"
        + EQ(f"{o2_mol:.4f}", "mol O2", [F("32.00", "g O2", 1, "mol O2", "molar mass of O2")], "23.5", "g O2", final=True),
))

# ------------------------------------------------------------ 6. grams of one reactant to moles of the other
cac2 = 32.0 / mm("CaC2")
h2o_mol = cac2 * 2
check(6, h2o_mol, 0.998, 0.0005)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Grams to moles of another substance", short="Ch 9 sl. 18",
    stem="Calcium carbide reacts with water: [[CaC2]](s) + 2[[H2O]](l) → [[C2H2]](g) + [[Ca(OH)2]](aq). How many moles of "
         "[[H2O]] are needed to react completely with 32.0 g of [[CaC2]]?",
    correct=(0.998, "0.998 mol", ""),
    wrong=[(cac2 / 2, f"{cac2 / 2:.3f} mol", "Ratio upside down: × 1/2 instead of × 2/1."),
           (cac2, f"{cac2:.3f} mol", "Assumed 1 : 1. Water's coefficient is 2."),
           (mm("CaC2") / 32.0, f"{mm('CaC2') / 32.0:.2f} mol", "Divided the molar mass by the grams (64.10 ÷ 32.0)."),
           (h2o_mol * mm("H2O"), f"{h2o_mol * mm('H2O'):.1f} mol",
            "Multiplied by the molar mass of H~2~O. That gives grams of water, not moles.")],
    cite=f"{C9}, slide 18 (Stoichiometry Practice 2: moles of H~2~SO~4~ from 19.9 g KOH), slide 14",
    hw="HW22 — hw22ex3.png (moles of Br~2~ needed to react with 0.206 g Al); HW23 — hw23ex1.png (CaC~2~ + H~2~O)",
    covers="Stopping at moles when the question asks for moles: g → mol → mol, no final mass step.",
    sol="**Step 1: molar mass of CaC~2~.** 40.08 + 2(12.01) = 64.10 g/mol.\n\n"
        "**Step 2: grams CaC~2~ to moles CaC~2~.**\n\n"
        + EQ("32.0", "g CaC2", [F(1, "mol CaC2", "64.10", "g CaC2", "molar mass of CaC2")], f"{cac2:.4f}", "mol CaC2")
        + "\n\n**Step 3: moles CaC~2~ to moles H~2~O.** Have CaC~2~ (coefficient **1**), want H~2~O (coefficient **2**). "
          "The question asks for **moles**, so stop here.\n\n"
        + EQ(f"{cac2:.4f}", "mol CaC2", [F(2, "mol H2O", 1, "mol CaC2", "coefficient of H2O / coefficient of CaC2")],
             "0.998", "mol H2O", final=True),
))

# ------------------------------------------------------------ 7. balance first, then reactant mass needed
p_mol = 12.4 / mm("P")
o2_need = p_mol * 5 / 4
o2_need_g = o2_need * mm("O2")
check(7, o2_need_g, 16.0, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Balance first, then grams of a reactant", short="Ch 9 sl. 9, 16, 19",
    stem="Phosphorus burns in oxygen according to the **unbalanced** equation P(s) + [[O2]](g) → [[P4O10]](s). What mass of "
         "[[O2]] is needed to react completely with 12.4 g of P?",
    correct=(16.0, "16.0 g", ""),
    wrong=[(o2_need, f"{o2_need:.3f} g", "That is the **moles** of O~2~."),
           (o2_need * 16.00, f"{o2_need * 16.00:.2f} g", "Used 16.00 g/mol (one O atom) instead of 32.00 g/mol for O~2~."),
           (p_mol * 4 / 5 * mm("O2"), f"{p_mol * 4 / 5 * mm('O2'):.1f} g", "Ratio upside down: × 4/5 instead of × 5/4."),
           (p_mol * mm("O2"), f"{p_mol * mm('O2'):.1f} g", "Used the unbalanced equation (1 : 1). Balance it first.")],
    cite=f"{C9}, slide 16 (why the equation must be balanced first), slide 9 (balancing a combustion equation), slide 19",
    hw="HW22 — hw22ex3.png (unbalanced equations such as Al + Br~2~ → AlBr~3~: balance, then convert)",
    covers="Balancing before using coefficients, then g → mol → mol → g for a second reactant.",
    sol="**Step 1: balance.** P~4~O~10~ has 4 P, so put **4** in front of P. It has 10 O, and O~2~ supplies O in pairs, "
        "so put **5** in front of O~2~ (5 × 2 = 10). Balanced: **4P + 5O~2~ $\\rightarrow$ P~4~O~10~**.\n\n"
        "**Step 2: grams P to moles P.** Atomic mass of P = 30.97 g/mol.\n\n"
        + EQ("12.4", "g P", [F(1, "mol P", "30.97", "g P", "molar mass of P")], f"{p_mol:.4f}", "mol P")
        + "\n\n**Step 3: moles P to moles O~2~.** Have P (coefficient **4**), want O~2~ (coefficient **5**).\n\n"
        + EQ(f"{p_mol:.4f}", "mol P", [F(5, "mol O2", 4, "mol P", "coefficient of O2 / coefficient of P")],
             f"{o2_need:.4f}", "mol O2")
        + "\n\n**Step 4: moles O~2~ to grams O~2~.** Molar mass of O~2~ = 2(16.00) = 32.00 g/mol.\n\n"
        + EQ(f"{o2_need:.4f}", "mol O2", [F("32.00", "g O2", 1, "mol O2", "molar mass of O2")], "16.0", "g O2", final=True),
))

# ------------------------------------------------------------ 8. limiting reactant from moles
co, o2 = 3.0, 2.0
o2_for_co = co / 2
assert o2_for_co < o2 and abs((o2 - o2_for_co) - 0.5) < 1e-9
Q.append(dict(
    ch=9, kind="calc", title="Limiting reactant and leftover", short="Ch 9 sl. 21–23",
    stem="For 2CO(g) + [[O2]](g) → 2[[CO2]](g), a mixture contains 3.0 mol of CO and 2.0 mol of [[O2]]. Which statement is correct?",
    correct=T("CO is limiting, and 0.5 mol of [[O2]] is left over"),
    wrong=[T("[[O2]] is limiting, because there are fewer moles of [[O2]] than of CO",
             "Compared raw moles. The equation needs only 1 O~2~ per 2 CO, so 3.0 mol CO uses just 1.5 mol O~2~."),
           T("CO is limiting, and 1.0 mol of [[O2]] is left over",
             "Right limiting reactant, wrong leftover. CO uses 1.5 mol O~2~, so 2.0 − 1.5 = 0.5 mol remains."),
           T("[[O2]] is limiting, and 1.0 mol of CO is left over",
             "2.0 mol O~2~ would need 4.0 mol CO, and there is only 3.0 mol. CO runs out first."),
           T("Neither is limiting; both are used up completely",
             "That needs exactly a 2 : 1 mole ratio. 3.0 : 2.0 is not 2 : 1.")],
    cite=f"{C9}, slide 23 (Limiting Reactants Practice: 3Mg + N~2~, both given in moles), slides 21–22",
    hw="HW23 — hw23ex2.png (determine which reactant is limiting)",
    covers="Comparing what one reactant needs with what is available, using the mole ratio, not raw moles.",
    sol="**Step 1: both amounts are already in moles.** CO 3.0 mol, O~2~ 2.0 mol.\n\n"
        "**Step 2: how much O~2~ does all the CO need?** Have CO (coefficient **2**), want O~2~ (coefficient **1**).\n\n"
        + EQ("3.0", "mol CO", [F(1, "mol O2", 2, "mol CO", "coefficient of O2 / coefficient of CO")], "1.5", "mol O2 needed")
        + "\n\n**Step 3: compare.** You **have** 2.0 mol O~2~ and only **need** 1.5 mol. O~2~ is in excess, so **CO is "
          "limiting**.\n\n"
          "**Step 4: leftover.** 2.0 mol O~2~ available − 1.5 mol used = **0.5 mol O~2~ left over**.\n\n"
          "O~2~ has fewer moles (2.0 vs 3.0) and is still the excess reactant. That's why you never compare raw moles.",
))

# ------------------------------------------------------------ 9. limiting reactant from grams, theoretical yield
al = 10.0 / mm("Al")
cl2 = 35.0 / mm("Cl2")
cl2_for_al = al * 3 / 2
assert cl2_for_al > cl2                       # Cl2 is limiting
alcl3_mol = cl2 * 2 / 3
alcl3_g = alcl3_mol * mm("AlCl3")
check(9, alcl3_g, 43.9, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Theoretical yield from two masses", short="Ch 9 sl. 24–27",
    stem="Aluminum reacts with chlorine according to the **unbalanced** equation Al(s) + [[Cl2]](g) → [[AlCl3]](s). If 10.0 g "
         "of Al reacts with 35.0 g of [[Cl2]], what is the theoretical yield of [[AlCl3]]?",
    correct=(43.9, "43.9 g", ""),
    wrong=[(alcl3_mol, f"{alcl3_mol:.3f} g", "That is the **moles** of AlCl~3~."),
           (45.0, "45.0 g", "Added the two reactant masses. Some Al is left over, so it isn't all in the product."),
           (al * mm("AlCl3"), f"{al * mm('AlCl3'):.1f} g",
            "Calculated from Al. Al is in excess here, so this is more than the Cl~2~ can make."),
           (cl2 * mm("AlCl3"), f"{cl2 * mm('AlCl3'):.1f} g", "Used Cl~2~ but assumed 1 : 1. The ratio is 2 AlCl~3~ : 3 Cl~2~.")],
    cite=f"{C9}, slide 27 (theoretical yield when both reactant masses are given), slide 24 (limiting reactant from grams), slide 25",
    hw="HW23 — hw23ex3.png (Fe + O~2~ unbalanced: find the limiting reactant, then the mass of product)",
    covers="Balance → moles of each reactant → limiting reactant → product from the limiting reactant only.",
    sol="**Step 1: balance.** AlCl~3~ has 3 Cl and Cl~2~ comes in pairs, so use 2AlCl~3~ (6 Cl) and 3Cl~2~ (6 Cl). Then 2 Al on "
        "the left: **2Al + 3Cl~2~ $\\rightarrow$ 2AlCl~3~**.\n\n"
        "**Step 2: grams to moles for each reactant.** Al = 26.98 g/mol; Cl~2~ = 2(35.45) = 70.90 g/mol.\n\n"
        + EQ("10.0", "g Al", [F(1, "mol Al", "26.98", "g Al", "molar mass of Al")], f"{al:.4f}", "mol Al")
        + "\n\n"
        + EQ("35.0", "g Cl2", [F(1, "mol Cl2", "70.90", "g Cl2", "molar mass of Cl2")], f"{cl2:.4f}", "mol Cl2")
        + "\n\n**Step 3: how much Cl~2~ does all the Al need?** Have Al (coefficient **2**), want Cl~2~ (coefficient **3**).\n\n"
        + EQ(f"{al:.4f}", "mol Al", [F(3, "mol Cl2", 2, "mol Al", "coefficient of Cl2 / coefficient of Al")],
             f"{cl2_for_al:.4f}", "mol Cl2 needed")
        + f"\n\n**Step 4: compare.** You **need** {cl2_for_al:.4f} mol Cl~2~ but only **have** {cl2:.4f} mol. The Cl~2~ runs out "
          "first, so **Cl~2~ is limiting** (even though Al has fewer moles and less mass).\n\n"
          "**Step 5: product from the limiting reactant.** Have Cl~2~ (coefficient **3**), want AlCl~3~ (coefficient **2**). "
          "Molar mass of AlCl~3~ = 26.98 + 3(35.45) = 133.33 g/mol.\n\n"
        + EQ(f"{cl2:.4f}", "mol Cl2", [F(2, "mol AlCl3", 3, "mol Cl2", "coefficient of AlCl3 / coefficient of Cl2"),
                                      F("133.33", "g AlCl3", 1, "mol AlCl3", "molar mass of AlCl3")],
             "43.9", "g AlCl3", final=True)
        + f"\n\n**Cross-check:** all the Al would make {al:.4f} mol AlCl~3~ × 133.33 = {al * mm('AlCl3'):.1f} g. The smaller "
          "amount (43.9 g, from Cl~2~) is the theoretical yield.",
))

# ------------------------------------------------------------ 10. percent yield
caco3 = 25.0 / mm("CaCO3")
cao_theo = caco3 * mm("CaO")
pct = 12.4 / cao_theo * 100
check(10, pct, 88.5, 0.05)
Q.append(dict(
    ch=9, kind="calc", numeric=True, title="Percent yield", short="Ch 9 sl. 28–32",
    stem="Limestone decomposes when heated: [[CaCO3]](s) → CaO(s) + [[CO2]](g). A student heats 25.0 g of [[CaCO3]] and "
         "collects 12.4 g of CaO. What is the percent yield?",
    correct=(88.5, "88.5%", ""),
    wrong=[(pct / 100, f"{pct / 100:.3f}%", "Forgot to multiply by 100."),
           (12.4 / 25.0 * 100, f"{12.4 / 25.0 * 100:.1f}%",
            "Divided by the mass of CaCO~3~. The bottom must be the theoretical yield of **CaO**."),
           (mm("CaO") / mm("CaCO3") * 100, f"{mm('CaO') / mm('CaCO3') * 100:.1f}%",
            "That is the mass percent of CaO in CaCO~3~ (56.08 / 100.09). It doesn't use the actual yield."),
           (cao_theo / 12.4 * 100, f"{cao_theo / 12.4 * 100:.0f}%",
            "Upside down: theoretical / actual. A yield can't be over 100% (slide 29).")],
    cite=f"{C9}, slide 30 (percent yield = actual / theoretical × 100%), slide 32 (2KClO~3~ decomposition), slides 25, 28",
    hw="HW24 — hw24ex1.png (percent yield from theoretical and actual mass of magnesium oxide)",
    covers="Two parts: theoretical yield from the only reactant, then actual / theoretical × 100.",
    sol="**Part 1: theoretical yield of CaO.** CaCO~3~ is the only reactant, so it is limiting. Molar masses: "
        "CaCO~3~ = 40.08 + 12.01 + 3(16.00) = 100.09 g/mol; CaO = 40.08 + 16.00 = 56.08 g/mol. "
        "Mole ratio: have CaCO~3~ (coefficient **1**), want CaO (coefficient **1**).\n\n"
        + EQ("25.0", "g CaCO3", [F(1, "mol CaCO3", "100.09", "g CaCO3", "molar mass of CaCO3")], f"{caco3:.4f}", "mol CaCO3")
        + "\n\n"
        + EQ(f"{caco3:.4f}", "mol CaCO3", [F(1, "mol CaO", 1, "mol CaCO3", "coefficients"),
                                          F("56.08", "g CaO", 1, "mol CaO", "molar mass of CaO")],
             f"{cao_theo:.2f}", "g CaO (theoretical)")
        + "\n\n**Part 2: percent yield.** The actual yield (12.4 g, measured) goes on top; the theoretical yield on the bottom.\n\n"
        + "$$\\text{percent yield}=\\frac{12.4\\ \\cancel{\\text{g CaO}}\\ (\\text{actual})}{"
        + f"{cao_theo:.2f}" + "\\ \\cancel{\\text{g CaO}}\\ (\\text{theoretical})}\\times100\\% = \\boxed{88.5\\%}$$",
))

if __name__ == "__main__":
    assert len(Q) == 10, len(Q)
    build_driller(9, 1, Q, seed=91)
    from collections import Counter
    dist = Counter(q["ans"] for q in Q)
    assert all(dist[L] == 2 for L in "abcde"), dist
