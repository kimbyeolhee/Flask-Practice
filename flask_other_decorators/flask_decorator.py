from flask import Flask
app = Flask(__name__)


@app.before_first_request
def before_first_request():
    print("π flask μ€ν ν μ²« μμ²­ λλ§ μ€ν")


@app.before_request
def before_request():
    print("π μμ²­μ΄ λ€μ΄μ¬ λλ§λ€ μ€ν")


@app.after_request
def after_request(response):
    print("π₯° HTTP μμ²­ μ²λ¦¬κ° λλκ³  λΈλΌμ°μ μ μλ΅νκΈ° μ μ μ€ν")
    return response


@app.route("/test")
def test():
    print("π€")
    return "<h1>Hello Flask</h1>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
