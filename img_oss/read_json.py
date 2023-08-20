import json


def read_json(jsonpath):
    f = open(jsonpath, 'r')
    content = f.read()
    a = json.loads(content)
    f.close()
    return a
