import streamlit as st
import pandas as pd
import pickle
import numpy as np

@st.cache_data
def load_model():
    with open('model/dropout_predictor.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

# Memuat model dan preprocessor
data = load_model()
model = data["model"]
preprocessor = data["preprocessor"]

# Tampilan Utama Aplikasi
st.set_page_config(page_title="Prediksi Dropout", page_icon="🎓")
st.title("🎓 Prediksi Potensi Dropout Mahasiswa")
st.write("Aplikasi ini membantu Jaya Jaya Institut mengidentifikasi mahasiswa yang berisiko dropout menggunakan model Machine Learning. Masukkan data di bawah untuk melihat prediksi.")

# Form Input Pengguna
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Data Diri & Keuangan")
        tuition_fees_up_to_date = st.selectbox("Status Kelunasan SPP", (1, 0), format_func=lambda x: 'Lunas' if x == 1 else 'Belum Lunas')
        scholarship_holder = st.selectbox("Status Beasiswa", (1, 0), format_func=lambda x: 'Penerima' if x == 1 else 'Bukan Penerima')
        age_at_enrollment = st.slider("Usia saat Pendaftaran", 17, 70, 20)
        gender = st.selectbox("Jenis Kelamin", (0, 1), format_func=lambda x: 'Perempuan' if x == 0 else 'Laki-laki')

    with col2:
        st.subheader("Data Akademik")
        curricular_units_1st_sem_approved = st.number_input("Jumlah SKS Lulus Semester 1", min_value=0, max_value=26, value=10)
        curricular_units_1st_sem_grade = st.number_input("Rata-rata Nilai Semester 1", min_value=0.0, max_value=20.0, value=12.0, step=0.1)
        curricular_units_2nd_sem_approved = st.number_input("Jumlah SKS Lulus Semester 2", min_value=0, max_value=20, value=10)
        curricular_units_2nd_sem_grade = st.number_input("Rata-rata Nilai Semester 2", min_value=0.0, max_value=20.0, value=12.0, step=0.1)

    # Tombol submit untuk form
    submitted = st.form_submit_button("✨ Prediksi Status Mahasiswa")


# Logika Setelah Tombol Ditekan
if submitted:
    # Membuat DataFrame dari input pengguna
    input_data = pd.DataFrame({
        'Tuition_fees_up_to_date': [tuition_fees_up_to_date], 'Scholarship_holder': [scholarship_holder],
        'Age_at_enrollment': [age_at_enrollment], 'Gender': [gender],
        'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
        'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
        'Curricular_units_2nd_sem_approved': [curricular_units_2nd_sem_approved],
        'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],
        'Marital_status': [1], 'Application_mode': [1], 'Application_order': [1], 'Course': [9500],
        'Daytime_evening_attendance': [1], 'Previous_qualification': [1], 'Previous_qualification_grade': [130],
        'Nacionality': [1], 'Mothers_qualification': [1], 'Fathers_qualification': [1],
        'Mothers_occupation': [5], 'Fathers_occupation': [5], 'Admission_grade': [130], 'Displaced': [0],
        'Educational_special_needs': [0], 'Debtor': [0], 'International': [0],
        'Curricular_units_1st_sem_credited': [0], 'Curricular_units_1st_sem_enrolled': [6],
        'Curricular_units_1st_sem_evaluations': [6], 'Curricular_units_1st_sem_without_evaluations': [0],
        'Curricular_units_2nd_sem_credited': [0], 'Curricular_units_2nd_sem_enrolled': [6],
        'Curricular_units_2nd_sem_evaluations': [6], 'Curricular_units_2nd_sem_without_evaluations': [0],
        'Unemployment_rate': [12], 'Inflation_rate': [1.2], 'GDP': [1.7]
    })
    
    # Melakukan prediksi
    prediction = model.predict(preprocessor.transform(input_data))
    prediction_proba = model.predict_proba(preprocessor.transform(input_data))

    # Menampilkan hasil
    st.subheader("Hasil Prediksi")
    
    # Menggunakan .item() untuk mengambil nilai tunggal
    if prediction.item() == 1:
        prob = prediction_proba[0][1]
        st.error(f"Mahasiswa Berpotensi **DROPOUT** (Probabilitas: {prob*100:.2f}%)")
        st.write("Tingkat Keyakinan Prediksi:")
        st.progress(prob)
    else:
        prob = prediction_proba[0][0]
        st.success(f"Mahasiswa Berpotensi **LULUS** (Probabilitas: {prob*100:.2f}%)")
        st.write("Tingkat Keyakinan Prediksi:")
        st.progress(prob)