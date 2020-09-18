import cv2
from flask import Flask, render_template, Response, url_for
import requests
from waitress import serve
import time

app = Flask(__name__, static_url_path='/static')
ip = 'admin:@10.16.130.59'

@app.route("/")
def home():
    return render_template("index.html")


j = 0

def get_video():
    global j
    capture = cv2.VideoCapture("rtsp://admin:@10.16.130.59/play1.sdp")

    # capture.set(cv2.CAP_PROP_BUFFERSIZE, 2) #Does not work
    print(capture.get(cv2.CAP_PROP_FPS))
    print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    capture.set(cv2.CAP_PROP_POS_AVI_RATIO, 1)
    
    if (capture.isOpened()):
        print("Camera is Open")
        while True:
            # if j % 7 == 0:
            # #time.sleep(0.025)
            #capture.set(cv2.CAP_PROP_FRAME_WIDTH, 176)#176
            #capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 120) #If the number increses the time between frames increases (the relationship is direclty proportional)
            if j % 9 == 0: #9 seems to work perfectly (in LAN)
                capture.set(cv2.CAP_PROP_FPS, 30)
                #Ver porqué de la nada ya no jala bien
            ret, img = capture.read()
            #capture.get(cv2.CAP_PROP_FPS)
            #capture.get(cv2.CAP_PROP_FRAME_WIDTH)
            #capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
            #time.sleep(4/30)
            if ret == True:
                #img = cv2.resize(img, (0,0), fx=0.95, fy=0.95)
                #if j % 2 == 0:
                frame = cv2.imencode('.jpg', img)[1].tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                # time.sleep(0.03)#0.025
                # print(j)
                j = j + 1
            else:
                print("Empty frame")
                print("Camera should be restarted")
                break
    else:
        print("Unable to Open Camera")      
            

@app.route("/show_video")
def show_video():
    return Response(get_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

# i = 0

@app.route("/commands/<cmd>", methods=["GET"])
def commands(cmd=None):
    # global i
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
    # print("Iteration" + str(i) + " Status: " + str(r.status_code))
    # i = i + 1
    return ("nothing")


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5003)
