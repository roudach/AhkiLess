from concurrent.futures import thread
from re import M
import socket
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import END, Variable, ttk
from tkinter import filedialog
from tkinter import messagebox
import pickle
from datetime import datetime
import os
import threading
import struct
from tkinter import Menu, simpledialog
import time
from numpy import var
from facial import *
import tkinter.font as tkFont
import sqlite3
from Audio import *
import facial
from video1 import *


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass



class FirstScreen(tk.Tk,threading.Thread):
    def __init__(self):
        super().__init__()

        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()

        self.x_co = int((screen_width / 2) - (550 / 2))
        self.y_co = int((screen_height / 2) - (400 / 2)) - 80
        self.geometry(f"1100x550+350+10")
        self.title("Ahkiless")

        self.user = None
        self.image_extension = None
        self.image_path = None

        self.first_frame = tk.Frame(self, bg="#E4D6AF")
        self.first_frame.pack(fill="both", expand=True)

        # self.right_frame = tk.Frame(self, bg="green")
        # self.right_frame.pack(fill="y", expand=True)

        app_icon = Image.open('images/chat_ca.png')
        app_icon = ImageTk.PhotoImage(app_icon)

        self.iconphoto(False, app_icon)

        background = Image.open("images/login_bg_ca.jpg")
        background = background.resize((850, 700), Image.ANTIALIAS)
        background = ImageTk.PhotoImage(background)

        upload_image = Image.open('images/upload_ca.png')
        upload_image = upload_image.resize((25, 25), Image.ANTIALIAS)
        upload_image = ImageTk.PhotoImage(upload_image)

        self.user_image = 'images/user.png' 

        # #tk.Label(self.first_frame, image=background).place(x=0, y=0)
        # self.login = tk.Frame(self.first_frame,bg="green", padx=80, 
        # pady=10, width=350, height=300)
        # self.login.grid(row=1, column=0, sticky="ns")
        # self.heade=tk.Frame(self.first_frame,bg="yellow",width=950, height=50)
        # self.heade.grid(row=0, column=1, sticky="ns")
        # create all of the main containers
        # create all of the main containers
 #****************************frame & widgets*******************************
        var = tk.StringVar()
        var.set('male')
        my_font = tk.font.Font(self.first_frame, ("courier new", 12, "bold italic"))
        countries = []
        variable = tk.StringVar()
        world = open('countries.txt', 'r')
        for country in world:
            country = country.rstrip('\n')
            countries.append(country)
        variable.set(countries[4])
        # widgets
        left_frame = tk.Frame(
            self.first_frame, 
            bd=2, 
            bg='#B3BDE6',   
            relief=tk.SOLID , 
            padx=10, 
            pady=10
            )

        
        self.username=tk.Label(
            left_frame, 
            text="Username", 
            fg="#541C1C",
            bg='#B3BDE6',
            font=my_font).grid(row=0, column=0, sticky=tk.W, pady=10)
        
        tk.Label(
            left_frame, 
            text="Enter Password", 
            fg="#541C1C",
            bg='#B3BDE6',
            font=my_font
            ).grid(row=1, column=0, pady=10)

        self.username_entry = tk.Entry(
            left_frame, 
            font=my_font,
            width=10,
            highlightcolor="blue", 
            highlightthickness=1
             )
        self.username_entry.focus_set()
        self.password_entry = tk.Entry(
            left_frame, 
            font=my_font,
            show='*',
            width=10,
            highlightcolor="blue",
            highlightthickness=1)
           
        submit_button = tk.Button(
            left_frame, 
            width=15, 
            text='Login', 
            fg="#27143D",
            font=my_font, 
            relief=tk.SOLID,
            cursor='hand2',
            command=self.login_response
            )

        self.right_frame = tk.Frame(
            self.first_frame, 
            bd=2, 
            bg='#B3BDE6',
            relief=tk.SOLID, 
            padx=10, 
            pady=10
            )

        tk.Label(
            self.right_frame, 
            text="Enter Name", 
            fg="#541C1C",
            bg='#B3BDE6',
            font=my_font
            ).grid(row=0, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self.right_frame, 
            text="Enter Email", 
            fg="#541C1C",
            bg='#B3BDE6',
            font=my_font
            ).grid(row=1, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self.right_frame, 
            text="Contact Number", 
            fg="#541C1C",
            bg='#B3BDE6',
            font=my_font
            ).grid(row=2, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self.right_frame, 
            text="Select Gender", 
            fg="#541C1C",
            bg='#B3BDE6',
            font=my_font
            ).grid(row=3, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self.right_frame, 
            text="Select Country",
            fg="#541C1C", 
            bg='#B3BDE6',
            font=my_font
            ).grid(row=4, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self.right_frame, 
            text="Enter Password", 
            fg="#541C1C",
            bg='#B3BDE6',
            font=my_font
            ).grid(row=5, column=0, sticky=tk.W, pady=10)

        tk.Label(
            self.right_frame, 
            text="Re-Enter Password", 
            fg="#541C1C",
            bg='#B3BDE6',
            font=my_font
            ).grid(row=6, column=0, sticky=tk.W, pady=10)

        self.gender_frame = tk.LabelFrame(
            self.right_frame,
            bg='#B3BDE6',
            padx=10, 
            pady=10,
            )


        self.register_name = tk.Entry(
            self.right_frame, 
            font=my_font
            )

        self.register_email = tk.Entry(
            self.right_frame, 
            font=my_font
            )

        self.register_mobile = tk.Entry(
            self.right_frame, 
            font=my_font
            )


        self.male_rb = tk.Radiobutton(
            self.gender_frame, 
            text='Male',
            fg="#541C1C",
            bg='#B3BDE6',
            variable=var,
            value='male',
            font=('Times', 10),
            
        )

        self.female_rb = tk.Radiobutton(
            self.gender_frame,
            text='Female',
            fg="#541C1C",
            bg='#B3BDE6',
            variable=var,
            value='female',
            font=('Times', 10),
        
        ) 

        self.register_country = tk.OptionMenu(
            self.right_frame, 
            variable, 
            *countries)

        self.register_country.config(
            width=15, 
            font=('Times', 12)
        )
        self.register_pwd = tk.Entry(
            self.right_frame, 
            font=my_font,
            show='*'
        )
        self.pwd_again = tk.Entry(
            self.right_frame, 
            font=my_font,
            show='*'
        )

        register_btn = tk.Button(
            self.right_frame, 
            width=15, 
            text='Register', 
            fg="#27143D",
            font=my_font, 
            relief=tk.SOLID,
            cursor='hand2',
            command=self.insert_record
        )


        # widgets placement
        self.username_entry.grid(row=0, column=1, pady=10, padx=20)
        self.password_entry.grid(row=1, column=1, pady=10, padx=20)
        submit_button.grid(row=2, column=1, pady=10, padx=20)
        left_frame.place(x=50, y=50)

        self.register_name.grid(row=0, column=1, pady=10, padx=20)
        self.register_email.grid(row=1, column=1, pady=10, padx=20) 
        self.register_mobile.grid(row=2, column=1, pady=10, padx=20)
        self.register_country.grid(row=4, column=1, pady=10, padx=20)
        self.register_pwd.grid(row=5, column=1, pady=10, padx=20)
        self.pwd_again.grid(row=6, column=1, pady=10, padx=20)
        register_btn.grid(row=7, column=1, pady=10, padx=20)
        self.right_frame.place(x=500, y=50)

        self.gender_frame.grid(row=3, column=1, pady=10, padx=20)
        self.male_rb.pack(expand=True, side=tk.LEFT)
        self.female_rb.pack(expand=True, side=tk.LEFT)
 # *************************end frame & widgetw*****************************       


        # layout all of the main containers
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        #head = tk.Label(self.first_frame, text="welcome", font="lucida 17 bold", bg="grey")
        #head.place(relwidth=1, y=10)
        
        
        #self.login.pack(fill="both", expand=True)
        
        # self.profile_label = tk.Label(self.first_frame, bg="grey")
        # self.profile_label.place(x=350, y=75, width=150, height=140)

        # upload_button = tk.Button(self.first_frame, image=upload_image, compound="left", text="Upload Image",
        #                           cursor="hand2", font="lucida 12 bold", padx=2, command=self.add_photo)
        # upload_button.place(x=345, y=220)

        # self.username = tk.Label(self.first_frame, text="Username", font="lucida 12 bold", bg="grey")
        # self.username.place(x=40, y=150)

        # self.username_entry = tk.Entry(self.first_frame,  font="lucida 12 bold", width=10,
        #                                highlightcolor="blue", highlightthickness=1)
        # self.username_entry.place(x=160, y=150)

        #self.username_entry.focus_set()
        #************************************************************
        
        # self.password = tk.Label(self.first_frame, text="Password", font="lucida 12 bold", bg="grey")
        # self.password.place(x=40, y=220)

        # self.password_entry = tk.Entry(self.first_frame,  font="lucida 12 bold", width=10,
        #                                highlightcolor="blue", highlightthickness=1)
        # self.password_entry.place(x=160, y=220)

        # self.password = tk.Label(self.first_frame, text="Password", font="lucida 12 bold", bg="grey")
        # self.password.place(x=500, y=220)
        # self.password_entry = tk.Entry(self.first_frame,  font="lucida 12 bold", width=10,
        #                                highlightcolor="blue", highlightthickness=1)
        # self.password_entry.place(x=600, y=220)
       

#************************************************************

        # submit_button = tk.Button(self.first_frame, text="Connect", font="lucida 12 bold", padx=30, cursor="hand2",
        #                           command=self.login_response,
        #                           bg="#16cade", relief="solid", bd=2)

        # submit_button.place(x=200, y=275)
        
        self.mainloop()
#*************************fonction verif utilisateur exite ou non
    def login_response(self):
        global username_entry
        global password_entry
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        c.execute("SELECT * FROM record where name=? AND password=? ", (self.username_entry.get()  , self.password_entry.get()))
        row=c.fetchone()
        if row:
            messagebox.showinfo('info', 'login success')
            # self.username_entry.delete(0, END)
            # self.password_entry.delete(0, END)
            self.process_data()
        else:
            messagebox.showinfo('info','login failed')
            c.connection.commit()
            con.close()

    def insert_record(self):
        # check_counter=0
        global register_name
        global register_email
        global register_mobile
        global var
        global variable
        global register_pwd
        global pwd_again
        con = sqlite3.connect('userdata.db')
        cur = con.cursor()
        messagebox.showinfo('info', ' insertion')
        cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :gender, :country, :password)", {
                        'name': self.register_name.get(),
                        'email': self.register_email.get(),
                        'contact': self.register_mobile.get(),
                        'gender': var.get(),
                        'country': self.variable.get(),
                        'password': self.register_pwd.get()

         })
        con.commit()
        messagebox.showinfo('confirmation', 'Record Saved')
        con.close()
        self.register_name.delete(0, END)
        self.register_email.delete(0, END)
        self.register_mobile.delete(0, END)
        self.register_pwd.delete(0, END)
        self.pwd_again.delete(0, END)


    #     except Exception as ep:
    #         messagebox.showerror('', ep) 
    # else:
    #     messagebox.showerror('Error', warn)
#*****************************fin fonction verif utilisateur ****************************

    def add_photo(self):
        self.image_path = filedialog.askopenfilename()
        image_name = os.path.basename(self.image_path)
        self.image_extension = image_name[image_name.rfind('.')+1:]

        if self.image_path:
            user_image = Image.open(self.image_path)
            user_image = user_image.resize((150, 140), Image.ANTIALIAS)
            user_image.save('resized'+image_name)
            user_image.close()

            self.image_path = 'resized'+image_name
            user_image = Image.open(self.image_path)

            user_image = ImageTk.PhotoImage(user_image)
            self.profile_label.image = user_image
            self.profile_label.config(image=user_image)



    

    def process_data(self):
        if self.username_entry.get():
            #self.profile_label.config(image="")

            if len((self.username_entry.get()).strip()) > 6:
                self.user = self.username_entry.get()
            
            else:
                self.user = self.username_entry.get()

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                client_socket.connect(('localhost', 12345))
                status = client_socket.recv(1024).decode()
                if status == 'not_allowed':
                    client_socket.close()
                    messagebox.showinfo(title="Can't connect !", message='Sorry, server is completely occupied.'
                                                                         'Try again later')
                    return

            except ConnectionRefusedError:
                messagebox.showinfo(title="Can't connect !", message="Server is offline , try again later.")
                print("Server is offline , try again later.")
                return

            client_socket.send(self.user.encode('utf-8'))

            if not self.image_path:
                self.image_path = self.user_image
            with open(self.image_path, 'rb') as image_data:
                image_bytes = image_data.read()

            image_len = len(image_bytes)
            image_len_bytes = struct.pack('i', image_len)
            client_socket.send(image_len_bytes)

            if client_socket.recv(1024).decode() == 'received':
                client_socket.send(str(self.image_extension).strip().encode())

            client_socket.send(image_bytes)

            clients_data_size_bytes = client_socket.recv(1024)
            clients_data_size_int = struct.unpack('i', clients_data_size_bytes)[0]
            b = b''
            while True:
                clients_data_bytes = client_socket.recv(1024)
                b += clients_data_bytes
                if len(b) == clients_data_size_int:
                    break

            clients_connected = pickle.loads(b)

            client_socket.send('image_received'.encode())

            user_id = struct.unpack('i', client_socket.recv(1024))[0]
            print(f"{self.user} is user no. {user_id}")
            ChatScreen(self, self.first_frame, client_socket, clients_connected, user_id)





    
class ChatScreen(tk.Canvas, threading.Thread):
    def __init__(self, parent, first_frame, client_socket, clients_connected, user_id):
        super().__init__(parent, bg="#2b2b2b")

        self.window = 'ChatScreen'

        self.first_frame = first_frame
        self.first_frame.pack_forget()

        self.parent = parent
        self.parent.bind('<Return>', lambda e: self.sent_message_format(e))

        self.all_user_image = {}

        self.user_id = user_id


        self.clients_connected = clients_connected

        # self.parent.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(self.first_frame))
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.client_socket = client_socket
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()

        x_co = int((screen_width / 2) - (680 / 2))
        y_co = int((screen_height / 2) - (750 / 2)) - 80
        self.parent.geometry(f"680x750+{x_co}+{y_co}")

        user_image = Image.open(self.parent.image_path)
        user_image = user_image.resize((40, 40), Image.ANTIALIAS)
        self.user_image = ImageTk.PhotoImage(user_image)

        # global background
        # background = Image.open("images/chat_bg_ca.jpg")
        # background = background.resize((1600, 1500), Image.ANTIALIAS)
        # background = ImageTk.PhotoImage(background)

        global group_photo
        group_photo = Image.open('images/group_ca.png')
        group_photo = group_photo.resize((60, 60), Image.ANTIALIAS)
        group_photo = ImageTk.PhotoImage(group_photo)

        self.y = 140
        self.clients_online_labels = {}

        # self.create_image(0, 0, image=background)

        self.create_text(545, 120, text="Online", font="lucida 12 bold", fill="#40C961")

        tk.Label(self, text="   ", font="lucida 15 bold", bg="#2b2b2b").place(x=4, y=29)

        tk.Label(self, text="Welcome To Ahkiless", font="lucida 15 bold", padx=20, fg="Orange",
                 bg="#2b2b2b", anchor="w", justify="left").place(x=88, y=29, relwidth=1)
       
       # ****************************Menu ******************************
        menubar=Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.videocall)
        filemenu.add_command(label="Open", command=self.videocall)
        filemenu.add_command(label="Save", command=self.videocall)
        menubar.add_cascade(label="File", menu=filemenu)

        menubar.add_command(label="Video Call", command=start_camera_stream)
        menubar.add_command(label="Audio Call", command=audio)
        menubar.add_command(label="Facial Recognition", command=facial.face)
        menubar.add_command(label="A Propos", command=self.quit)
        menubar.add_command(label="Help", command=self.quit)
        menubar.add_command(label="Exit!", command=self.quit)
        self.parent.config(menu=menubar)

       # ***************************Fin Menu**************************

        self.create_image(60, 40, image=group_photo)

        container = tk.Frame(self)
        # 595656
        # d9d5d4
        container.place(x=40, y=120, width=450, height=550)
        self.canvas = tk.Canvas(container, bg="#0B1622")
        self.scrollable_frame = tk.Frame(self.canvas, bg="#0B1622")

        scrollable_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        def configure_scroll_region(e):
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))

        def resize_frame(e):
            self.canvas.itemconfig(scrollable_window, width=e.width)

        self.scrollable_frame.bind("<Configure>", configure_scroll_region)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

        scrollbar.pack(side="right", fill="y")

        self.canvas.bind("<Configure>", resize_frame)
        self.canvas.pack(fill="both", expand=True)

        send_button = tk.Button(self, text="Send", fg="#83eaf7", font="lucida 11 bold", bg="#7d7d7d", padx=10,
                                relief="solid", bd=2, command=self.sent_message_format)
        send_button.place(x=400, y=680)

        self.entry = tk.Text(self, font="lucida 10 bold", width=38, height=2,
                             highlightcolor="blue", highlightthickness=1)
        self.entry.place(x=40, y=681)

        self.entry.focus_set()

        #*******************************

        hourString = tk.StringVar()
        minuteString = tk.StringVar()
        secondString = tk.StringVar()
        ### Set strings to default value
        hourString.set("00")
        minuteString.set("00")
        secondString.set("40")
        ### Get user input
        hourTextbox = tk.Entry(self, width=2, bg="#483659",font=("Calibri", 20, ""), textvariable=hourString)
        minuteTextbox = tk.Entry(self, width=2,bg="#483659", font=("Calibri", 20, ""), textvariable=minuteString)
        secondTextbox = tk.Entry(self, width=2,bg="#483659", font=("Calibri", 20, ""), textvariable=secondString)

        # ### Center textboxes
        hourTextbox.place(x=500, y=680)
        minuteTextbox.place(x=550, y=680)
        secondTextbox.place(x=600, y=680)
        #*******************************

        # ---------------------------emoji code logic-----------------------------------

        emoji_data = [('emojis/u0001f44a.png', '\U0001F44A'), ('emojis/u0001f44c.png', '\U0001F44C'), ('emojis/u0001f44d.png', '\U0001F44D'),
                      ('emojis/u0001f495.png', '\U0001F495'), ('emojis/u0001f496.png', '\U0001F496'), ('emojis/u0001f4a6.png', '\U0001F4A6'),
                      ('emojis/u0001f4a9.png', '\U0001F4A9'), ('emojis/u0001f4af.png', '\U0001F4AF'), ('emojis/u0001f595.png', '\U0001F595'),
                      ('emojis/u0001f600.png', '\U0001F600'), ('emojis/u0001f602.png', '\U0001F602'), ('emojis/u0001f603.png', '\U0001F603'),
                      ('emojis/u0001f605.png', '\U0001F605'), ('emojis/u0001f606.png', '\U0001F606'), ('emojis/u0001f608.png', '\U0001F608'),
                      ('emojis/u0001f60d.png', '\U0001F60D'), ('emojis/u0001f60e.png', '\U0001F60E'), ('emojis/u0001f60f.png', '\U0001F60F'),
                      ('emojis/u0001f610.png', '\U0001F610'), ('emojis/u0001f618.png', '\U0001F618'), ('emojis/u0001f61b.png', '\U0001F61B'),
                      ('emojis/u0001f61d.png', '\U0001F61D'), ('emojis/u0001f621.png', '\U0001F621'), ('emojis/u0001f624.png', '\U0001F621'),
                      ('emojis/u0001f631.png', '\U0001F631'), ('emojis/u0001f632.png', '\U0001F632'), ('emojis/u0001f634.png', '\U0001F634'),
                      ('emojis/u0001f637.png', '\U0001F637'), ('emojis/u0001f642.png', '\U0001F642'), ('emojis/u0001f64f.png', '\U0001F64F'),
                      ('emojis/u0001f920.png', '\U0001F920'), ('emojis/u0001f923.png', '\U0001F923'), ('emojis/u0001f928.png', '\U0001F928')]

        emoji_x_pos = 490
        emoji_y_pos = 520
        for Emoji in emoji_data:
            global emojis
            emojis = Image.open(Emoji[0])
            emojis = emojis.resize((20, 20), Image.ANTIALIAS)
            emojis = ImageTk.PhotoImage(emojis)

            emoji_unicode = Emoji[1]
            emoji_label = tk.Label(self, image=emojis, text=emoji_unicode, bg="yellow", cursor="hand2")
            emoji_label.image = emojis
            emoji_label.place(x=emoji_x_pos, y=emoji_y_pos)
            emoji_label.bind('<Button-1>', lambda x: self.insert_emoji(x))

            emoji_x_pos += 25
            cur_index = emoji_data.index(Emoji)
            if (cur_index + 1) % 6 == 0:
                emoji_y_pos += 25
                emoji_x_pos = 490

        # -------------------end of emoji code logic-------------------------------------

        m_frame = tk.Frame(self.scrollable_frame, bg="#d9d5d4")

        t_label = tk.Label(m_frame, bg="#d9d5d4", text=datetime.now().strftime('%H:%M'), font="lucida 9 bold")
        t_label.pack()

        m_label = tk.Label(m_frame, wraplength=250, text=f"Happy Chatting {self.parent.user}",
                           font="lucida 10 bold", bg="orange")
        m_label.pack(fill="x")

        m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")

        self.pack(fill="both", expand=True)

        self.clients_online([])

        t = threading.Thread(target=self.receive_data)
        #t.setDaemon(True)
       
        t.start()
        time.sleep(3)
#**************************Fonctions du menu*****************************

    def videocall():
        pass

#**************************Fin fonctions du menu************************

    def receive_data(self):
        while True:
            try:
                data_type = self.client_socket.recv(2048).decode()

                if data_type == 'notification':
                    data_size = self.client_socket.recv(2048)
                    data_size_int = struct.unpack('i', data_size)[0]

                    b = b''
                    while True:
                        data_bytes = self.client_socket.recv(1024)
                        b += data_bytes
                        if len(b) == data_size_int:
                            break
                    data = pickle.loads(b)
                    self.notification_format(data)

                else:
                    data_bytes = self.client_socket.recv(1024)
                    data = pickle.loads(data_bytes)
                    self.received_message_format(data)

            except ConnectionAbortedError:
                print("you disconnected ...")
                self.client_socket.close()
                break
            except ConnectionResetError:
                messagebox.showinfo(title='No Connection !', message="Server offline..try connecting again later")
                self.client_socket.close()
                self.first_screen()
                break

    def on_closing(self):
        if self.window == 'ChatScreen':
            res = messagebox.askyesno(title='Warning !',message="Do you really want to disconnect ?")
            if res:
                import os
                os.remove(self.all_user_image[self.user_id])
                self.client_socket.close()
                self.first_screen()
        else:
            self.parent.destroy()

    def received_message_format(self, data):

        message = data['message']
        from_ = data['from']

        sender_image = self.clients_connected[from_][1]
        sender_image_extension = self.clients_connected[from_][2]

        # if not os.path.exists(f"{from_}.{sender_image_extension}"):
        with open(f"{from_}.{sender_image_extension}", 'wb') as f:
            f.write(sender_image)

        im = Image.open(f"{from_}.{sender_image_extension}")
        im = im.resize((40, 40), Image.ANTIALIAS)
        im = ImageTk.PhotoImage(im)

        m_frame = tk.Frame(self.scrollable_frame, bg="#595656")

        m_frame.columnconfigure(1, weight=1)

        t_label = tk.Label(m_frame, bg="#595656",fg="white", text=datetime.now().strftime('%H:%M'), font="lucida 7 bold",
                           justify="left", anchor="w")
        t_label.grid(row=0, column=1, padx=2, sticky="w")

        m_label = tk.Label(m_frame, wraplength=250,fg="black", bg="#c5c7c9", text=message, font="lucida 9 bold", justify="left",
                           anchor="w")
        m_label.grid(row=1, column=1, padx=2, pady=2, sticky="w")

        i_label = tk.Label(m_frame, bg="#595656", image=im)
        i_label.image = im
        i_label.grid(row=0, column=0, rowspan=2)

        m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")

        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def sent_message_format(self, event=None):

        message = self.entry.get('1.0', 'end-1c')

        if message:
            if event:
                message = message.strip()
            self.entry.delete("1.0", "end-1c")

            from_ = self.user_id

            data = {'from': from_, 'message': message}
            data_bytes = pickle.dumps(data)

            self.client_socket.send(data_bytes)

            m_frame = tk.Frame(self.scrollable_frame, bg="#595656")

            m_frame.columnconfigure(0, weight=1)

            t_label = tk.Label(m_frame, bg="#595656", fg="white", text=datetime.now().strftime('%H:%M'),
                               font="lucida 7 bold", justify="right", anchor="e")
            t_label.grid(row=0, column=0, padx=2, sticky="e")

            m_label = tk.Label(m_frame, wraplength=250, text=message, fg="black", bg="#40C961",
                               font="lucida 9 bold", justify="left",
                               anchor="e")
            m_label.grid(row=1, column=0, padx=2, pady=2, sticky="e")

            i_label = tk.Label(m_frame, bg="#595656", image=self.user_image)
            i_label.image = self.user_image
            i_label.grid(row=0, column=1, rowspan=2, sticky="e")

            m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")

            self.canvas.update_idletasks()
            self.canvas.yview_moveto(1.0)

    def notification_format(self, data):
        if data['n_type'] == 'joined':

            name = data['name']
            image = data['image_bytes']
            extension = data['extension']
            message = data['message']
            client_id = data['id']
            self.clients_connected[client_id] = (name, image, extension)
            self.clients_online([client_id, name, image, extension])
            # print(self.clients_connected)

        elif data['n_type'] == 'left':
            client_id = data['id']
            message = data['message']
            self.remove_labels(client_id)
            del self.clients_connected[client_id]

        m_frame = tk.Frame(self.scrollable_frame, bg="#595656")

        t_label = tk.Label(m_frame, fg="white", bg="#595656", text=datetime.now().strftime('%H:%M'),
                           font="lucida 9 bold")
        t_label.pack()

        m_label = tk.Label(m_frame, wraplength=250, text=message, font="lucida 10 bold", justify="left", bg="sky blue")
        m_label.pack()

        m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")

        self.canvas.yview_moveto(1.0)
# *******************************Affichage du photo de l'utilisateur********************
    def clients_online(self, new_added):
        if not new_added:
            pass
            for user_id in self.clients_connected:
                name = self.clients_connected[user_id][0]
                image_bytes = self.clients_connected[user_id][1]
                extension = self.clients_connected[user_id][2]

                with open(f"{user_id}.{extension}", 'wb') as f:
                    f.write(image_bytes)

                self.all_user_image[user_id] = f"{user_id}.{extension}"

                user = Image.open(f"{user_id}.{extension}")
                user = user.resize((45, 45), Image.ANTIALIAS)
                user = ImageTk.PhotoImage(user)

                b = tk.Label(self, image=user, text=name, compound="left",fg="white", bg="#2b2b2b", font="lucida 10 bold", padx=15)
                b.image = user
                self.clients_online_labels[user_id] = (b, self.y)

                b.place(x=500, y=self.y)
                self.y += 60


        else:
            user_id = new_added[0]
            name = new_added[1]
            image_bytes = new_added[2]
            extension = new_added[3]

            with open(f"{user_id}.{extension}", 'wb') as f:
                f.write(image_bytes)

            self.all_user_image[user_id] = f"{user_id}.{extension}"

            user = Image.open(f"{user_id}.{extension}")
            user = user.resize((45, 45), Image.ANTIALIAS)
            user = ImageTk.PhotoImage(user)

            b = tk.Label(self, image=user, text=name, compound="left", fg="white", bg="#2b2b2b",
                         font="lucida 10 bold", padx=15)
            b.image = user
            self.clients_online_labels[user_id] = (b, self.y)

            b.place(x=500, y=self.y)
            self.y += 60

    def remove_labels(self, client_id):
        for user_id in self.clients_online_labels.copy():
            b = self.clients_online_labels[user_id][0]
            y_co = self.clients_online_labels[user_id][1]
            if user_id == client_id:
                print("yes")
                b.destroy()
                del self.clients_online_labels[client_id]
                import os
                # os.remove(self.all_user_image[user_id])

            elif user_id > client_id:
                y_co -= 60
                b.place(x=510, y=y_co)
                self.clients_online_labels[user_id] = (b, y_co)
                self.y -= 60

    def insert_emoji(self, x):
        self.entry.insert("end-1c", x.widget['text'])

    def first_screen(self):
        self.destroy()
        self.parent.geometry(f"550x400+{self.parent.x_co}+{self.parent.y_co}")
        self.parent.first_frame.pack(fill="both", expand=True)
        self.window = None



FirstScreen()