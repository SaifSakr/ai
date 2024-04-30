from flask import Flask, render_template, Response
import cv2
import numpy as np
import mediapipe as mp
import math
import matplotlib.pyplot as plt
from  biceb import Biceb_api 
from  jump import jump_api 
from  squat import squat_api 
from  yoga import yoga_api 


app = Flask(__name__)
app.register_blueprint(Biceb_api)
app.register_blueprint(jump_api)
app.register_blueprint(squat_api)
app.register_blueprint(yoga_api)
@app.route('/',methods=['GET', 'POST'])
def hello():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)