from sportka import vsad_sportku, dokud_nevyhraju

vsazeno = vsad_sportku()
trvani_sec, leta, cena = dokud_nevyhraju(vsazeno)

print(f"Losování trvalo {trvani_sec} sekund.")
print(f"Na výhru bych čekal {leta} let.")
print(f"Prosázel bych {cena} Kč.")
