Berikut adalah **dokumentasi lengkap** proyek Anda berdasarkan penjelasan dan instruksi yang Anda berikan:

---

# Dep-Pur-IDS: Intrusion Detection System

Sistem ini digunakan untuk mendeteksi apakah sebuah koneksi jaringan merupakan **serangan (Attack)** atau **normal**, menggunakan model Machine Learning berbasis **Random Forest**.

---

## Struktur Direktori

```
Dep-Pur-IDS/
├── app.py                       # Aplikasi utama Flask
├── model/
│   ├── rf_model.pkl            # Model RandomForest hasil training
│   ├── lgb_model.pkl           # (Opsional) Model LightGBM jika ingin digunakan
│   └── encoders.pkl            # LabelEncoder untuk kolom kategorikal
├── requirements.txt            # Dependensi Python
├── static/                     # Folder asset statis (optional)
└── templates/
    └── index.html              # UI/UX form input & hasil prediksi
```

---

## Fitur Aplikasi

* Input manual data koneksi jaringan
* Prediksi hasil: **Attack** atau **Normal**
* Tampilan web responsif (Tailwind CSS)
* Support via `Flask` dan bisa dijalankan lokal atau via Docker

---

## Training Model (Offline)

Model dilatih menggunakan dataset yang sesuai dengan fitur berikut:

```python
REQUIRED_FEATURES = ['dur', 'proto', 'service', 'state', 'spkts', 'dpkts', 'sbytes', 'dbytes', 
    'rate', 'sttl', 'dttl', 'sload', 'dload', 'sloss', 'dloss', 'sinpkt', 
    'dinpkt', 'sjit', 'djit', 'swin', 'stcpb', 'dtcpb', 'dwin', 'tcprtt', 
    'synack', 'ackdat', 'smean', 'dmean', 'trans_depth', 'response_body_len',
    'ct_srv_src', 'ct_state_ttl', 'ct_dst_ltm', 'ct_src_dport_ltm', 
    'ct_dst_sport_ltm', 'ct_dst_src_ltm', 'is_ftp_login', 'ct_ftp_cmd', 
    'ct_flw_http_mthd', 'ct_src_ltm', 'ct_srv_dst', 'is_sm_ips_ports']
```

### Contoh simpan model dari training:

```python
joblib.dump(best_rf, "rf_model.pkl")
joblib.dump(best_lgb, "lgb_model.pkl")
joblib.dump(label_encoders, "encoders.pkl")
```

Lalu, salin file `.pkl` tersebut ke folder `model/`.

---


## Model Machine Learning

Model yang digunakan saat ini adalah:

* **RandomForestClassifier**
* LabelEncoder untuk kolom: `proto`, `service`, `state`

Jika ingin menggunakan algoritma lain seperti **LightGBM**, tinggal ubah baris di `app.py`:

```python
model = joblib.load('model/lgb_model.pkl')  # Jika ingin pakai LightGBM
```

---

## Menjalankan Aplikasi

### Secara Lokal

```bash
python app.py
```

Akses: [http://localhost:5000](http://localhost:5000)

> Pastikan Anda sudah menginstall dependensi:
>
> ```bash
> pip install -r requirements.txt
> ```

---

### Menggunakan Docker

1. **Build image:**

```bash
docker build -t flask-ids-app .
```

2. **Jalankan container:**

```bash
docker run -d -p 5000:5000 flask-ids-app
```

3. **Akses aplikasi:**

Buka [http://localhost:5000](http://localhost:5000) di browser Anda.

---

## UI/UX

Tampilan antarmuka ada di:

```
templates/index.html
```

Sudah menggunakan Tailwind CSS dan mendukung input seluruh fitur yang diperlukan. Form akan tampil otomatis berdasarkan nama kolom `REQUIRED_FEATURES`.

---

Jika Anda butuh file `README.md` versi Markdown untuk langsung commit ke GitHub, saya bisa bantu generate juga. Mau saya buatkan?
