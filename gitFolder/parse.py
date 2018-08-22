import re

def findFiles(folder_name, html):
    raw_files = re.findall(r"%s/[A-Za-z1-9_&-]+.[A-Za-z]+" % folder_name, html)
    files = []
    for fl in raw_files:
        if '.' not in fl:
            continue
        temp = fl.split('/')[-1]
        files.append(temp)

    return files

def getCode(html):
    code = ""
    check = 0
    for line in html.split('\n'):
        if "class=\"blob-code blob-code-inner js-file-line\"" in line:
            index = line.find(">")
            current_line = line[index:]
            for char in current_line:
                if char == '>':
                    check = 1
                    continue
                if char == '<':
                    check = 0
                    
                if check:
                    code += char
    
            if "&quot;" in code:
                code = code.replace("&quot;", '"')
            elif "&#39;" in code:
                code = code.replace("&#39;", "'")
            elif "&gt;" in code:
                code = code.replace("&gt;", '>')
            elif "&lt;" in code:
                code = code.replace("&lt;", '<')
            elif "&amp;" in code:
                code = code.replace("&amp;", '&')
            code += '\n'

    return code

def findFolders(url, html):
    sub_folder = url[19:]
    return re.findall(r"%s/[A-Za-z1-9_&-]+" % (sub_folder), html)