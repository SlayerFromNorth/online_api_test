from flask import Flask, request, jsonify
from PIL import Image


import fastbook
fastbook.setup_book()

from fastbook import *


path = Path()
learn = load_learner(path/'export.pkl')



app = Flask(__name__)

@app.route("/marius", methods=["POST"])
def process_image():
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)
    img.save("testerIMG.jpg")
    prediction = learn.predict("testerIMG.jpg")
    return jsonify({'msg': 'success', 'size': prediction[0]})

import os
if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
        port=int(os.getenv('PORT', 3342)))
