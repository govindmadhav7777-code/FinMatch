from flask import Flask, render_template, request, redirect, url_for
from models.bank_model import get_all_banks, get_banks_by_type, get_bank_by_name
from ai.recommender import get_ai_insights
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    banks = get_all_banks()
    return render_template('index.html', banks=banks)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/banks/<bank_type>')
def banks_page(bank_type):
    bank_type = bank_type.capitalize()
    if bank_type not in ('Public', 'Private'):
        return 'Invalid bank type', 404
    banks = get_banks_by_type(bank_type)
    return render_template('banks.html', banks=banks, bank_type=bank_type)

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    banks = get_all_banks()
    bank1 = bank2 = None
    if request.method == 'POST':
        name1 = request.form.get('bank1')
        name2 = request.form.get('bank2')
        if name1:
            bank1 = get_bank_by_name(name1)
        if name2:
            bank2 = get_bank_by_name(name2)
    return render_template('compare.html', banks=banks, bank1=bank1, bank2=bank2)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    banks = get_all_banks()
    results = None
    summary = None
    if request.method == 'POST':
        pref = request.form.get('preference') or 'general'
        results, summary = get_ai_insights(banks, pref)
    return render_template('recommend.html', banks=banks, results=results, summary=summary)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
