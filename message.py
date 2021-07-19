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