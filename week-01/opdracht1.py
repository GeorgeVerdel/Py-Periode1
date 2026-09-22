# Oefening 1
# Print de volgende zin "Hello World"

print("Hello World!")


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "George"
leeftijd = 17
woonstad = "Oudewater"


# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")

print(f"Hallo mijn naam is {naam}, ik ben {leeftijd} jaar oud en ik woon in {woonstad}.")


# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"

favgame = "Warzone"
playtime = 400
rating = 8

print(f"Mijn favorieten game is {favgame}, ik heb {playtime} uur playtime en ik geef het een {rating}/10.")

# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit

nummer1 = 43
nummer2 = 91

antwoord1 = nummer1 + nummer2
antwoord2 = nummer1 - nummer2
antwoord3 = nummer1 * nummer2

print(antwoord1, antwoord2, antwoord3)

# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit

name = "George"
health = 100
level = 0
damage = 50

player = name, health, level, damage
print(player)

newhealth = health - 20
print(newhealth)

# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 

weapon = "sword"
weapondamage = 40
hitdamage = damage + weapondamage
print(hitdamage)

# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe

name1 = "George"
age1 = 17
favgame1 = "Call of Duty: Black ops 3"
favgamemode1 = "Zombies"
playtime1 = 2100
level1 = 847
prestige1 = 10
prestigetitel1 = "Master"
score1 = 4300000

print(f"Mijn naam is {name1}, ik ben {age1}, mijn favorieten game is {favgame1}, en mijn favorieten gamemode in dat spel is {favgamemode1}, ik heb daar ongeveer {playtime1} uur speeltijd daarin, ik ben prestige {prestigetitel1} dat is de hoogste prestige dat is de{prestige1}e prestige, ik ben level {level1} en mijn hoogste score was ongeveer {score1}.")
score2 = score1 + 250
print(score2)