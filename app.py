from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

app = Flask('ml-app')

iris = load_iris()
X = iris['data']
y = iris['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json() 

    prediction = model.predict([data['features']])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
