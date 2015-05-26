#!/usr/bin/env python
import os
import zipfile



class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

if __name__ == '__main__':
#Renaming files OSHpark style
    print('Renaming files...\n')   
    for filenames in os.listdir(".."):
        if os.path.splitext(filenames)[1] == '.brd':
            if filenames[8] != ('autosave' or 'AUTOSAVE'):
                Pname = filenames[:-4] 
                
    for filenames in os.listdir("."):
        
        ext = os.path.splitext(filenames)[1]
        
        if ext == '.drl':
            os.rename(filenames, Pname + '.XLN')
        else:
            for case in switch(filenames):
                if case('Board_outline.art'):
                    os.rename(filenames, Pname + '.GKO')
                    break
                if case('Silkscreen_top.art'):
                    os.rename(filenames, Pname + '.GTO')
                    break
                if case('Silkscreen_bot.art'):
                    os.rename(filenames, Pname + '.GBO')
                    break
                if case('Soldermask_top.art'):
                    os.rename(filenames, Pname + '.GTS')
                    break
                if case('Soldermask_bot.art'): 
                    os.rename(filenames, Pname + '.GBS')
                    break
                if case('1_TOP.art'):
                    os.rename(filenames, Pname + '.GTL')
                    break
                if case('2_BOTTOM.art'):
                    os.rename(filenames, Pname + '.GBL')
                    break
    
    #Adding file to Zip archive            
    print('Creating ZIP archive\n')
    zf = zipfile.ZipFile(Pname + '.zip',  mode='w')
    
    try:
        for filenames in os.listdir("."):
            if (filenames[:-4] == Pname) and (os.path.splitext(filenames)[1] != '.zip'):
                zf.write(filenames)
    finally:
        print('Closing ZIP file\n')
        zf.close()        
            
    exit()