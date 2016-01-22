import pycurl
import json
import StringIO
#import pdb; pdb.set_trace()

 
c = pycurl.Curl()
c.setopt(c.CONNECTTIMEOUT, 5)
c.setopt(c.TIMEOUT, 8)
c.setopt(c.FAILONERROR, True)
#c.setopt(c.ERRORBUFFER, errbuf)
#c.setopt(c.VERBOSE, True)
#c.setopt(c.COOKIEFILE, '')
c.setopt(c.HTTPHEADER, ['Accept: text/json', 'Accept-Charset: UTF-8'])


def create_responseWriterFor(contentType):
    pass


def httpGet(url):
    result = {}
    httpCode = 0
    contentType = ''
    response = StringIO.StringIO()

    try:
        c.setopt(c.WRITEFUNCTION, response.write)
        c.setopt(c.URL, url)
        c.setopt(c.POST, 0)
        c.setopt(c.PUT, 0)
        c.perform()
        contentType = c.getinfo(pycurl.CONTENT_TYPE)
    except pycurl.error, error:
        errno, errstr = error
        stacktrace = ""
        response.write(""" {"ok": false, "error": "request %s failed: %s"} """ %  (url, errstr, ))
    finally:
        httpCode = c.getinfo(pycurl.RESPONSE_CODE)

    if httpCode >= 400:
        result = json.loads(response.getvalue())
    elif contentType == 'application/json':
        result = json.loads(response.getvalue())

    return result


def httpPost(url, payload):
    result = {}
    httpCode = 0
    response = StringIO.StringIO()

    try:
        c.setopt(c.URL, url)
        c.setopt(c.POST, 1)
        c.setopt(c.POSTFIELDS, payload)
        c.perform()
    except pycurl.error, error:
        errno, errstr = error
        response.write(""" {"ok": false, "error": "request %s failed: %s"} """ %  (url, errstr, ))
    finally:
        httpCode = c.getinfo(pycurl.RESPONSE_CODE)

    if httpCode >= 400:
        result = json.loads(response.getvalue())
    else:
        result = response.getvalue() 

    return result

