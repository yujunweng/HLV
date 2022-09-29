import os 
from pathlib import Path



def get_dir_file(root, files):
    dirs_or_files = os.listdir(root)
    for dir_or_file in dirs_or_files:
        path = os.path.join(root, dir_or_file)
        print(path)    
        if os.path.isdir(path):
            #print(dir_or_file, "is dir")
            write_files(files)
            files = []
            dirs.append(dir_or_file)
            get_dir_file(path, files)
        else:
            fileName = Path(dir_or_file).stem
            files.append(fileName)
            #print(dir_or_file, "is file")
    write_files(files)
    files = []    
    return dirs    
    
    
def write_files(files):
    """files is a list"""
    with open("./FileNames.txt", 'a+', encoding='big5') as wFile:
        for file in files:
            wFile.write(file)
            wFile.write("\n")
            
            
            
            
if __name__ =='__main__':
    dirs = []
    files = []
    root = os.getcwd()
    get_dir_file(root, files)    