import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

menus = {"Pizza": 40.00,"Tacos": 49.00,"Sandwich": 30.00,"Burger": 32.00,"Frites": 15.00,"Nuggets": 35.00,"Soda": 15.00, "Limonade": 18.00}

commande = {}
def ajouter_commande():
    plat = stocker_plat.get().strip().capitalize()
    quantite = int(stocker_quantite.get())
     
    if plat in commande:
        commande[plat] += quantite
    else:
        commande[plat] = quantite
    messagebox.showinfo("Succès", f"{quantite} x {plat} ajouté(s) à la commande.")

    stocker_quantite.set("")  
    stocker_plat.set("")  
    mettre_a_jour_plats_commandes()

def mettre_a_jour_plats_commandes():
    liste_plats_commandes.delete(0, tk.END)
    for plat, quantite in commande.items():
        liste_plats_commandes.insert(tk.END, f"{plat} - {quantite}")
def modifier_commande():    
    selection = liste_plats_commandes.curselection()
    if not selection:
        messagebox.showerror("Erreur", "Veuillez sélectionner un plat à modifier ou supprimer.")
        return
    plat_selectionne = liste_plats_commandes.get(selection).split(" - ")[0] 
    quantite_nouvelle = int(stocker_quantite_modifier.get())
    if quantite_nouvelle == 0: 
        del commande[plat_selectionne]
        messagebox.showinfo("Succès", f"{plat_selectionne} a été supprimé de la commande.")
    else:
        commande[plat_selectionne] = quantite_nouvelle
        messagebox.showinfo("Succès", f"La quantité de {plat_selectionne} a été mise à jour à {quantite_nouvelle}.")
    mettre_a_jour_plats_commandes()
    stocker_quantite_modifier.set("")

def afficher_recu():
    total = 0.0
    recu_window = tk.Toplevel(screen)
    recu_window.title("Reçu")
    tk.Label(recu_window, text="-------------------- Reçu ---------------------", font=("Helvetica", 14)).pack()
    tk.Label(recu_window, text="---- La commande ----", font=("Helvetica", 12)).pack()
    for plat, quantite in commande.items():
        prix = menus[plat] * quantite
        total += prix
        tk.Label(recu_window, text=f'{quantite} x {plat} = {prix:.2f} DH').pack()
    tk.Label(recu_window, text="---------------------------------", font=("Helvetica", 12)).pack()
    tk.Label(recu_window, text=f'Total = {total:.2f} DH', font=("Helvetica", 14)).pack()

screen = tk.Tk()
screen.title("Restaurant - Commande")
screen.geometry("400x1000")
tk.Label(screen, text="--- Menu ---", font=("Helvetica", 16)).pack(pady=10)
for plat, prix in menus.items():
    tk.Label(screen, text=f"{plat} - {prix:.2f} DH", font=("Helvetica", 12)).pack()

plat = list(menus.keys())
tk.Label(screen, text="Sélectionnez un plat:", font=("Helvetica", 12)).pack(pady=5)
stocker_plat = tk.StringVar()
plat_list = ttk.Combobox(width=12, textvariable=stocker_plat, values=plat, font=('Arial', 14))
plat_list.pack()

tk.Label(screen, text="Entrez la quantité:", font=("Helvetica", 12)).pack(pady=5)
stocker_quantite = tk.StringVar()
entrer_la_quantite = tk.Entry(screen, textvariable=stocker_quantite, font=("Helvetica", 12))
entrer_la_quantite.pack()

ajouter_btn = tk.Button(screen, text="Ajouter à la commande", font=("Helvetica", 12), command=ajouter_commande)
ajouter_btn.pack(pady=10)

tk.Label(screen, text="Plats commandés:", font=("Helvetica", 12)).pack(pady=5)
liste_plats_commandes = tk.Listbox(screen, width=40, height=10)
liste_plats_commandes.pack()
tk.Label(screen, text="Nouvelle quantité (0 pour supprimer):", font=("Helvetica", 12)).pack(pady=5)
stocker_quantite_modifier = tk.StringVar()
entrer_quantite_modifier = tk.Entry(screen, textvariable=stocker_quantite_modifier, font=("Helvetica", 12))
entrer_quantite_modifier.pack()

modifier_btn = tk.Button(screen, text="Modifier/Supprimer", font=("Helvetica", 12), command=modifier_commande)
modifier_btn.pack(pady=10)
recu_btn = tk.Button(screen, text="Afficher le reçu", font=("Helvetica", 12), command=afficher_recu)
recu_btn.pack(pady=10)

screen.mainloop()