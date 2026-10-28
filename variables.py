product1_naam = "Brood"
product2_naam = "Melk"
product3_naam = "Kaas"

product1_prijs = 2.50
product2_prijs = 1.20
product3_prijs = 4.75

product1_aantal = 15
product2_aantal = 28
product3_aantal = 9

omzet_product1 = product1_prijs * product1_aantal
omzet_product2 = product2_prijs * product2_aantal
omzet_product3 = product3_prijs * product3_aantal

totale_omzet = omzet_product1 + omzet_product2 + omzet_product3

print(f"Product: {product1_naam}")
print(f"Prijs: €{product1_prijs:.2f}")
print(f"Aantal verkocht: {product1_aantal}\n")

print(f"Product: {product2_naam}")
print(f"Prijs: €{product2_prijs:.2f}")
print(f"Aantal verkocht: {product2_aantal}\n")

print(f"Product: {product3_naam}")
print(f"Prijs: €{product3_prijs:.2f}")
print(f"Aantal verkocht: {product3_aantal}\n")

print(f"De winkel heeft in totaal €{totale_omzet:.2f} verdiend.")