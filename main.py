from projectq import MainEngine
from transmitter import send_full_message

if __name__ == '__main__':

    quantum_engine = MainEngine()
    message = input("message: ")
    # message = 'This is a test message - quantum p2p messaging protocol - Soran Ghadri, 2021'
    send_full_message(message=message, quantum_engine=quantum_engine)


    '''
    If you are going to run the codes on IBM quantum computers you have to get a token from IBM 
    '''
    token = 'your token'
    # device = 'ibmq_armonk'
    device = 'ibmq_belem'
    # compiler_engines = projectq.setups.ibm.get_engine_list(token=token, device=device)
    # eng = MainEngine(IBMBackend(token=token, use_hardware=True, num_runs=1024,
    #                             verbose=False, device=device),
    #                  engine_list=compiler_engines)
    # quantum_engine = MainEngine()
    # The bit we want to send
    # bit = 0
    #
    # # make a Bell-pair
    # qubit_one, qubit_two = create_bell_pair(eng)
    #
    # # Entangle the bit with qubit_one
    # print('Sending bit: ', bit)
    # classical_encoded_message = create_message(quantum_engine=eng, qubit_one=qubit_one, message_value=bit)
    # print('Encoded in classical message: ', classical_encoded_message)
    #
    # # Sending the message along with the second qubit for state re-creation
    # recieved_bit = message_reciever(eng, classical_encoded_message, qubit_two)
    # print('Received bit: ', recieved_bit)