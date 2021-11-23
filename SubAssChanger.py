import tkinter as tk
import re
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

sub_path = filedialog.askopenfilename(initialdir = "/",title = "Выбрать файл Саба",filetypes = (("Субтитры","*.ass"),("all files","*.*")))
pres_path = filedialog.askopenfilename(initialdir = "/",title = "Выбрать файл пресета",filetypes = (("Lupin Preset File","*.lpf"),("all files","*.*")))



text = open(sub_path,encoding='UTF-8')

def presetParsing(pres_path):
    massPres = []
    text = open(pres_path,encoding='UTF-8')

    while True:
        line = text.readline()
        massPres.append(line.strip())
        if not line:
            return massPres
            break

def changeWords(text,presets_mass):
    intext = text.read()
    count = len(presets_mass)
    insensitive_hippo = ""
    for i in range(count-1):

        preset = presets_mass[i].split(':')
        insensitive_hippo = re.compile(re.escape(preset[0]), re.IGNORECASE)
        intext = insensitive_hippo.sub(preset[1],intext)
    return intext

presets_mas = presetParsing(pres_path)
change = changeWords(text,presets_mas)


openfile = open("NEW_SUB.ass",'tw',encoding='UTF-8')
openfile.write(change)
openfile.close()

