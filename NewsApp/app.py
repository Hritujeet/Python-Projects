from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

def getData(url):
    jsonData = requests.get(url).text
    # print(jsonData)
    data = json.loads(jsonData)
    # print(data['articles'])
    return data['articles']

@app.route("/")
def main():
    url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=945bc3a7e29646ed83805268870a45a4"
    data = getData(url)
    return render_template("index.html", data=data)
if __name__ == "__main__":
    app.run(debug=True)
