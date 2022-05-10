from flask import Flask
import requests

app = Flask(__name__)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(
        "flask_log.log", maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>해당 페이지는 존재하지 않습니다😎</h1>", 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=False)
