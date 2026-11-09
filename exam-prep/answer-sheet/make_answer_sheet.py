"""Generate a printable replica of the orange 100-question bubble answer sheet.

Run:  python make_answer_sheet.py
Writes answer-sheet.svg and answer-sheet.html next to this script. The HTML
is printed to answer-sheet.pdf (US Letter, landscape, no margins) with
headless Edge; see the commands in the README section at the bottom.

All coordinates are in points (1/72 in) on an 11 x 8.5 in page.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent
W, H = 792, 612
INK = "#E8792B"        # sheet orange
SHADE = "#F6C9A6"      # light orange fill for shaded bars and headers
FONT = "Arial, Helvetica, sans-serif"

svg = []


def rect(x, y, w, h, fill="none", stroke=INK, sw=0.8):
    svg.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
               f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def line(x1, y1, x2, y2, sw=0.8):
    svg.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
               f'stroke="{INK}" stroke-width="{sw}"/>')


def text(x, y, s, size=6, weight="bold", anchor="middle", fill=INK):
    svg.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{FONT}" font-size="{size}" '
               f'font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{s}</text>')


def bubble(cx, cy, label="", r=4.6, size=4.6):
    svg.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="white" stroke="{INK}" stroke-width="0.7"/>')
    if label:
        text(cx, cy + size * 0.36, label, size=size, weight="normal")


# ------------------------------------------------------------ name grid
NX, NY = 30, 40                 # top-left of the name block
COLW = 12.9                     # column pitch shared by every bubble grid
NAME_COLS, PREFIX_COLS = 16, 4
ROW = 11.7                      # bubble row pitch in the name grid
LETTERS = [""] + [chr(c) for c in range(ord("A"), ord("Z") + 1)]
name_w = (NAME_COLS + PREFIX_COLS) * COLW
prefix_x = NX + NAME_COLS * COLW

hdr_h, box_h = 24, 15
line(NX, NY - 6, NX, NY + 4, sw=1)
text(NX + 4, NY + 14, "LAST NAME (Space) FIRST NAME", 6.2, anchor="start")
grid_top = NY + hdr_h
grid_h = box_h + len(LETTERS) * ROW + 6
rect(NX, NY + 4, name_w, hdr_h - 4 + grid_h, sw=1)
# Raised "COURSE PREFIX" tab, drawn over the outer border so no line crosses its label.
rect(prefix_x, NY - 8, PREFIX_COLS * COLW, hdr_h + 8, fill="white", sw=1)
text(prefix_x + PREFIX_COLS * COLW / 2, NY + 3, "COURSE", 5.5)
text(prefix_x + PREFIX_COLS * COLW / 2, NY + 11, "PREFIX", 5.5)
for c in range(NAME_COLS + PREFIX_COLS):
    x = NX + c * COLW
    rect(x + 1.2, grid_top + 1.5, COLW - 2.4, box_h - 3, sw=0.6)          # write-in box
    if c:
        line(x, grid_top, x, grid_top + grid_h, sw=0.35 if c != NAME_COLS else 1)
    for r, ch in enumerate(LETTERS):
        bubble(x + COLW / 2, grid_top + box_h + 5 + r * ROW + ROW / 2 - 2, ch)
line(NX, grid_top + box_h, NX + name_w, grid_top + box_h, sw=0.6)

# ------------------------------------------------------------ ID blocks
IY = grid_top + grid_h + 11     # top of the ID blocks
ID_ROW = 10.9
DIGITS = [str(d) for d in range(10)]
id_hdr = 22
id_h = id_hdr + box_h + len(DIGITS) * ID_ROW + 5
BAR = 10                        # shaded divider width

blocks = [("STUDENT ID", 8), None, ("COURSE|NUMBER", 4), None, ("CRN", 5), ("TEST|VERSION", 1)]
x = NX
for blk in blocks:
    if blk is None:
        rect(x, IY, BAR, id_h, fill=SHADE, stroke=INK, sw=0.6)
        x += BAR
        continue
    label, ncols = blk
    w = ncols * COLW
    pad = 8 if label.startswith("TEST") else 0   # shaded margins around test version
    if pad:
        rect(x, IY, w + 2 * pad, id_h, fill=SHADE, stroke=INK, sw=0.6)
        rect(x + pad, IY + id_hdr, w, id_h - id_hdr, fill="white", sw=0.6)
        rect(x, IY, w + 2 * pad, id_hdr, fill="white", sw=0.8)
    else:
        rect(x, IY, w, id_h, sw=1)
        line(x, IY + id_hdr, x + w, IY + id_hdr, sw=0.8)
    parts = label.split("|")
    cx = x + (w + 2 * pad) / 2
    for i, p in enumerate(parts):
        text(cx, IY + 10 + i * 7 - (len(parts) - 1) * 3, p, 4.8 if pad else 5.5)
    top = IY + id_hdr
    for c in range(ncols):
        bx = x + pad + c * COLW
        rect(bx + 1.2, top + 1.5, COLW - 2.4, box_h - 3, sw=0.6)
        if c:
            line(bx, top, bx, IY + id_h, sw=0.35)
        for r, d in enumerate(DIGITS):
            bubble(bx + COLW / 2, top + box_h + 4 + r * ID_ROW + ID_ROW / 2 - 1.5, d)
    line(x + pad, top + box_h, x + pad + w, top + box_h, sw=0.6)
    x += w + 2 * pad

# ------------------------------------------------------------ answers
AX = NX + name_w + 14           # left edge of the answer panel
AW = W - 22 - AX
AY = 34
rect(AX + AW - 46, AY - 8, 46, 12, sw=0.8)
text(AX + AW - 23, AY, "SIDE 1", 5.5)
title_h = 32
rect(AX + 50, AY + 4, AW - 110, title_h, sw=1)
text(AX + AW / 2 - 5, AY + 18, "GENERAL PURPOSE - ANSWER SHEET", 11)
text(AX + AW / 2 - 5, AY + 29, "FILL EACH CIRCLE COMPLETELY · ONE ANSWER PER QUESTION", 6.3)

COLS, PER_COL = 5, 10
col_w = AW / COLS
Q_PITCH = 22.0                  # vertical pitch per question (letter row + bubble row)
B_PITCH = 13.2                  # horizontal pitch between A–E bubbles
half_h = PER_COL * Q_PITCH + 22


def answer_half(top, first_q, tf_header):
    rect(AX, top, AW, half_h, sw=1)
    for c in range(COLS):
        x0 = AX + c * col_w + 18
        if tf_header:
            text(x0 + 6, top + 8, "T", 5.3)
            text(x0 + 6 + B_PITCH, top + 8, "F", 5.3)
        for r in range(PER_COL):
            q = first_q + c * PER_COL + r
            y_letters = top + 15 + r * Q_PITCH + (2 if tf_header else -2)
            y_bub = y_letters + 8.5
            text(x0 - 3.5, y_bub + 2.2, str(q), 6.3, anchor="end")
            for k, L in enumerate("ABCDE"):
                bx = x0 + 6 + k * B_PITCH
                text(bx, y_letters, L, 5.3)
                bubble(bx, y_bub, str(k + 1), r=5.0, size=5)


top1 = AY + title_h + 10
answer_half(top1, 1, tf_header=True)
top2 = top1 + half_h + 8
answer_half(top2, 51, tf_header=False)

# ------------------------------------------------------------ timing marks
for i in range(int((W - 40) / 9.2)):
    svg.append(f'<rect x="{24 + i * 9.2:.2f}" y="{H - 16}" width="3.2" height="7" fill="#111"/>')
for i in range(3):
    svg.append(f'<rect x="12" y="{IY + id_h - 52 + i * 17:.2f}" width="6" height="7" fill="#111"/>')

body = "\n".join(svg)
svg_doc = (f'<svg xmlns="http://www.w3.org/2000/svg" width="11in" height="8.5in" '
           f'viewBox="0 0 {W} {H}">\n<rect width="{W}" height="{H}" fill="white"/>\n{body}\n</svg>\n')
(OUT / "answer-sheet.svg").write_text(svg_doc, encoding="utf-8")
html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Answer Sheet</title>
<style>@page {{ size: 11in 8.5in; margin: 0; }} html, body {{ margin: 0; padding: 0; background: white; }}
svg {{ display: block; width: 11in; height: 8.5in; }}</style></head>
<body>{svg_doc}</body></html>
"""
(OUT / "answer-sheet.html").write_text(html, encoding="utf-8")
print(f"bottom of ID block: {IY + id_h:.1f}pt, bottom of answers: {top2 + half_h:.1f}pt (page {H}pt)")
