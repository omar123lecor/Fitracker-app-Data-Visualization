def set_macros(weight,weight_gol,tdee):
    liste = []
    weight = float(weight)
    weight_gol = float(weight_gol)
    tdee = float(tdee)
    if weight_gol > weight:
        protein = weight * 2
        fats = ((tdee+500) * 0.25)/9
        carbs = (tdee + 500 -(tdee*0.25) - protein * 4)/4
    elif weight_gol < weight:
        protein = weight * 2
        fats = ((tdee-500) * 0.25)/9
        carbs = (tdee - 500 -(tdee*0.25) - protein * 4)/4
    else:
        protein = weight * 2
        fats =  (tdee * 0.25)/9
        carbs = (tdee -(tdee*0.25) - protein * 4)/4
    liste.append(sum([protein*4,fats*9,carbs*4]))
    liste.append(protein)
    liste.append(carbs)
    liste.append(fats)
    return liste



