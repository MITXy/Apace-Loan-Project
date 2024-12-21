from flask import Flask, jsonify, request
import pandas as pd

model1 = load_model('model1')
model2 = load_model('model2')

# Initialize the Flask app
app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome apace"


# Define a route for the prediction API
@app.route('/predict', methods=['POST'])
def predict():
    #format the supplied input into formats needed
    loan_data = request.get_json()
    loan_df = pd.DataFrame.from_dict([loan_data])

    #predict on the models
    prediction1 = model1.predict(loan_data)
    prediction2 = model2.predict(loan_data)

    if prediction1 == 1:
        return jsonify({ "message":"Creditable", 'prediction': prediction1, "amount": prediction2})
    else:
        return jsonify({ "message":"Not Creditable", 'prediction': prediction1, "amount": prediction2})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)