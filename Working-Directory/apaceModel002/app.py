from flask import Flask, jsonify, request
import pandas as pd
from pycaret.classification import load_model, predict_model

model = load_model('loan_classification_model')
prep_pipe = load_model('loan_classification_model')

# Initialize the Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome apace"


# Define a route for the prediction API
@app.route('/predict', methods=['POST'])
def predict():
    loan_data = request.get_json()
    loan_df = pd.DataFrame.from_dict([loan_data])
    preprocessed_loan_df = prep_pipe.transform(loan_df)
    predictions = predict_model(model, data=preprocessed_loan_df)

    label = predictions['Label'].iloc[0]
    probability = predictions['Score'].iloc[0]

    return jsonify({'class': label, 'probability': probability})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)