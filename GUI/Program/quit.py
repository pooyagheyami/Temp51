#In the name of God
# -*- coding: utf-8 -*-
#!usr/bin/env python



import wx


def size():
    return (-1,-1)

def main(panel=None):
    
    q = wx.GetActiveWindow()
    p = wx.GetApp()
    #print(dir(p))
    #print(dir(q.m_mgr))
    p.ExitMainLoop()
    q.m_mgr.Unlink()
    #q.m_mgr.Unbind()
    q.m_mgr.Destroy()
    #if str(q) == 'None':
    #    p.Exit()
    #    p.__del__()
        #wx.App_CleanUp()
    #else:
    #    q.Destroy()
        #wx.App_CleanUp()
    
if __name__ == '__main__':
    main(None)
