from flask import Flask

# 创建flask的应用对象
# __name__表示当前模块的名字，一般无需修改，默认会以当前文件所在目录作为文件搜寻目录
app = Flask(__name__)
# app.config.from_pyfile('config.cfg')
# class Config(object):
#     DEBUG = True
#
# app.config.from_object(Config)

# app.config["DEBUG"] = True

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
