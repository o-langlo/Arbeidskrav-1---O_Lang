""" Besvarelse av arbeidskrav 1 - Olav Langlo 

Oppgave: Lag et Python-program som beregner og presenterer (viser) de årlige totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse 

Til tross for at dette ikke er gjennomgått i forelesninger eller spesifisert i oppgaveteksten:
Velger å besvare oppgaven ved bruk av input funksjonen - for å gjøre oppgaven og besvarelsen litt mer interaktiv. 
Jeg prøvde meg også på en "If funksjon avslutningsvis.

Parametere som brukes: 

    Antall kjørte KM: *Input* fra bruker
    Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
    Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
    Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
    Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.
"""
#Input funksjon for å gjøre regnestykket dynamisk basert på angitt bilforbruk 

km_per_aar = float(input("Hvor mange km i året er ditt typiske bilforbruk?"))

#Forsikring kostnad per år for El-bil og Bensin-bil 
el_f = 5000
bensin_f = 7500

#Trafikkforsikringsavgift per år - Dagssats er oppjuster med antall dager for å finne årssats. 
tf_avgift = (8.38 * 365)

#Drivstoff - kostnad per KM (ganger med antatt kjørte KM i året - altså input funksjonen)
d_kost_el = (0.2 * km_per_aar) * 2 
d_kost_bensin = 1 * km_per_aar

#Bomavgift - kostnad per KM (ganger med antatt kjørte KM i året - altså input funksjonen)
b_avgift_el = 0.1 * km_per_aar
b_avgift_bensin = 0.3 * km_per_aar

#Totalkostnad per år basert på angitt kjørelengde - fordelt på elbil og bensinbil 
aars_kost_el = float(el_f + tf_avgift + d_kost_el + b_avgift_el)
aars_kost_bensin = float(bensin_f + tf_avgift + d_kost_bensin + b_avgift_bensin)

#Kostnadsdifferansen 
diff = int(aars_kost_bensin - aars_kost_el)

print("\nHvis du kjører", km_per_aar, "km i året, så koster elbilen totalt", aars_kost_el, "kroner i året, mens bensinbilen totalt koster", aars_kost_bensin, "kr i året")
print("\nDifferansen mellom bensinbil og elbil vil være kr i året", diff, "\n")

if aars_kost_bensin < aars_kost_el:
    print ("\nDu bør kjøpe en bensin bil")
elif aars_kost_bensin > aars_kost_el:
     print("\nDu bør kjøpe en elbil\n")



