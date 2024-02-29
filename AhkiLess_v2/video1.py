from vidstream import CameraClient
from vidstream import StreamingServer
import threading
import time


#recv=sarra
#send=ena
#192.168.30.154
def start_camera_stream():
    receiving = StreamingServer('192.168.1.12',8888)
    t1 = threading.Thread(target=receiving.start_server)
        
        
    sending = CameraClient('192.168.1.12',8888)
    t2 = threading.Thread(target=sending.start_stream)

    t1.start()
    t2.start()

    #time.sleep(2)

        

    while input("") != "STOP":
        continue

    receiving.stop_server()
    sending.stop_stream()


