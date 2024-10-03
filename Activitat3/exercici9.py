#Versió amb dues llistes
assignatures=["Català","Castellà", "Anglès", "Matemàtiques","Biologia","Història"]
notes=[]
for assignatura in assignatures:
    print(f"Quina nota has tret a {assignatura}")
    nota=float(input())
    notes.append(nota)
for i in range(len(assignatures)):
    print(f"A l'assignatura {assignatures[i]} has tret un {notes[i]}")

#Versió amb un diccionari
diccionariNotes={
    "Català":0,
    "Castellà":0,
    "Anglès":0,
    "Matemàtiques":0,
    "Biologia":0,
    "Història":0
}
for assignatura in diccionariNotes:
    print(f"Quina nota has tret a {assignatura}")
    diccionariNotes[assignatura]=float(input())

for assignatura,nota in diccionariNotes.items:
    print(f"A l'assignatura {assignatura} ha tret un {nota}")