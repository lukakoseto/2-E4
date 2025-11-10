def izracunaj_ukupan_napon(lista_napona):
    
    if len(lista_napona) == 0:
        return 0
    
    
    suma = 0
    for napon in lista_napona:
        suma += napon
    return suma

lista_napona = []

while True:
    print("\n--- ALAT ZA UKUPNI NAPON ---")
    print(f"Trenutno unesenih: {len(lista_napona)} napona")
    print("1. Unesi novi napon (u V)")
    print("2. Izračunaj UKUPNI napon i obriši")
    print("3. Pregledaj sve spremljene napone")
    print("0. Izlaz")
    print("-----------------------------")

    
    try:
        opcija = int(input("Odaberi opciju: "))
    except ValueError:
        print("Pogrešan unos! Unesi broj 0–3.")
        continue

    
    if opcija == 1:
        try:
            vrijednost = float(input("Unesi vrijednost napona (V): "))
            lista_napona.append(vrijednost)
        except ValueError:
            print("Neispravan unos! Unesi brojčanu vrijednost.")

    
    elif opcija == 2:
        ukupan_napon = izracunaj_ukupan_napon(lista_napona)
        print(f"Ukupni napon iznosi: {ukupan_napon} V")
        lista_napona.clear()

    
    elif opcija == 3:
        print(f"Spremljeni naponi (V): {lista_napona}")

   
    elif opcija == 0:
        print("Izlaz iz programa.")
        break

    else:
        print("Nepostojeća opcija! Pokušaj ponovno.")