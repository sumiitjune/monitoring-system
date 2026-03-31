from flask import Flask, jsonify
from flask_cors import CORS
import psutil
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Monitoring Server Running "

@app.route('/stats')
def stats():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    try:
        containers = subprocess.check_output(
            ["docker", "ps", "--format", "{{.Names}}"]
        ).decode().split("\n")
        containers = [c for c in containers if c]
    except Exception as e:
        containers = []

    return jsonify({
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "containers": containers
    })

@app.route('/logs/<name>')
def logs(name):
    try:
        output = subprocess.check_output(
            ["docker", "logs", "--tail", "20", name]
        ).decode()
        return jsonify({"logs": output})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)