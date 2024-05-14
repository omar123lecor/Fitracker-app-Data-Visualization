import requests
def apiTDEE(age,gender,height,weight,activity):
	url = "https://fitness-calculator.p.rapidapi.com/dailycalorie"
	querystring = {"age":age,"gender":gender,"height":height,"weight":weight,"activitylevel":"level_1"}
	headers = {
		"X-RapidAPI-Key": "21c855ad1amsh1e860f52c848bcbp16ff8ajsn56f79d1b6d5b",
		"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com"
	}
	response = requests.get(url, headers=headers, params=querystring)
	data = response.json()['data']['BMR']
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
	bmi = (weight/((height*10**(-2))**2))
	return bmi.__format__(".2f")

def apiconc(height,weight):
	bmi = (weight / ((height * 10 ** (-2)) ** 2))
	if bmi < 18.5 :
		return 'underweight'
	elif bmi >= 18.5 and bmi < 24.9:
		return 'normal'
	elif bmi >=24.9 and bmi < 29.9:
		return 'overweight'
	elif bmi >= 29.9 :
		return 'obesity'

