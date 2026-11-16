"""Solubility-rule engine and question generators for the Chapter 7 solubility drillers.

Every soluble/insoluble call comes from the six rules of Ch 7 slide 11 (Table 7.1), applied in the
course's priority order: rules 1 and 2 (nitrate; Na+, K+, NH4+) beat everything else. Ion pairs that
the course rules don't settle cleanly, or where the table disagrees with real chemistry, are excluded
(EXCLUDED) and the generators refuse to use them, so no question depends on them.
"""
import itertools
import math

C7 = "Chapter 7 post"


def T(text, why=""):
    return (None, text, why)


# ------------------------------------------------------------ ions
# key: (formula piece, charge, name, polyatomic?)
CAT = {
    "Na": ("Na", 1, "sodium", False), "K": ("K", 1, "potassium", False), "NH4": ("NH4", 1, "ammonium", True),
    "Ag": ("Ag", 1, "silver", False), "Pb": ("Pb", 2, "lead(II)", False), "Hg2": ("Hg2", 2, "mercury(I)", False),
    "Ba": ("Ba", 2, "barium", False), "Ca": ("Ca", 2, "calcium", False), "Mg": ("Mg", 2, "magnesium", False),
    "Zn": ("Zn", 2, "zinc", False), "Cu": ("Cu", 2, "copper(II)", False), "Fe2": ("Fe", 2, "iron(II)", False),
    "Fe3": ("Fe", 3, "iron(III)", False), "Ni": ("Ni", 2, "nickel(II)", False), "Co": ("Co", 2, "cobalt(II)", False),
    "Al": ("Al", 3, "aluminum", False), "Mn": ("Mn", 2, "manganese(II)", False), "Cr": ("Cr", 3, "chromium(III)", False),
}
AN = {
    "NO3": ("NO3", 1, "nitrate", True), "Cl": ("Cl", 1, "chloride", False), "SO4": ("SO4", 2, "sulfate", True),
    "OH": ("OH", 1, "hydroxide", True), "S": ("S", 2, "sulfide", False), "CO3": ("CO3", 2, "carbonate", True),
    "PO4": ("PO4", 3, "phosphate", True),
}
RULE2 = ("Na", "K", "NH4")
CL_EXC = ("Ag", "Pb", "Hg2")
SO4_EXC = ("Ba", "Pb", "Ca")

# Pairs not settled cleanly by Table 7.1 (moderately soluble, or the table and real chemistry disagree).
EXCLUDED = {("Ba", "OH"), ("Ca", "OH"), ("NH4", "OH"), ("Ag", "SO4"), ("Hg2", "SO4"), ("Ag", "OH"), ("Hg2", "OH"),
            ("Hg2", "S"), ("Hg2", "CO3"), ("Hg2", "PO4"), ("Ba", "S"), ("Ca", "S"), ("Mg", "S"),
            ("Al", "S"), ("Al", "CO3"), ("Fe3", "S"), ("Fe3", "CO3"), ("Cr", "S"), ("Cr", "CO3")}

RULES = {
    1: "Rule 1: most nitrate ([[NO3^-^]]) salts are soluble",
    2: "Rule 2: most salts of Na^+^, K^+^, and [[NH4^+^]] are soluble",
    3: "Rule 3: most chlorides are soluble, except AgCl, [[PbCl2]], and [[Hg2Cl2]]",
    4: "Rule 4: most sulfates are soluble, except [[BaSO4]], [[PbSO4]], and [[CaSO4]]",
    5: "Rule 5: most hydroxides are only slightly soluble (NaOH and KOH are the exceptions)",
    6: "Rule 6: most sulfides, carbonates, and phosphates are only slightly soluble",
}
RULE_TOPIC = {1: "NO3", 2: None, 3: "Cl", 4: "SO4", 5: "OH", 6: ("S", "CO3", "PO4")}


def ok(c, a):
    assert (c, a) not in EXCLUDED, f"{c}+{a} is excluded (not settled by the course rules)"
    return True


def counts(c, a):
    qc, qa = CAT[c][1], AN[a][1]
    l = qc * qa // math.gcd(qc, qa)
    return l // qc, l // qa


def F(c, a):
    """Plain formula: Ca3(PO4)2, Hg2Cl2, (NH4)2S."""
    nc, na = counts(c, a)
    cs, _, _, cp = CAT[c]
    as_, _, _, ap = AN[a]
    left = (f"({cs}){nc}" if cp else f"{cs}{nc}") if nc > 1 else cs
    right = (f"({as_}){na}" if ap else f"{as_}{na}") if na > 1 else as_
    return left + right


def name(c, a):
    return f"{CAT[c][2]} {AN[a][2]}"


def ion(x, n=1):
    """Ion markup, optionally with a coefficient: 3 OH^-^ -> '3[[OH^-^]]'."""
    if x in CAT:
        s, q = CAT[x][0], CAT[x][1]
    else:
        s, q = AN[x][0], -AN[x][1]
    charge = ("" if abs(q) == 1 else str(abs(q))) + ("+" if q > 0 else "-")
    return (str(n) if n > 1 else "") + f"[[{s}^{charge}^]]"


def soluble(c, a):
    ok(c, a)
    if a == "NO3" or c in RULE2:
        return True
    if a == "Cl":
        return c not in CL_EXC
    if a == "SO4":
        return c not in SO4_EXC
    return False                              # OH (rule 5), S / CO3 / PO4 (rule 6)


def rule_of(c, a):
    """The single rule that decides (c, a). Asserts that only one rule applies."""
    ok(c, a)
    if a == "NO3":
        assert c not in RULE2, "nitrate + rule-2 cation: two rules apply"
        return 1
    if c in RULE2:
        assert a not in ("Cl", "SO4"), "rule-2 cation + chloride/sulfate: two rules apply"
        return 2
    return {"Cl": 3, "SO4": 4, "OH": 5, "S": 6, "CO3": 6, "PO4": 6}[a]


def why(c, a):
    """One-sentence explanation of the solubility call, citing the deciding rule."""
    f = f"[[{F(c, a)}]]"
    if a == "NO3":
        return f"{f}: it's a nitrate, so it is **soluble** (rule 1)."
    if c in RULE2:
        extra = {"OH": " Rule 2 beats rule 5.", "S": " Rule 2 beats rule 6.", "CO3": " Rule 2 beats rule 6.",
                 "PO4": " Rule 2 beats rule 6."}.get(a, "")
        return f"{f}: it contains {ion(c)}, so it is **soluble** (rule 2).{extra}"
    if a == "Cl":
        if c in CL_EXC:
            return f"{f}: chlorides are soluble **except** AgCl, PbCl~2~, Hg~2~Cl~2~, and this is one of them, so it is **insoluble** (rule 3)."
        return f"{f}: most chlorides are soluble and {ion(c)} isn't an exception (Ag, Pb, Hg~2~), so it is **soluble** (rule 3)."
    if a == "SO4":
        if c in SO4_EXC:
            return f"{f}: sulfates are soluble **except** BaSO~4~, PbSO~4~, CaSO~4~, and this is one of them, so it is **insoluble** (rule 4)."
        return f"{f}: most sulfates are soluble and {ion(c)} isn't an exception (Ba, Pb, Ca), so it is **soluble** (rule 4)."
    if a == "OH":
        return f"{f}: most hydroxides are only slightly soluble and only NaOH and KOH are exceptions, so it is **insoluble** (rule 5)."
    return (f"{f}: most {AN[a][2]}s are only slightly soluble and {ion(c)} isn't Na^+^, K^+^, or NH~4~^+^, "
            "so it is **insoluble** (rule 6).")


TIERS = ("**How to decide (study guide 7.3):** check rules 1 and 2 first (nitrate? Na^+^, K^+^, NH~4~^+^? then soluble, "
         "no matter what the other ion is). Then chloride → rule 3, sulfate → rule 4, hydroxide → rule 5, "
         "sulfide/carbonate/phosphate → rule 6.")


# ------------------------------------------------------------ classification questions
def q_pick(title, short, stem, items, want_soluble, cite, hw, use_names=False):
    """'Which compound is (in)soluble?' — exactly one of the five items matches."""
    match = [it for it in items if soluble(*it) == want_soluble]
    assert len(match) == 1, (title, [F(*m) for m in match])
    disp = (lambda it: name(*it)) if use_names else (lambda it: f"[[{F(*it)}]]")
    correct = T(disp(match[0]))
    wrong = [T(disp(it), why(*it)) for it in items if it != match[0]]
    lines = "\n".join(f"* {why(*it)}" for it in items)
    sol = TIERS + "\n\n" + (("Names to formulas: " + "; ".join(f"{name(*it)} = [[{F(*it)}]]" for it in items) + ".\n\n")
                            if use_names else "") + lines
    return dict(ch=7, kind="concept", title=title, short=short, stem=stem, correct=correct, wrong=wrong,
                cite=cite, hw=hw, covers="Applying Table 7.1, including the rule-1/rule-2 priority and the named exceptions.",
                sol=sol)


def q_rule(title, short, c, a, cite, hw, others):
    """'Which rule explains why X is (in)soluble?' (HW14 style). `others` = 4 distractor rule numbers."""
    r = rule_of(c, a)
    sol_word = "soluble" if soluble(c, a) else "insoluble"
    f = f"[[{F(c, a)}]]"
    wrong = []
    for k in others:
        assert k != r
        topic = RULE_TOPIC[k]
        if k == 2:
            w = f"{f} contains no Na^+^, K^+^, or NH~4~^+^."
        elif isinstance(topic, tuple) and a in topic or topic == a:
            w = f"Rule {k} covers the {AN[a][2]} ion, but rule {r} takes priority and decides it."
        else:
            names_ = {"NO3": "nitrate", "Cl": "chloride", "SO4": "sulfate", "OH": "hydroxide"}
            w = (f"{f} has no {names_[topic]} ion." if isinstance(topic, str)
                 else f"{f} has no sulfide, carbonate, or phosphate ion.")
        wrong.append(T(RULES[k], w))
    return dict(ch=7, kind="concept", title=title, short=short,
                stem=f"Which solubility rule explains why {f} is **{sol_word}** in water?",
                correct=T(RULES[r]), wrong=wrong, cite=cite, hw=hw,
                covers="Naming the rule that decides a compound, including when rule 2 overrides the anion's rule.",
                sol=TIERS + "\n\n" + why(c, a))


def q_count(title, short, items, cite, hw, choices=(1, 2, 3, 4, 5)):
    n = sum(soluble(*it) for it in items)
    assert n in choices
    wrong = [(k, str(k), f"Recount: exactly {n} of the five are soluble.") for k in choices if k != n]
    lst = ", ".join(f"[[{F(*it)}]]" for it in items)
    return dict(ch=7, kind="concept", numeric=True, title=title, short=short,
                stem=f"How many of the following compounds are **soluble** in water? {lst}",
                correct=(n, str(n), ""), wrong=wrong, cite=cite, hw=hw,
                covers="Fast classification with Table 7.1.",
                sol=TIERS + "\n\n" + "\n".join(f"* {why(*it)}" for it in items) + f"\n\nSoluble count: **{n}**."), n


# ------------------------------------------------------------ mixing two solutions
def mix(s1, s2):
    """s1=(c1,a1), s2=(c2,a2), both soluble. Returns products, precipitates, balanced molecular coefficients."""
    (c1, a1), (c2, a2) = s1, s2
    assert soluble(*s1) and soluble(*s2), "reactants must be soluble"
    p1, p2 = (c1, a2), (c2, a1)
    ppt = [p for p in (p1, p2) if not soluble(*p)]
    # balance x s1 + y s2 -> z p1 + w p2 by brute force
    for x, y, z, w in itertools.product(range(1, 7), repeat=4):
        n1, n2, q1, q2 = counts(*s1), counts(*s2), counts(*p1), counts(*p2)
        if (x * n1[0] == z * q1[0] and x * n1[1] == w * q2[1] and y * n2[0] == w * q2[0] and y * n2[1] == z * q1[1]):
            return dict(p1=p1, p2=p2, ppt=ppt, coef=(x, y, z, w))
    raise ValueError("cannot balance")


def co(n, s):
    return (f"{n}" if n > 1 else "") + s


def molecular(s1, s2, m):
    x, y, z, w = m["coef"]
    st = lambda p: "(s)" if p in m["ppt"] else "(aq)"
    return (co(x, f"[[{F(*s1)}]](aq)") + " + " + co(y, f"[[{F(*s2)}]](aq)") + " → "
            + co(z, f"[[{F(*m['p1'])}]]{st(m['p1'])}") + " + " + co(w, f"[[{F(*m['p2'])}]]{st(m['p2'])}"))


def net_ionic(p):
    nc, na = counts(*p)
    return f"{ion(p[0], nc)}(aq) + {ion(p[1], na)}(aq) → [[{F(*p)}]](s)"


def complete_ionic(s1, s2, m):
    x, y, z, w = m["coef"]

    def ions(sp, k, state="(aq)"):
        nc, na = counts(*sp)
        return f"{ion(sp[0], k * nc)}{state} + {ion(sp[1], k * na)}{state}"
    right = []
    for p, k in ((m["p1"], z), (m["p2"], w)):
        right.append(co(k, f"[[{F(*p)}]](s)") if p in m["ppt"] else ions(p, k))
    return ions(s1, x) + " + " + ions(s2, y) + " → " + " + ".join(right)


def mix_solution(s1, s2, m):
    (c1, a1), (c2, a2) = s1, s2
    lines = [f"**Step 1: write the reactants as ions** (slide 14). [[{F(*s1)}]] gives {ion(c1)} and {ion(a1)}; "
             f"[[{F(*s2)}]] gives {ion(c2)} and {ion(a2)}.",
             f"**Step 2: exchange the anions** to find the possible solids: [[{F(*m['p1'])}]] and [[{F(*m['p2'])}]]. "
             "(Write each formula from the ion charges so it is neutral.)",
             "**Step 3: apply the solubility rules to each.**\n\n" + f"* {why(*m['p1'])}\n* {why(*m['p2'])}"]
    if m["ppt"]:
        lines.append("**Molecular equation:** " + molecular(s1, s2, m))
    else:
        lines.append("Neither product is insoluble, so **no precipitate forms (NR)**.")
    return "\n\n".join(lines)


def q_mix(title, short, s1, s2, cite, hw, wrong_formula, by_name=True):
    """'Which precipitate forms?' `wrong_formula` = (text, why) for a mis-written formula of the precipitate."""
    m = mix(s1, s2)
    assert len(m["ppt"]) == 1, (title, m["ppt"])
    p = m["ppt"][0]
    other = m["p2"] if p == m["p1"] else m["p1"]
    stem_items = (f"{name(*s1)} and {name(*s2)}" if by_name else f"[[{F(*s1)}]] and [[{F(*s2)}]]")
    wrong = [T(f"[[{F(*other)}]]", why(*other) + " It stays dissolved as spectator ions."),
             T(wrong_formula[0], wrong_formula[1]),
             T("No precipitate forms", f"[[{F(*p)}]] is insoluble, so it precipitates."),
             T(f"Both [[{F(*m['p1'])}]] and [[{F(*m['p2'])}]]", why(*other))]
    return dict(ch=7, kind="concept", title=title, short=short,
                stem=f"Aqueous solutions of {stem_items} are mixed. What precipitate forms?",
                correct=T(f"[[{F(*p)}]]"), wrong=wrong, cite=cite, hw=hw,
                covers="Slide 14's three steps: ions → swap anions → solubility rules; writing the solid's formula from charges.",
                sol=mix_solution(s1, s2, m))


def q_pair(title, short, pairs, want_ppt, cite, hw):
    """'Which pair forms a precipitate?' / 'Which pair gives no precipitate?' over five pairs."""
    res = [(s1, s2, mix(s1, s2)) for s1, s2 in pairs]
    match = [r for r in res if bool(r[2]["ppt"]) == want_ppt]
    assert len(match) == 1, (title, len(match))
    disp = lambda s1, s2: f"[[{F(*s1)}]] and [[{F(*s2)}]]"

    def w(s1, s2, m):
        if m["ppt"]:
            return f"Forms {', '.join(f'[[{F(*p)}]]' for p in m['ppt'])}. " + " ".join(why(*p) for p in m["ppt"])
        return f"Swapping gives [[{F(*m['p1'])}]] and [[{F(*m['p2'])}]], both soluble, so NR."
    s1, s2, m = match[0]
    wrong = [T(disp(a, b), w(a, b, mm_)) for a, b, mm_ in res if (a, b) != (s1, s2)]
    stem = ("Which pair of aqueous solutions forms a **precipitate** when mixed?" if want_ppt else
            "Which pair of aqueous solutions does **not** form a precipitate when mixed?")
    sol = ("For each pair, swap the anions and check both products (slide 14).\n\n"
           + "\n".join(f"* {disp(a, b)}: products [[{F(*mm_['p1'])}]] and [[{F(*mm_['p2'])}]]. "
                       + (f"**Precipitate: {', '.join(f'[[{F(*p)}]]' for p in mm_['ppt'])}.**" if mm_["ppt"] else "**Both soluble: NR.**")
                       for a, b, mm_ in res))
    return dict(ch=7, kind="concept", title=title, short=short, stem=stem, correct=T(disp(s1, s2)), wrong=wrong,
                cite=cite, hw=hw, covers="Predicting precipitation vs no reaction (NR) for several mixtures.", sol=sol)


def q_net(title, short, s1, s2, cite, hw, by_name=True):
    m = mix(s1, s2)
    assert len(m["ppt"]) == 1
    p = m["ppt"][0]
    other = m["p2"] if p == m["p1"] else m["p1"]
    nc, na = counts(*p)
    wrong = [T(complete_ionic(s1, s2, m), "That is the **complete** ionic equation. It still contains the spectator ions."),
             T(f"{ion(other[0])}(aq) + {ion(other[1])}(aq) → [[{F(*other)}]](s)",
               why(*other) + " Those ions are spectators, so they don't form a solid."),
             T("No reaction occurs (NR)", f"[[{F(*p)}]] is insoluble, so a precipitate forms.")]
    if nc > 1 or na > 1:
        wrong.append(T(f"{ion(p[0])}(aq) + {ion(p[1])}(aq) → [[{F(*p)}]](s)",
                       "Not balanced: the atoms and charges on the left don't match the solid's formula."))
    else:
        wrong.append(T(f"{ion(p[0])}(aq) + {ion(p[1])}(aq) → [[{F(*p)}]](aq)",
                       "The product is a precipitate, so its state is (s), not (aq)."))
    stem_items = (f"{name(*s1)} and {name(*s2)}" if by_name else f"[[{F(*s1)}]] and [[{F(*s2)}]]")
    spect = [x for x in (s1[0], s1[1], s2[0], s2[1]) if x not in p]
    sol = (mix_solution(s1, s2, m) + "\n\n**Complete ionic equation** (strong electrolytes as ions, slide 16): "
           + complete_ionic(s1, s2, m) + "\n\n"
           + f"**Cancel the spectator ions** ({' and '.join(ion(x) for x in spect)}): they appear unchanged on both sides.\n\n"
           + f"**Net ionic equation:** **{net_ionic(p)}**. Check: atoms and charge balance, smallest whole numbers, states shown.")
    return dict(ch=7, kind="concept", title=title, short=short,
                stem=f"Aqueous solutions of {stem_items} are mixed. What is the **net ionic** equation?",
                correct=T(net_ionic(p)), wrong=wrong, cite=cite, hw=hw,
                covers="Molecular → complete ionic → net ionic: keep only the ions that form the solid.", sol=sol)


def q_spect(title, short, s1, s2, cite, hw, by_name=True):
    m = mix(s1, s2)
    assert len(m["ppt"]) == 1
    p = m["ppt"][0]
    ions_all = [s1[0], s1[1], s2[0], s2[1]]
    spect = [x for x in ions_all if x not in p]
    react = [x for x in ions_all if x in p]
    j = lambda xs: " and ".join(ion(x) for x in xs)
    wrong = [T(j(react), "Those ions form the precipitate, so they **do** take part."),
             T(j([spect[0], react[1]]), f"{ion(react[1])} ends up in the solid, so it isn't a spectator."),
             T(", ".join(ion(x) for x in ions_all), "Not all four: the ions in the precipitate change."),
             T("There are no spectator ions in this reaction", f"{j(spect)} stay dissolved and unchanged.")]
    stem_items = (f"{name(*s1)} and {name(*s2)}" if by_name else f"[[{F(*s1)}]] and [[{F(*s2)}]]")
    return dict(ch=7, kind="concept", title=title, short=short,
                stem=f"Aqueous solutions of {stem_items} are mixed and a precipitate forms. Which ions are **spectator ions**?",
                correct=T(j(spect)), wrong=wrong, cite=cite, hw=hw,
                covers="Spectator ions (slide 17): ions that appear unchanged on both sides.",
                sol=mix_solution(s1, s2, m) + f"\n\nThe solid uses {j(react)}. The remaining ions, **{j(spect)}**, stay in "
                    "solution unchanged, so they are the spectator ions and are left out of the net ionic equation.")


def q_select(title, short, target, other, reagents, cite, hw):
    """A solution holds two cations (as nitrates). Which reagent precipitates only `target`?"""
    def effect(rg):
        rc, ra = rg
        t, o = not soluble(target, ra), not soluble(other, ra)
        return t, o
    good = [rg for rg in reagents if effect(rg) == (True, False)]
    assert len(good) == 1, (title, good)

    def w(rg):
        t, o = effect(rg)
        ra = rg[1]
        if t and o:
            return f"Precipitates **both**: {why(target, ra)} {why(other, ra)}"
        if not t and not o:
            return f"Precipitates **neither**: {why(target, ra)} {why(other, ra)}"
        return f"Precipitates only the wrong ion: {why(other, ra)}"
    disp = lambda rg: f"[[{F(*rg)}]](aq)"
    sol = (f"You want a solid with {ion(target)} but not with {ion(other)}. The reagent's own cation is Na^+^/K^+^ "
           "(rule 2), so it never precipitates; only the reagent's **anion** matters. Check it with each metal ion:\n\n"
           + "\n".join(f"* {disp(rg)}: " + w(rg) if rg != good[0] else
                       f"* {disp(rg)}: {why(target, rg[1])} {why(other, rg[1])} **Only {ion(target)} precipitates.**"
                       for rg in reagents))
    return dict(ch=7, kind="concept", title=title, short=short,
                stem=f"A solution contains both {ion(target)} and {ion(other)} ions (as nitrates). Adding which solution "
                     f"precipitates **only** the {ion(target)}?",
                correct=T(disp(good[0])), wrong=[T(disp(rg), w(rg)) for rg in reagents if rg != good[0]],
                cite=cite, hw=hw, covers="Using the exception lists to choose a reagent that separates two ions.",
                sol=sol)


def q_mol(title, short, s1, s2, cite, hw, by_name=True):
    """Balanced molecular equation for a precipitation (HW15 style)."""
    m = mix(s1, s2)
    assert len(m["ppt"]) == 1
    x, y, z, w = m["coef"]
    p = m["ppt"][0]
    other = m["p2"] if p == m["p1"] else m["p1"]
    st = lambda q, solid: "(s)" if q == solid else "(aq)"

    def eq(cx, cy, cz, cw, solid=p, f1=None, f2=None):
        return (co(cx, f"[[{F(*s1)}]](aq)") + " + " + co(cy, f"[[{F(*s2)}]](aq)") + " → "
                + co(cz, f"[[{f1 or F(*m['p1'])}]]{st(m['p1'], solid)}") + " + "
                + co(cw, f"[[{f2 or F(*m['p2'])}]]{st(m['p2'], solid)}"))
    correct = T(eq(x, y, z, w))
    wrong = [T(eq(x, y, z, w, solid=other), why(*other) + " " + why(*p))]
    if max(x, y, z, w) > 1:
        wrong.append(T(eq(1, 1, 1, 1), "Not balanced: count each ion on both sides."))
    naive = lambda q: CAT[q[0]][0] + AN[q[1]][0]
    if naive(p) != F(*p):
        wrong.append(T(eq(1, 1, 1, 1, f1=naive(m["p1"]), f2=naive(m["p2"])),
                       "Formulas written by just joining the ions. Each formula must use the charges so it is neutral."))
    wrong.append(T("No reaction (NR)", f"[[{F(*p)}]] is insoluble, so a precipitate forms."))
    wrong.append(T(eq(x, y, z, w, solid=None), f"[[{F(*p)}]] is insoluble, so it must be labeled (s)."))
    from drillib import pick
    stem_items = (f"{name(*s1)} and {name(*s2)}" if by_name else f"[[{F(*s1)}]] and [[{F(*s2)}]]")
    sol = (mix_solution(s1, s2, m) + "\n\n**Balance:** "
           + f"the coefficients {x}, {y}, {z}, {w} make every ion count match on both sides (count each ion separately). "
           "Only the insoluble product gets (s); everything else is (aq).")
    return dict(ch=7, kind="concept", title=title, short=short,
                stem=f"Which is the balanced **molecular** equation for mixing aqueous {stem_items}?",
                correct=correct, wrong=pick(correct[1], wrong), cite=cite, hw=hw,
                covers="Writing and balancing the molecular equation for a precipitation, with correct states.", sol=sol)
