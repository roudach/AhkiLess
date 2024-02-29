from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter.font as tkFont


f = ('Times', 14)

# con = sqlite3.connect('userdata.db')
# cur = con.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS record(
#                     name text, 
#                     email text, 
#                     contact number, 
#                     gender text, 
#                     country text,
#                     password text
#                 )
#             ''')
# con.commit()

            

ws = Tk()
ws.title('Ahkiless')
ws.geometry('940x500')
ws.config(bg='#E4D6AF')





def insert_record():
    # check_counter=0
    # warn = ""
    # if register_name.get() == "":
    #    warn = "Write your name please"
    # else:
    #     check_counter += 1
        
    # if register_email.get() == "":
    #     warn = "Write your email please"
    # else:
    #     check_counter += 1

    # if register_mobile.get() == "":
    #    warn = "Write your contact please"
    # else:
    #     check_counter += 1
    
    # if  var.get() == "":
    #     warn = "Select Gender"
    # else:
    #     check_counter += 1

    # if variable.get() == "":
    #    warn = "Select Country"
    # else:
    #     check_counter += 1

    # if register_pwd.get() == "":
    #     warn = "Password can't be empty"
    # else:
    #     check_counter += 1

    # if pwd_again.get() == "":
    #     warn = "Re-enter password correctly"
    # else:
    #     check_counter += 1

    # if register_pwd.get() != pwd_again.get():
    #     warn = "Passwords didn't match!"
    # else:
    #     check_counter += 1

    # if check_counter == 8:        
    #     try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :gender, :country, :password)", {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'gender': var.get(),
                            'country': variable.get(),
                            'password': register_pwd.get()

            })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')
            register_name.delete(0, END)
            register_email.delete(0, END)
            register_mobile.delete(0, END)
            register_pwd.delete(0, END)
            pwd_again.delete(0, END)


    #     except Exception as ep:
    #         messagebox.showerror('', ep) 
    # else:
    #     messagebox.showerror('Error', warn)

def login_response():
   
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        c.execute("SELECT * FROM record where name=? AND password=? ", (email_tf.get(),pwd_tf.get()))
        row=c.fetchone()
        if row:
            messagebox.showinfo('info', 'login success')
            email_tf.delete(0, END)
            pwd_tf.delete(0, END)
        else:
            messagebox.showinfo('info','login failed')
            c.connection.commit()
            con.close()


    #         username = row[1]
    #         pwd = row[5]
        
    
    # uname = email_tf.get()
    # upwd = pwd_tf.get()
    # check_counter=0
    # if uname == "":
    #    warn = "Username can't be empty"
    # else:
    #     check_counter += 1
    # if upwd == "":
    #     warn = "Password can't be empty"
    # else:
    #     check_counter += 1
    # if check_counter == 2:
    #     if (uname == username and upwd == pwd):
    #         messagebox.showinfo('Login Status', 'Logged in Successfully!')
        
    #     else:
    #         messagebox.showerror('Login Status', 'invalid username or password')
    # else:
    #     messagebox.showerror('', warn)

    
var = StringVar()
var.set('male')

countries = []
variable = StringVar()
world = open('countries.txt', 'r')
for country in world:
    country = country.rstrip('\n')
    countries.append(country)
variable.set(countries[4])

# widgets
left_frame = Frame(
    ws, 
    bd=2, 
    bg='#B3BDE6',   
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    left_frame, 
    text="Enter Email", 
    fg="#541C1C",
    bg='#B3BDE6',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame, 
    text="Enter Password", 
     fg="#541C1C",
    bg='#B3BDE6',
    font=f
    ).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame, 
    font=f
    )
pwd_tf = Entry(
    left_frame, 
    font=f,
    show='*'
    )
login_btn = Button(
    left_frame, 
    width=15, 
    text='Login', 
    fg="#27143D",
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=login_response
    )

right_frame = Frame(
    ws, 
    bd=2, 
    bg='#B3BDE6',
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    right_frame, 
    text="Enter Name", 
    fg="#541C1C",
    bg='#B3BDE6',
    font=f
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Email", 
    fg="#541C1C",
    bg='#B3BDE6',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Contact Number", 
    fg="#541C1C",
    bg='#B3BDE6',
    font=f
    ).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select Gender", 
    fg="#541C1C",
    bg='#B3BDE6',
    font=f
    ).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select Country",
    fg="#541C1C", 
    bg='#B3BDE6',
    font=f
    ).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Password", 
    fg="#541C1C",
    bg='#B3BDE6',
    font=f
    ).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Re-Enter Password", 
    fg="#541C1C",
    bg='#B3BDE6',
    font=f
    ).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg='#B3BDE6',
    padx=10, 
    pady=10,
    )


register_name = Entry(
    right_frame, 
    font=f
    )

register_email = Entry(
    right_frame, 
    font=f
    )

register_mobile = Entry(
    right_frame, 
    font=f
    )


male_rb = Radiobutton(
    gender_frame, 
    text='Male',
    fg="#541C1C",
    bg='#B3BDE6',
    variable=var,
    value='male',
    font=('Times', 10),
    
)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    fg="#541C1C",
    bg='#B3BDE6',
    variable=var,
    value='female',
    font=('Times', 10),
  
)


   

register_country = OptionMenu(
    right_frame, 
    variable, 
    *countries)

register_country.config(
    width=15, 
    font=('Times', 12)
)
register_pwd = Entry(
    right_frame, 
    font=f,
    show='*'
)
pwd_again = Entry(
    right_frame, 
    font=f,
    show='*'
)

register_btn = Button(
    right_frame, 
    width=15, 
    text='Register', 
     fg="#27143D",
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)


# widgets placement
email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=50, y=50)

register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20) 
register_mobile.grid(row=2, column=1, pady=10, padx=20)
register_country.grid(row=4, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(x=500, y=50)

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
#others_rb.pack(expand=True, side=LEFT)

# infinite loop
ws.mainloop()