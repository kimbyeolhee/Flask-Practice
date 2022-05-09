from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_url_path="/static")


@app.route("/login")
def login():
    email_address = request.args.get("email_address")
    passwd = request.args.get("passpw")

    if email_address == "qufgml@naver.com":
        return_data = {'auth': 'success'}
    else:
        return_data = {'auth': 'fail'}
    return jsonify(return_data)


@app.route("/html_test")
def test_html():
    return render_template("login_test.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8080")
