from flask import Flask, render_template, request, redirect, url_for
from data import storage

app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = storage.load_data()
    return render_template('index.html', post=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        storage.add_post(title, author, content)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    storage.delete_post(post_id)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        storage.update_post(post_id, title, author, content)
        return redirect(url_for('index'))

    post = storage.get_post(post_id)
    if post is None:
        return "Post no found", 404
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
