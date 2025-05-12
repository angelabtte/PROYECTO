import http.client
import flask
import util
from calc import Calculator

api_application = flask.Flask(__name__)
CALCULATOR = Calculator()
HEADERS = {"Content-Type": "text/plain; charset=utf-8"}

@api_application.route("/", methods=["GET"])
def index():
    return ("Hello from The Calculator!\n", http.client.OK, HEADERS)

@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        op_1 = util.convert_to_number(op_1)
        op_2 = util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(op_1, op_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        op_1 = util.convert_to_number(op_1)
        op_2 = util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.substract(op_1, op_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/sqrt/<number>", methods=["GET"])
def sqrt(number):
    try:
        num = util.convert_to_number(number)
        return ("{}".format(CALCULATOR.sqrt(num)), http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

if __name__ == "__main__":
    api_application.run(host="0.0.0.0")
