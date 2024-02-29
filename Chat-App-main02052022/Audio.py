from vidstream import AudioReceiver
from vidstream import AudioSender
import threading

def audio():
    receiver  = AudioReceiver('localhost',6666)
    receive_thread = threading.Thread(target=receiver.start_server)

    sender = AudioSender('localhost',5555)
    sender_thread = threading.Thread(target=sender.start_stream)

    receive_thread.start()
    sender_thread.start()