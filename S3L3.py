def calcPerim():
	print("Calcolo del perimetro di figure geometriche.")
	print("1 * Triangolo isoscele")
	print("2 * Ottagono")
	print("3 * Rettangolo")
	scelta = int(input("Scegli da 1 a 3: "))
	
	if scelta == 1:
		print("Calcolo del triangolo isoscele.")
		print("Il triangolo isoscele e' una forma geometrica triangolare che possiede due lati uguali e uno diverso, che chiameremo base.")
		base = float(input("Inserisci la base: "))
		lati = float(input("Inserisci i lati uguali: "))
		print("Il perimetro della figura e'", 2 * lati + base, "cm.")
		
	elif scelta == 2:
		print("Calcolo dell'ottagono.")
		print("L'ottagono e' una forma geometrica che possiede otto lati e angoli uguali.")
		lato = float(input("Inserisci il lato: "))
		print("Il perimetro della figura e'", 8 * lato, "cm.")
		
	elif scelta == 3:
		print("Calcolo del rettangolo.")
		print("Il rettangolo e' una forma geometrica a quattro lati, uguali a coppie, che chiameremo base e altezza")
		base = float(input("Inserisci la base: "))
		altz = float(input("Inserisci l'altezza: "))
		print("Il perimetro della figura e'", base * 2 + altz * 2, "cm.")
		
	else:
		print("Input Errato / Fai una scelta da 1 a 3.")
	
calcPerim();
