import os
import sentry_sdk

from bottle import route, run, request, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration
from http import HTTPStatus

SENTRY_DSN = os.environ.get("SENTRY_DSN")
sentry_sdk.init(dsn=SENTRY_DSN, integrations=[BottleIntegration()])

@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>server success/fail</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>Это мой сервер для проверки HW модуля D2</p>
      <p class="small">Запросы можно отправлять на /success и /fail</p>
    </div>
  </body>
</html>
"""
    return html


@route('/success')  
def index():  
    return  HTTPResponse(status=HTTPStatus.OK)

@route('/fail')  
def index():  
    raise RuntimeError("There is an error!")
    return
  
if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
