#In the name of God

import sys
import os
import codecs
#from khayyam import *

#NOW = JalaliDatetime.now().strftime('%N/%P/%K')
MAP = os.getcwd()

if MAP.find(u'\\') > 0:
    SLASH = u'\\'
else:
    SLASH = u'/'
    


def opj(path):
    """Convert paths to the platform-specific separator"""
    st = os.path.join(*tuple(path.split('/')))
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        st = '/' + st
    #print st    
    return st



DATABASE_PATH = os.path.join(MAP,opj(u'Database')+SLASH)

GUI_PATH      = os.path.join(MAP,opj(u'GUI')+SLASH)
RES_PATH      = os.path.join(MAP,opj(u'Res')+SLASH)

ICONS_PATH    = os.path.join(RES_PATH,opj(u'Icons')+SLASH)
PICS_PATH     = os.path.join(RES_PATH,opj(u'Pics')+SLASH)
SPALSH_PATH   = os.path.join(RES_PATH,opj(u'Splash')+SLASH)

UTILITY_PATH  = os.path.join(MAP,opj(u'Utility')+SLASH)
CONFIG_PATH   = os.path.join(MAP,opj(u'Config')+SLASH)
LOGS_PATH     = os.path.join(MAP,opj(u'Logs')+SLASH)

TEMPS_PATH    = os.path.join(MAP,opj(u'Temps')+SLASH)


def thistxt(filename):
    f = codecs.open(LOGS_PATH+filename,mode='r',encoding='utf-8')
    lines = f.readlines()
    f.close()
    txt = ''
    for t in range(len(lines)):
            txt = txt + '\n' + lines[t]
    #print txt
    return txt
    
