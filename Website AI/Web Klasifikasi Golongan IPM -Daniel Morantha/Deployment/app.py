from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model-DT-DanielMorantha.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Harapan_Lama_Sekolah = float(request.form['Harapan_Lama_Sekolah'])
        Pengeluaran_Perkapita = int(request.form['Pengeluaran_Perkapita'])
        Rerata_Lama_Sekolah = float(request.form['Rerata_Lama_Sekolah'])
        Usia_Harapan_Hidup = float(request.form['Usia_Harapan_Hidup'])


        values = np.array([[Harapan_Lama_Sekolah,Pengeluaran_Perkapita,Rerata_Lama_Sekolah,Usia_Harapan_Hidup]])
        prediction = model.predict(values)


        return render_template('index.html', prediction_text='Hasilnya adalah {}'.format(prediction))





if __name__ == "__main__":
    app.run(debug=True)

