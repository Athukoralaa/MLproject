from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from src.components.data_ingestion import model_train


from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application
app.debug=True

## Route for a home page


@app.template_filter('number_format')
def number_format(value):
    return "{:,.2f}".format(value)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = CustomData(
            area=request.form.get('area'),
            bedrooms=request.form.get('bedrooms'),
            bathrooms=request.form.get('bathrooms'),
            stories=request.form.get('stories'),
            mainroad=request.form.get('mainroad'),
            guestroom=request.form.get('guestroom'),
            basement=request.form.get('basement'),
            hotwaterheating=request.form.get('hotwaterheating'),
            airconditioning=request.form.get('airconditioning'),
            parking=request.form.get('parking'),
            prefarea=request.form.get('prefarea'),
            furnishingstatus=request.form.get('furnishingstatus')
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    #model_train()
    app.run(host="0.0.0.0")        