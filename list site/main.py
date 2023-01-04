from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/8571dd961c8e595d3393").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

for post in post_objects:
    print(post.title)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", post_objects=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)