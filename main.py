import numpy as np


def is_table_positive(table):
    print("table : ", table)
    for element in table:
        if element < 0:
            return 1
    return 0


def max_simplex(cout_z, constraint, b):
    nb_variables = len(cout_z)  # nombre de variable de decision
    nb_constraint = len(constraint)  # nombre de contraint
    base_depart = np.identity(nb_constraint).tolist()  # initialisation de la matrice de départ
    base_variable = [i for i in range(nb_variables, nb_variables + nb_constraint)]  # les indices de la base de départ
    couts_reduits = cout_z + [0 for i in range(nb_constraint)]  # initialisation des couts réduits
    bi = b

    grande_matrice = constraint
    for i in range(nb_constraint):
        print("grandline i ",grande_matrice)
        print("based depart i ",base_depart[i])
        grande_matrice[i] += base_depart[i]

    grande_matrice += couts_reduits

    while is_table_positive(grande_matrice[nb_constraint]):
        entrant_index = grande_matrice[nb_constraint].index(min(couts_reduits))
        min_sortant = bi[0] / grande_matrice[entrant_index][0]
        sortant_index = 0
        for i in range(1, nb_constraint):
            if grande_matrice[entrant_index][i] > 0:
                if bi[i] / grande_matrice[entrant_index][i] < min_sortant:
                    min_sortant = bi[i] / grande_matrice[entrant_index][i]
                    sortant_index = i

        if min_sortant == bi[0] / grande_matrice[entrant_index][0] and constraint[0] <= 0:
            return "solution infinie"

        base_variable[base_variable.index(sortant_index)] = entrant_index
    return grande_matrice[sortant_index][entrant_index]


print(max_simplex([-15, -14, 2], [[9, 7], [1, 1]], [100,12]))
