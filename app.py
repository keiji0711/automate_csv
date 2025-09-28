from flask import Flask, render_template, request, redirect, flash, url_for
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

CSV_FILE = 'survey_data.csv'

# Ensure CSV exists and write header if not
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            "AgeGroup","Gender","MaritalStatus","Occupation","Income",
            "LoanType","LoanAmount","LoanTerm","Amortization","Downpayment",
            "PropertyType","Location","Purpose","Reason","Satisfaction",
            "FuturePlan","Factor_Interest","Factor_Reputation","Factor_Location",
            "Factor_Property","Factor_Amortization","Factor_Rental"
        ])

@app.route('/', methods=['GET', 'POST'])
def manual_entry():
    if request.method == 'POST':
        # Collect all form data
        data = {key: request.form.get(key,"") for key in [
            "AgeGroup","Gender","MaritalStatus","Occupation","Income",
            "LoanType","LoanAmount","LoanTerm","Amortization","Downpayment",
            "PropertyType","Location","Purpose","Reason","Satisfaction",
            "FuturePlan","Factor_Interest","Factor_Reputation","Factor_Location",
            "Factor_Property","Factor_Amortization","Factor_Rental"
        ]}

        # Save to CSV
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data.values())

        flash("✅ Survey entry saved successfully!", "success")
        return redirect(url_for('manual_entry'))

    return render_template('survey.html')

if __name__ == "__main__":
    app.run(debug=True)
