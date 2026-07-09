import json


def load_data():
    with open("data/blog_data.json", "r", encoding="utf-8") as handle:
        data = json.load(handle)
    return data


def save_data(data):
    with open("data/blog_data.json", "w", encoding="utf-8") as handle:
        json.dump(data, handle)
    return


def add_post(title, author, content):
    posts = load_data()
    if posts:
        post_id = max(post['id'] for post in posts) + 1
    else:
        post_id = 1

    new_post = {
        "id": post_id,
        "title": title,
        "author": author,
        "content": content
    }
    posts.append(new_post)
    save_data(posts)
