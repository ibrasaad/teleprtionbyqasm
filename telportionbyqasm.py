

from qiskit.quantum_info import random_statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister,Aer,execute,qasm3
qc = QuantumCircuit(3,2)

print(qasm3.dumps(qc))
program="""
OPENQASM 3.0;
include "stdgates.inc";
qubit [3] q1;
bit [1]c2;
bit [1]c3;
h q1[1];
cx q1[1], q1[2];
cx q1[0],q1[1];
h q1[0];
c2[0] = measure q1[0];
c3[0] = measure q1[1];
if(c2==1) {x q1[2];}


"""
# circuit = qasm3.loads(program)
# circuit.draw("mpl")
print(qasm3.loads(program))