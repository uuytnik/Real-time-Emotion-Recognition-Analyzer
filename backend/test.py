# Flask app.py
from flask import Flask, Response, render_template, jsonify
import cv2
from deepface import DeepFace
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域
cap = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

def gen_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/emotion')
def emotion_api():
    ret, frame = cap.read()
    if not ret:
        return jsonify({'error': 'no frame'})
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        face = result if isinstance(result, dict) else result[0]
        return jsonify(face['emotion'])
    except:
        return jsonify({'error': 'no face detected'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#在浏览器访问http://127.0.0.1:5000/