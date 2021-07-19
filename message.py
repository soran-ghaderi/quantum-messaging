from projectq.ops import X, CNOT, H, Measure


def create_message(quantum_engine='',qubit_one='', message_value = 0):

    qubit_to_send = quantum_engine.allocate_qubit()
    if message_value == 1:
        '''
        Flip the state using Pauli-X gate to set the qubit to positive if the value was 1
        '''
        X | qubit_to_send


    # entangle the original qubit with the message qubit
    CNOT | (qubit_to_send, qubit_one)

    '''
        1 - Put the message qubit in superposition 
        2 - Measure out the two values to get the classical bit value
            by collapsing the state. 
        '''
    H | qubit_to_send
    Measure | qubit_to_send
    Measure | qubit_one

    # The qubits are now turned into normal bits we can send through classical channels
    classical_encoded_message = [int(qubit_to_send), int(qubit_one)]

    return classical_encoded_message