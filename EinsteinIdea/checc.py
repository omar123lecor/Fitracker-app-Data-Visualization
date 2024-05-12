'''import requests

url = "https://fitness-api.p.rapidapi.com/fitness"

payload = {
	"height": "190",
	"weight": "77",
	"age": "21",
	"gender": "male",
	"exercise": "little",
	"neck": "41",
	"hip": "100",
	"waist": "88",
	"goal": "maintenance",
	"deficit": "500",
	"goalWeight": 68
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "751fc78129mshf4eb79713ae3a0ap12b67ajsn7b166fb2a422",
	"X-RapidAPI-Host": "fitness-api.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)
print(response.status_code)
print(response.json())
'''  '''import requests

url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/cardio"

querystring = {"limit":"10"}

headers = {
	"X-RapidAPI-Key": "751fc78129mshf4eb79713ae3a0ap12b67ajsn7b166fb2a422",
	"X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())'''
import customtkinter

window = customtkinter.CTk()
window.geometry('500x600')
def label():
	mam.tkraise()
def revive():
	mim.tkraise()
global mim,mam
mam = customtkinter.CTkLabel(window, text='hii',width=40,height=40)
mam.place(x=40, y=40)
mim = customtkinter.CTkLabel(window,text='He\nllo',width=40,height=40)
customtkinter.CTkButton(window,text='Clicl me',command=label).place(x=200,y=200)
customtkinter.CTkButton(window,text='click tk',command=revive,width=40).place(x=50,y=200)
mim.place(x=40,y=40)
window.mainloop()