import os 
import shutil
source="/Users/kuberapaul/Downloads/C102_assets-main"
destination="/Users/kuberapaul/Downloads/C102_assets-main/documents"
list_of_files=os.listdir(source)
print(list_of_files)

for x in list_of_files:
    root,extension=os.path.splitext(x)
    print(root)
    print(extension)

    if extension=="":
        continue
    if extension in [".docx",".pdf",".ppt",".txt"]:
        path1=source+"/"+x
        path2=destination
        path3=destination+"/"+x
        if os.path.exists(path2):
            print("The destination folder aldready exists")
            shutil.move(path1,path3)
        else:
            print("Creating a new folder")
            os.mkdir(path2)
            shutil.move(path1,path3)