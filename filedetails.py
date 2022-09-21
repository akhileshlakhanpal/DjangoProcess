import os
import shutil
def details(filename,projectcode,projectname):
    dir=fr'{os.getcwd()}\media\final'
    if os.path.isdir(dir):
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
    else:
        os.mkdir(dir)
    source=os.getcwd()+'\\'+'media\\'+filename
    destination=dir
    vNewName=projectname+'_'+projectcode+'.'+filename.split('.')[-1]
    shutil.copy(source,destination+'\\'+vNewName)
    print("File Move Successfully")
