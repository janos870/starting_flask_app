from flask import render_template
from app.blog import blog
from app.blog.models import Post


@blog.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template('posts.html', title='Posts', posts=posts)


@blog.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', title=post.title, post=post)



