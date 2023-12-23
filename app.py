from flask import Flask,  redirect, url_for, render_template, request
import pickle

model = pickle.load(open("pipe.pkl" , 'rb'))

app = Flask(__name__)

@app.route('/')
def welcome():
    #print(round(model.predict([[1, 5.1,3.5,1.4	,0.2]])) )
    return render_template('index.html')


@app.route('/result/<int:score>')
def result(score):
    return "Your score is " + str(score)

@app.route('/predict' , methods = ['GET' , 'POST'])
def predict():
    sepal_length = request.form.get('sepal-length')
    petal_length = request.form.get('petal-length')
    petal_width = request.form.get('petal-width')
    sepal_width = request.form.get('sepal-width')
    
    prediction = (model.predict([[sepal_length, sepal_width, petal_length, petal_width ]]))[0]

    if prediction == 0:
        prediction = 'Setosa'
    elif prediction == 1:
        prediction = 'Versicolor'
    else:
        prediction = 'Virginica'
    return render_template('predict.html' , prediction = prediction )



@app.route('/pass/<int:score>')
def passed(score):
    return "You have failed with score of " + str(score)


@app.route('/fail/<int:score>')
def failed(score):
    return "you have failed with score of " + str(score)

@app.route('/grade/<int:score>')
def grade(score):
    if score >= 40:
        result = 'passed'
    else:
        result = 'failed'

    return redirect(url_for(result, score = score))


'''
jinja2 template engine
(%...%) --> for statements( conditions, for loops , etc)
{{...}}  --> for expressions to print output
{#...#}  --> for internal comments
'''



if __name__ == '__main__':
    app.run(host = '0.0.0.0' ,debug= True , port= 5000)