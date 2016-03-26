import os

#def loopDir():
rootdir = os.getcwd()

print rootdir

for subdir, dirs, files in os.walk(rootdir+'/.git'):

    for file in files:

        print os.path.join(subdir, file)
