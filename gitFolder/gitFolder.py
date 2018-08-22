import downloader
import parse
import sys

def createFolder(folder_name):
    import os
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

def subFolder(url, html, path):
    folders = parse.findFolders(url, html)
    
    if not len(folders):
        return 0
    else:
        for folder in folders:
            folder_name = folder.split('/')[-1]
            url = "https://github.com/" + folder
            sub_folder = path + folder_name + '\\'
            html = downloader.getHtml(url)
            files = parse.findFiles(folder_name, html)

            createFolder(sub_folder)
            subFolder(url, html, sub_folder)
            writeFile(url, files, sub_folder)

def writeFile(url, files, folder):
    if len(files):
        fl_count = 0
        fl_quant = len(files)
        for fl in files:
            fl_name = folder + fl
            fl_url = url + "/" + fl
            html = downloader.getHtml(fl_url)
            code = parse.getCode(html)

            with open(fl_name, 'w') as f:
                f.write(code)
            
            fl_count += 1
            print(" Folder {} Files: [{}/{}] downloaded.\r".format(folder, fl_count, fl_quant), end="")
    
        print()
    
    return 0

def main():
    argv = sys.argv[1:]
    if not len(argv):
        print("usage:\npython gitFolder.py https://github/[user]/[repository]/[folder name]\n")
        print("optional:\npython gitFolder.py https://github/[user]/[repository]/[Folder Name] -o [Output Folder]\n")
        exit()
    
    url = argv[0]
    folder_name = url.split('/')[-1]
    if '-o' in sys.argv:
        output = argv[2] + '\\'
        folder =  output + folder_name + '\\'
        createFolder(output)
        createFolder(output + folder_name)
    else:
        folder = folder_name + '\\'

    html  = downloader.getHtml(url)
    files = parse.findFiles(folder_name, html)

    subFolder(url, html, folder)
    writeFile(url, files, folder)

if __name__ == "__main__":
    main()
