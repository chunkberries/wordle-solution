import requests
from datetime import date

today = date.today().strftime("%Y-%m-%d")

url = f"https://www.nytimes.com/svc/wordle/v2/{today}.json"

response = requests.get(url)
response.raise_for_status()

data = response.json()
solution = data["solution"]

print(f"Wordle solution for {today}: {solution}")

input("\nPress Enter to exit...")
