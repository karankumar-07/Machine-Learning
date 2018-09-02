import numpy as np
from sklearn.linear_model import LogisticRegression
import _pickle as pickle
from flask import Flask, request, jsonify

def predict(num1, num2):
	out = {'a' : 0}
	input = np.array([num1,num2]).reshape(1,2)
	file = 'lr.pkl'
	m1 = pickle.load(open(file, 'rb'))
	k = m1.predict(input)	
	k = k.tolist()
	out['a'] = k
	print(out['a'])
	return out['a']

app = Flask(__name__)

@app.route("/")
def index():
	return "Logistic Regression"

@app.route("/lr", methods = ["GET"])
def cal():
	body = request.get_data()
	num1 = int(request.args['x1'])
	num2 = int(request.args['x2'])
	res = predict(num1, num2)
	return jsonify(res)

if __name__ == "__main__":
	app.run(port = 8007)
