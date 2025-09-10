import sqlite3, os
DB = os.path.join(os.path.dirname(__file__), 'banks.db')
sample = [
    ('State Bank of India','Public','High',7.0,'A',3.8,6.1),
    ('Punjab National Bank','Public','High',6.5,'B',3.5,5.8),
    ('Bank of Baroda','Public','Medium',6.8,'B+',3.6,4.9),
    ('HDFC Bank','Private','Low',12.0,'A+',4.5,1.9),
    ('ICICI Bank','Private','Low',11.5,'A',4.2,2.1),
    ('Axis Bank','Private','Low',10.8,'A',4.0,2.3)
]
def create_db():
    if os.path.exists(DB):
        os.remove(DB)
    conn = sqlite3.connect(DB); cur = conn.cursor()
    cur.execute('''CREATE TABLE banks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bank_name TEXT, sector TEXT, risk_factor TEXT, cagr REAL, camel_rating TEXT, customer_satisfaction REAL, npa REAL
    )''')
    cur.executemany('INSERT INTO banks (bank_name, sector, risk_factor, cagr, camel_rating, customer_satisfaction, npa) VALUES (?,?,?,?,?,?,?)', sample)
    conn.commit(); conn.close()
    print('banks.db created at', DB)

if __name__ == '__main__':
    create_db()
