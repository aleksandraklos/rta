import pickle
from flask import Flask, request
from flask_restful import Api
from model import Perceptron

with open("RTA_model_1.pkl", 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)
api = Api(app)


@app.route('/')
def start():
    return 'hello world'


@app.route('/api/predict/', methods=['GET'])
def home():
    sl = request.args.get("sl", "8.7")
    pl = request.args.get("pl", "6.7")
    res = model.predict([float(sl), float(pl)])
    mapper = {'0': 'setosa',
              '1': 'versicolor'}
    return mapper[f"{res}"]


app.run(port='5032')