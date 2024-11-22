import requests

def get_data(url):
    reponse = requests.get(url)
    reponse_js = reponse.json()
    setup, punchline = reponse_js["setup"], reponse_js["punchline"]
    return f"{setup}\n{punchline}"

print(get_data("https://official-joke-api.appspot.com/random_joke"))
