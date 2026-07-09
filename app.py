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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
