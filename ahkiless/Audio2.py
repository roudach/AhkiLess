from vidstream import AudioReceiver
from vidstream import AudioSender
import threading

def audio():
    receiver = AudioReceiver('127.0.0.1',5555)
    receive_thread = threading.Thread(target=receiver.start_server)

    sender = AudioSender('127.0.0.1',6666)
    sender_thread = threading.Thread(target=sender.start_stream)

    receive_thread.start()
    sender_thread.start()