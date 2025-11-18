# -*- coding: utf-8 -*-
"""
TP5 - Projet unifié (Évolution des TP1, TP2, TP3, TP4)
"""

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def calcul_moyenne(coefficients, notes):
    """Calcule la moyenne pondérée (TP1)"""
    coefficients = np.array(list(coefficients.values()))
    notes = np.array(list(notes.values()))
    moyenne = np.average(notes, weights=coefficients)
    return moyenne


coef_ue1 = {
    'R101':10,'R102':10,'R103':7,'R104':7,'R105':0,'R106':5,'R107':0,'R108':6,'R109':0,
    'R110':5,'R111':4,'R112':2,'R113':5,'R114':5,'R115':0,'SAE11':20,'SAE12':20,'SAE13':0,
    'SAE14':0,'SAE15':0,'SAE16':7,
}

coef_ue2 = {
    'R101':4,'R102':0,'R103':2,'R104':8,'R105':6,'R106':0,'R107':0,'R108':0,'R109':0,
    'R110':5,'R111':5,'R112':2,'R113':9,'R114':9,'R115':3,'SAE11':0,'SAE12':0,'SAE13':29,
    'SAE14':0,'SAE15':0,'SAE16':7,
}

coef_ue3 = {
    'R101':4,'R102':0,'R103':2,'R104':0,'R105':0,'R106':5,'R107':15,'R108':6,'R109':4,
    'R110':5,'R111':5,'R112':2,'R113':0,'R114':0,'R115':3,'SAE11':0,'SAE12':0,'SAE13':0,
    'SAE14':20,'SAE15':20,'SAE16':7,
}


note_ue1 = {
    'R101':12,'R102':12,'R103':12,'R104':4,'R105':0,'R106':14,'R107':0,'R108':9,'R109':0,
    'R110':12,'R111':9,'R112':12,'R113':7,'R114':12,'R115':0,'SAE11':1,'SAE12':1,'SAE13':0,
    'SAE14':0,'SAE15':0,'SAE16':13,
}

note_ue2 = {
    'R101':12,'R102':0,'R103':12,'R104':4,'R105':6,'R106':0,'R107':0,'R108':0,'R109':0,
    'R110':12,'R111':9,'R112':12,'R113':7,'R114':12,'R115':13,'SAE11':0,'SAE12':0,'SAE13':8,
    'SAE14':0,'SAE15':0,'SAE16':13,
}

note_ue3 = {
    'R101':12,'R102':0,'R103':12,'R104':0,'R105':0,'R106':9,'R107':9,'R108':9,'R109':13.9,
    'R110':12,'R111':9,'R112':12,'R113':0,'R114':0,'R115':13,'SAE11':0,'SAE12':0,'SAE13':0,
    'SAE14':12,'SAE15':14,'SAE16':13,
}

def calculer_moyennes_ues():
    """Calcule et affiche les moyennes des trois UE (TP1)"""
    moyenne_ue1 = calcul_moyenne(coef_ue1, note_ue1)
    moyenne_ue2 = calcul_moyenne(coef_ue2, note_ue2)
    moyenne_ue3 = calcul_moyenne(coef_ue3, note_ue3)

    print('Moyenne pondérée de UE 1 :', round(moyenne_ue1, 2))
    print('Moyenne pondérée de UE 2 :', round(moyenne_ue2, 2))
    print('Moyenne pondérée de UE 3 :', round(moyenne_ue3, 2))
    
    return moyenne_ue1, moyenne_ue2, moyenne_ue3


def f(x):
    """Fonction ln(x) - 1 (TP2)"""
    return np.log(x) - 1

def f_prime(x):
    """Dérivée de la fonction f(x) (TP2)"""
    return 1/x

def tracer_fonction():
    """Trace le graphique de la fonction f(x) = ln(x) - 1 (TP2)"""
    x = np.arange(1, 6.01, 0.05)
    y = f(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="f(x) = ln(x) - 1")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Représentation de f(x) - TP2")
    plt.grid()
    plt.axhline(0, color="red", linestyle="--")
    plt.legend()
    plt.show()

def methode_dichotomie(a=1, b=6, precision=1e-6):
    """
    Résout f(x)=0 par la méthode de dichotomie (TP2)
    """
    print(f"Résolution par dichotomie sur l'intervalle [{a}, {b}]")
    
    iterations = 0
    while abs(b - a) >= precision:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
        iterations += 1
        print(f"Itération {iterations}: a={a:.6f}, c={c:.6f}, b={b:.6f}")
    
    solution = (a + b) / 2
    print(f"Solution trouvée: x = {solution:.6f}")
    return solution


class ApplicationMoyennes(tk.Tk):
    """Interface graphique pour le calcul des moyennes (TP3/TP4)"""
    
    def __init__(self):
        super().__init__()
        self.title("Calcul de mes Moyennes - TP3/TP4")
        self.geometry("600x700")
        
        self.coef_ue1 = coef_ue1
        self.coef_ue2 = coef_ue2
        self.coef_ue3 = coef_ue3
        self.matieres = list(coef_ue1.keys())
        self.zones_notes = []
        
        self.creer_interface()
    
    def creer_interface(self):
        """Crée l'interface graphique (TP3/TP4)"""
        frm = ttk.Frame(self)
        frm.pack(pady=20)
        
        ttk.Label(frm, text="Saisissez vos notes", font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(frm, text="Matière", font=('Arial', 10, 'bold')).grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(frm, text="Note", font=('Arial', 10, 'bold')).grid(row=1, column=1, padx=5, pady=5)
        
        for i, matiere in enumerate(self.matieres):
            ttk.Label(frm, text=matiere).grid(row=i+2, column=0, padx=5, pady=3)
            entry = ttk.Entry(frm, width=5)
            entry.grid(row=i+2, column=1, padx=5, pady=3)
            if matiere in note_ue1 and note_ue1[matiere] > 0:
                entry.insert(0, str(note_ue1[matiere]))
            self.zones_notes.append(entry)
        
        ttk.Button(self, text="Calculer Moyennes", command=self.calculer).pack(pady=10)
        
        self.resultat = ttk.Label(self, text="Les moyennes apparaîtront ici", font=('Arial', 11))
        self.resultat.pack(pady=10)
        
        ttk.Button(self, text="Quitter", command=self.quit).pack(pady=5)
    
    def calculer(self):
        """Calcule les moyennes à partir des notes saisies (TP3/TP4)"""
        notes = {}
        for i, matiere in enumerate(self.matieres):
            try:
                note = float(self.zones_notes[i].get())
            except ValueError:
                note = 0.0
            notes[matiere] = note
        
        moy1 = calcul_moyenne(self.coef_ue1, notes)
        moy2 = calcul_moyenne(self.coef_ue2, notes)
        moy3 = calcul_moyenne(self.coef_ue3, notes)
        
        resultat_text = f"UE1: {moy1:.2f} | UE2: {moy2:.2f} | UE3: {moy3:.2f}"
        self.resultat.config(text=resultat_text)


def main():
    """Fonction principale du TP5 unifié"""
    print("=" * 50)
    print("TP5 - PROJET UNIFIÉ (Évolution TP1→TP5)")
    print("=" * 50)
    
    while True:
        print("\nMenu principal TP5:")
        print("1. Calculer les moyennes des UE (TP1)")
        print("2. Tracer la fonction f(x) = ln(x)-1 (TP2)")
        print("3. Résoudre f(x)=0 par dichotomie (TP2)")
        print("4. Interface graphique des moyennes (TP3/TP4)")
        print("5. Quitter")
        
        choix = input("\nVotre choix (1-5): ").strip()
        
        if choix == "1":
            print("\n--- Calcul des moyennes des UE (TP1) ---")
            calculer_moyennes_ues()
        
        elif choix == "2":
            print("\n--- Trac