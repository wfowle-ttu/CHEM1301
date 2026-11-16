"""Build driller-7-3: solubility rules and precipitation (15 questions, layout in soldrill.py).

Run:  python CHEM1301/exam-prep/exam-3/_scripts/build_driller_7_3.py
"""
from soldrill import build
from solib import C7, T

SPEC = dict(
    concept1=dict(
        ch=7, kind="concept", title="What a net ionic equation shows", short="Ch 7 sl. 17–18",
        stem="What does the **net ionic equation** for a reaction in solution show?",
        correct=T("Only the components that are directly involved in the reaction, without spectator ions"),
        wrong=[T("Every ion and compound present, including spectator ions",
                 "That is the **complete** ionic equation (slide 16)."),
               T("The complete formulas of all reactants and products", "That is the **molecular** equation (slide 15)."),
               T("Only the spectator ions", "Backwards: spectator ions are the ones left out."),
               T("Only the ions that stay dissolved", "Ions that stay dissolved and unchanged are spectators, which are left out.")],
        cite=f"{C7}, slide 17 (net ionic equations include only components directly involved), slide 18 (three types of equations)",
        hw="HW15 — hw15ex1.png (what is a net ionic equation?)",
        covers="Molecular vs complete ionic vs net ionic equations (slide 18).",
        sol="""Slide 18 compares the three kinds of equation:

* **Molecular:** complete formulas of all reactants and products.
* **Complete ionic:** every strong electrolyte written as ions; all reactants and products included.
* **Net ionic:** only the components that **undergo a change**; spectator ions are not included.""",
    ),
    insol=[("Na", "OH"), ("Hg2", "Cl"), ("Fe2", "NO3"), ("Al", "SO4"), ("K", "CO3")],
    sol=[("Al", "OH"), ("Ag", "PO4"), ("Ba", "CO3"), ("Cu", "S"), ("Ca", "Cl")],
    rule_sol=("Cu", "Cl"), rule_sol_others=[1, 2, 4, 5],
    rule_ins=("Fe3", "PO4"), rule_ins_others=[1, 2, 4, 5],
    count=[("Ag", "NO3"), ("Na", "PO4"), ("Cr", "Cl"), ("Mg", "CO3"), ("Ca", "SO4")],
    names=[("Zn", "Cl"), ("NH4", "S"), ("Cu", "CO3"), ("Co", "NO3"), ("Mg", "SO4")],
    mix=(("Ag", "NO3"), ("Na", "PO4")),
    mix_wrong=("[[AgPO4]]", "Ag^+^ is only +1, so three are needed to cancel PO~4~^3−^: Ag~3~PO~4~."),
    mol=(("Al", "NO3"), ("K", "OH")),
    pairs_nr=[(("NH4", "CO3"), ("Na", "Cl")), (("Hg2", "NO3"), ("Na", "Cl")), (("Ca", "NO3"), ("K", "SO4")),
              (("Ni", "NO3"), ("K", "OH")), (("Mn", "Cl"), ("Na", "S"))],
    pairs_ppt=[(("Co", "Cl"), ("Na", "PO4")), (("Fe2", "NO3"), ("K", "Cl")), (("Al", "Cl"), ("Na", "NO3")),
               (("Ni", "SO4"), ("NH4", "Cl")), (("Mg", "NO3"), ("Na", "SO4"))],
    net=(("Zn", "NO3"), ("K", "PO4")),
    spect=(("Ni", "Cl"), ("Na", "OH")),
    select=("Pb", "Ba", [("Na", "Cl"), ("Na", "SO4"), ("Na", "CO3"), ("Na", "PO4"), ("K", "NO3")]),
    concept2=dict(
        ch=7, kind="concept", title="Predicting precipitates: step 2", short="Ch 7 sl. 14",
        stem="After writing the reactants as separated ions, what is the next step in predicting whether a precipitate forms "
             "when two ionic solutions are mixed?",
        correct=T("Exchange the anions of the two salts to find the solids that could form"),
        wrong=[T("Exchange the cations with the anions within the same salt",
                 "That just rebuilds the original salts. You pair each cation with the **other** salt's anion."),
               T("Combine the two cations into one solid", "A solid needs zero charge, so it can't be two cations (slide 10)."),
               T("Balance the molecular equation", "Balancing comes after you know the products."),
               T("Cancel the spectator ions", "You can't know which ions are spectators until you know what precipitates.")],
        cite=f"{C7}, slide 14 (How to Predict Precipitates: 1 write ions, 2 exchange the anions, 3 use the solubility rules)",
        hw="HW15 — hw15ex3.png and hw15ex4.png (predict NR or a precipitate)",
        covers="The three steps of slide 14, in order.",
        sol="""Slide 14's method:

1. Write the reactants as they actually exist: **separated ions**.
2. **Consider the solids that could form by exchanging the anions** of the two salts.
3. Use the solubility rules (Table 7.1) to decide whether either product is insoluble. If neither is, it's NR.""",
    ),
)

if __name__ == "__main__":
    build(3, SPEC)
