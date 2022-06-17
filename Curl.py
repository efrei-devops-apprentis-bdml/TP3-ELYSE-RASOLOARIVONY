from flask import Flask,request
import os,requests


app = Flask(__name__)
@app.route('/', methods =['GET'])
def home():
    api_key = str(os.environ.get("API_KEY"))
    latitude = request.args.get("lat")
    longitude = request.args.get("lon")
    


    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}".format(lat=latitude,lon=longitude,API_key=api_key))

    data = response.json()
    
    html_data = f""" <p>{data} </p> """
    return html_data

if __name__ == "__main__":
    app.run(port =80,debug=True)
