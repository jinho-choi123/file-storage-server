import sqlite3

connect = sqlite3.connect('fileInfo.db')
cursor = connect.cursor()

def add_file_group(linkId, filenames):
    return cursor.execute("INSERT INTO FILE_TABLE VALUES(:linkId, :files)", {"linkId": linkId, "files": filenames})

def search_file_group(linkId):
    cursor.execute("SELECT * FROM FILE_TABLE WHERE linkId=?", (linkId,))
    data = cursor.fetchOne()
    return data.files

