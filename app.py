from flask import Flask, render_template, request,send_file ,redirect
import os 
import pafy


app = Flask(__name__)

SECRET_KEY = 'secret_key_in_this_place'

path = os.getcwd() + '/output/'


@app.route('/')
def index():
    for file in os.listdir(path):
        os.remove(path+'/'+file)
        
    return render_template('index.html')

@app.route('/envia', methods=['POST'])
def envia():
    if request.method == 'POST':
        url = request.form['url']
        video = pafy.new(url)
        best = video.getbest(preftype="mp4",)
        best.download(filepath=path)
        p = path + best.filename
        return send_file(p, as_attachment=True)



if __name__ == '__main__':
    app.run(host='localhost', port=8000 )
