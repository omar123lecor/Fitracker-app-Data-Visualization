import requests
def apiTDEE(age,gender,height,weight,activity):
	gender = gender
	height = float(height)
	weight = float(weight)
	age = float(age)
	if gender == 'male':
		bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
	else:
		bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
	data = bmr
	act = ['little', 'light', 'moderate', 'heavy', 'veryheavy']
	if activity == act[0]:
		data = data*1.2
	elif activity == act[1]:
		data = data*1.375
	elif activity == act[2]:
		data = data*1.55
	elif activity == act[3]:
		data = data*1.725
	elif activity == act[4]:
		data = data*2
	return data.__format__(".2f")
def apiBMI(height,weight):
	height = float(height)
	weight = float(weight)
	bmi = (weight/((height*10**(-2))**2))
	return bmi.__format__(".2f")

def apiconc(height,weight):
	height = float(height)
	weight = float(weight)
	bmi = (weight / ((height * 10 ** (-2)) ** 2))
	if bmi < 18.5 :
		return 'underweight'
	elif bmi >= 18.5 and bmi < 24.9:
		return 'normal'
	elif bmi >=24.9 and bmi < 29.9:
		return 'overweight'
	elif bmi >= 29.9 :
		return 'obesity'


