from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/calibration')
def calibration():
    return "Calibration"

@app.route('/agdisplay/<period>')
def agdisplay(period):
    return f"Agregrate {period} display"

@app.route('/agdownload/<period>')
def agdownload(period):
    return f"Agregate {period} download"

@app.route('/weeklydisplay')
def weeklydisplay():
    return "Weekly display"

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')