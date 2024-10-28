from  tkinter import  *

# plátno
canvas = Tk()
canvas.title("Převod měn z CZK na EUR")
canvas.minsize(250, 200)
canvas.resizable(False, False)
canvas.config(bg="#072a00")
canvas.iconbitmap("icon.ico")

# kurz v eurech
kurz = 25.36

# funkce pro výpočet
def count_course():
    czk = float(input_amount.get())
    label_result["text"] = round(czk / kurz, 2)
    input_amount.delete(0, END)

# vstup
input_amount = Entry(width=10, font=("Helvetica", 15))
input_amount.grid(row=0, column=0, padx=10, pady=10)

#štítky
label_CZK = Label(text="CZK", font=("Helvetica", 15))
label_CZK.grid(row=0, column=1)
label_CZK.config(bg="#072a00", fg="white")

label_result = Label(text="0", font=("Helvetica", 15))
label_result.grid(row=1, column=0)
label_result.config(bg="#072a00", fg="white")

label_EUR = Label(text="EUR", font=("Helvetica", 15))
label_EUR.grid(row=1, column=1)
label_EUR.config(bg="#072a00", fg="white")

# tlačítko
count_result = Button(text="Převést", font=("Helvetica", 15), command=count_course)
count_result.grid(row=0, column=2, padx=10, pady=10)

# hlavní cyklus
canvas.mainloop()