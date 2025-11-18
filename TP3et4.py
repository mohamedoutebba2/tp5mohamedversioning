# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 19:53:24 2025

@author: moham
"""

import tkinter as tk
from tkinter import ttk
import numpy as np

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

def calcul_moyenne(coefs, notes):
    return np.average(list(notes.values()), weights=list(coefs.values()))

fenetre = tk.Tk()
fenetre.title("Calcul de ma Moyenne")
fenetre.geometry("600x700")

frm = ttk.Frame(fenetre)
frm.pack(pady=20)

matieres = list(coef_ue1.keys())
zones = [] 

for i, matiere in enumerate(matieres):
    ttk.Label(frm, text=matiere).grid(row=i, column=0, padx=5, pady=3)
    entry = ttk.Entry(frm, width=5)
    entry.grid(row=i, column=1, padx=5, pady=3)
    zones.append(entry) 

def calculer():
    notes = {}
    for i, matiere in enumerate(matieres):
        try:
            note = float(zones[i].get())
        except ValueError:
            note = 0
        notes[matiere] = note

    moy1 = calcul_moyenne(coef_ue1, notes)
    moy2 = calcul_moyenne(coef_ue2, notes)
    moy3 = calcul_moyenne(coef_ue3, notes)

    resultat.config(text="UE1 : " + str(round(moy1, 2)) + " UE2 : " + str(round(moy2, 2)) + " UE3 : " + str(round(moy3, 2)))


ttk.Button(fenetre, text="Calculer Moyennes", command=calculer).pack(pady=10)

resultat = ttk.Label(fenetre, text="Les moyennes seront la.")
resultat.pack(pady=10)

fenetre.mainloop()