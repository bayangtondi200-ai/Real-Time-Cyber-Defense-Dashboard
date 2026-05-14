from flask import Flask, render_template
from detector import analyze_logs
from log_generator import stream_logs

app = Flask(__name__)

logs = []
alerts = []

@app.route("/")
def index():
    return render_template("index.html", alerts=alerts[-10:])

def run_detection():
    for log in stream_logs():
        logs.append(log)

        new_alerts = analyze_logs(logs)
        for alert in new_alerts:
            if alert not in alerts:
                alerts.append(alert)

if __name__ == "__main__":
    import threading

    t = threading.Thread(target=run_detection)
    t.daemon = True
    t.start()

    app.run(debug=True)
