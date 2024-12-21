from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', "rb"))


@app.route("/")
def home():
    return "Welcome apace"


@app.route("/predict", methods=["GET"])
def predict():
    Gender = request.args.get('Gender')
    Age = request.args.get("Age")
    MaritalStatus = request.args.get('MaritalStatus')
    EmploymentStatus = request.args.get("EmploymentStatus")
    LoanAmount = request.args.get("LoanAmount")
    Tenure = request.args.get('Tenure')
    MerchantServiceCharge = request.args.get('MerchantServiceCharge')
    ExpectedRevenue = request.args.get('ExpectedRevenue')
    LoanDuration = request.args.get('LoanDuration')
    MonthlyRepaymentAmount = request.args.get('MonthlyRepaymentAmount')
    AmountReceived = request.args.get('AmountReceived')
    InterestRate = request.args.get("InterestRate")
    CurrentOutstandingBalance = request.args.get('CurrentOutstandingBalance')
    DefaultCharge = request.args.get("DefaultCharge")
    InflationScore = request.args.get("InflationScore")
    Primelending = request.args.get("Primelending")
    Maxlending = request.args.get("Maxlending")

    makePrediction = model.predict([[Gender, Age, MaritalStatus, EmploymentStatus, LoanAmount, Tenure,
                                     MerchantServiceCharge, ExpectedRevenue, LoanDuration, MonthlyRepaymentAmount,
                                     AmountReceived, InterestRate, CurrentOutstandingBalance, DefaultCharge,
                                     InflationScore, Primelending, Maxlending]])

    Value = round(makePrediction[0])

    if Value == 1:
        return jsonify({"This Costumer is Eligible": Value})
    elif Value == 0:
        return jsonify({"The Costumer is not Eligible": Value})


if __name__ == "__main__":
    app.run(debug=True)
