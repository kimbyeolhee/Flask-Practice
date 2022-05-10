from flask import Flask
app = Flask(__name__)


@app.before_first_request
def before_first_request():
    print("😀 flask 실행 후 첫 요청 때만 실행")


@app.before_request
def before_request():
    print("😎 요청이 들어올 때마다 실행")


@app.after_request
def after_request(response):
    print("🥰 HTTP 요청 처리가 끝나고 브라우저에 응답하기 전에 실행")
    return response


@app.route("/test")
def test():
    print("🤐")
    return "<h1>Hello Flask</h1>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
