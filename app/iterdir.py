#from app import app
import os

def loopDir():
    #rootdir = os.getcwd()
    flst=[]
    #print rootdir

    for subdir, dirs, files in os.walk('app/static/uploads'):

        for file in files:
            if file[-4:]=='.jpg':
                flst.append("""<li> <img src="/static/uploads/{}" alt="pic"width="410" height="305" </li>""".format(file))
            else:
                flst.append("<li>{}</li>".format(file))

            #os.path.join(subdir,file) #delete subdir to get file names onl
        return flst

