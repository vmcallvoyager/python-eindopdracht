product_namen = ["Brood", "Melk", "Kaas", "Kip", "Sap"]

product_namen.append("Yoghurt")
product_namen.append("Oude kaas")
product_namen.remove("Melk")

# print aantal en volledige lijst
print("Aantal producten in de lijst:", len(product_namen))
print("Boodschappenlijst:", product_namen)

# bonus controleren of een product in de lijst staat
if "Kaas" in product_namen:
    print("Kaas staat in de lijst")
else:
    print("Kaas staat niet in de lijst")