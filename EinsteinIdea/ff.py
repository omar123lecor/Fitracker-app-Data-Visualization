import numpy as np
import matplotlib.pyplot as plt
import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
window = customtkinter.CTk()
window.geometry('500x500')
liste1 = []
liste2 = []
fig1 = Figure(figsize=(2.5,2.5),facecolor="#262626")
ax_1 = fig1.add_subplot()
ax_1.set_title('macro nutrition')
ax_1.set_facecolor('#262626')
ax_1.pie(liste2,autopct='%1.1f%%')
canvas = FigureCanvasTkAgg(figure=fig1,master=window)
canvas.draw()
canvas.get_tk_widget().place(x=135,y=200)
print(not isinstance(liste1,list))
window.mainloop()

