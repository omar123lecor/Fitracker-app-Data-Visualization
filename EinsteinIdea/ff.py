import numpy as np
import matplotlib.pyplot as plt
import customtkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
window = customtkinter.CTk()
window.geometry('500x500')
liste1 = ['C++','Java','Python','C#']
liste2 = [40,12,58,63]
fig1 = Figure(figsize=(2.5,2.5),facecolor="#917FB3")
ax_1 = fig1.add_subplot()
ax_1.set_facecolor('#917FB3')
ax_1.bar(liste1,liste2)
canvas = FigureCanvasTkAgg(figure=fig1,master=window)
canvas.draw()
canvas.get_tk_widget().place(x=35,y=200)
window.mainloop()

