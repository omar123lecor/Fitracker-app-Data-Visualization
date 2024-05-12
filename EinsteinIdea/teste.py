import customtkinter
window = customtkinter.CTk()
window.geometry('400x500')
def info():
    global x
    x = customtkinter.CTkEntry(window, width=40)
    x.place(x=50,y=50)
def myfunc():
    customtkinter.CTkLabel(window,text=f"{x.get()}").place(x=100,y=100)

info()
myfunc()
customtkinter.CTkButton(window,text='submit',command=myfunc).place(x=200,y=200)
window.mainloop()