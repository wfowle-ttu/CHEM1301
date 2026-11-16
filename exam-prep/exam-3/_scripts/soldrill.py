"""Shared 15-question layout for the solubility drillers (driller-7-n).

Layout: 1 concept · 2 pick the insoluble formula · 3 pick the soluble formula (rule-2 trap) ·
4 pick the soluble compound by name · 5 net ionic equation from formulas · 6 count the soluble ones · 7 pick the insoluble
compound by name · 8 which precipitate forms · 9 balanced molecular equation · 10 which pair gives
NR · 11 which pair gives a precipitate · 12 net ionic equation · 13 spectator ions · 14 selective
precipitation · 15 concept.
"""
from collections import Counter

from examlib import build_driller
from solib import C7, q_count, q_mix, q_mol, q_net, q_pair, q_pick, q_rule, q_select, q_spect

SCOPE = "Solubility rules and precipitation reactions (Chapter 7, slides 10–20)"
INTRO = """Every answer was checked by `_scripts/solib.py`, which applies the six rules of Table 7.1 (slide 11) in the
course's priority order and refuses any compound the rules don't settle cleanly. Citations name the slide (same
number in the `.pdf` and `.pptx`) plus the closest homework screenshot.

**How to read the solutions.** Each compound's call names the rule that decides it. Mixing problems follow
slide 14: write the ions, exchange the anions, apply the rules. Study guide 7.3–7.5 uses the same method."""
NOTE = " **Solubility rules are not provided:** work from memory, as on the exam."

BANDS = ("14–15 solubility rules are solid · 11–13 reread study guide 7.3–7.5 for the questions you missed ·\n"
         "10 or below rewrite Table 7.1 from memory, then redo this driller before the next one.")

CL = f"{C7}, slide 11 (Table 7.1: General Rules for Solubility), slide 12 (Solubility Practice: NaOH, BaSO~4~, CaCO~3~)"
PRED = f"{C7}, slide 14 (How to Predict Precipitates When Solutions of Two Ionic Compounds Are Mixed), slide 11"
MOL = f"{C7}, slide 15 (Molecular Equations: K~2~CrO~4~ + Ba(NO~3~)~2~), slide 14, slide 11"
NET = f"{C7}, slides 16–17 (complete ionic and net ionic equations), slides 19–20 (Writing Equations Practice), slide 11"
SPEC = f"{C7}, slide 17 (spectator ions), slide 18 (Types of Equations), slide 14"
HW_CL = "HW14 — hw14ex5.png (classify iron(II) sulfate, sodium carbonate, nickel(II) hydroxide)"
HW_RULE = "HW14 — hw14ex3.png and hw14ex4.png (which rule explains the solubility: ammonium sulfide, cobalt(II) sulfate)"
HW_MIX = "HW15 — hw15ex3.png (does a reaction occur? NR or net ionic: KNO~3~ + Na~2~S, AlCl~3~ + KOH)"
HW_MOL = "HW15 — hw15ex4.png (balanced molecular equations for precipitations, or NR)"
HW_NET = "HW15 — hw15ex2.png (net ionic equations: Sr^2+^ + CrO~4~^2−^, MgCl~2~ + K~2~CO~3~)"


def legacy_rule_questions(s):
    """Drillers 7-1 to 7-3 only. Don't use for new drillers: the choices print the rules, which gives them away
    (the user asked to stop using this question type on 2026-11-10)."""
    return [q_rule("Which rule decides (soluble)", "Ch 7 sl. 11", *s["rule_sol"], CL, HW_RULE, s["rule_sol_others"]),
            q_rule("Which rule decides (insoluble)", "Ch 7 sl. 11", *s["rule_ins"], CL, HW_RULE, s["rule_ins_others"])]


def build(n, s):
    Q = [
        s["concept1"],
        q_pick("Which compound is insoluble?", "Ch 7 sl. 11–12", "Which compound is **insoluble** in water?",
               s["insol"], False, CL, HW_CL),
        q_pick("Which compound is soluble?", "Ch 7 sl. 11–12", "Which compound is **soluble** in water?",
               s["sol"], True, CL, HW_CL),
        *(legacy_rule_questions(s) if "rule_sol" in s else [
            q_pick("Classifying compounds by name (soluble)", "Ch 7 sl. 11",
                   "Which of these compounds **is** soluble in water?", s["names_sol"], True, CL, HW_CL, use_names=True),
            q_net("Net ionic equation from formulas", "Ch 7 sl. 16–20", *s["net2"], NET, HW_NET, by_name=False),
        ]),
        q_count("Counting soluble compounds", "Ch 7 sl. 11–12", s["count"], CL, HW_CL)[0],
        q_pick("Classifying compounds by name", "Ch 7 sl. 11", "Which of these compounds is **not** soluble in water?",
               s["names"], False, CL, HW_CL, use_names=True),
        q_mix("Predicting the precipitate", "Ch 7 sl. 14", *s["mix"], PRED, HW_MIX, s["mix_wrong"]),
        q_mol("Balanced molecular equation", "Ch 7 sl. 14–15", *s["mol"], MOL, HW_MOL, by_name=False),
        q_pair("Which mixture gives no reaction?", "Ch 7 sl. 14", s["pairs_nr"], False, PRED, HW_MIX),
        q_pair("Which mixture forms a precipitate?", "Ch 7 sl. 14", s["pairs_ppt"], True, PRED, HW_MIX),
        q_net("Net ionic equation", "Ch 7 sl. 16–20", *s["net"], NET, HW_NET),
        q_spect("Spectator ions", "Ch 7 sl. 17–18", *s["spect"], SPEC, HW_NET),
        q_select("Precipitating one ion but not another", "Ch 7 sl. 11, 14", *s["select"], PRED, HW_MIX),
        s["concept2"],
    ]
    assert len(Q) == 15
    build_driller(7, n, Q, seed=70 + n, scope=SCOPE, bands=BANDS, intro=INTRO, note=NOTE)
    dist = Counter(q["ans"] for q in Q)
    assert all(dist[L] == 3 for L in "abcde"), dist
