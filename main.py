from flask import Flask, render_template, Response
from camera import VideoCamera
<<<<<<< HEAD


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

=======
import time
import pandas as pd

EMOTIONS_LIST = ["Angry", "Disgust","Fear", "Happy","Neutral", "Sad","Surprise"]

app = Flask(__name__)

#Creating a log file
log = pd.DataFrame(columns=EMOTIONS_LIST)
log_filename = time.strftime("%Y%m%d%H%M%S")
pd.to_pickle(log , f'logs/{log_filename}.pkl')

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')



@app.route('/test')
def model_page():
    return render_template('model.html')
>>>>>>> e5151adb4 (final)
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
<<<<<<< HEAD
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

=======
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed(log_filename=log_filename):
    return Response(gen(VideoCamera(logging=log_filename,link=0)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def plot_bar():
    while True:
        time.sleep(0.5)
        f = open("charts/chart", "rb")
        result = f.read()
        f.close()
        print("Plotting!!")
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + result + b'\r\n\r\n')
        
@app.route('/ratio_chart')
def ratio_chart():
    return Response(plot_bar(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
                    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
>>>>>>> e5151adb4 (final)
