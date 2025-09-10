import sqlite3, os
DB = os.path.join(os.path.dirname(__file__), '..', 'banks.db')
def _connect():
    return sqlite3.connect(DB)
def get_all_banks():
    conn=_connect(); cur=conn.cursor()
    cur.execute("SELECT bank_name, sector, risk_factor, cagr, camel_rating, customer_satisfaction, npa FROM banks")
    rows=cur.fetchall(); conn.close()
    keys=['bank_name','sector','risk_factor','cagr','camel_rating','customer_satisfaction','npa']
    return [dict(zip(keys,r)) for r in rows]
def get_banks_by_type(t):
    conn=_connect(); cur=conn.cursor()
    cur.execute("SELECT bank_name, sector, risk_factor, cagr, camel_rating, customer_satisfaction, npa FROM banks WHERE sector=?", (t,))
    rows=cur.fetchall(); conn.close()
    keys=['bank_name','sector','risk_factor','cagr','camel_rating','customer_satisfaction','npa']
    return [dict(zip(keys,r)) for r in rows]
def get_bank_by_name(name):
    conn=_connect(); cur=conn.cursor()
    cur.execute("SELECT bank_name, sector, risk_factor, cagr, camel_rating, customer_satisfaction, npa FROM banks WHERE bank_name=?", (name,))
    r=cur.fetchone(); conn.close()
    if not r: return None
    keys=['bank_name','sector','risk_factor','cagr','camel_rating','customer_satisfaction','npa']
    return dict(zip(keys,r))
