import urllib.request

def getHtml(url):
    try:
        data = urllib.request.urlopen(url)
        return data.read().decode("utf-8")
    except:
        return ""