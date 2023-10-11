from flask import Flask, jsonify
from dice import Dice 


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    result = Dice().roll()
    return jsonify({"roll": result}) 


if __name__ == "__main__": 

    app.run(port=9000, debug=True)