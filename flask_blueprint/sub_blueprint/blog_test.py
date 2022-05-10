from flask import Blueprint

# 객체
blog_ab = Blueprint('blog', __name__)


# http://localhost:8080/blog/blog1
@blog_ab.route('/blog1')
def blog():
    return "📌BluePrint: blog1"
