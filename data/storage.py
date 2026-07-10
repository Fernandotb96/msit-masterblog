import json


def load_data():
    """Load and return all blog posts from the JSON database file."""
    try:
        with open("data/blog_data.json", "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(data):
    """Save the provided list of blog posts to the JSON database file."""
    with open("data/blog_data.json", "w", encoding="utf-8") as handle:
        json.dump(data, handle)


def add_post(title, author, content):
    """Create a new blog post and append it to the database.
    Generate a unique ID for the new post by finding the maximum existing ID
    and adding 1."""
    posts = load_data()
    if posts:
        post_id = max(post['id'] for post in posts) + 1
    else:
        post_id = 1

    new_post = {
        "id": post_id,
        "title": title,
        "author": author,
        "content": content,
        "likes": 0
    }
    posts.append(new_post)
    save_data(posts)


def get_post(post_id):
    """Search for and returns a single blog post by its unique ID."""
    posts = load_data()
    for post in posts:
        if post['id'] == post_id:
            return post
    return None


def delete_post(post_id):
    """Remove a blog post from the database by its unique ID."""
    posts = load_data()
    final_posts = [post for post in posts if post['id'] != post_id]
    save_data(final_posts)


def update_post(post_id, title, author, content):
    """Update the details of an existing blog post."""
    posts = load_data()
    for post in posts:
        if post['id'] == post_id:
            post['title'] = title
            post['author'] = author
            post['content'] = content
            break
    save_data(posts)


def like_post(post_id):
    """Search for a post and increment the number of likes."""
    posts = load_data()
    for post in posts:
        if post['id'] == post_id:
            post['likes'] = post.get('likes', 0) + 1
            break
    save_data(posts)
