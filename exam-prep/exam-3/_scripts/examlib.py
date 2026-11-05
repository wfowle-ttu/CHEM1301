"""Shared helpers for building CHEM1301 Exam 3 practice exams and keys.

A practice exam is a list of question dicts. Each build script calls
`build(n, questions, seed)`, which places the answer choices, writes
practice-exam-3-n.qmd and practice-exam-3-n-key.qmd next to this folder, and
asserts that every computed answer matches the keyed choice.

Chemical formulas are written inside [[ ]] and converted to Quarto
sub/superscripts: [[Ca3(PO4)2]] -> Ca~3~(PO~4~)~2~, [[SO4^2-^]] -> SO~4~^2−^.
"""
import random
import re
from collections import Counter
from pathlib import Path

LETTERS = "abcde"
OUT = Path(__file__).resolve().parent.parent

# Average atomic masses as used on the course slides (Ch 8 slide 5, slide 9) / periodic table.
AM = {
    "H": 1.008, "C": 12.01, "N": 14.01, "O": 16.00, "F": 19.00, "Na": 22.99,
    "Mg": 24.31, "Al": 26.98, "Si": 28.09, "P": 30.97, "S": 32.07, "Cl": 35.45,
    "K": 39.10, "Ca": 40.08, "Fe": 55.85, "Cu": 63.55, "Br": 79.90, "Ag": 107.87,
    "Ba": 137.33, "Au": 196.97, "Pb": 207.2, "B": 10.81, "Zn": 65.38, "I": 126.90,
    "Li": 6.94, "Mn": 54.94, "Ni": 58.69, "Cr": 52.00, "Xe": 131.29, "Ge": 72.63,
    "Sr": 87.62, "Hg": 200.59, "Co": 58.93, "Ne": 20.18, "U": 238.03,
}
NA = 6.022e23


def mm(formula):
    """Molar mass of a formula like 'Al2(SO4)3' or 'C2H5OH'."""
    def parse(s, i=0):
        total = 0.0
        while i < len(s):
            if s[i] == "(":
                sub, i = parse(s, i + 1)
                m = re.match(r"\d*", s[i:]).group()
                i += len(m)
                total += sub * (int(m) if m else 1)
            elif s[i] == ")":
                return total, i + 1
            else:
                m = re.match(r"([A-Z][a-z]?)(\d*)", s[i:])
                total += AM[m.group(1)] * (int(m.group(2)) if m.group(2) else 1)
                i += len(m.group())
        return total, i
    return parse(formula)[0]


SYMBOLS = {"→": r"$\rightarrow$", "⇔": r"$\Leftrightarrow$", "≈": r"$\approx$"}


def chem(text):
    """Convert [[formula]] markers to Quarto subscript/superscript markup and
    swap arrow symbols the PDF font lacks for LaTeX math."""
    for k, v in SYMBOLS.items():
        text = text.replace(k, v)
    def conv(m):
        parts = re.split(r"(\^[^^]*\^)", m.group(1))
        out = []
        for p in parts:
            if p.startswith("^"):
                out.append(p.replace("-", "−"))
            else:
                out.append(re.sub(r"(?<=[A-Za-z\)])(\d+)", r"~\1~", p))
        return "".join(out)
    return re.sub(r"\[\[(.+?)\]\]", conv, text)


def sci(x, sig=3):
    """Format x as 'a.bc × 10^n^' (Quarto superscript) for exam display."""
    s = f"{x:.{sig - 1}e}"
    mant, exp = s.split("e")
    exp = int(exp)
    if exp == 0:
        return mant
    return f"{mant} × 10^{str(exp).replace('-', '−')}^"


def check(num, computed, shown, tol):
    ok = abs(computed - shown) <= tol
    print(f"{'OK ' if ok else 'FAIL'} Q{num:>2}: computed {computed:.6g} vs keyed {shown}")
    assert ok, f"Q{num}: computed {computed} does not match keyed {shown}"


def place(questions, seed):
    """Order choices. Numeric questions are sorted by value; text questions are
    shuffled, steering the correct answer toward under-used letters so the key
    is spread evenly across a–e."""
    rng = random.Random(seed)
    counts = Counter()
    for q in questions:
        if q.get("numeric"):
            q["choices"] = sorted([q["correct"]] + q["wrong"], key=lambda c: c[0])
            q["ans"] = LETTERS[q["choices"].index(q["correct"])]
            counts[q["ans"]] += 1
    for q in questions:
        if q.get("numeric"):
            continue
        low = min(counts[L] for L in LETTERS)
        target = rng.choice([L for L in LETTERS if counts[L] == low])
        wrong = q["wrong"][:]
        rng.shuffle(wrong)
        idx = LETTERS.index(target)
        q["choices"] = wrong[:idx] + [q["correct"]] + wrong[idx:]
        q["ans"] = target
        counts[target] += 1
    for q in questions:
        assert len(q["choices"]) == 5, q["title"]
        texts = [c[1] for c in q["choices"]]
        assert len(set(texts)) == 5, f"duplicate choices in {q['title']}"
    print("Answer distribution:", dict(sorted(counts.items())))


EXAM_HEADER = """---
title: "CHEM 1301 Practice Exam 3-{n}"
subtitle: "Chapters 7, 8, and 9 — {count} multiple-choice questions"
format:
  pdf:
    geometry: margin=0.8in
    fontsize: 11pt
    include-in-header:
      text: |
        \\usepackage{{needspace}}
        \\usepackage{{array}}
---

**Instructions.** Choose the single best answer (a–e) for each question. You may use a periodic table.
Solubility rules are **not** provided. Calculators are allowed. Answers are rounded to the precision shown.
Time yourself: aim to finish in 75 minutes or less.

"""

KEY_HEADER = """---
title: "CHEM 1301 Practice Exam 3-{n} — Answer Key"
subtitle: "Worked solutions with course-material citations"
format:
  pdf:
    geometry: margin=0.75in
    fontsize: 11pt
---

Every numeric answer was recomputed by `_scripts/build_exam_3_{n}.py`, which builds this key and the exam
from the same data. Atomic masses are periodic-table values (H 1.008, C 12.01, N 14.01, O 16.00, ...),
matching Ch 8 slides 5, 9, and 22. Citations name the slide (same number in the `.pdf` and `.pptx`) where the
content is taught, plus the homework screenshot with the closest problem.

**Score bands.** 32–35 exam-ready · 27–31 review the missed topics · 26 or below rework the study guide sections cited.

"""


def build(n, questions, seed):
    place(questions, seed)
    exam = [EXAM_HEADER.format(n=n, count=len(questions))]
    for i, q in enumerate(questions, 1):
        exam.append("```{=latex}\n\\needspace{9\\baselineskip}\n```\n")
        exam.append(f"**{i}.** {chem(q['stem'])}\n\n")
        lines = [f"{L})\\ {chem(c[1])}" for L, c in zip(LETTERS, q["choices"])]
        exam.append("```{=latex}\n\\begingroup\\leftskip=1.5em\n```\n")
        exam.append("\\\n".join(lines) + "\n\n")
        exam.append("```{=latex}\n\\par\\endgroup\\medskip\n```\n\n")
    # Answer sheet
    exam.append("```{=latex}\n\\newpage\n```\n\n## Answer Sheet\n\n")
    exam.append("Circle one letter per question.\n\n")
    half = (len(questions) + 1) // 2
    exam.append("| Q | Answer | | Q | Answer |\n|:-:|:-:|:-:|:-:|:-:|\n")
    for r in range(half):
        bubbles = " $\\quad$ ".join("abcde")
        left = f"{r + 1} | {bubbles}"
        j = r + 1 + half
        right = f"{j} | {bubbles}" if j <= len(questions) else " | "
        exam.append(f"| {left} | | {right} |\n")
    (OUT / f"practice-exam-3-{n}.qmd").write_text("".join(exam), encoding="utf-8")

    key = [KEY_HEADER.format(n=n)]
    key.append("| Q | Ans | Answer | Type | Topic (source) |\n|:-:|:-:|:----------------|:----:|:------------------------|\n")
    for i, q in enumerate(questions, 1):
        ans_text = q["choices"][LETTERS.index(q["ans"])][1]
        key.append(f"| {i} | **{q['ans']}** | {chem(ans_text)} | {q['kind']} | {chem(q['title'])} ({q['short']}) |\n")
    kinds = Counter(q["kind"] for q in questions)
    chs = Counter(q["ch"] for q in questions)
    key.append(f"\nMix: {kinds['concept']} concept / {kinds['calc']} calculation · "
               + " · ".join(f"Ch {c}: {k}" for c, k in sorted(chs.items())) + "\n\n")
    for i, q in enumerate(questions, 1):
        ans_text = q["choices"][LETTERS.index(q["ans"])][1]
        key.append(f"# {i}. {chem(q['title'])} — **{q['ans']}) {chem(ans_text)}**\n\n")
        key.append(f"**Source:** {q['cite']}  \n")
        if q.get("hw"):
            key.append(f"**Homework match:** {q['hw']}  \n")
        key.append(f"**What it tests:** {chem(q['covers'])}\n\n")
        key.append(chem(q["sol"]).strip() + "\n\n")
        notes = [(L, c) for L, c in zip(LETTERS, q["choices"]) if c is not q["correct"] and c[2]]
        if notes:
            key.append("Why the other choices are wrong:\n\n")
            for L, c in notes:
                key.append(f"* {L}) {chem(c[1])}: {chem(c[2])}\n")
            key.append("\n")
    (OUT / f"practice-exam-3-{n}-key.qmd").write_text("".join(key), encoding="utf-8")
    print(f"Wrote practice-exam-3-{n}.qmd and practice-exam-3-{n}-key.qmd")
