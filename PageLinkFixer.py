import os
import re

#opens a file, finds all instances of an ip address, and replaces them with 'hartwelg.github.io'
def openFile(fileToFix):
    with open(fileToFix, 'r+') as inFile:
    # inFile = open(fileToFix, "r+")
        file = inFile.read()
        file = re.sub(r"/192.168.[0-9]{0,3}.[0-9]{0,3}/gm", 'hartwelg.github.io', file)
        inFile.seek(0)
        inFile.write(file)
        inFile.truncate()
    # print(inFile.readlines())
    # matches = re.finditer(r"/192.168.[0-9]{0,3}.[0-9]{0,3}/gm", inFile.read())
    # for item in matches:
    #     print(item)
    #     print(item.group())
    # inFile.close()
    return "replaced"

def main():
    #tool starts reading from directory it is placed in
    rootDirectory = '.'
    #keeps track of the name of the directory it is currently in, a list of subdirectories, and a list of files
    for dirName, subdirList, fileList in os.walk(rootDirectory):
        # print('Found directory: %s' % dirName)

        #find "index.html" in its list of files and open it with openFile()
        for fname in fileList:
            if fname == 'index.html':
                print('in directory: %s: found \n\t%s' % (dirName, fname))
                openFile(fname)
            # print('\t%s' % fname)
    return

if __name__ == "__main__":
    main()