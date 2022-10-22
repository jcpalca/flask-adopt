import requests
import os
from dotenv import load_dotenv
from random import choice

load_dotenv()

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']
BASE_URL = 'https://api.petfinder.com/v2/animals'
AUTH_URL = 'https://api.petfinder.com/v2/oauth2/token'

def authenticate_pet_api():
    """ Authenticating with the API to get an Oauth token
    Input: None
    Output: Oauth Token (string)
    """
    response = requests.post(
      AUTH_URL,
      data={
        'grant_type': 'client_credentials',
        'client_id': PETFINDER_API_KEY,
        'client_secret': PETFINDER_SECRET_KEY
      }
    )

    return response.json()['access_token']

def get_pets_api(token):
    """ Makes GET request to /animals/url to find a random pet
    Input: token (string)
    Output: Pets (list of dictionaries containing pet info)"""

    response = requests.get(
        BASE_URL,
        params={
          'limit': 100
        },
        headers={
          "Authorization": f"Bearer {token}"
        }
    )

    try:
        return response.json()["animals"]
    except KeyError:
        auth_token = authenticate_pet_api()
        return get_pets_api(auth_token)

def get_random_pet(pets):
    """ Returns a random pet with valid photo
    Input: pets (list of pets)
    Output: pet_info (dictionary)
    """

    pets_with_photo = [pet for pet in pets if pet['primary_photo_cropped']]
    chosen_pet = choice(pets_with_photo)
    pet_info = {
      'name': chosen_pet['name'],
      'age': chosen_pet['age'],
      'picture': chosen_pet['primary_photo_cropped']['full']
    }

    return pet_info

# oauth = authenticate_pet_api()
# get_pets_api(oauth)
