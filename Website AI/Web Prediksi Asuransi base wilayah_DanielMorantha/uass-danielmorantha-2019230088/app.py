from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model_uas.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')

def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    age, sex, bmi, childern, smoker, region = [x for x in request.form.values()]

#southwest':1,'southeast':2, 'northwest':3, 'northeast':4

    data = []

    data.append(int(age))
    data.append(int(bmi))
    data.append(int(childern))
    if sex == 'Laki-laki': #1
        data.extend([1])
    else: #0 perempuan
        data.extend([0])

    if smoker == 'Ya':
        data.extend([1])
    else:
        data.extend([0])

    if region == 'southwest':
        data.extend([1])
    elif region == 'southeast':
        data.extend([2])
    elif region == 'northwest':
        data.extend([3])
    else:
        data.extend([4])
    
    prediction = model.predict([data])
    output = round(prediction[0], 2)

    return render_template('index.html', insurance_cost=output, age=age, sex=sex, bmi=bmi, childern=childern, smoker=smoker, region=region)


if __name__ == '__main__':
    app.run(debug=True)