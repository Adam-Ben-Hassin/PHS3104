import numpy as np
import qutip as qt
import matplotlib.pyplot as plt

# construction de l'hamiltonien dépendant du temps H(t) = σy * cos(ωt)

def Htd(t, args):
    om = 1
    return qt.sigmay()*np.cos(om*t)

# etat initial |z+> 

psi0 = qt.basis(2, 0)

t = np.linspace(0, 10, 500)

output = qt.sesolve(Htd, psi0, t)

# calcul de la probabilité

P = []

for state in output.states:
    b = state[1, 0]
    P.append(np.abs(b)**2)

plt.plot(t, P)
plt.xlabel('Temps')
plt.ylabel('Probabilité')
plt.title('Évolution de la probabilité')
plt.show()