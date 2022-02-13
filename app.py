from flask import Flask, render_template, request, redirect ,flash ,send_file
import os
from os import remove
import pafy

app = Flask(__name__)

SECRET_KEY = 'bihb4swnw7d4fwec8datlmjbn8rklk9bed0v8g1xnbnbpug7yt3xprvwe6vhqjec34sy0nvoz774ynnb87y85vaw7hxzip1y1016c9gpd5axaf3fegsmruwpy3hei8sve4q4kvw3f8vr4ok691lukv648sur0zgnkh5yw67bugrr73ie0qu4tw0t7uhuome6j8jugtsu4rxxuc39ni6f64jmwrnq6u9g93pmg1vshcya96fwph73s5ocur'

path = os.getcwd() + '\\output\\'

def delete():
    for file in os.listdir(path):
        os.remove(path + file)

@app.route('/')
def index():
    os.remove(path + '.mp4')
    return render_template('index.html')

@app.route('/envia', methods=['POST'])
def envia():
    if request.method == 'POST':
        url = request.form['url']
        video = pafy.new(url)
        best = video.getbest(preftype="mp4", ftypestrict=False)
        best.download(filepath=path)
        p = path + best.filename
        return send_file(p, as_attachment=True)



if __name__ == '__main__':
    app.run(host='localhost', port=8000)