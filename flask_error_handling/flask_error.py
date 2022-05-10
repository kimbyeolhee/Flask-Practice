from flask import Flask
import requests

app = Flask(__name__)


# 없는 페이지를 요청했을 때의 에러
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>해당 페이지는 존재하지 않습니다.😎</h1>"


@app.route("/google")
def get_google():
    res = requests.get("http://www.google.co.kr")
    return res.text


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
