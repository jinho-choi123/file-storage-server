import uuid 
import os
ALLOWED_EXTENSIONS={'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3', 'mp4'}

def makeuid():
    return uuid.uuid4().hex

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def createDir(uid):
    try:
        if not os.path.exists(os.environ.get('UPLOAD_FOLDER')+uid):
            os.makedirs(os.environ.get('UPLOAD_FOLDER')+uid)
    except OSError:
        print('Error: Creating directory failed')
