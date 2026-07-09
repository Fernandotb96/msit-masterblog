import json


def load_data():
    with open("data/blog_data.json", "r", encoding="utf-8") as handle:
        data = json.load(handle)
    return data


def save_data(data):
    with open("data/blog_data.json", "w", encoding="utf-8") as handle:
        json.dump(data, handle)
    return
