import json



def search_id(json_file, id):
    with open(json_file) as f:
        data = json.load(f)
    # Search for the person by id
    for card in data["data"]:
        if card["id"] == id:
            return card

    return None
result = search_id("card_list.json", 23771716)

