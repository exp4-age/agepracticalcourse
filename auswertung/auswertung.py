"""Beispiel für eine Auswertung in Python.
Natürlich gibt es auch Packages zur Fehlerfortpflanzung, allerdings wird
es hier bewusst 'per Hand' gemacht; Im Protokoll müssen die Formeln
angegeben werden, die zur Fehlerfortpflanzung verwendet wurden.

"""

import numpy as np

# Messwerte
# Länge l
l = 1.5  # in m
ul = 0.003  # Messunsicherheit in m

# Durchmesser d
d = 5.0e-4  # in m
ud = 0.2e-4  # Messunsicherheit in m
r = 0.5 * d  # Radius
ur = 0.5 * ud  # Messunsicherheit in m

# Masse m
m = 0.393  # in kg
um = 0.001  # Messunsicherheit in kg

# Position R
R1 = 0.045  # in m
uR1 = 0.003  # Messunsicherheit in m

R2 = 0.200  # in m
uR2 = 0.003  # Messunsicherheit in m

# Einzelmessungen der Schwingungsdauern
t01 = 755.53  # in s
n01 = 26

t02 = 726.29  # in s
n02 = 25

t11 = 806.59  # in s
n11 = 26

t12 = 775.66  # in s
n12 = 25

t21 = 1637.8  # in s
n21 = 30

t22 = 1638.0  # in s
n22 = 30

# Unsicherheit der Einzelmessungen
ut = 1  # in s

print("Berechnung der Schwingungsdauern und jeweiligen Unsicherheiten in s:")
print("--------------------------------------------------------------------")
T0 = 0.5 * (t01 / n01 + t02 / n02)
uT0 = 0.5 * np.sqrt((ut / n01) ** 2 + (ut / n02) ** 2)
print("T0 = {:.2f} ± {:.2f}".format(T0, uT0))

T1 = 0.5 * (t11 / n11 + t12 / n12)
uT1 = 0.5 * np.sqrt((ut / n11) ** 2 + (ut / n12) ** 2)
print("T1 = {:.2f} ± {:.2f}".format(T1, uT1))

T2 = 0.5 * (t21 / n21 + t22 / n22)
uT2 = 0.5 * np.sqrt((ut / n21) ** 2 + (ut / n22) ** 2)
print("T2 = {:.2f} ± {:.2f}".format(T2, uT2))
print()

print("Berechnung der Federkonstante in Nm:")
print("------------------------------------")
D = 4 * np.pi**2 * m * (R2**2 - R1**2) / (T2**2 - T1**2)
uDm = ((R2**2 - R1**2) / (T2**2 - T1**2) * um)**2
uDR1 = (m * 2 * R1 / (T2**2 - T1**2) * uR1)**2
uDR2 = (m * 2 * R2 / (T2**2 - T1**2) * uR2)**2
uDT1 = (m * 2 * (R2**2 - R1**2) / (T2**2 - T1**2)**2 * T1 * uT1)**2
uDT2 = (m * 2 * (R2**2 - R1**2) / (T2**2 - T1**2)**2 * T2 * uT2)**2
uD = 4 * np.pi**2 * np.sqrt(uDm + uDR1 + uDR2 + uDT1 + uDT2)
print("D = ({:.2f} ± {:.2f})e-4".format(D * 10**4, uD * 10**4))
print("Beiträge zur Unsicherheit:")
print("  um: {:.2f}".format(uDm * 10**15))
print("  uR1: {:.2f}".format(uDR1 * 10**15))
print("  uR2: {:.2f}".format(uDR2 * 10**15))
print("  uT1: {:.2f}".format(uDT1 * 10**15))
print("  uT2: {:.2f}".format(uDT2 * 10**15))
print()

print("Berechnung des Torsionsmoduls in Nm^-2:")
print("----------------------------------------")
G = 2 * D * l / (np.pi * r**4)
uGD = (l / r**4 * uD)**2
uGl = (D / r**4 * ul)**2
uGr = (D * 4 * l / r**5 * ur)**2
uG = 2 / np.pi * np.sqrt(uGD + uGl + uGr)
print("G = ({:.2f} ± {:.2f})e10".format(G * 10**-10, uG * 10**-10))
print("Beiträge zur Unsicherheit:")
print("  uD: {:.2f}".format(uGD * 10**-18))
print("  ul: {:.2f}".format(uGl * 10**-18))
print("  ur: {:.2f}".format(uGr * 10**-18))
print()

print("Berechnung des Trägheitsmoments in kgm^2:")
print("-----------------------------------------")
J0 = T0**2 * D / (4 * np.pi**2)
uJ0 = np.sqrt(
    (T0**2 / (4 * np.pi**2) * uD)**2
    + (2 * T0 * D / (4 * np.pi**2) * uT0)**2
)
print("J0 = ({:.2f} ± {:.2f})e-3".format(J0 * 10**3, uJ0 * 10**3))
print()