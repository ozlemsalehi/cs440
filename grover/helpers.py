import numpy as np
from qiskit.quantum_info import Statevector


def print_dirac(qc, eps=1e-4):
    sv = Statevector.from_instruction(qc)
    l = []
    n = int(np.log2(len(sv)))
    for i, amp in enumerate(sv):
        if abs(amp) > eps:
            b = format(i, f"0{n}b")
            l.append(f"{amp.real:.3g} |{b}⟩")
    print(" + ".join(l))