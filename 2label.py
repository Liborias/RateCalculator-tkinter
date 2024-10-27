from tkinter import *

# nastavení plátna
window = Tk()
window.minsize(500, 500)
window.resizable(False, False)
window.iconbitmap("pictures/icon_ratecalc.ico")
window.title("Přepočet kurzu")
window.config(bg="black")

# štítek
currency = Label(window, text="Eura", font=("Cambria", 20, "bold"), bg="black", fg="white", borderwidth=5, relief="sunken")
currency.pack(ipadx=50)

currecy2 = Label(window, text="CZK", font=("Cambria", 20, "bold"), bg="black", fg="white")
currecy2.pack()

window.mainloop()