import cv2
from flask import Flask, render_template, Response, url_for
import requests
from waitress import serve
import time

app = Flask(__name__, static_url_path='/static')
ip = 'admin:@10.16.130.59'

@app.route("/")
def home():
    return render_template("index6.html")

def get_video():
    capture = cv2.VideoCapture('rtsp://'+ip+':554/play1.sdp')
    capture.set(cv2.CAP_PROP_BUFFERSIZE, 3)
    while True:
        ret, img = capture.read()
        if ret == True:
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.025)
        else:
            break        

@app.route("/show_video")
def show_video():
    return Response(get_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/commands/<cmd>", methods=["GET"])
def commands(cmd=None):
    url = 'http://'+ip+'/cgi/ptdc.cgi?command='
    mov = cmd.lower()
    movs = {
    'right': 'set_relative_pos&posX=10&posY=0',
    'left': 'set_relative_pos&posX=-10&posY=0', 
    'up': 'set_relative_pos&posX=0&posY=10', 
    'down': 'set_relative_pos&posX=0&posY=-10', 
    'up-right': 'set_relative_pos&posX=10&posY=10',  
    'up-left': 'set_relative_pos&posX=-10&posY=10', 
    'down-right': 'set_relative_pos&posX=10&posY=-10', 
    'down-left': 'set_relative_pos&posX=-10&posY=-10', 
    'zoomin': 'set_relative_zoom&zoom_mag=0.5',
    'zoomout': 'set_relative_zoom&zoom_mag=-0.5',
    'home': 'go_home',
    'qube': 'goto_preset_position&presetName=Qube',
    'robot': 'goto_preset_position&presetName=Robot',
    'posctr': 'goto_preset_position&presetName=PosCtr',
    'cocas': 'goto_preset_position&presetName=Cocas',
    'takepos': 'goto_preset_position&presetName=TakePos',
    'pendulum': 'goto_preset_position&presetName=Pendulum'
    }
    
    url = url + movs[mov]
    r = requests.get(url)
    return ("nothing")

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5003)

