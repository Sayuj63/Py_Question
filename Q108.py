import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Title:", data["title"])
    print("Body:", data["body"])
else:
    print("Failed to fetch data. Status Code:", response.status_code)
