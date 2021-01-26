from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello Dachochai from Server Start 5555"

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=80)
