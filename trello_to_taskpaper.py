import sys
import json

def get_card_list(board_data):
    output = {}
    card_data = board_data["cards"]

    for card in card_data:
        if card["closed"]:
            continue

        board_id = card["idList"]
        if board_id not in output:
            output[board_id] = []
        output[board_id].append(card["name"])

    return output

def name_lists(card_list, board_data):
    output = {}
    list_json = board_data["lists"]

    for list_id in card_list:
        for list_data in list_json:
            if list_data["id"] == list_id:
                output[list_data["name"]] = card_list[list_id]

    return output

def convert_to_taskpaper(card_data):
    output = ""

    for list_name in card_data:
        output += list_name + ":\n"
        for card in card_data[list_name]:
            output += "    - " + card + "\n"
        output += "\n"

    return output

def main():
    with open(sys.argv[1]) as data_file:
        board_data = json.load(data_file)

    card_list = get_card_list(board_data)
    card_list = name_lists(card_list, board_data)
    taskpaper = convert_to_taskpaper(card_list)
    print taskpaper

if __name__ == "__main__":
    main()
