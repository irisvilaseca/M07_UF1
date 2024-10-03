areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]
print(f"El segon element és: {areas_pis[1]}")
print(f"L'últim element és: {areas_pis[-1]}")
posicioTerrassa=areas_pis.index("Terrassa")
print(f"L'àrea de la terrassa és: {areas_pis[posicioTerrassa+1]}")
print(f"Imprimir del primer al tercer element {areas_pis[0:3]}")
print(f"Imprimir del tercer element a l'últim: {areas_pis[2:]}")
posicioHabitacio1=areas_pis.index("Habitació1")
posicioHabitacio2=areas_pis.index("Habitació1")
area_habitacio1=areas_pis[posicioHabitacio1+1]
area_habitacio2=areas_pis[posicioHabitacio2+1]
area_total=area_habitacio1+area_habitacio2
print(f"L'àrea total de les dues habitacions és: {area_total}")
posicioLavabo=areas_pis.index("Lavabo")
areas_pis[posicioLavabo+1]=9.00
print(areas_pis)
areas_pis.extend(["Pati interior", 2.78])
print(areas_pis)
area_total_pis=0
for element in areas_pis:
    if isinstance(element, (int, float)):
        area_total_pis+=element

print(f"L'àrea total del pis és de {area_total_pis} metres")