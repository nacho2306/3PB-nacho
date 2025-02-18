import tkinter as tk 
from tkcalendar import Calendar

def fecha_seleccionada():
    selected_date.config(text="fecha seleccionada "+ cal.get_date())
    
root=tk.Tk()
root.title("app calendario")
root.geometry("400x400")


cal = Calendar(root,selctmode="day", date_pattern="yyyy-mm-dd")
cal.pack(pady=20)

selected_date= tk.Label(root, text="")
selected_date.pack(pady=10)

cal.bind("<<calendarSelected>>",lambda event: fecha_seleccionada())

root.mainloop()
