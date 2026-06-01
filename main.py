import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Bloc-notes David")
root.geometry("900x650")
root.configure(bg="#FFF9C4")  # jaune clair

current_file = None

# =========================
# Fonctions Fichier
# =========================

def nouveau():
    global current_file
    text.delete("1.0", tk.END)
    current_file = None
    root.title("Bloc-notes David - Nouveau")

def ouvrir():
    global current_file

    file = filedialog.askopenfilename(
        filetypes=[
            ("Fichiers texte", "*.txt"),
            ("Tous les fichiers", "*.*")
        ]
    )

    if file:
        current_file = file

        with open(file, "r", encoding="utf-8") as f:
            contenu = f.read()

        text.delete("1.0", tk.END)
        text.insert(tk.END, contenu)

        root.title("Bloc-notes David - " + file)

def enregistrer():
    global current_file

    if current_file is None:
        enregistrer_sous()
    else:
        contenu = text.get("1.0", tk.END)

        with open(current_file, "w", encoding="utf-8") as f:
            f.write(contenu)

        messagebox.showinfo("Sauvegarde", "Note enregistrée")

def enregistrer_sous():
    global current_file

    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Fichiers texte", "*.txt"),
            ("Tous les fichiers", "*.*")
        ]
    )

    if file:
        current_file = file
        enregistrer()

def quitter():
    confirmation = messagebox.askyesno(
        "Quitter",
        "Voulez-vous vraiment quitter ?"
    )

    if confirmation:
        root.destroy()

# =========================
# Fonctions Copier / Coller
# =========================

def copier():
    try:
        texte_selectionne = text.selection_get()

        root.clipboard_clear()
        root.clipboard_append(texte_selectionne)

    except:
        pass

def couper():
    try:
        texte_selectionne = text.selection_get()

        root.clipboard_clear()
        root.clipboard_append(texte_selectionne)

        text.delete(tk.SEL_FIRST, tk.SEL_LAST)

    except:
        pass

def coller():
    try:
        texte_presse_papier = root.clipboard_get()
        text.insert(tk.INSERT, texte_presse_papier)

    except:
        pass

def tout_selectionner():
    text.tag_add(tk.SEL, "1.0", tk.END)
    text.mark_set(tk.INSERT, "1.0")
    text.see(tk.INSERT)

# =========================
# Barre du haut
# =========================

top = tk.Frame(root, bg="#FFF9C4")
top.pack(fill="x", padx=10, pady=10)

btn_style = {
    "bg": "#BBDEFB",
    "font": ("Arial", 12),
    "padx": 10,
    "pady": 5
}

tk.Button(top, text="Nouveau", command=nouveau, **btn_style).pack(side="left", padx=5)

tk.Button(top, text="Ouvrir", command=ouvrir, **btn_style).pack(side="left", padx=5)

tk.Button(top, text="Enregistrer", command=enregistrer, **btn_style).pack(side="left", padx=5)

tk.Button(top, text="Enregistrer sous", command=enregistrer_sous, **btn_style).pack(side="left", padx=5)

tk.Button(top, text="Copier", command=copier, **btn_style).pack(side="left", padx=5)

tk.Button(top, text="Couper", command=couper, **btn_style).pack(side="left", padx=5)

tk.Button(top, text="Coller", command=coller, **btn_style).pack(side="left", padx=5)

tk.Button(top, text="Tout sélectionner", command=tout_selectionner, **btn_style).pack(side="left", padx=5)

tk.Button(
    top,
    text="Quitter",
    command=quitter,
    bg="#EF9A9A",
    font=("Arial", 12),
    padx=10,
    pady=5
).pack(side="right", padx=5)

# =========================
# Zone texte
# =========================

text = tk.Text(
    root,
    bg="#BBDEFB",
    fg="black",
    font=("Arial", 16),
    wrap="word",
    undo=True
)

text.pack(fill="both", expand=True, padx=10, pady=10)

# =========================
# Raccourcis clavier
# =========================

root.bind("<Control-c>", lambda event: copier())
root.bind("<Control-x>", lambda event: couper())
root.bind("<Control-v>", lambda event: coller())
root.bind("<Control-a>", lambda event: tout_selectionner())

# =========================
# Menu clic droit
# =========================

menu = tk.Menu(root, tearoff=0)

menu.add_command(label="Copier", command=copier)
menu.add_command(label="Couper", command=couper)
menu.add_command(label="Coller", command=coller)

def afficher_menu(event):
    menu.tk_popup(event.x_root, event.y_root)

text.bind("<Button-3>", afficher_menu)

# =========================
# Lancement
# =========================

root.protocol("WM_DELETE_WINDOW", quitter)

root.mainloop()