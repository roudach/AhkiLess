import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import Button, PhotoImage, simpledialog
import time
from setuptools import Command 
from win10toast import ToastNotifier
from notif import CountdownTimer
HOST = '127.0.0.1'
PORT = 5566

class Client:
    def __init__(self,host,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((host,port))

        msg = tkinter.Tk()
        msg.withdraw
        self.pseudo = simpledialog.askstring("Pseudo","Veuillez choisir un pseudonyme",parent=msg)

        self.gui_done = False
        self.running = True 
        

        gui_thread = threading.Thread(target= self.gui_loop)
        receive_thread = threading.Thread(target= self.receive)

        gui_thread.start()
        receive_thread.start()
    
    def popup():
        pass

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.title("Ahkili")

        self.win.configure(bg="")

        #timer_label = self.win()
        #self.timer_label = tkinter.Label(self.win, text="reminder", )

        timer_button = tkinter.Button(self.win, text="CountdownTimer", command=CountdownTimer )
        timer_button.pack(padx=40,pady=20,)


        self.chat_label = tkinter.Label(self.win, text="Chat:",bg="#D6ABF9")
        self.chat_label.config(font=('Arial',12))
        self.chat_label.pack(padx=20,pady=5)
      


        self.text_area = tkinter.scrolledtext.ScrolledText(self.win,bg="#F2BCFC")
        self.text_area.pack(padx=20,pady=5)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(self.win, text="Message",bg="#D6ABF9")
        self.msg_label.config(font=("Arial",12))
        self.msg_label.pack(padx=20,pady=5)
        

        self.input_area = tkinter.Text(self.win , height=3,bg="#B8C6FE")
        self.input_area.pack(padx=20 , pady=5)

        self.send_button = tkinter.Button(self.win , text='Send',command = self.write, bg="#D6ABF9")
        self.send_button.config(font=("Arial",12))
        self.send_button.pack(padx=20,pady= 5)

        self.gui_done = True
        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        self.win.mainloop()
       



        
    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode()
                if message =='NICK':
                    self.sock.send(self.pseudo.encode())
                else:
                    if self.gui_done:
                        self.text_area.config(state = 'normal')
                        self.text_area.insert('end',message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break

       
    def write(self):
        message =f"\n{self.pseudo}:\n{self.input_area.get('1.0','end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0','end')      
     


    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)  

      

client = Client(HOST,PORT)
    
