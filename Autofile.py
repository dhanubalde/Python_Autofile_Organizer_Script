# kedanubalde@gmail.com
# Autofile Organizer
import os
import shutil

print("Auto_File Organizer  ")
path = input("Enter Path from your Desktop [*]:")
files = os.listdir(path)


for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    if os.path.exists(path+"/" + extension):
        shutil.move(path + "/" + file, path + "/"+extension + "/"+file)
        print("Successfully Created ")
    else:
        os.makedirs(path+"/" + extension)
        shutil.move(path+"/" + file, path+"/"+extension)
        print("Please Try Again ! ")
