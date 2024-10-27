import tkinter

# Okno
window = tkinter.Tk()
window.title("moje první okno")
window.minsize(width=500, height=400)
window.resizable(False, False)
window.iconbitmap("pictures/icon_ratecalc.ico")
window.config(bg="#072a00")

# hlavní cyklus
window.mainloop()