from flask import Flask, render_template, request, redirect, url_for
from data import storage

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main homepage showing a list of all blog posts."""
    blog_posts = storage.load_data()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    """Handle creating a new blog post.
    If the request is GET, render the page with the form.
    If the request is POST, process the submitted form data to create
    the post and redirect to the homepage."""
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        storage.add_post(title, author, content)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    """Handle the deletion of a blog post.
    Accept only POST requests to prevent accidental deletion"""
    storage.delete_post(post_id)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    """Handle updating/editing an existing blog post.
    If the request is GET, retrieve the post and render the edit form.
    If the request is POST, update the post with the new form values and
    redirect to the homepage."""
    post = storage.get_post(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        storage.update_post(post_id, title, author, content)
        return redirect(url_for('index'))
    return render_template('update.html', post=post)


@app.route('/like/<int:post_id>')
def like_post(post_id):
    storage.like_post(post_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
