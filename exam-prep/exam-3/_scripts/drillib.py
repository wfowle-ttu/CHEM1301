"""Question generators for the drillers (section 8.7 + Chapter 9).

Each generator computes the answer, the distractors (each tied to a named mistake), and a key
solution in the study-guide format: every step named, every conversion factor written
want-over-have with an underbrace label saying where its numbers come from, cancelled units
struck out. All numbers come from examlib.AM, so the key and the choices always agree.
"""
import math
import re
from functools import reduce

from examlib import AM, check, mm  # noqa: F401 (check re-exported for build scripts)

C8, C9 = "Chapter 8 post", "Chapter 9 post"


def T(text, why=""):
    return (None, text, why)


# ------------------------------------------------------------ number formatting
def sig(x, n=3):
    """x to n significant figures, without scientific notation."""
    if x == 0:
        return "0"
    d = n - 1 - math.floor(math.log10(abs(x)))
    return f"{x:.{d}f}" if d > 0 else f"{round(x, d):.0f}"


def amt(a):
    """Given mass/percent as written in the question (keeps trailing zeros)."""
    return f"{a:.2f}" if round(a, 2) == a else f"{a:.3f}"


def amf(el):
    v = AM[el]
    return f"{v:.2f}" if round(v, 2) == v else f"{v:.3f}"


# ------------------------------------------------------------ formulas
def counts(formula):
    """Ordered element counts: 'Al2(SO4)3' -> {'Al': 2, 'S': 3, 'O': 12}."""
    def parse(s, i=0):
        out = {}
        while i < len(s):
            if s[i] == "(":
                sub, i = parse(s, i + 1)
                m = re.match(r"\d*", s[i:]).group()
                i += len(m)
                k = int(m) if m else 1
                for el, n in sub.items():
                    out[el] = out.get(el, 0) + n * k
            elif s[i] == ")":
                return out, i + 1
            else:
                m = re.match(r"([A-Z][a-z]?)(\d*)", s[i:])
                out[m.group(1)] = out.get(m.group(1), 0) + (int(m.group(2)) if m.group(2) else 1)
                i += len(m.group())
        return out, i
    return parse(formula)[0]


def fstr(els, subs):
    """('C','H','O'), (9, 8, 4) -> 'C9H8O4'."""
    return "".join(e + (str(n) if n != 1 else "") for e, n in zip(els, subs))


def mm_text(formula):
    """'98.09' style molar mass with its sum: H2SO4 = 2(1.008) + 32.07 + 4(16.00) = 98.09 g/mol."""
    c = counts(formula)
    if len(c) == 1 and list(c.values())[0] == 1:
        return f"[[{formula}]] = {mm(formula):.2f} g/mol (periodic table)"
    parts = [f"{n}({amf(el)})" if n > 1 else amf(el) for el, n in c.items()]
    return f"[[{formula}]] = " + " + ".join(parts) + f" = {mm(formula):.2f} g/mol"


# ------------------------------------------------------------ LaTeX helpers
def U(s):
    """'mol C3H8' -> \\text{mol C}_{3}\\text{H}_{8}."""
    body = re.sub(r"(?<=[A-Za-z\)])(\d+)", r"}_{\1}\\text{", s)
    return (r"\text{" + body + "}").replace(r"\text{}", "")


def X(s):
    return r"\cancel{" + U(s) + "}"


def F(top_n, top_u, bot_n, bot_u, label):
    return (r"\underbrace{\frac{" + f"{top_n}\\ " + U(top_u) + "}{" + f"{bot_n}\\ " + X(bot_u) + "}}_{"
            + U(label) + "}")


def EQ(n, unit, factors, result, runit, final=False):
    right = f"{result}\\ " + U(runit)
    if final:
        right = r"\boxed{" + right + "}"
    return "$$" + f"{n}\\ " + X(unit) + r" \times " + r" \times ".join(factors) + " = " + right + "$$"


def to_mol(g, f, gs=None):
    """Grams of f -> moles, as a display equation. Returns (moles, latex)."""
    mol = g / mm(f)
    return mol, EQ(gs or sig(g), f"g {f}", [F(1, f"mol {f}", f"{mm(f):.2f}", f"g {f}", f"molar mass of {f}")],
                   sig(mol, 4), f"mol {f}")


def ratio(mol, have, c_have, want, c_want, final=False, result=None):
    out = mol * c_want / c_have
    return out, EQ(sig(mol, 4), f"mol {have}",
                   [F(c_want, f"mol {want}", c_have, f"mol {have}", f"coefficient of {want} / coefficient of {have}")],
                   result or sig(out, 4), f"mol {want}", final)


def to_g(mol, f, final=False, result=None):
    g = mol * mm(f)
    return g, EQ(sig(mol, 4), f"mol {f}", [F(f"{mm(f):.2f}", f"g {f}", 1, f"mol {f}", f"molar mass of {f}")],
                 result or sig(g), f"g {f}", final)


class Steps:
    """Numbered '**Step n: title.** text' paragraphs."""
    def __init__(self):
        self.parts, self.n = [], 0

    def add(self, title, *body):
        self.n += 1
        end = "" if title.endswith("?") else "."
        self.parts.append(f"**Step {self.n}: {title}{end}** " + "\n\n".join(b for b in body if b))
        return self

    def note(self, text):
        self.parts.append(text)
        return self

    def __str__(self):
        return "\n\n".join(self.parts)


def pick(correct_text, cands, k=4):
    """First k distractors whose display text is distinct and differs from the answer."""
    out, seen = [], {correct_text}
    for c in cands:
        if c[1] not in seen and (c[0] is None or c[0] > 0):
            out.append(c)
            seen.add(c[1])
        if len(out) == k:
            return out
    raise ValueError(f"only {len(out)} distractors for {correct_text}")


# ============================================================ section 8.7
def empirical(els, amounts):
    """Empirical formula from masses (g). Returns dict with moles, ratios, multiplier, subscripts."""
    moles = [a / AM[e] for e, a in zip(els, amounts)]
    small = min(moles)
    ratios = [m / small for m in moles]
    for mult in range(1, 7):
        if all(abs(r * mult - round(r * mult)) <= 0.1 for r in ratios):
            break
    else:
        raise ValueError("no multiplier")
    subs = [round(r * mult) for r in ratios]
    g = reduce(math.gcd, subs)
    assert g == 1, (els, subs)
    return dict(moles=moles, small=small, ratios=ratios, mult=mult, subs=subs, formula=fstr(els, subs))


MULT_WHY = {2: "a decimal near .5 (halves), so multiply **every** result by 2",
            3: "a decimal near .33 or .67 (thirds), so multiply **every** result by 3",
            4: "a decimal near .25 or .75 (quarters), so multiply **every** result by 4"}


def empirical_steps(els, amounts, given, steps=None, grams_note=None):
    """Solution steps for a percent/grams -> empirical formula problem. Returns (result dict, Steps)."""
    r = empirical(els, amounts)
    s = steps or Steps()
    if given == "percent":
        s.add("percent to grams", "Pretend you have exactly **100 g** of the compound, so each percent becomes that many grams: "
              + ", ".join(f"{amt(a)} g {e}" for e, a in zip(els, amounts)) + ".")
    else:
        s.add("grams of each element", grams_note or "The grams are given: "
              + ", ".join(f"{amt(a)} g {e}" for e, a in zip(els, amounts)) + ".")
    eqs = [EQ(amt(a), f"g {e}", [F(1, f"mol {e}", amf(e), f"g {e}", f"atomic mass of {e}")], sig(m, 4), f"mol {e}")
           for e, a, m in zip(els, amounts, r["moles"])]
    s.add("grams to moles for each element", "Divide by each element's own atomic mass (periodic table):", *eqs)
    small_el = els[r["moles"].index(r["small"])]
    rows = ["| Element | Moles (step 2) | ÷ smallest (" + sig(r["small"], 4) + f" mol {small_el}) |"
            + (f" × {r['mult']} |" if r["mult"] > 1 else "") + " Subscript |",
            "|:-:|:-:|:-:|" + (":-:|" if r["mult"] > 1 else "") + ":-:|"]
    for e, m, q, n in zip(els, r["moles"], r["ratios"], r["subs"]):
        rows.append(f"| {e} | {sig(m, 4)} | {q:.2f} |" + (f" {q * r['mult']:.2f} |" if r["mult"] > 1 else "") + f" {n} |")
    s.add("divide every mole value by the smallest one",
          f"The smallest mole value is {sig(r['small'], 4)} mol ({small_el}). Divide **each** element's moles by it:",
          "\n".join(rows))
    frac = [q for q in r["ratios"] if abs(q - round(q)) > 0.1]
    if r["mult"] == 1:
        s.add("whole numbers?", "Every result is within 0.1 of a whole number, so round them. No multiplier is needed. "
              f"Empirical formula: **[[{r['formula']}]]**.")
    else:
        s.add("whole numbers?", f"{frac[0]:.2f} is not within 0.1 of a whole number. It ends in {MULT_WHY[r['mult']]}, "
              f"including the elements that were already whole (last columns of the table). "
              f"Empirical formula: **[[{r['formula']}]]**.")
    return r, s


def emp_distractors(els, amounts, r, extra=()):
    """Formula distractors tied to the classic empirical-formula mistakes."""
    cands = list(extra)
    if r["mult"] > 1:
        rounded = [max(1, round(q)) for q in r["ratios"]]
        cands.append(T(f"[[{fstr(els, rounded)}]]", "Rounded the fractional result instead of multiplying "
                       f"(only results within 0.1 of a whole number may be rounded)."))
        only = [round(q * r["mult"]) if abs(q - round(q)) > 0.1 else round(q) for q in r["ratios"]]
        cands.append(T(f"[[{fstr(els, only)}]]", f"Multiplied only the fractional element by {r['mult']}. "
                       "The same multiplier goes on **every** element."))
    pct = [round(a / min(amounts)) for a in amounts]
    cands.append(T(f"[[{fstr(els, [max(1, p) for p in pct])}]]",
                   "Used the masses (percents) directly instead of converting to moles first."))
    cands.append(T(f"[[{fstr(els, [n * 2 for n in r['subs']])}]]",
                   "Not the **smallest** whole-number ratio; every subscript can still be divided by 2."))
    cands.append(T(f"[[{fstr(els, r['subs'][::-1])}]]", "Subscripts swapped between the elements."))
    for i, (e, n, q) in enumerate(zip(els, r["subs"], r["ratios"])):
        for d in (1, -1):
            if n + d >= 1:
                alt = r["subs"][:i] + [n + d] + r["subs"][i + 1:]
                if reduce(math.gcd, alt) == 1:
                    cands.append(T(f"[[{fstr(els, alt)}]]",
                                   f"Miscounted {e}: its step-3 result is {q:.2f}"
                                   + (f" (× {r['mult']} = {q * r['mult']:.2f})" if r["mult"] > 1 else "")
                                   + f", which gives {n}, not {n + d}."))
    return pick(f"[[{r['formula']}]]", cands)


def q_empirical(title, short, stem, els, amounts, given, cite, hw, extra=(), grams_note=None, slides="slides 42–43"):
    r, s = empirical_steps(els, amounts, given, grams_note=grams_note)
    return dict(
        ch=8, kind="calc", title=title, short=short, stem=stem,
        correct=T(f"[[{r['formula']}]]"), wrong=emp_distractors(els, amounts, r, extra),
        cite=cite, hw=hw,
        covers="The 4-step method: grams → moles → divide by the smallest → whole numbers (multiply every element if needed).",
        sol=str(s),
    ), r


def q_molecular(title, short, stem, emp, molar, cite, hw):
    """Empirical formula + molar mass -> molecular formula."""
    c = counts(emp)
    em = mm(emp)
    n = round(molar / em)
    assert abs(molar / em - n) < 0.02, (emp, molar / em)
    els, subs = list(c), list(c.values())
    mol_f = fstr(els, [k * n for k in subs])
    cands = [T(f"[[{emp}]]", "That is the empirical formula itself (n = 1). Its molar mass would be "
               f"{em:.2f} g/mol, not {molar}."),
             T(f"[[{fstr(els, [subs[0] * n] + subs[1:])}]]", f"Multiplied only the first subscript by n = {n}. "
               "**Every** subscript gets multiplied."),
             T(f"[[{fstr(els, [k * (n + 1) for k in subs])}]]", f"n = {n + 1} would give a molar mass of {em * (n + 1):.2f} g/mol."),
             T(f"[[{fstr(els, [k * (n - 1) for k in subs])}]]" if n > 2 else f"[[{fstr(els, [k * 2 * n for k in subs])}]]",
               f"n = {n - 1} would give {em * (n - 1):.2f} g/mol." if n > 2 else
               f"n = {2 * n} would give {em * 2 * n:.2f} g/mol."),
             T(f"[[{fstr(els, [k + n for k in subs])}]]", f"Added n = {n} to each subscript instead of multiplying.")]
    s = Steps()
    s.add("empirical formula mass", "Add up the atomic masses in the empirical formula: " + mm_text(emp) + ".")
    s.add("find n", "$$n=\\frac{\\text{molar mass of the compound}}{\\text{empirical formula mass}}=\\frac{"
          + f"{molar}\\ \\text{{g/mol}}}}{{{em:.2f}\\ \\text{{g/mol}}}} = {molar / em:.2f}\\approx {n}$$")
    s.add("multiply every subscript by n",
          f"([[{emp}]])~{n}~: " + ", ".join(f"{e} {k} × {n} = {k * n}" for e, k in zip(els, subs))
          + f". Molecular formula: **[[{mol_f}]]**.")
    return dict(ch=8, kind="calc", title=title, short=short, stem=stem, correct=T(f"[[{mol_f}]]"),
                wrong=pick(f"[[{mol_f}]]", cands), cite=cite, hw=hw,
                covers="Molecular formula = (empirical formula)~n~ with n = molar mass ÷ empirical formula mass.",
                sol=str(s))


# ============================================================ Chapter 9
def q_mass(title, short, stem, A, cA, B, cB, given, gu, wu, cite, hw, balance=None, others=(), covers=None,
           drop=()):
    """Stoichiometry: given amount of A (gu = 'g' or 'mol') -> amount of B (wu = 'g' or 'mol')."""
    molA = given / mm(A) if gu == "g" else given
    molB = molA * cB / cA
    res = molB * mm(B) if wu == "g" else molB
    ans = sig(res)
    unit = " g" if wu == "g" else " mol"

    def disp(v):
        return (v, sig(v) + unit)
    conv = (lambda m: m * mm(B)) if wu == "g" else (lambda m: m)
    cands = [disp(conv(molA * cA / cB)) + (f"Mole ratio upside down: × {cA}/{cB} instead of × {cB}/{cA}.",)]
    if cA != cB:
        cands.append(disp(conv(molA)) + (f"Assumed 1 : 1. The coefficients are {cA} ({A}) and {cB} ({B}).",))
    if wu == "g":
        cands.append(disp(molB) + (f"That is the **moles** of {B}. The last step (× molar mass) is missing.",))
        if A != B:
            cands.append(disp(molB * mm(A)) + (f"Used the molar mass of {A} in the last step instead of {B}'s.",))
    else:
        cands.append(disp(molB * mm(B)) + (f"Multiplied by the molar mass of {B}. That gives grams, not moles.",))
    for name, c in others:
        cands.append(disp(conv(molA * c / cA)) + (f"Used {name}'s coefficient ({c}) instead of {B}'s ({cB}).",))
    if gu == "g" and wu == "g":
        cands.append(disp(given) + ("Assumed the mass of product equals the mass of reactant.",))
    if gu == "g":
        cands.append(disp(conv(mm(A) / given * cB / cA)) + (f"Divided the molar mass by the grams ({mm(A):.2f} ÷ {sig(given)}).",))
    cands.append(disp(conv(molA * cA * cB)) + (f"Multiplied by both coefficients (× {cB} × {cA}) instead of × {cB}/{cA}.",))
    cands = [c for c in cands if not any(d in c[2] for d in drop)]
    cands = [(v, t.replace("[[", "").replace("]]", ""), w) for v, t, w in cands]
    cands = [(v, t, re.sub(r"\b([A-Z][a-z]?\d[A-Za-z0-9()]*|[A-Z][a-z]?[A-Z][A-Za-z0-9()]*)\b", r"[[\1]]", w)) for v, t, w in cands]

    s = Steps()
    if balance:
        s.add("balance the equation", balance)
    mms = []
    if gu == "g":
        mms.append(mm_text(A))
    if wu == "g":
        mms.append(mm_text(B))
    if mms:
        s.add("molar masses", "; ".join(mms) + ".")
    if gu == "g":
        _, e = to_mol(given, A)
        s.add(f"grams [[{A}]] to moles [[{A}]]", e)
    last = wu == "mol"
    _, e = ratio(molA, A, cA, B, cB, final=last, result=ans if last else None)
    s.add(f"moles [[{A}]] to moles [[{B}]]",
          f"Have [[{A}]] (coefficient **{cA}**), want [[{B}]] (coefficient **{cB}**)."
          + (" The question asks for **moles**, so stop here." if last else ""), e)
    if wu == "g":
        _, e = to_g(molB, B, final=True, result=ans)
        s.add(f"moles [[{B}]] to grams [[{B}]]", e)
    return dict(ch=9, kind="calc", numeric=True, title=title, short=short, stem=stem,
                correct=(float(ans), ans + unit, ""), wrong=pick(ans + unit, cands), cite=cite, hw=hw,
                covers=covers or f"{gu} → mol → mole ratio → {wu}" + (", after balancing" if balance else "") + ".",
                sol=str(s)), res


def q_yield(title, short, stem, A, cA, gA, B, cB, gB, P, cP, cite, hw, balance=None):
    """Theoretical yield (g of P) from grams of two reactants."""
    mA, mB = gA / mm(A), gB / mm(B)
    needB = mA * cB / cA
    if needB > mB:
        L, cL, mL, E, cE, mE = B, cB, mB, A, cA, mA
    else:
        L, cL, mL, E, cE, mE = A, cA, mA, B, cB, mB
    molP = mL * cP / cL
    gP = molP * mm(P)
    ans = sig(gP)
    fromE = mE * cP / cE * mm(P)
    cands = [(fromE, sig(fromE) + " g", f"Calculated from {E}. {E} is in excess, so this is more than the {L} can make."),
             (molP, sig(molP) + " g", f"That is the **moles** of {P}."),
             (gA + gB, sig(gA + gB) + " g", "Added the reactant masses. Part of the excess reactant is left over."),
             (mL * mm(P), sig(mL * mm(P)) + " g", f"Used {L} but assumed 1 : 1. The ratio is {cP} {P} : {cL} {L}."),
             (molP * mm(L), sig(molP * mm(L)) + " g", f"Used the molar mass of {L} instead of {P} in the last step.")]
    cands = [(v, t, re.sub(r"\b([A-Z][a-z]?\d[A-Za-z0-9()]*|[A-Z][a-z]?[A-Z][A-Za-z0-9()]*)\b", r"[[\1]]", w)) for v, t, w in cands]
    s = Steps()
    if balance:
        s.add("balance the equation", balance)
    s.add("molar masses", "; ".join(mm_text(f) for f in (A, B, P)) + ".")
    _, eA = to_mol(gA, A)
    _, eB = to_mol(gB, B)
    s.add("grams to moles for each reactant", eA, eB)
    _, e = ratio(mA, A, cA, B, cB)
    s.add(f"how much [[{B}]] does all the [[{A}]] need?",
          f"Have [[{A}]] (coefficient **{cA}**), want [[{B}]] (coefficient **{cB}**).", e.replace("$$ ", "$$").replace(
              f"\\ {U('mol ' + B)}$$", f"\\ {U('mol ' + B + ' needed')}$$"))
    if L == B:
        cmp = (f"You **need** {sig(needB, 4)} mol [[{B}]] but only **have** {sig(mB, 4)} mol. The [[{B}]] runs out first, "
               f"so **[[{B}]] is limiting** and [[{A}]] is in excess.")
    else:
        cmp = (f"You **have** {sig(mB, 4)} mol [[{B}]] and only **need** {sig(needB, 4)} mol. [[{B}]] is in excess, "
               f"so **[[{A}]] is limiting**.")
    s.add("compare", cmp)
    _, e1 = ratio(mL, L, cL, P, cP)
    _, e2 = to_g(molP, P, final=True, result=ans)
    s.add(f"theoretical yield from the limiting reactant ([[{L}]])",
          f"Have [[{L}]] (coefficient **{cL}**), want [[{P}]] (coefficient **{cP}**).", e1, e2)
    s.note(f"**Cross-check:** all the [[{E}]] would make {sig(fromE)} g [[{P}]]. The smaller amount, {ans} g, is the "
           "theoretical yield.")
    return dict(ch=9, kind="calc", numeric=True, title=title, short=short, stem=stem,
                correct=(float(ans), ans + " g", ""), wrong=pick(ans + " g", cands), cite=cite, hw=hw,
                covers="Moles of each reactant → limiting reactant → product from the limiting reactant only.",
                sol=str(s)), (L, gP)


def q_percent(title, short, stem, A, cA, gA, P, cP, actual, cite, hw, balance=None, excess_note=None):
    molA = gA / mm(A)
    molP = molA * cP / cA
    theo = molP * mm(P)
    pct = actual / theo * 100
    ans = sig(pct)
    cands = [(pct / 100, sig(pct / 100) + "%", "Forgot to multiply by 100."),
             (actual / gA * 100, sig(actual / gA * 100) + "%",
              f"Divided by the mass of {A}. The bottom must be the theoretical yield of {P}."),
             (theo / actual * 100, sig(theo / actual * 100) + "%", "Upside down: theoretical / actual. A yield can't be over 100%.")]
    if cA != cP:
        wrong_theo = molA * mm(P)
        cands.append((actual / wrong_theo * 100, sig(actual / wrong_theo * 100) + "%",
                      f"Theoretical yield found with a 1 : 1 ratio. The coefficients are {cA} ({A}) and {cP} ({P})."))
    cands.append((actual / (molP * mm(A)) * 100, sig(actual / (molP * mm(A)) * 100) + "%",
                  f"Theoretical yield used the molar mass of {A} instead of {P}."))
    cands.append((actual / mm(P) * 100, sig(actual / mm(P) * 100) + "%",
                  f"Divided the actual mass by the molar mass of {P} ({mm(P):.2f}) instead of by the theoretical yield."))
    cands = [(v, t, re.sub(r"\b([A-Z][a-z]?\d[A-Za-z0-9()]*|[A-Z][a-z]?[A-Z][A-Za-z0-9()]*)\b", r"[[\1]]", w)) for v, t, w in cands]
    s = Steps()
    if balance:
        s.add("balance the equation", balance)
    s.add("which reactant controls the yield?", excess_note or f"[[{A}]] is the only reactant, so it is limiting.")
    s.add("molar masses", mm_text(A) + "; " + mm_text(P) + ".")
    _, e0 = to_mol(gA, A)
    _, e1 = ratio(molA, A, cA, P, cP)
    _, e2 = to_g(molP, P, result=sig(theo, 4))
    s.add(f"theoretical yield of [[{P}]]",
          f"Have [[{A}]] (coefficient **{cA}**), want [[{P}]] (coefficient **{cP}**).", e0, e1,
          e2.replace("$$", "", 1).join(["$$", ""]).replace(U(f"g {P}") + "$$", U(f"g {P}") + r"\ (\text{theoretical})$$"))
    s.add("percent yield", f"The actual yield ({actual} g, measured) goes on top, the theoretical yield on the bottom:",
          "$$\\text{percent yield}=\\frac{" + f"{actual}" + r"\ \cancel{\text{g}}\ (\text{actual})}{" + sig(theo, 4)
          + r"\ \cancel{\text{g}}\ (\text{theoretical})}\times100\% = \boxed{" + ans + r"\%}$$")
    return dict(ch=9, kind="calc", numeric=True, title=title, short=short, stem=stem,
                correct=(float(ans), ans + "%", ""), wrong=pick(ans + "%", cands), cite=cite, hw=hw,
                covers="Two parts: theoretical yield from the limiting reactant, then actual / theoretical × 100.",
                sol=str(s)), pct


# ============================================================ 8.7 -> 9 bridge
def q_bridge(title, short, stem, els, pcts, molar, balance_text, M, cM, P, cP, given_mol, wrong, cite, hw):
    """Percent composition + molar mass -> molecular formula -> moles of P from moles of the compound.

    `wrong` is a list of (value, why) pairs; values are moles of P.
    """
    r, s = empirical_steps(els, pcts, "percent")
    em = mm(r["formula"])
    n = round(molar / em)
    assert abs(molar / em - n) < 0.02
    mol_f = fstr(els, [k * n for k in r["subs"]])
    assert mol_f == M, (mol_f, M)
    s.add("molecular formula",
          "Empirical formula mass: " + mm_text(r["formula"]) + ". "
          f"n = {molar} ÷ {em:.2f} = {molar / em:.2f} ≈ {n}, so multiply every subscript by {n}: **[[{M}]]**.")
    s.add("write the balanced equation", balance_text)
    res = given_mol * cP / cM
    ans = sig(res)
    _, e = ratio(given_mol, M, cM, P, cP, final=True, result=ans)
    s.add(f"moles [[{M}]] to moles [[{P}]]",
          f"Have [[{M}]] (coefficient **{cM}**), want [[{P}]] (coefficient **{cP}**).", e)
    s.note("The molecular formula matters here. A mole of the **empirical** unit is a different amount of substance "
           "from a mole of the real molecule, so it would give a different number of moles of product.")
    cands = [(v, sig(v) + " mol", re.sub(r"\b([A-Z][a-z]?\d[A-Za-z0-9()]*|[A-Z][a-z]?[A-Z][A-Za-z0-9()]*)\b", r"[[\1]]", w))
             for v, w in wrong]
    return dict(ch=9, kind="calc", numeric=True, title=title, short=short, stem=stem,
                correct=(float(ans), ans + " mol", ""), wrong=pick(ans + " mol", cands), cite=cite, hw=hw,
                covers="Section 8.7 feeding Chapter 9: percent composition → empirical → molecular formula → balanced "
                       "equation → mole ratio.",
                sol=str(s)), res


def q_limit(title, short, stem, A, cA, gA, B, cB, gB, cite, hw):
    """Which reactant is limiting, and how much of the other is left over (text choices)."""
    mA, mB = gA / mm(A), gB / mm(B)
    needB = mA * cB / cA
    if needB > mB:
        L, cL, mL, gL, E, cE, mE, gE = B, cB, mB, gB, A, cA, mA, gA
    else:
        L, cL, mL, gL, E, cE, mE, gE = A, cA, mA, gA, B, cB, mB, gB
    usedE = mL * cE / cL
    used_g, left_g = usedE * mm(E), gE - usedE * mm(E)
    assert left_g > 0.05 * gE
    correct = T(f"[[{L}]] is limiting, and {sig(left_g)} g of [[{E}]] is left over")
    wrong = [T(f"[[{E}]] is limiting, and [[{L}]] is left over",
               f"Check what all of one reactant needs. The need-vs-have comparison shows the [[{L}]] runs out first."),
             T(f"[[{L}]] is limiting, and {sig(gE)} g of [[{E}]] is left over",
               f"That is **all** of the [[{E}]]. Some of it reacts with the [[{L}]], so less is left."),
             T(f"[[{L}]] is limiting, and {sig(used_g)} g of [[{E}]] is left over",
               f"That is the mass of [[{E}]] that **reacts**. Left over = {sig(gE)} g − {sig(used_g)} g."),
             T("Neither is limiting; both reactants are used up completely",
               f"That needs the moles to be in exactly a {cA} : {cB} ratio, and they aren't.")]
    s = Steps()
    s.add("molar masses", mm_text(A) + "; " + mm_text(B) + ".")
    _, eA = to_mol(gA, A)
    _, eB = to_mol(gB, B)
    s.add("grams to moles for each reactant", eA, eB)
    _, e = ratio(mA, A, cA, B, cB)
    s.add(f"how much [[{B}]] does all the [[{A}]] need?",
          f"Have [[{A}]] (coefficient **{cA}**), want [[{B}]] (coefficient **{cB}**).", e)
    if L == B:
        cmp = (f"You **need** {sig(needB, 4)} mol [[{B}]] but only **have** {sig(mB, 4)} mol, so **[[{B}]] is limiting** "
               f"and [[{A}]] is in excess.")
    else:
        cmp = (f"You **have** {sig(mB, 4)} mol [[{B}]] and only **need** {sig(needB, 4)} mol, so [[{B}]] is in excess "
               f"and **[[{A}]] is limiting**.")
    s.add("compare", cmp)
    _, e1 = ratio(mL, L, cL, E, cE)
    _, e2 = to_g(usedE, E)
    s.add(f"how much [[{E}]] reacts?", f"All {sig(mL, 4)} mol of the limiting [[{L}]] reacts. "
          f"Have [[{L}]] (coefficient **{cL}**), want [[{E}]] (coefficient **{cE}**).", e1, e2)
    s.add("left over", f"{sig(gE)} g [[{E}]] at the start − {sig(used_g)} g that reacts = **{sig(left_g)} g left over**.")
    s.note("Mass alone never decides the limiting reactant: compare in moles, through the mole ratio.")
    return dict(ch=9, kind="calc", title=title, short=short, stem=stem, correct=correct, wrong=wrong, cite=cite, hw=hw,
                covers="Limiting reactant by need-vs-have in moles, then the leftover mass of the excess reactant.",
                sol=str(s)), (L, left_g)
