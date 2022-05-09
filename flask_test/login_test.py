from flask import Flask, jsonify, request, render_template
app = Flask(__name__)


@app.route("/login")
def login():
    username = request.args.get("user_name")
    password = request.args.get("pw")

    if username == "byeol":
        return_data = {'auth': 'success'}
    else:
        return_data = {'auth': 'fail'}
    return jsonify(return_data)


@app.route("/html_test")
def test_html():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8080")
