# GLP1_GLP1R.py

import numpy as np
import matplotlib.pyplot as plt

def Fact(L1, L2, Kd1, Kd2):
    """Fractional receptor activation with two agonists L1 and L2"""
    return (Kd2*L1+Kd1*L2) / (Kd1*Kd2 + Kd2*L1 + Kd1*L2)

# Dissociation constants [nM] for each ligand at GLP1R
Kd1 = 0.17 # L1, GLP1
Kd2 = 0.38 # L2, semaglutide

# Ligand concentration, 0.001 to 100 [nM] (centered on the sub-nM Kd values)
L1s = {
    "fasting":    0.015, # [nM] GLP1
    "after meal": 0.040, # [nM] GLP1
}
L2 = np.logspace(-3, 2, 500) # [nM] semaglutide

plt.figure()
for state, L1 in L1s.items():
    line, = plt.semilogx(L2, Fact(L1, L2, Kd1, Kd2), lw=2,
                         label=f"GLP1 {state} ({L1} nM)")
    # Baseline activation from GLP1 alone (no semaglutide), same color as its curve
    plt.axhline(Fact(L1, 0, Kd1, Kd2), ls=":", c=line.get_color(), lw=1)

# Mark the semaglutide Kd
plt.axvline(Kd2, ls=":", c="k", lw=1, label=f"semaglutide Kd ({Kd2} nM)")

plt.axhline(0.5, ls="--", c="gray", lw=1)
plt.ylim(0, 1)
plt.xlabel("[semaglutide] (nM, log scale)")
plt.ylabel("Fraction active (Fact)")
plt.title("GLP1R activation by semaglutide with GLP1 present")
plt.legend(loc="upper left")
plt.show()