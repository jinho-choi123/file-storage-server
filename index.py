from flask import Flask, render_template, redirect, url_for
from flask import request 
from dotenv import load_dotenv
from utils import createDir, makeuid
import os
from werkzeug.utils import secure_filename
import zipfile
from database import add_file_group, search_file_group

app = Flask(__name__)
load_dotenv()

UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
        if files is []:
            return 'no files'
        linkId = makeuid()
        createDir(linkId)
        filenamelist = []
        for file in files:
            filename = secure_filename(file.filename)
            filenamelist.append(filename)
            file.save(UPLOAD_FOLDER+linkId+'/'+filename)
        add_file_group(linkId, filenamelist)
        return [linkId, 'link']

@app.route('/downloadlist')
def download():
    linkId = request.args.get('linkid')
    filenamelist = search_file_group(linkId)
    return filenamelist




if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=9000)