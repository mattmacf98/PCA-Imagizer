from flask import Flask, render_template, request
import random
import pca
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/pca_picture', methods=['POST'])
def preform_pca():
    path = request.form['picturePath'] 
    pca.createImage(path)
    dummy = random.randint(0,50)
    return render_template('showImages.html', key = dummy)

if __name__ == '__main__':
    app.run()