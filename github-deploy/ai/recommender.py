def get_ai_insights(banks, preference_key):
    if not banks: return [], 'No banks'
    weights_map={
        'general':{'cagr':0.3,'npa':0.3,'cust':0.2,'risk':0.2},
        'low_npa':{'cagr':0.2,'npa':0.5,'cust':0.2,'risk':0.1},
        'high_cagr':{'cagr':0.5,'npa':0.2,'cust':0.2,'risk':0.1},
        'customer_first':{'cagr':0.2,'npa':0.2,'cust':0.5,'risk':0.1},
        'balanced':{'cagr':0.33,'npa':0.33,'cust':0.17,'risk':0.17}
    }
    pref=preference_key or 'general'; weights=weights_map.get(pref, weights_map['general'])
    risk_map={'Low':0.0,'Medium':0.5,'High':1.0}
    scored=[]
    for b in banks:
        cagr=float(b.get('cagr') or 0); npa=float(b.get('npa') or 0); cust=float(b.get('customer_satisfaction') or 0)
        risk=risk_map.get(b.get('risk_factor','Medium'),0.5)
        cagr_s=min(cagr/20.0,1.0); npa_s=1-min(npa/10.0,1.0); cust_s=min(cust/5.0,1.0); risk_s=1-min(risk/1.0,1.0)
        score=(cagr_s*weights['cagr'])+(npa_s*weights['npa'])+(cust_s*weights['cust'])+(risk_s*weights['risk'])
        scored.append((b,round(score,4)))
    scored.sort(key=lambda x:x[1], reverse=True)
    top3=[{'bank':x[0]['bank_name'],'sector':x[0]['sector'],'score':x[1]} for x in scored[:3]]
    return top3, 'AI summary generated (rule-based)'
