import requests

# Your API key
api_key = '985b63c16fd84780aeeebd35a3d61c64'

# The ingredient you want to search for
ingredient = "pizza"

# API endpoint
url = f'https://api.spoonacular.com/food/ingredients/search?query={ingredient}&number=1&apiKey={api_key}'

response = requests.get(url)
if response.status_code == 200:
    ingredient_data = response.json()
    print(ingredient_data)
    if ingredient_data['results']:
        ingredient_id = ingredient_data['results'][0]['id']

        # Get nutritional information for the ingredient
        nutrition_url = f'https://api.spoonacular.com/food/ingredients/{ingredient_id}/information?amount=1&apiKey={api_key}'
        nutrition_response = requests.get(nutrition_url)

        if nutrition_response.status_code == 200:
            nutrition_data = nutrition_response.json()
            print(nutrition_data)
        else:
            print(f"Error: Unable to fetch nutrition data ({nutrition_response.status_code})")
    else:
        print("Ingredient not found.")
else:
    print(f"Error: Unable to search ingredient ({response.status_code})")

