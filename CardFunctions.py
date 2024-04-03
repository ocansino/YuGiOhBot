import json
import requests


def search_id(json_file, id):
    with open(json_file) as f:
        data = json.load(f)
    # Search for the person by id
    for card in data["data"]:
        if card["id"] == id:
            return card

def get_image(json_file, id):
    temp = search_id(json_file, id)

    return temp['card_images']

result = search_id("card_list.json", 54652250)
result_image = get_image("card_list.json", 54652250)
#r = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Dark Magician')
print(result)
#print(r.json())
print(result_image)
