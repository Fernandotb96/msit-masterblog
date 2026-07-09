from flask import Flask, render_template
from data import storage

app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = storage.load_data()
    return render_template('index.html', post=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
