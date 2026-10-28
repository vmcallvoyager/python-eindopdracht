monster_health = 150
player_damage = 25
aantal_aanvallen = 0

while monster_health > 0:
    monster_health = max(0, monster_health - player_damage)
    aantal_aanvallen += 1

    print("Monster health:", monster_health)

print("Monster verslagen!")
print("Aantal aanvallen:", aantal_aanvallen)

monsters = [75, 100, 150]

for monster_health in monsters:
    aantal_aanvallen = 0
    print("\nNieuw monster! Health:", monster_health)

    while monster_health > 0:
        monster_health = max(0, monster_health - player_damage)
        aantal_aanvallen += 1

        print("Monster health:", monster_health)

    print("Monster verslagen in", aantal_aanvallen, "aanvallen!")