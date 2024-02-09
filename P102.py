import os
import shutil
from_dir="C:/Users/hp/Desktop/Mukundan/Python (pro)/C102_assets-main"
to_dir="C:/Users/hp/Desktop"
img_extensions=[".txt", ".docx", ".pdf"]
file_list=os.listdir(from_dir)
print(file_list)
for file in file_list:
    name,ext=os.path.splitext(file)
    if ext == "":
        continue
    if ext in img_extensions:
        path1=from_dir+"/"+file
        path2=to_dir+"/doc_folder"
        path3=path2+"/"+file
        if(os.path.exists(path2)):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)