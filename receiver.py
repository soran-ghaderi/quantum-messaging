from projectq.ops import X, Z, Measure

from bell_pair import Bell_pair
from message import create_message

def message_reciever(quantum_engine, message, qubit_two):
    '''
    Pauli-X and/or Pauli-Z gates are applied to the Qubit,
    conditionally on the values in the message.
    '''
    if message[1] == 1:
        X | qubit_two
    if message[0] == 1:
        Z | qubit_two