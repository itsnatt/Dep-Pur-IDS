from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model dan encoder saat start
model = joblib.load('model/rf_model.pkl')
label_encoders = joblib.load('model/encoders.pkl')

REQUIRED_FEATURES = ['dur', 'proto', 'service', 'state', 'spkts', 'dpkts', 'sbytes', 'dbytes', 
    'rate', 'sttl', 'dttl', 'sload', 'dload', 'sloss', 'dloss', 'sinpkt', 
    'dinpkt', 'sjit', 'djit', 'swin', 'stcpb', 'dtcpb', 'dwin', 'tcprtt', 
    'synack', 'ackdat', 'smean', 'dmean', 'trans_depth', 'response_body_len',
    'ct_srv_src', 'ct_state_ttl', 'ct_dst_ltm', 'ct_src_dport_ltm', 
    'ct_dst_sport_ltm', 'ct_dst_src_ltm', 'is_ftp_login', 'ct_ftp_cmd', 
    'ct_flw_http_mthd', 'ct_src_ltm', 'ct_srv_dst', 'is_sm_ips_ports']

def predict_new_data(new_data):
    df = pd.DataFrame([new_data])
    
    for col in ['proto', 'service', 'state']:
        if col in df.columns:
            le = label_encoders[col]
            df[col] = df[col].apply(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

    for col in REQUIRED_FEATURES:
        if col not in df.columns:
            df[col] = 0

    df = df[REQUIRED_FEATURES]

    proba = model.predict_proba(df)[0][1]
    pred = int(proba >= 0.4)

    return {'prediction': pred, 'probability': round(proba, 4)}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        input_data = {key: request.form.get(key, type=float if key != 'proto' and key != 'state' and key != 'service' else str) for key in REQUIRED_FEATURES}
        result = predict_new_data(input_data)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
