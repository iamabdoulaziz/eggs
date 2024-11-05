import time
"""
3 options :
oeufs à la coque: 3 minutes
oeufs mollets: 6 minutes
oeufs durs: 9 minutes

A chaque seconde, afficher un "." sur une même ligne
Toutes les 10 secondes aller à la ligne suivante en affichant le temps restant.
en minutes et secondes
cuissons terminé
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(1)


"""
print("Options de cuisson :")
print("1. Oeufs à la coque: 3 minutes.")
print("2. Oeufs mollets: 6 minutes.")
print("3. Oeufs durs: 9 minutes.")
duration = 0
choice = int(input("Entre ton choix de cuisson : "))

if choice == 1:
    duration = 3 * 60
elif choice == 2:
    duration = 6 * 60
else:
    duration = 9 * 60

while duration > 0:
    for i in range(10):
        time.sleep(1)
        print(".", end="", flush=True)
        duration -= 1
        if duration <= 0:
            break

    if duration <= 0:
        break

    minut = duration//60
    sec = duration-minut*60
    print()
    print(f"Temps restant : {minut:02d}:{sec:02d}", end="", flush=True)

print()
print('Cuisson terminée !')