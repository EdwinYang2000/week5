import os
import json
from flask import Flask

print (111)

def create_app():

    app = Flask('rmon')

    file = os.environ.get('RMON_CONFIG')
    content = ''
    with open(file) as f:
        for l in f:
            l = l.strip()
            if l.startswith('#'):
                continue
            else:
                content = content + l

    data = json.loads(content)
    for key in data:
        print (key)
        print (data.get(key))
        app.config[key.upper()] = data.get(key)

if __name__ == "__main__ " :
    create_app()
    #return app
