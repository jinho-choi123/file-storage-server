from datetime import datetime, timedelta


def add_file_group(cursor, linkId):
    now = datetime.now()
    expiredAt = now + timedelta(days=1)
    return cursor.execute("INSERT INTO FILE_TABLE VALUES(:linkId, :expiredAt)", {"linkId": linkId, "expiredAt": expiredAt})

def search_file_group(cursor, linkId):
    cursor.execute("SELECT * FROM FILE_TABLE WHERE linkId=?", (linkId,))
    data = cursor.fetchOne()
    return data.files

