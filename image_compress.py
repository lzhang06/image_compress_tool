import os
import sys
from PIL import Image, ImageFile

from os import remove, rename, walk, stat
from os.path import getsize, isfile, isdir, join
import fnmatch

def compress_me(filename):
    filepath = os.path.join(os.getcwd(), filename)
    origsize = getsize(filepath)
    picture = Image.open(filepath)
    
    dim = picture.size
    
    ImageFile.MAXBLOCK = picture.size[0] * picture.size[1]
    
    newfile_name = "Compressed_"+filename        
    picture.save(newfile_name,"JPEG",optimize=True,quality=85) 

    newsize = getsize(os.path.join(os.getcwd(), newfile_name))    
    percent = (origsize - newsize)/float(origsize)*100    
    print('The file compressed from {} to {} or {}'.format(origsize, newsize, percent))
    
    
def process_dir(dirpath):
    #change the working directory
    os.chdir(dirpath)
    
    file_count = 0
    for root, dirs, files in os.walk(dirpath):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.gif', '.png')):
                file_count+=1
                compress_me(filename)
    return file_count