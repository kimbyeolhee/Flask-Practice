from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for, session
from blog_control.user_mgmt import User
from flask_login import login_user, current_user, logout_user
import datetime
from blog_control.session_mgmt import BlogSession

blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        print(request.args.get('user_email'))
        return redirect('/blog/test_blog')
    elif request.method == 'POST':
        # print(request.form['user_email'])
        # print(request.get_json()) # content type이 application/json인 경우만 가져올 수 있음
        # print(request.form['blog_id'])
        user = User.create(request.form['user_email'], request.form['blog_id'])
        login_user(user, remember=True, duration=datetime.timedelta(days=365))

        return redirect('/blog/test_blog')


@blog_abtest.route('/test_blog')
def blog_fullstack1():
    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(
            session['client_id'], current_user.user_email, webpage_name)
        return render_template(webpage_name, user_email=current_user.user_email)
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(
            session['client_id'], 'anonymous', webpage_name)
        return render_template(webpage_name)


@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect('/blog/test_blog')
