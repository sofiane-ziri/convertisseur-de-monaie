import tkinter as tk

conversion_rates = {"USD": {"EUR": 0.8, "CAD": 1.3}, "EUR": {"USD": 1.2, "CAD": 1.6}}

def convert():
    # Récupère les valeurs saisies par l'utilisateur
    amount = float(amount_entry.get())
    from_currency = selected1.get()
    to_currency = selected2.get()

    # Vérifie si la conversion est possible
    if from_currency not in conversion_rates or to_currency not in conversion_rates[from_currency]:
        result_label.config(text="Conversion impossible")
        return

    # Effectue le calcul de conversion
    result = amount * conversion_rates[from_currency][to_currency]

    # Met à jour le label pour afficher le résultat
    result_label.config(text=str(result))

# Initialise la fenêtre principale
root = tk.Tk()
root.title("Convertisseur de devises")

# Crée les widgets pour saisir le montant à convertir
amount_label = tk.Label(root, text="Montant à convertir :")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# Crée les widgets pour sélectionner les devises
from_label = tk.Label(root, text="De :")
from_label.pack()
selected1 = tk.StringVar(root)
selected1.set("USD")
option_menu1 = tk.OptionMenu(root, selected1, *conversion_rates.keys())
option_menu1.pack()

to_label = tk.Label(root, text="Vers :")
to_label.pack()
selected2 = tk.StringVar(root)
selected2.set("EUR")
option_menu2 = tk.OptionMenu(root, selected2, *conversion_rates[selected1.get()].keys())
option_menu2.pack()

# Crée le bouton de conversion
convert_button = tk.Button(root, text="Convertir", command=convert)
convert_button.pack()

# Crée le label pour afficher le résultat
result_label = tk.Label(root, text="")
result_label.pack()

# Lance la boucle d'événements Tkinter
root.mainloop()
