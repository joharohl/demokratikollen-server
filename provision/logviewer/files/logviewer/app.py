# Import flask and template operators
from flask import Flask, render_template
from docker import Client
import os
import subprocess
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/log.txt')
def log_test():
    log = ''
    with open('/home/deploy/deploy.log', encoding='UTF-8') as f:
        for i, line in enumerate(f.readlines()):
            log += str(i) + ': '
            log += line + '\n'
            log += '<br>'
    return log

@app.route('/docker/containers')
def docker_containers():
    result = subprocess.Popen(["docker", "ps",'-a'], stdout=subprocess.PIPE)

    data = result.communicate()[0].decode('utf-8')

    return html_escape(data)

@app.route('/docker/images')
def docker_images():
    result = subprocess.Popen(["docker", "images"], stdout=subprocess.PIPE)

    data = result.communicate()[0].decode('utf-8')

    return html_escape(data)

@app.route('/docker/top')
def top():
    result = subprocess.Popen(["top", "-bn1"], stdout=subprocess.PIPE)

    data = result.communicate()[0].decode('utf-8')

    return html_escape(data)


html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    " ": "&nbsp;",
    "\n": "<br>"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

if __name__ == '__main__':
    app.debug = True
    app.run(port=8080,host='0.0.0.0')
