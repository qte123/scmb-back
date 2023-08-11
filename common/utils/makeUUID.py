# 随机生成uuid
import uuid


def get_uuid():
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    return suid
