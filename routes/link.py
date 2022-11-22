from flask import request 

def upload():
    files = request.files.getlist("files")
    for file in files:
        print('hello world!')
    return "hello world!"