import requests
def foodr(foodname):
    liste = []
    query = foodname
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'ab+Wn0R632JuDu8Opyjtcg==gnoSn5JJXEspUrob'})
    if response.status_code == requests.codes.ok:
        responses = response.json()
        for answer in responses:
            liste.append(answer['title'])
    else:
        print("Error:", response.status_code, response.text)
    return liste
def foodingredients(foodcat,title):
    query = foodcat
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'ab+Wn0R632JuDu8Opyjtcg==gnoSn5JJXEspUrob'})
    if response.status_code == requests.codes.ok:
        responses = response.json()
        for i in range(len(responses)):
            if responses[i]['title'] == title:
                ingredients = responses[i]['ingredients']
    else:
        print("Error:", response.status_code, response.text)
    return ingredients
def foodingredients(foodcat,title):
    query = foodcat
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'ab+Wn0R632JuDu8Opyjtcg==gnoSn5JJXEspUrob'})
    if response.status_code == requests.codes.ok:
        responses = response.json()
        for i in range(len(responses)):
            if responses[i]['title'] == title:
                ingredients = responses[i]['ingredients']
    else:
        print("Error:", response.status_code, response.text)
    return ingredients
def foodinstra(foodcat,title):
    query = foodcat
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'ab+Wn0R632JuDu8Opyjtcg==gnoSn5JJXEspUrob'})
    if response.status_code == requests.codes.ok:
        responses = response.json()
        for i in range(len(responses)):
            if responses[i]['title'] == title:
                serving = responses[i]['servings']
    else:
        print("Error:", response.status_code, response.text)
    return serving
def foodserving(foodcat,title):
    query = foodcat
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'ab+Wn0R632JuDu8Opyjtcg==gnoSn5JJXEspUrob'})
    if response.status_code == requests.codes.ok:
        responses = response.json()
        for i in range(len(responses)):
            if responses[i]['title'] == title:
                serving = responses[i]['servings']
    else:
        print("Error:", response.status_code, response.text)
    return serving
def foodinstra(foodcat,title):
    query = foodcat
    api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'ab+Wn0R632JuDu8Opyjtcg==gnoSn5JJXEspUrob'})
    if response.status_code == requests.codes.ok:
        responses = response.json()
        for i in range(len(responses)):
            if responses[i]['title'] == title:
                instructions = responses[i]['instructions']
    else:
        print("Error:", response.status_code, response.text)
    return instructions