from vidstream import AudioReceiver
from vidstream import AudioSender
import threading

def audio():
    receiver  = AudioReceiver('192.168.1.12',6666)
    receive_thread = threading.Thread(target=receiver.start_server)

    sender = AudioSender('192.168.1.12',6666)
    sender_thread = threading.Thread(target=sender.start_stream)



    while input("") != "STOP":
        continue
    
    receive_thread.start()
    sender_thread.start()