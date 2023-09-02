# variables:
listorigine = []
listsortie = []
alpha = "	AÁÀÂÄÆBCÇDEÉÈÊËFGHIÍÌÎÏJKLMNOÒÓÔÖŒPQRSTUÚÙÛÜVWXYÝŸZaáàâäæbcçdeéèêëfghiíìîïjklmnoòóôöœpqrstuúùûüvwxyýÿz0123456789 "
seed = 0


def convert_txt_bin(text):
    clef = seed
    # On vide les listes
    listorigine[:] = []
    listsortie[:] = []
    cle = str(clef)  # clef de chiffrement - déchiffrement (peut être autre que 0)
    txtorigine = text  # texte
    # On initialise un compteur à 0
    cpt = 0
    # On parcourt le texte à chiffrer et on range toutes les lettres dans la list origine
    while cpt < len(txtorigine):
        lettre = txtorigine[cpt]
        listorigine.append(lettre)
        cpt = cpt + 1
    # On réinitialise le compteur à 0
    cpt = 0
    # On initialise un compteur à 0 pour la clef
    place_cle = 0
    # On parcourt toute la list origine
    while cpt < len(listorigine):
        # On chiffre la lettre de la list origine en regardant sa position dans la variable alpha
        nbre_origine = alpha.find(listorigine[cpt])
        # On chiffre la lettre de la clef en regardant sa position dans la variable alpha
        nbre_cle = alpha.find(cle[place_cle])
        # Si la lettre de la list origine existe dans la variable alpha
        if nbre_origine != -1:
            # On calcule la somme
            nbre_sortie = nbre_origine + nbre_cle
            # Si cette somme est supérieure à 113, on retranche 114 (nombre de caractères dans alpha +1)
            if nbre_sortie > 113:
                nbre_sortie = nbre_sortie - 114
            # On cherche dans la variable alpha la lettre correspondante à la position trouvée et on l'ajoute à la list sortie
            lettre_sortie = alpha[nbre_sortie]
            listsortie.append(lettre_sortie)
            # On incrémente le compteur de la clef et on le remet à 0 si dépasse la longueur de la clef
            place_cle = place_cle + 1
            if place_cle >= len(cle):
                place_cle = 0
        # Sinon, on ajoute à la list sortie le même caractère que la list origine
        else:
            listsortie.append(listorigine[cpt])
        # On incrémente le compteur pour la list origine
        cpt = cpt + 1
    # On joint toutes les lettres de la list sortie et on place le tout dans le Text de sortie
    txtsortie = "".join(listsortie)
    text = txtsortie
    text = text.replace("\n", "")
    text = bin(int.from_bytes(text.encode(), 'big'))
    return text


def convert_bin_txt(text):
    text = text.replace("\n", "")
    text = int(text, 2)
    text = text.to_bytes((text.bit_length() + 7) // 8, 'big').decode()
    # On vide les listes
    listorigine[:] = []
    listsortie[:] = []
    clef = seed
    txt = text
    # On récupère la clef de chiffrement - déchiffrement
    cle = str(clef)  # clef de chiffrement - déchiffrement (peut être autre que 0)
    # On récupère le text à déchiffrer
    txtorigine = txt
    # On initialise un compteur à 0
    cpt = 0
    # On parcourt le texte à déchiffrer et on range toutes les lettres dans la listorigine
    while cpt < len(txtorigine):
        lettre = txtorigine[cpt]
        listorigine.append(lettre)
        cpt = cpt + 1
    # On réinitialise le compteur à 0
    cpt = 0
    # On initialise un compteur à 0 pour la clef
    place_cle = 0
    # On parcourt toute la listorigine
    while cpt < len(listorigine):
        # On chiffre la lettre de la listorigine en regardant sa position dans la variable alpha
        nbre_origine = alpha.find(listorigine[cpt])
        # On chiffre la lettre de la clef en regardant sa position dans la variable alpha
        nbre_cle = alpha.find(cle[place_cle])
        # Si la lettre de la listorigine existe dans la variable alpha
        if nbre_origine != -1:
            # On calcule la différence
            nbre_sortie = nbre_origine - nbre_cle
            # Si cette différence est inférieure à 0, on ajoute 114 (nombre de caractères dans alpha +1)
            if nbre_sortie < 0:
                nbre_sortie = nbre_sortie + 114
            # On cherche dans la variable alpha la lettre correspondante à la position trouvée et on l'ajoute à la listsortie
            lettre_sortie = alpha[nbre_sortie]
            listsortie.append(lettre_sortie)
            # On incrémente le compteur de la clef et on le remet à 0 si dépasse la longueur de la clef
            place_cle = place_cle + 1
            if place_cle >= len(cle):
                place_cle = 0
        # Sinon, on ajoute à la listsortie le même caractère que la listorigine
        else:
            listsortie.append(listorigine[cpt])
        # On incrémente le compteur pour la listorigine
        cpt = cpt + 1
    # On joint toutes les lettres de la listsortie et on place le tout dans le Text de sortie
    txtsortie = "".join(listsortie)
    return txtsortie