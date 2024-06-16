def set_macros(weight,weight_gol):
    liste = []
    weight = float(weight)
    weight_gol = float(weight_gol)
    if weight_gol > weight:
        protein = weight * 4
        carbs = weight * 2 * 4
        fats = weight * 0.45 * 9
    elif weight_gol < weight:
        protein = weight * 1.4 * 4
        carbs = weight * 4
        fats = weight * 0.25 * 9
    else:
        protein = weight * 4
        carbs = weight * 4
        fats = weight * 0.25 * 9
    liste.append(sum([protein,fats,carbs]))
    liste.append(protein)
    liste.append(carbs)
    liste.append(fats)
    return liste



