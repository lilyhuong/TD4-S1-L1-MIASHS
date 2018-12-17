# LA BOULE "WHILE"
#while <condition.:
    #<bloc d'intruction>
#example on demande a l'ultilisateur d'entrer des notes
#quand il a fini il entre un entier negatif
#l'objectif est de calculer la moyennen
#somme, nbdenotes = 0,0
#note = float(input("entre votre premier note, puis les suivante, en finissant par un nb negatif"))
#while note >= 0:
    #somme += note
    #nbdenotes += 1
    #note = float(input())
#print("la moyenne des note est: ", somme/nbdenotes)l'o
#exo1
#l'objectif est ecrite une fonction qui compte le nombre d'occurrences d'un caractere x dans une chaine de caractere ch.
def saisieOuioNon():
    rep = input("donnez votre reponse, oui ou non")
    while rep != "oui" and rep != "non":
        rep = input("Recommenz: ")
    if rep == "oui: ":
        return 1
    else:
        return 0

#while not(rep ="oui" or rep = "non")
def approximer(epsilon):
#revoie le plus petit in tq |u ^ 2 - 2| < $
    n = 0
    u = 2
    while 