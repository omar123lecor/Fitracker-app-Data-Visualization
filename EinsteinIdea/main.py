import mysql.connector
import customtkinter
import bcrypt
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image as im
app = customtkinter.CTk()
app.title('Login')
app.geometry('980x560')
app.config(bg='#001220')
app.resizable(False, False)
font1 = ('Helvetica', 40, 'bold')
font2 = ('Arial', 27, 'bold')
font3 = ('Arial', 19, 'bold')
font4 = ('Arial', 19, 'bold', 'underline')
conn = mysql.connector.connect(
	user='root',
	host='localhost',
	database='fittracker',
	passwd='omar123Lecor'
)
cursor = conn.cursor()
cursor.execute('''
    create table if not exists users(
    username varchar(100) primary key,
    password varchar(100) not null)
''')
cursor.execute('''
    create table if not exists usersdata(
    username varchar(100),
    gender varchar(100),
    name varchar(100),
    age int,
    height int,
    weight int,
    activity varchar(100),
    fatGoel int,
    carbsGoel int,
    proteinGol int,
    caloriGoel int,
    weightGoel int,
    constraint user foreign key(username) references users(username))
''')
def logout():
    if messagebox.askyesno('Log out','Sure ! You wanna quit?'):
        frame3.destroy()
        raise1()
    else:
        pass
def openButton():
    global frame4
    pil3 = im.open('images\house-solid.png')
    image17 = customtkinter.CTkImage(pil3)
    pil4 = im.open('images\\utensils-solid.png')
    image18 = customtkinter.CTkImage(pil4)
    pil5 = im.open('images\workout.png')
    image19 = customtkinter.CTkImage(pil5)
    pil6 = im.open('images\calendar-days-solid.png')
    image20 = customtkinter.CTkImage(pil6)
    pil17 = im.open('images\\file-pen-solid.png')
    image21 = customtkinter.CTkImage(pil17)
    pil18 = im.open('images\logout.png')
    image22 = customtkinter.CTkImage(pil18)
    frame4 = customtkinter.CTkFrame(frame3, width=250, height=980, bg_color='#262626', fg_color='#262626')
    frame4.place(x=0, y=0)
    customtkinter.CTkLabel(frame4,text='Menu',font=('Arial', 34, 'italic','bold'),text_color='#748498').place(relx=0.5,y=39,anchor=CENTER)
    Frame(frame4,width=380,height=10,bg='#001220').place(x=0,y=124)
    customtkinter.CTkButton(frame4,text='Home',font= ('Arial', 27, 'bold'),
                            fg_color='#262626',width=250,
                            bg_color='#262626',hover_color='#1a1919',
                            text_color='#195e94',corner_radius=0,image=image17).place(relx=0.5,y=145,anchor=CENTER)
    customtkinter.CTkButton(frame4,text='Food',font= ('Arial', 27, 'bold'),
                            fg_color='#262626',width=250,
                            bg_color='#262626',hover_color='#1a1919',
                            text_color='#195e94',corner_radius=0,image=image18).place(relx=0.5,y=210,anchor=CENTER)
    customtkinter.CTkButton(frame4, text='WorkOut', font=('Arial', 27, 'bold'),
                            fg_color='#262626', width=250,
                            bg_color='#262626', hover_color='#1a1919',
                            text_color='#195e94', corner_radius=0,image=image19).place(relx=0.5, y=275, anchor=CENTER)
    customtkinter.CTkButton(frame4, text='Program', font=('Arial', 27, 'bold'),
                            fg_color='#262626', width=250,
                            bg_color='#262626', hover_color='#1a1919',
                            text_color='#195e94', corner_radius=0, image=image20).place(relx=0.5, y=340, anchor=CENTER)
    customtkinter.CTkButton(frame4, text='Edit', font=('Arial', 27, 'bold'),
                            fg_color='#262626', width=250,
                            bg_color='#262626', hover_color='#1a1919',
                            text_color='#195e94', corner_radius=0, image=image21).place(relx=0.5, y=405, anchor=CENTER)
    customtkinter.CTkButton(frame4, text='Log out', font=('Arial', 27, 'bold'),
                            fg_color='#262626', width=250,
                            bg_color='#262626', hover_color='#1a1919',
                            text_color='#195e94', corner_radius=0, image=image22,
                            command=logout).place(relx=0.5, y=470, anchor=CENTER)
    def closeButton():
        frame4.destroy()
    customtkinter.CTkButton(frame4,text='',bg_color='#262626',fg_color='#262626',
                            hover_color='#262626',command=closeButton,
                            image=image10,width=20).place(x=220,y=0)
#connected
def MyAccount():
    global frame3,image11,image10
    frame2.destroy()
    frame3 = customtkinter.CTkFrame(app,bg_color='#001220',fg_color='#001220',
                                width=980,height=560)
    frame3.place(x=0,y=0)
    pil_image = im.open('images\open.png')
    pil2_image = im.open('images\closee.png')
    image11 = customtkinter.CTkImage(pil_image)
    image10 = customtkinter.CTkImage(pil2_image)
    pil18 = im.open('images\poulet.png')
    image18 = customtkinter.CTkImage(pil18)
    customtkinter.CTkButton(frame3, command=openButton, text='',
                            image=image11, hover_color='#262626',
                            width=20, bg_color='#262626',
                            fg_color='#262626').place(x=0, y=0)
    customtkinter.CTkLabel(frame3,text='MyfitnessTracker',font=font2).place(relx=0.5,y=20,anchor=CENTER)
    frame5 = customtkinter.CTkFrame(frame3, width=170, height=980, bg_color='#262626', fg_color='#262626')
    frame5.place(x=810,y=0)
    customtkinter.CTkLabel(frame5,text='Health-state',text_color='#748498',font=('Comic Sans MS',25,'bold'),
                           bg_color='#262626',fg_color='#262626').place(relx=0.5,y=39,anchor=CENTER)
    Frame(frame5,width=280,height=10,bg='#001220').place(x=0,y=124)
    customtkinter.CTkLabel(frame5,text='Meal',text_color='#ff950a',font=('Comfortaa',24,'bold'),
                           bg_color='#262626',fg_color='#262626').place(relx=0.6,y=120,anchor=CENTER)
    customtkinter.CTkLabel(frame5,image=image18,text='',bg_color='#262626',fg_color='#262626',
                           font=('Comfortaa',24,'bold')).place(relx=0.3,y=120,anchor=CENTER)
    customtkinter.CTkLabel(frame5, text=0, text_color='#fff', font=('Comfortaa', 24, 'bold'),
                           bg_color='#262626', fg_color='#262626').place(relx=0.5, y=155, anchor=CENTER)
    customtkinter.CTkLabel(frame5, text='Excercice', text_color='#ff950a', font=('Comfortaa', 24, 'bold'),
                           bg_color='#262626', fg_color='#262626').place(relx=0.6, y=200, anchor=CENTER)
def check():
    global cursor, conn
    if '' in [var_age.get(), var_weight.get(), var_weightG.get(), var_height.get(),
              var_prot.get(), var_carb.get(), activ_var.get(), var_fat.get(), var_name.get(), var_cal.get(),
              var_x.get()]:
        messagebox.showerror('error', 'complete the form')
    else:
        cursor.execute('insert into usersdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       [username, var_x.get(), var_name.get(), var_age.get(), var_height.get(),
                        var_weight.get(), activ_var.get(), var_fat.get(), var_carb.get(), var_prot.get(),
                        var_cal.get(), var_weightG.get()])
        conn.commit()
        messagebox.showinfo('greate', 'Your info has been saved , wait for the next step')
        app.destroy()


# se connecter
def login_account():
    global cursor, conn, username
    username = username_entry2.get()
    password = password_entry2.get()
    if username != '' and password != '':
        cursor.execute('select password from users where username=%s', (username,))
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0].encode()):
                messagebox.showinfo('Success', 'Logged in successfully.')
                cursor.execute('select username from usersdata where username=%s', (username,))
                if cursor.fetchone() is None:
                    forme()
                else:
                    MyAccount()
            else:
                messagebox.showerror('Error', 'Invalid password.')
        else:
            messagebox.showerror('Error', 'Invalid username.')
    else:
        messagebox.showerror('Error', 'Enter all data.')


def login():
    global frame2
    global cursor, conn
    frame1.destroy()
    frame2 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220',
                                    width=980, height=560)
    frame2.place(x=0, y=0)
    image1 = PhotoImage(file="images\girl.png")
    image1_label = Label(frame2, image=image1, bg='#001220')
    image1_label.place(x=0, y=0)
    frame2.image1 = image1

    global username_entry2
    global password_entry2

    login_label = customtkinter.CTkLabel(frame2, font=font1, text='Log in', text_color='#fff')
    login_label.place(x=620, y=50)

    username_entry2 = customtkinter.CTkEntry(frame2, font=font2, text_color='#fff',
                                             fg_color='#001a2e', border_color='#004780',
                                             border_width=3, placeholder_text='Username',
                                             placeholder_text_color='#a3a3a3',
                                             bg_color='#121111',
                                             width=400, height=50,
                                             corner_radius=18)
    username_entry2.place(x=500, y=150)
    password_entry2 = customtkinter.CTkEntry(frame2, font=font2, text_color='#fff',
                                             fg_color='#001a2e', bg_color='#121111', border_color='#004780',
                                             border_width=3, placeholder_text='Password',
                                             placeholder_text_color='#a3a3a3',
                                             width=400, height=50, show='*',
                                             corner_radius=18)
    password_entry2.place(x=500, y=250)
    login_button = customtkinter.CTkButton(frame2, font=font2, text_color='#fff', text='Log in',
                                           fg_color='#00965d', hover_color='#006e44',
                                           bg_color='#121111', cursor='hand2',
                                           corner_radius=10, width=220, command=login_account)
    login_button.place(x=585, y=350)
    sign_button = customtkinter.CTkButton(frame2, font=font4, text_color='#00bf77',
                                          text='Sign up', fg_color='#001220',
                                          hover_color='#001220', cursor='hand2',
                                          width=40, command=raise1)
    sign_button.place(x=765, y=420)
    signup_label = customtkinter.CTkLabel(frame2, font=font3,
                                          text="Don't have an account?",
                                          text_color='#fff', bg_color='#001220')
    signup_label.place(x=550, y=420)


# s'inscrire
def signup():
    global cursor, conn
    username = username_entry.get()
    password = password_entry.get()
    if username != '' and password != '':
        cursor.execute('select username from users where username=%s', [username])
        if cursor.fetchone() is not None:
            messagebox.showerror('error', 'Username already exists')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            cursor.execute('insert into users values(%s,%s)', (username, hashed_password))
            conn.commit()
            messagebox.showinfo('Success', 'Account has been created.')
    else:
        messagebox.showerror('error', 'enter all data. ')


#frame1 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220',
                              #  width=980, height=560)
# frame1.place(x=0,y=0)
image1 = PhotoImage(file="images\man.png")
imag1 = im.open('images\open.png')
# image1_label = Label(frame1,image=image1,bg='#001220')
# image1_label.place(x=0,y=0)
'''signup_label = customtkinter.CTkLabel(frame1,font=font1,text='Sign up',text_color='#fff')
signup_label.place(x=620,y=50)


signup_button = customtkinter.CTkButton(frame1,font=font2,text_color='#fff',text='Sign up',
                                        fg_color='#00965d',hover_color='#006e44',
                                        bg_color='#121111',cursor='hand2',
                                        corner_radius=10,width=220,command=signup)
signup_button.place(x=585,y=350)

login_label = customtkinter.CTkLabel(frame1,font=font3,
                                     text='Already have an account?',
                                     text_color='#fff',bg_color='#001220')
login_label.place(x=550,y=420)

login_button = customtkinter.CTkButton(frame1,font=font4,text_color='#00bf77',
                                       text='Login',fg_color='#001220',
                                       hover_color='#001220',cursor='hand2',
                                       width=40,command=login)
login_button.place(x=783,y=420)'''
'''username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fff',
                                        fg_color='#001a2e',
                                        border_width=3, placeholder_text='Username',
                                        placeholder_text_color='#a3a3a3',
                                        bg_color='#001220',
                                        width=400, height=50,
                                        corner_radius=18)
# username_entry.place(x=500,y=150)
password_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fff',
                                        fg_color='#001a2e', bg_color='#121111',
                                        border_width=3, placeholder_text='Password',
                                        placeholder_text_color='#a3a3a3',
                                        width=400, height=50, show='*',
                                        corner_radius=18)'''


# password_entry.place(x=500,y=250)
def raise1():
    global image1, password_entry, username_entry, frame1
    frame1 = customtkinter.CTkFrame(app, bg_color='#001220', fg_color='#001220',
                                    width=980, height=560)
    frame1.place(x=0, y=0)
    # image1 = PhotoImage(file="images\girl.png")
    image1_label = Label(frame1, image=image1, bg='#001220')
    image1_label.place(x=0, y=0)
    signup_label = customtkinter.CTkLabel(frame1, font=font1, text='Sign up', text_color='#fff')
    signup_label.place(x=620, y=50)
    username_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fff',
                                            fg_color='#001a2e',
                                            border_width=3, placeholder_text='Username',
                                            placeholder_text_color='#a3a3a3',
                                            bg_color='#001220',
                                            width=400, height=50,
                                            corner_radius=18)
    username_entry.place(x=500, y=150)
    password_entry = customtkinter.CTkEntry(frame1, font=font2, text_color='#fff',
                                            fg_color='#001a2e', bg_color='#121111',
                                            border_width=3, placeholder_text='Password',
                                            placeholder_text_color='#a3a3a3',
                                            width=400, height=50, show='*',
                                            corner_radius=18)
    password_entry.place(x=500, y=250)
    signup_button = customtkinter.CTkButton(frame1, font=font2, text_color='#fff', text='Sign up',
                                            fg_color='#00965d', hover_color='#006e44',
                                            bg_color='#121111', cursor='hand2',
                                            corner_radius=10, width=220, command=signup)
    signup_button.place(x=585, y=350)

    login_label = customtkinter.CTkLabel(frame1, font=font3,
                                         text='Already have an account?',
                                         text_color='#fff', bg_color='#001220')
    login_label.place(x=550, y=420)

    login_button = customtkinter.CTkButton(frame1, font=font4, text_color='#00bf77',
                                           text='Login', fg_color='#001220',
                                           hover_color='#001220', cursor='hand2',
                                           width=40, command=login)
    login_button.place(x=783, y=420)


# raise1()
def forme():
    global cursor, conn
    app.title("You're new , please complete the form")
    frame1.destroy()
    global img1, var_weight, var_age, var_name, var_cal, var_prot, var_carb, var_fat, var_weightG, var_x, activ_var, var_height
    img1 = PhotoImage(file="images\pattern.png")
    Label(app, image=img1).pack()
    frame2 = customtkinter.CTkFrame(app, corner_radius=15,
                                    fg_color="#2e435c",
                                    border_width=2,
                                    bg_color="#11202b",
                                    width=420, height=510,
                                    )
    frame2.place(relx=0.5, rely=0.5, anchor=CENTER)

    customtkinter.CTkLabel(frame2, text_color="#ffffff", text_color_disabled="#c8d0de",
                           text="Hi , Welcome to Fit Tracker App", font=("SF Display", 17, "bold")).place(relx=0.5,
                                                                                                          y=20,
                                                                                                          anchor=CENTER)
    '''customtkinter.CTkLabel(frame1,text_color="yellow",text="Name :",font=('Arial',14,'bold')).place(x=24,y=74)
    customtkinter.CTkEntry(frame1,text_color="#ffffff",placeholder_text='Name',
                           font=('Arial',14,'normal'),border_width=3,bg_color='#2e435c',
                           fg_color='#2e435c',
                           corner_radius=13,
                           border_color="#001220",width=70
                           ).place(x=20,y=103)
    customtkinter.CTkLabel(frame1,text_color="yellow",text="Age :",font=('Arial',14,'bold')).place(x=230,y=74)
    customtkinter.CTkEntry(frame1,text_color="#ffffff",placeholder_text='Age',width=60,
                           font=('Arial',14,'normal'),border_width=3,bg_color='#2e435c',
                           fg_color='#2e435c',
                           corner_radius=13,
                           border_color="#001220"
                           ).place(x=230,y=103)'''
    var_x = StringVar()
    customtkinter.CTkLabel(frame2, text_color="yellow", text="Gender :", font=('Arial', 16, 'bold')).place(x=24,
                                                                                                           y=74)
    customtkinter.CTkRadioButton(frame2, variable=var_x, text='Male', value='male').place(x=24, y=109)
    customtkinter.CTkRadioButton(frame2, variable=var_x, text='Female', value='female').place(x=24, y=139)
    customtkinter.CTkLabel(frame2, text_color="yellow", text="Name :", font=('Arial', 16, 'bold')).place(x=140,
                                                                                                         y=74)
    var_name = customtkinter.CTkEntry(frame2, text_color="#ffffff", placeholder_text='Myname', width=100,
                                      font=('Arial', 14, 'normal'), border_width=3, bg_color='#2e435c',
                                      fg_color='#2e435c',
                                      corner_radius=13,
                                      border_color="#001220"
                                      )
    var_name.place(x=140, y=110)
    customtkinter.CTkLabel(frame2, text_color="yellow", text="Age :", font=('Arial', 16, 'bold')).place(x=280, y=74)
    var_age = customtkinter.CTkEntry(frame2, text_color="#ffffff", placeholder_text='Myage', width=80,
                                     font=('Arial', 14, 'normal'), border_width=3, bg_color='#2e435c',
                                     fg_color='#2e435c',
                                     corner_radius=13,
                                     border_color="#001220"
                                     )
    var_age.place(x=280, y=110)
    customtkinter.CTkLabel(frame2, text_color="yellow", text="Height :", font=('Arial', 16, 'bold')).place(x=24,
                                                                                                           y=185)
    var_height = customtkinter.CTkEntry(frame2, text_color="#ffffff", placeholder_text='Cm', width=80,
                                        font=('Arial', 14, 'normal'), border_width=3, bg_color='#2e435c',
                                        fg_color='#2e435c',
                                        corner_radius=13,
                                        border_color="#001220"
                                        )
    var_height.place(x=24, y=221)
    customtkinter.CTkLabel(frame2, text_color="yellow", text="Activity level :", font=('Arial', 16, 'bold')).place(
        x=250, y=185)
    Activity = ['Sedentary', 'Lightly active', 'Moderately', 'Very active', 'Extremely']
    activ_var = StringVar()
    customtkinter.CTkComboBox(frame2, values=Activity, bg_color='#2e435c', variable=activ_var,
                              border_width=3,
                              corner_radius=10,
                              border_color="#001220",
                              fg_color='#2e435c',
                              font=('Arial', 14, 'bold')
                              ).place(x=250, y=221)
    customtkinter.CTkLabel(frame2, text_color="yellow", text="Weight :", font=('Arial', 16, 'bold')).place(x=140,
                                                                                                           y=185)
    var_weight = customtkinter.CTkEntry(frame2, text_color="#ffffff", placeholder_text='Kg', width=80,
                                        font=('Arial', 14, 'normal'), border_width=3, bg_color='#2e435c',
                                        fg_color='#2e435c',
                                        corner_radius=13,
                                        border_color="#001220"
                                        )
    var_weight.place(x=140, y=221)
    customtkinter.CTkLabel(frame2, text_color="yellow", text="Fat goal :", font=('Arial', 16, 'bold')).place(x=24,
                                                                                                             y=276)
    var_fat = customtkinter.CTkEntry(frame2, text_color="#ffffff", placeholder_text='grams', width=80,
                                     font=('Arial', 14, 'normal'), border_width=3, bg_color='#2e435c',
                                     fg_color='#2e435c',
                                     corner_radius=13,
                                     border_color="#001220"
                                     )
    var_fat.place(x=24, y=311)
    customtkinter.CTkLabel(frame2, text_color="yellow", text="Carbs goal :", font=('Arial', 16, 'bold')).place(
        x=140, y=276)
    var_carb = customtkinter.CTkEntry(frame2, text_color="#ffffff", placeholder_text='grams', width=80,
                                      font=('Arial', 14, 'normal'), border_width=3, bg_color='#2e435c',
                                      fg_color='#2e435c',
                                      corner_radius=13,
                                      border_color="#001220"
                                      )
    var_carb.place(x=140, y=311)
    customtkinter.CTkLabel(frame2, text_color="yellow", text="Protein goal :", font=('Arial', 16, 'bold')).place(
        x=256, y=276)
    var_prot = customtkinter.CTkEntry(frame2, text_color="#ffffff", placeholder_text='grams', width=80,
                                      font=('Arial', 14, 'normal'), border_width=3, bg_color='#2e435c',
                                      fg_color='#2e435c',
                                      corner_radius=13,
                                      border_color="#001220"
                                      )
    var_prot.place(x=256, y=311)
    customtkinter.CTkLabel(frame2, text_color="yellow", text="Calories goal :", font=('Arial', 16, 'bold')).place(
        x=24, y=367)
    var_cal = customtkinter.CTkEntry(frame2, text_color="#ffffff", placeholder_text='Kcal', width=80,
                                     font=('Arial', 14, 'normal'), border_width=3, bg_color='#2e435c',
                                     fg_color='#2e435c',
                                     corner_radius=13,
                                     border_color="#001220"
                                     )
    var_cal.place(x=24, y=403)

    customtkinter.CTkLabel(frame2, text_color="yellow", text="Weight goal :", font=('Arial', 16, 'bold')).place(
        x=184, y=367)
    var_weightG = customtkinter.CTkEntry(frame2, text_color="#ffffff", placeholder_text='grams', width=80,
                                         font=('Arial', 14, 'normal'), border_width=3, bg_color='#2e435c',
                                         fg_color='#2e435c',
                                         corner_radius=13,
                                         border_color="#001220"
                                         )
    var_weightG.place(x=184, y=403)
    submit_label = customtkinter.CTkButton(frame2, font=('Arial', 15, 'normal'), text='Submit', text_color='#fff',
                                           command=check)
    submit_label.place(relx=0.5, y=480, anchor=CENTER)





raise1()
app.mainloop()
conn.close()
