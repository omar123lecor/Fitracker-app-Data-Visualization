import requests

query = 'panini'
api_url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
response = requests.get(api_url, headers={'X-Api-Key': 'ab+Wn0R632JuDu8Opyjtcg==gnoSn5JJXEspUrob'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
