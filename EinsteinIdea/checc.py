import requests
import mysql.connector

url = "https://fitness-api.p.rapidapi.com/fitness"

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "21c855ad1amsh1e860f52c848bcbp16ff8ajsn56f79d1b6d5b",
	"X-RapidAPI-Host": "fitness-api.p.rapidapi.com"
}
def apiTDEE(height,weight,age,gender,activity):
	payload = {
		"height": height,
		"weight": weight,
		"age": age,
		"gender": gender,
		"exercise": "little",
		"neck": "41",
		"hip": "100",
		"waist": "88",
		"goal": "maintenance",
		"deficit": "500",
		"goalWeight": 60
	}
	response = requests.post(url, data=payload, headers=headers)
	return response.json()['totalDailyEnergyExpenditure']['bmi']['calories']['value']
def apiBMI(height,weight,age,gender,activity):
	payload = {
		"height": height,
		"weight": weight,
		"age": age,
		"gender": gender,
		"exercise": activity,
		"neck": "41",
		"hip": "100",
		"waist": "88",
		"goal": "maintenance",
		"deficit": "500",
		"goalWeight": 60
	}

	response = requests.post(url, data=payload, headers=headers)
	return response.json()['bodyMassIndex']['value']
def apiconc(height,weight,age,gender,activity):
	payload = {
		"height": height,
		"weight": weight,
		"age": age,
		"gender": gender,
		"exercise": activity,
		"neck": "41",
		"hip": "100",
		"waist": "88",
		"goal": "maintenance",
		"deficit": "500",
		"goalWeight": 60
	}
	response = requests.post(url, data=payload, headers=headers)
	return response.json()['bodyMassIndex']['conclusion']
print(apiBMI(180,77,21,'male','little'))