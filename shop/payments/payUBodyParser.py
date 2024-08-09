import urllib.parse

def payUParse(body):
    bobyStr = str(body, 'utf-8')
    bodyMaxJson = urllib.parse.parse_qs(bobyStr)
    bodyJson = {}

    for i in bodyMaxJson:
        bodyJson[i] = (bodyMaxJson.get(i))[0] # type: ignore
    return bodyJson