import requests

url = "https://api.divar.ir/v8/postlist/w/search"
pass

json = {"city_ids": ["1"]}


headers = {"Content-Type": "application/json"}

res = requests.post(url,json=json, headers=headers)

data = res.json()

last_post_date = data["pagination"]["data"]['last_post_date']


list_of_tokens = []
count = 0
while True:

    json = {"city_ids": ["1"]}
    res = requests.post(url,json=json, headers=headers)
    data = res.json()
    last_post_date = data["pagination"]["data"]['last_post_date']

    for widget in data['list_widgets']:
        if 'token' not in widget['data']:
            continue
        else:
            token = widget["data"]["token"]
            list_of_tokens.append(token)
            count +=1
            print(token)

    if count >=100:
        break

print(list_of_tokens)

txt_file = open("tokens.txt", "w", encoding="utf8")
txt_file.write(','.join(list_of_tokens))
txt_file.close
    