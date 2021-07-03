import numpy as np


def is_table_positive(table):
    print("table : ", table)
    for element in table:
        if element > 0:
            return 1
    return 0


def max_simplex(cout_z, constraint, b):
    nb_variables = len(cout_z)  # nombre de variable de decision
    nb_constraint = len(constraint)  # nombre de contraint
    base_depart = np.identity(nb_constraint).tolist()  # initialisation de la matrice de départ
    base_variable = [i for i in range(nb_variables, nb_variables + nb_constraint)]  # les indices de la base de départ
    couts_reduits = cout_z + [0 for i in range(nb_constraint)]  # initialisation des couts réduits
    bi = b
    print("couts réduit  : ", couts_reduits)

    # initialisation de la grande matrice
    grande_matrice = constraint
    for i in range(nb_constraint):
        grande_matrice[i] += base_depart[i]
    grande_matrice += [couts_reduits]
    print(grande_matrice)

    for i in range(nb_constraint):
        grande_matrice[i] += base_depart[i]
    grande_matrice += [couts_reduits]

    # starting the simplex iteration
    while is_table_positive(grande_matrice[nb_constraint]):  # tanque les couts réduits negative
        entrant_index = grande_matrice[nb_constraint].index(max(couts_reduits))  # cherchant la variable entrante
        sortant_index = -1
        # cherchant la variable sortante
        min_sortant = -1
        beggin_index = -1
        # on assure que touts ai sont positive
        for i in range(nb_constraint):
            if grande_matrice[i][entrant_index] > 0:
                min_sortant = bi[i] / grande_matrice[i][entrant_index]
                sortant_index = i
                beggin_index = i
                break

        if beggin_index == -1:
            return "solution infinie"

        # cherchons le plus petit bi/ai
        for i in range(beggin_index + 1, nb_constraint):
            if grande_matrice[i][entrant_index] > 0:
                if (bi[i] / grande_matrice[i][entrant_index]) < min_sortant:
                    min_sortant = bi[i] / grande_matrice[i][entrant_index]
                    sortant_index = i  # variable sortante toruvée

        base_variable[sortant_index] = entrant_index  # changeons les variablede base
        pivot = grande_matrice[sortant_index][entrant_index]
        print("Le pivot ", grande_matrice[sortant_index][entrant_index])


        for i in range(len(grande_matrice)):
            if i != entrant_index:
                grande_matrice[i][entrant_index] = 0

        for i in range(len(grande_matrice[0])):
            grande_matrice[sortant_index][i] = grande_matrice[sortant_index][i] / pivot

        for i in range(len(grande_matrice)):
            if i != sortant_index:
                for j in range(len(grande_matrice[0])):
                    if j != entrant_index:
                        grande_matrice[i][j] = ((grande_matrice[i][j] * pivot) - (grande_matrice[sortant_index][j] *
                                                                                  grande_matrice[i][entrant_index])) \
                                               / pivot

        return "resuu", grande_matrice


#Print(max_simplex([-15, -14], [[9, 7], [1, 1]], [100, 12]))

print(max_simplex([7, 9, 18, 17], [[2, 4, 5, 7], [1, 1, 2, 2], [1, 2, 3, 3]], [42, 17, 24]))
