
from flask import Flask, json, request
import socket

api = Flask(__name__)

@api.route('/', methods=['POST'])
def press_right():
        print(request.data)
        return {'msg': 'Success'}

if __name__ == '__main__':
        name = socket.gethostname()
        print("\nCommand: http://" + socket.gethostbyname(name.split('.')[0]) + ":6786/right\n\n\n\n___________________________________")
        api.run(host='0.0.0.0', port='6786')
