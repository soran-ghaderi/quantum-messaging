from projectq import MainEngine
from transmitter import send_full_message

if __name__ == '__main__':

    quantum_engine = MainEngine()
    message = input("message: ")
    # message = 'This is a test message - quantum p2p messaging protocol - Soran Ghadri, 2021'
    send_full_message(message=message, quantum_engine=quantum_engine)
