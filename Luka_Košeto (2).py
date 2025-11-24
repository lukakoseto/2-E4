while True:
  
    print("\n=== KALKULATOR ZA PRETVORBU DIGITALNIH VELIČINA ===")
    print("1. Kilobajti (KB) → Bajti (B)")
    print("2. Megabajti (MB) → Kilobajti (KB)")
    print("3. Gigabajti (GB) → Megabajti (MB)")
    print("0. Izlaz")

    izbor = input("Odaberi opciju: ")

    if izbor == "0":
        print("Hvala na korištenju programa! Doviđenja!")
        break
    
    elif izbor == "1":
        kb = float(input("Unesi veličinu u KB: "))
        b = kb * 1024
        print(f"{kb} KB = {b} B")
    elif izbor == "2":
        mb = float(input("Unesi veličinu u MB: "))
        kb = mb * 1024
        print(f"{mb} MB = {kb} KB")
    elif izbor == "3":
        gb = float(input("Unesi veličinu u GB: "))
        mb = gb * 1024
        print(f"{gb} GB = {mb} MB")
    else:
        print("Greška: Unesena je nepostojeća opcija. Pokušaj ponovno.")
