import requests
import argparse
from config import API_KEY, API_TOKEN, LIST_ID

def main():
    # parse args and add_card
    parser = argparse.ArgumentParser(
                    prog='trellogtd',
                    description='Adds card to Trello board (GTD IN list) with name and description',)
    parser.add_argument('name', help='A card name')
    parser.add_argument('description', nargs='?', default='', help='An optional card description')
    args = parser.parse_args()

    add_card(args.name, args.description)

def add_card(name, desc=""):
    url = "https://api.trello.com/1/cards"
    params = {
        "key": API_KEY,
        "token": API_TOKEN,
        "idList": LIST_ID,
        "name": name,
        "desc": desc,
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print(f"✅ Card '{name}' successfully added!")
    else:
        print(f"❌ Error: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    main()
