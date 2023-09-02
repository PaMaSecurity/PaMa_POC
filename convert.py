# variables
dico_int_char = {'33': '!', '34': '', '35': '#', '36': '$', '37': '%', '38': '&', '39': "'", '40': '(', '41': ')', '42': '*', '43': '+', '44': ',', '45': '-', '46': '.', '47': '/', '48': '0', '49': '1', '50': '2', '51': '3', '52': '4', '53': '5', '54': '6', '55': '7', '56': '8', '57': '9', '58': ':', '59': ';', '60': '<', '61': '=', '62': '>', '63': '?', '64': '@', '65': 'A', '66': 'B', '67': 'C', '68': 'D', '69': 'E', '70': 'F', '71': 'G', '72': 'H', '73': 'I', '74': 'J', '75': 'K', '76': 'L', '77': 'M', '78': 'N', '79': 'O', '80': 'P', '81': 'Q', '82': 'R', '83': 'S', '84': 'T', '85': 'U', '86': 'V', '87': 'W', '88': 'X', '89': 'Y', '90': 'Z', '91': '[', '93': ']', '94': '^', '95': '_', '96': '`', '97': 'a', '98': 'b', '99': 'c', '100': 'd', '101': 'e', '102': 'f', '103': 'g', '104': 'h', '105': 'i', '106': 'j', '107': 'k', '108': 'l', '109': 'm', '110': 'n', '111': 'o', '112': 'p', '113': 'q', '114': 'r', '115': 's', '116': 't', '117': 'u', '118': 'v', '119': 'w', '120': 'x', '121': 'y', '122': 'z', '123': '{', '124': '|', '125': '}', '126': '~'}
dico_char_int = {'!': '33', '': '34', '#': '35', '$': '36', '%': '37', '&': '38', "'": '39', '(': '40', ')': '41', '*': '42', '+': '43', ',': '44', '-': '45', '.': '46', '/': '47', '0': '48', '1': '49', '2': '50', '3': '51', '4': '52', '5': '53', '6': '54', '7': '55', '8': '56', '9': '57', ':': '58', ';': '59', '<': '60', '=': '61', '>': '62', '?': '63', '@': '64', 'A': '65', 'B': '66', 'C': '67', 'D': '68', 'E': '69', 'F': '70', 'G': '71', 'H': '72', 'I': '73', 'J': '74', 'K': '75', 'L': '76', 'M': '77', 'N': '78', 'O': '79', 'P': '80', 'Q': '81', 'R': '82', 'S': '83', 'T': '84', 'U': '85', 'V': '86', 'W': '87', 'X': '88', 'Y': '89', 'Z': '90', '[': '91', ']': '93', '^': '94', '_': '95', '`': '96', 'a': '97', 'b': '98', 'c': '99', 'd': '100', 'e': '101', 'f': '102', 'g': '103', 'h': '104', 'i': '105', 'j': '106', 'k': '107', 'l': '108', 'm': '109', 'n': '110', 'o': '111', 'p': '112', 'q': '113', 'r': '114', 's': '115', 't': '116', 'u': '117', 'v': '118', 'w': '119', 'x': '120', 'y': '121', 'z': '122', '{': '123', '|': '124', '}': '125', '~': '126'}
liste_q = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999]
liste_p = [3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513, 4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, 4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, 4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733, 4751, 4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, 4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, 4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999]
liste_e = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513, 4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, 4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, 4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733, 4751, 4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, 4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, 4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999]
listorigine = []
listsortie = []
alpha = "	AÁÀÂÄÆBCÇDEÉÈÊËFGHIÍÌÎÏJKLMNOÒÓÔÖŒPQRSTUÚÙÛÜVWXYÝŸZaáàâäæbcçdeéèêëfghiíìîïjklmnoòóôöœpqrstuúùûüvwxyýÿz0123456789 "
seed = 0
# imports
import random


def convert_txt_bin(text):
    random.seed(seed)
    q = random.choice(liste_q)
    p = random.choice(liste_p)
    N = p * q
    e = random.choice(liste_e)
    liste_c = [str(pow(i, e, N)) for i in [int(dico_char_int[i.replace("\n", "")]) for i in text]]
    text = "/".join(liste_c)
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
    text = txtsortie.split("/")
    random.seed(seed)
    q = random.choice(liste_q)
    p = random.choice(liste_p)
    N = p * q
    phi = (q - 1) * (p - 1)
    e = random.choice(liste_e)
    x = 1 ; xx = 0
    d = 0 ; yy = 1
    while e != 0:
        q = phi // e
        phi, e = e, phi % e
        xx, x = x - q * xx, xx
        yy, d = d - q * yy, yy
    txtsortie = "".join([dico_int_char[str(i)] for i in [pow(int(i), d, N) for i in text]])
    return txtsortie