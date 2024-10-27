import tkinter
from idlelib.colorizer import color_config

# Okno
window = tkinter.Tk()
window.title("moje první okno")
# window.minsize(width=500, height=400)
window.geometry("500x600+450+300")# určuje rozměry a zároveň koordináty
window.resizable(False, False)
window.iconbitmap("pictures/icon_ratecalc.ico")
window.config(bg="#072a00")

window2 = tkinter.Tk()
window2.title("druhé okno")
# window2.minsize(300, 350)
window2.geometry("300x400+1000+300")# určuje rozměry a zároveň koordináty
window.resizable(False, False)
window2.iconbitmap("pictures/icon_ratecalc.ico")
window2.config(bg="darkred")

# label (popisek)
welcome_label = tkinter.Label(window2, text="Vítej", bg="#072a00", fg="white", font=("Helvetica", 24, "bold"))
welcome_label.pack(side="top") # můžu do závorky zadat kromě side="top" klidně i další parametry , expand=True



# hlavní cyklus
window.mainloop()