from ast import arg
import json
import subprocess
from flask import Flask, request, abort
app = Flask(__name__)

VERIFY_TOKEN = 'Lixo'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        resposta = request.json
        try:
            if resposta['text']['body']:
                strResp = str(resposta)
#                paramProg = '"' + strResp + '"'
#                progToCall = 'testando.exe ' + paramProg
#                subprocess.call(progToCall)
                return 'Success', 200
        except:
            return 'Success', 200
    else:

        if request.method == 'GET':
            ##print('hub.verify_token', request.args.get('hub.verify_token'))
            print('metodo', request.method)
            if request.args.get('hub.verify_token') == VERIFY_TOKEN:
                return request.args.get('hub.challenge')
            else:
                return 'Informações erradas'


if __name__ == '__main__':
    app.run()
