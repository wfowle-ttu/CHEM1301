"""Shared pieces for the reaction-type drillers (study guide 7.6–7.8, Ch 7 slides 21–45).

Layout (15): 1–5 acid–base (7.6): definition · strong acid/base identification · the salt ·
net ionic equation · balancing. 6–9 oxidation–reduction (7.7): which reaction is redox ·
electrons per atom · electron transfer in a single replacement · redox principles. 10–15
classification (7.8): classify one reaction · class by type · multiple classes · a definition ·
balancing from words · balancing a combustion.

Questions are hand-written; every balanced equation is checked by `balanced()`.
"""
from collections import Counter

from drillib import T, counts
from examlib import build_driller

C7 = "Chapter 7 post"
SCOPE = "Types of reactions: acid–base, oxidation–reduction, and classifying reactions (Chapter 7, slides 21–45)"
INTRO = """Every balanced equation in this driller and key was checked atom by atom by `_scripts/rxndrill.py`.
Definitions follow the course slides (Chapter 7, slides 21–45); where the course wording differs from other sources,
the course wins. Citations name the slide (same number in the `.pdf` and `.pptx`) plus the closest homework screenshot.

**How to read the solutions.** Classification answers name the clue that decides each class (a solid, water, a gas,
electrons moving, O~2~ and a flame, one compound from simpler ones, or one compound breaking apart). Balancing answers
count each element on both sides. Study guide 7.6–7.8 uses the same approach."""
NOTE = " The strong-acid and strong-base lists are **not** provided: work from memory."
BANDS = ("14–15 reaction types are solid · 11–13 reread study guide 7.6–7.8 for the questions you missed ·\n"
         "10 or below rework slides 21–45, then redo this driller before the next one.")

AB = f"{C7}, slides 21–26 (Arrhenius acids and bases; strong acids and bases, principles 1–6)"
AB_PRAC = f"{C7}, slides 27–28 (Practice: H~3~PO~4~ + Ca(OH)~2~; nitrous acid + potassium hydroxide)"
RX = f"{C7}, slides 29–32 (electron transfer; redox principles 1 and 2)"
RX_PRAC = f"{C7}, slides 33–34 (Practice: 2Al + N~2~; Cu + FeCl~2~), slide 38 (2Li + F~2~)"
CLS = f"{C7}, slides 35–43 (precipitation, double-displacement, acid–base, redox, gas evolution, single-replacement, combustion, synthesis, decomposition)"
CLS_PRAC = f"{C7}, slide 44 (Reaction Classification Practice), slide 45 (Summary of Classes of Reactions)"
HW16_BASE = "HW16 — hw16ex1.png (what is meant by a strong base; strong electrolytes)"
HW16_SALT = "HW16 — hw16ex2.png (what salt forms: HI + NaOH, NaOH + HNO~3~, HCl + CsOH)"
HW16_RX = "HW16 — hw16ex3.png (Ba + Cl~2~: electrons lost and gained)"
HW17_CLS = "HW17 — hw17ex1.png (precipitation, acid–base, and/or oxidation–reduction)"
HW17_COMB = "HW17 — hw17ex2.png (definition of combustion; heat energy; 2C~3~H~6~ + 9O~2~ → 6CO~2~ + 6H~2~O)"
HW17_WORDS = "HW17 — hw17ex4.png (balance from words: P~4~ + 6Cl~2~ → 4PCl~3~; NH~4~NO~2~ → N~2~ + 2H~2~O)"


def balanced(lhs, rhs):
    """Assert that sum(coef × formula) has the same atoms on both sides. lhs/rhs: [(coef, 'H2SO4'), ...]."""
    def tally(side):
        c = Counter()
        for k, f in side:
            for el, n in counts(f).items():
                c[el] += k * n
        return c
    assert tally(lhs) == tally(rhs), (lhs, rhs, tally(lhs), tally(rhs))


def num(correct, wrong):
    """Numeric choice tuples: correct=int, wrong=[(int, why), ...]."""
    return dict(numeric=True, correct=(correct, str(correct), ""), wrong=[(v, str(v), w) for v, w in wrong])


def build(n, Q):
    assert len(Q) == 15, len(Q)
    for q in Q:
        q.setdefault("ch", 7)
        q.setdefault("kind", "calc" if q.get("numeric") else "concept")
    build_driller(7, n, Q, seed=70 + n, scope=SCOPE, bands=BANDS, intro=INTRO, note=NOTE)
    dist = Counter(q["ans"] for q in Q)
    assert all(dist[L] == 3 for L in "abcde"), dist
