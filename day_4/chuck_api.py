import requests

# pip install requests

url = "https://api.chucknorris.io/jokes/random"

response_img = requests.get(url)
print(response_img)  # <Response [200]>
# 2xx - ok
# 3xx - warningi
# 4xx - błędy po stronie użtkownika, 404 brak zasobu, 400 Bad Rewuest bład w danych
# 5xx - błedy po stronie serwera np 500 Internal serwer error
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP

print(response_img.text)
print(type(response_img.text))  # <class 'str'>

data = response_img.json()
print(type(data))  # <class 'dict'>

for k in data:
    print(k)
# categories
# created_at
# icon_url
# id
# updated_at
# url
# value

print(data['value'])
# Chuck Norris Rounhouse kicked Voldemort now he has n nose

print(data['icon_url'])  # https://api.chucknorris.io/img/avatar/chuck-norris.png

response_img = requests.get(data['icon_url'])
with open('icona.jpg', "wb") as f:
    f.write(response_img.content)
print("Zdjęcie zostało zapisane")
