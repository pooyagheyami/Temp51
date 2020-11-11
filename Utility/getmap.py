#In the name of God
# -*- coding: utf-8 -*-
#!usr/bin/env python

import wx
import codecs

class GetMapKey:
    def __init__(self):
        self.row1 , self.row2 , self.row3 , self.row4 = [] , [] , [] , []
        self.srow1 , self.srow2 , self.srow3 , self.srow4 = [] , [] ,[] , []
        

    def Loadmap(self,filename):
        f = codecs.open(filename,encoding='utf-8')
        lines = f.readlines()
        f.close()
        i = 1
        #print lines[3]
        for car in range(14):
            self.row1.append(lines[car+i].split(u'\n')[0])
            
        i = 15
       
        for car in range(12):
            self.row2.append(lines[car+i].split(u'\n')[0])
            
        i = 27
        
        for car in range(11):
            self.row3.append(lines[car+i].split(u'\n')[0])
            
        i = 38
       
        for car in range(10):
            self.row4.append(lines[car+i].split(u'\n')[0])
            
        i = 48
            
       
        for car in range(14):
            self.srow1.append(lines[car+i].split(u'\n')[0])
            
        i = 62
        
        for car in range(12):
            self.srow2.append(lines[car+i].split(u'\n')[0])
            
        i = 74
        
        for car in range(11):
            self.srow3.append(lines[car+i].split(u'\n')[0])
            
        i = 85
         
        for car in range(10):
            
            self.srow4.append(lines[car+i].split(u'\n')[0])
            

        #print lines[5]    

        #print self.row1,self.row2,self.row3,self.row4
        #print self.srow1#,self.srow2,self.srow3,self.srow4
        #return self.row1,self.row2,self.row3,self.row4 , self.srow1,self.srow2,self.srow3,self.srow4

            

    def Savemap(self,filename,Data):
        f = codecs.open(filename,'w',encoding='utf-8')
        f.write(u'# -*- coding: utf-8 -*- \n')
        for D in Data:
            f.write(D)
        f.close()

        
'''

row1 = [u'`',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'0',u'-',u'=',u'<-']
row2 = [u'ஆ',u'ஈ',u'ஊ',u'ஐ',u'ஏ',u'ள',u'ற',u'ன',u'ட',u'ண',u'ச',u'ஞ']
row3 = [u'அ',u'இ',u'உ',u'்',u'எ',u'க',u'ப',u'ம',u'த',u'ந',u'ய']
row4 = [u'ஔ',u'ஓ',u'ஒ',u'வ',u'ங',u'ல',u'ர',u',',u'.',u'ழ']



srow1 = [u'~',u'!',u'@',u'#',u'$',u'%',u'^',u'&',u'*',u'(',u')',u'_',u'+',u'<-']
srow2 = [u'ஸ',u'ஷ',u'ஜ',u'ஹ',u'ஸ்ரீ',u'க்ஷ',u'',u'',u'',u'',u'',u'']
srow3 = [u'௹',u'௺',u'௸',u'ஃ',u'',u'',u'',u'',u"",u"",u""]
srow4 = [u'௳',u'௴',u'௵',u'௶',u'௷',u'',u'',u'',u'',u'']

arow1 = []
arow2 = []
arow3 = []
arow4 = []

asrow1 = []
asrow2 = []
asrow3 = []
asrow4 = []

'''

