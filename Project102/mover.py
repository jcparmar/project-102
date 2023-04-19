import os
import shutil

movefrom= "D:\Downloads"
moveto="D:\Document_Files"

fileslist=os.listdir("D:\Downloads")
#print(fileslist)

for a in fileslist:
    root,extention=os.path.splitext(a)
    print(root)

    if extention == " ":
        continue
    if extention in ['.txt','.doc','.docx','.pdf']:
        path1= movefrom+ '/' + a
        path2 = moveto + '/' + "Files"
        path3 = moveto + '/' + "Files" + '/' + a
        print("path1",path1)
        print("path2",path3)
    

    if os.path.exists(path2):
        print("Moving Your Files "+ a + "........")

        shutil.move(path1,path3)

    else:
        os.makedirs(path2)
        print("Moving your files" + a + "...........")
        shutil.move(path1,path3)





