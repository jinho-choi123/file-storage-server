from flask import Flask, render_template, request, send_from_directory
from dotenv import load_dotenv
from utils import createDir, makeuid, allowed_file
import os
from werkzeug.utils import secure_filename
from werkzeug.security import safe_join
from database import add_file_group, search_file_group
import sqlite3
from math import ceil
app = Flask(__name__)
load_dotenv()
connect = sqlite3.connect('fileInfo.db', check_same_thread = False, isolation_level=None)
cursor = connect.cursor()


UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = os.environ.get('MAX_CONTENT_LENGTH')


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/link')
def linkpage():
    return render_template('link.html')

@app.route('/p2p')
def p2p():
    return render_template('p2p.html')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist("files")
    if files == []:
        return render_template("fail.html", msg="no file")
    linkId = makeuid()
    createDir(linkId)
    size = 0
    cnt = 0
    expirationHours = 3
    for file in files:
        filename = secure_filename(file.filename)
        if allowed_file(filename):
            filepath = os.path.join(*[UPLOAD_FOLDER, linkId, filename])
            file.save(filepath)
            cnt += 1
            size += os.path.getsize(filepath)
        else:
            return render_template("fail.html", msg="please check uploading file's extention. we only allow txt, pdf, png, jpg, jpeg, gif, mp3, mp4")
    size = ceil(size / pow(2, 10))
    add_file_group(cursor, linkId, expirationHours, cnt, size)
    return render_template("success.html", data={"linkId": linkId, "cnt": cnt, "size": size, "expirationHours": expirationHours})

@app.route('/downloadlist')
def downloadlist():
    linkId = request.args.get('linkid')
    filesData = search_file_group(cursor, linkId)
    if(filesData == None):
        return render_template("fail.html", msg="please check your LinkID and expiration datetime")
    filepath = safe_join(UPLOAD_FOLDER, linkId)
    filenameList = os.listdir(filepath)
    filenumbers = filesData[2]
    filesize = filesData[3]
    expiredAt = filesData[1]
    return render_template("download.html", data={"linkId": linkId, "filenames": filenameList, "filenumbers": filenumbers, "size": filesize, "expiredAt": expiredAt})

@app.route('/download')
def download():
    linkId = request.args.get('linkid')
    filename = request.args.get('filename')
    filepath = safe_join(UPLOAD_FOLDER, linkId)
    return send_from_directory(filepath, filename, as_attachment=True)



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=9000)