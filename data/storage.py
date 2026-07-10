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


def get_post(post_id):
    """Search for a post by ID and return its data"""
    posts = load_data()
    for post in posts:
        if post['id'] == post_id:
            return post
    return None


def delete_post(post_id):
    posts = load_data()
    final_posts = [post for post in posts if post['id'] != post_id]
    save_data(final_posts)


def update_post(post_id, title, author, content):
    """Search for a post by ID and update title, author and content"""
    posts = load_data()
    for post in posts:
        if post['id'] == post_id:
            post['title'] = title
            post['author'] = author
            post['content'] = content
            break
    save_data(posts)
