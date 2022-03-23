from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

def fetchDetails():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name),str(host_ip)

@app.route('/')
def hello():
    #name = request.args.get("name", "World")
    #return f'Hello, {escape(name)}!'
    return '<p>Hello World</p>'

@app.route('/health')
def health():
    return jsonify(Status='UP')

@app.route('/details')
def details():
    hostname , IP = fetchDetails()
    return render_template('index.html',hostname=hostname,IP=IP)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)