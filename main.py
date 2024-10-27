# Naimportujte tkinter
# Vytvořte jedno okno o rozměru 500 na 500 a nastavte hlavní cyklus
# Do okna přidejte ikonku s názvem icon.ico.
# Nastavte popisek okna "Přepočet kurzu"

# Vytvořte label s textem "Eura" a názvem currency, jeho font nastavte na Cambria, 20 pixelů, tučný (bold)
# Barvu pozadí celého okna! nastavte na černou
# Barvu pozadí labelu nastavte na černou
# Barvu textu labelu nastavte na bílou (fg)

import tkinter
# nastavení plátna
window = tkinter.Tk()
window.minsize(500, 500)
window.resizable(False, False)
window.iconbitmap("pictures/icon_ratecalc.ico")
window.title("Přepočet kurzu")
window.config(bg="black")

# Label
currency = tkinter.Label(text="Eura", font=("Cambria", 20, "bold"), bg="black", fg="white")
currency.pack()

window.mainloop()