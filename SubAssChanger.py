import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

sub_path = filedialog.askopenfilename(initialdir = "/",title = "Выбрать файл Саба",filetypes = (("Субтитры","*.ass"),("all files","*.*")))
pres_path = filedialog.askopenfilename(initialdir = "/",title = "Выбрать файл пресета",filetypes = (("Lupin Preset File","*.lpf"),("all files","*.*")))



text = open(sub_path,encoding='utf_8_sig')

def presetParsing(pres_path):
    massPres = []
    text = open(pres_path,encoding='utf_8_sig')

    while True:
        line = text.readline()
        massPres.append(line.strip())
        if not line:
            return massPres
            break

def changeWords(text,presets_mass):
    intext = text.read()
    count = len(presets_mass)
    for i in range(count-1):
        preset = presets_mass[i].split(':')
        intext = intext.replace(preset[0],preset[1])
    return intext

presets_mas = presetParsing(pres_path)
change = changeWords(text,presets_mas)


openfile = open("NEW_SUB.ass",'tw',encoding='utf-8')
openfile.write(change)
openfile.close()

