

def monnayeur(somme):
    liste_pieces = [1, 2, 5, 10, 20]

    liste_resultat = []
    while somme > 0:
        choix_valeur = max(piece for piece in liste_pieces if piece <= somme)
        liste_resultat.append(choix_valeur)
        somme = somme - choix_valeur
    return liste_resultat
