import requests

def fetch_data_from_api():
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"

    querystring = {"Category":"soccer","Timezone":"-7"}

    headers = {
        "X-RapidAPI-Key": "ed0bcdb056msh95cfa52e4780e59p181b44jsn2b6994d502e6",
        "X-RapidAPI-Host": "livescore6.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # Handle errors or raise exceptions as needed
        return None
