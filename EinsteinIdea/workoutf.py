import time

import requests
def listname(muscl):
    liste = []
    muscle = muscl
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
    response = requests.get(api_url, headers={'X-Api-Key': 'ab+Wn0R632JuDu8Opyjtcg==gnoSn5JJXEspUrob'})
    if response.status_code == requests.codes.ok:
        response = response.json()
        for i in response:
            liste.append(i['name'])
    else:
        print("Error:", response.status_code, response.text)
    return liste

