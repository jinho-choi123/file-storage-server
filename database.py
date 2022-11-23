from datetime import datetime, timedelta
from pytz import timezone


def add_file_group(cursor, linkId, expirationHours, filesNumbers, fileSize):
    cursor.execute("CREATE TABLE IF NOT EXISTS FILE_TABLE(linkId, expiredAt, number, size)")
    now = datetime.now(timezone('Asia/Seoul'))
    expiredAt = now + timedelta(hours=expirationHours)
    cursor.execute("INSERT INTO FILE_TABLE VALUES(:linkId, :expiredAt, :numbers, :size)", {"linkId": linkId, "expiredAt": expiredAt, "numbers": filesNumbers, "size": fileSize})
    return 0

def search_file_group(cursor, linkId):
    now = datetime.now(timezone('Asia/Seoul'))
    cursor.execute("SELECT * FROM FILE_TABLE WHERE linkId=?", (linkId, ))
    data = cursor.fetchone()
    return data

