from projectq.ops import H, CNOT

class Bell_pair:
    def __init__(self):
        self.qubit_one = None
        self.qubit_two = None

    def create_bell_pair(self, quantum_engine):
        # Qubit one is the sender's qubit, and will be used to create a message
        self.qubit_one = quantum_engine.allocate_qubit()
        # Qubit two is the receiver's qubit, and will be used to re-create the message state
        self.qubit_two = quantum_engine.allocate_qubit()

        ''' 
        Hadamard gate to put Qubit one in superposition
        This sets the value of a equal probability of being 1 or 0
        '''
        H | self.qubit_one