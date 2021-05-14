# 本地网络接口
# http://localhost:8110
import os
import json
from flask import Flask,render_template,request,send_from_directory
from lichv.utils import * 


app = Flask(__name__,template_folder=os.path.join(os.getcwd(),"public/"),static_folder=os.path.join(os.getcwd(),"public/_assets"))


@app.route('/', methods=['POST', 'GET'])
def index():
	return {"state":2000,"msg":"success"}

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'public'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8110)
