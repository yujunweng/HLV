import os


def walk(root):
    for rootdir, dirs, files in os.walk(root):
        for file in files:
            print(file)
        
        
def get_dirs_files(root, files, dirs):
    dirsOrFiles = os.listdir(root)      # 列出目錄下所有資料夾和檔案
    for dirOrfile in dirsOrFiles:       # 逐一檢視
        nowDir = os.path.join(root, dirOrfile)
        #print(dirOrfile)
        if os.path.isdir(nowDir):         # 如果是資料夾
            write_txt(files)
            files = []
            dirs.append(dirOrfile)      # 加入這個資料夾 
            get_dirs_files(nowDir, files, dirs)   # 進入這個資料夾
        else:
            files.append(dirOrfile)   
    write_txt(files)
    return dirs
    
    
def get_file_name_type(fileName):
    """取得檔名與副檔名"""
    nameAndTypes = fileName.split(".", fileName.count("."))
    if len(nameAndTypes) > 1:
        ftype = nameAndTypes[-1]
        fname = ''
        for i in range(len(nameAndTypes)-1):
            fname += str(nameAndTypes[i])
    else:
        ftype = ''
        fname = nameAndTypes[0]
    return fname, ftype


def write_txt(files, mode='a+', fields=None):
    """files is a list"""
    with open("./FileNames.txt", mode=mode, encoding='big5') as wFile:
        if fields is not None:
            wFile.write(fields)
        for file in files:
            name, fileType = get_file_name_type(file)
            wFile.write(name+","+fileType)
            wFile.write("\n")



if __name__ == '__main__':
    root = os.getcwd()
    files = [] 
    dirs = []
    get_dirs_files(root, files, dirs)    