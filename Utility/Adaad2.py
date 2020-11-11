# -*- coding: utf-8 -*-
#In the name of God
#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import codecs
import unicodedata 
import string

MAX = 1000000000000000
MIN = 1
Dste = 1000
#C = 4

abjad = {u'ا':1,u'ب':2,u'ج':3,u'د':4,u'ه':5,u'و':6,u'ز':7,u'ح':8,u'ط':9,
        u'ي':10,u'ک':20,u'ل':30,u'م':40,u'ن':50,u'س':60,u'ع':70,u'ف':80,u'ص':90,
        u'ق':100,u'ر':200,u'ش':300,u'ت':400,u'ث':500,u'خ':600,u'ذ':700,u'ض':800,u'ظ':900,
        u'غ':1000,u'ی':10}


class Adaad:
    def __init__(self, num , txt):
        self.num = num
        self.txt = txt
        self.mytxt = ''
        self.mynum = 0
        self.t = loadadadha()



    def chkDst(self,num , C):
        if C < 0:
            return num
        else:
            return self.chkDst(num%(MAX/Dste),C-1)

    def YektaSad(self,num,txt=''):
        mtxt = ''
        if num > Dste or num < MIN:
            return mtxt
        
        if num < 10 and num > 0:
            return mtxt + self.t.yekan[num]
        if num < 20 and num >= 10 :
            mtxt = mtxt + self.t.dah1[num%10]
            if num  == 10:
                return mtxt 
            else:
                return mtxt + self.t.dah1[0]
            
        if num < 100 and num >= 20 :
            mtxt = mtxt + self.t.dah2[num//10]
            if num % 10 == 0 :
                return mtxt  + self.YektaSad(num%10)
            else:
                return mtxt  + self.t.dah2[0] + self.YektaSad(num%10)
            
        if num < 1000 and num >= 100 :
            if num // 100 == 2 :
                mtxt = mtxt + self.t.sadha[2]
                if num % 100 == 0 :
                    return mtxt 
                else:
                    return mtxt  + self.t.dah2[0] + self.YektaSad(num%100)
            else:
                mtxt = mtxt + self.t.sadha[num//100] + self.t.sadha[0]
                if num % 100 == 0 :
                    return mtxt  + self.YektaSad(num%100)
                else:
                    return mtxt  + self.t.dah2[0] + self.YektaSad(num%100)
                
        return mtxt            
            


    def num2txt(self,num,SBT=MAX):
        mtxt = ''
        
        if num > MAX or num < MIN :
            return mtxt
        elif num // SBT > 0:
            #print SBT
            mtxt = mtxt + self.YektaSad(num//SBT)+' '+self.t.farsi(SBT)
            if num%SBT != 0:
                mtxt = mtxt + self.t.dah2[0]
                
        else:
            if num < Dste :
                return mtxt + self.YektaSad(num)
                     
        return mtxt + self.num2txt(num%SBT,SBT/Dste)   

    def Shifnum(self, num , sh):
        pass

    def Ril2Tmn(self, num):
        pass

    def abjad(self, txt):
        num = 0
        for ch in txt:
            #print unichr(ord(ch))
            if unichr(ord(ch)) in abjad:
                #print num,
                num = num + abjad[unichr(ord(ch))]
        return num

    def txt2num(self, txt):
        number = 0
        self.n = loadhroof()
        sp = txt.split(' ')
        if len(txt) < 2:
            return number
        elif len(sp) == 1:
            return self.checktxt(sp[0])
        else:
            for t in sp:
                if t == u'و':
                    number = number + 0
                    
                if t in self.n.hezar.keys():
                    number = number * self.n.hezar[t]
            return number 
                

    def cntrltxt(self,num , txt):
        pass


    def checktxt(self, txt):
        if txt == u'ده':
            return self.n.dah2[txt]
        if u'ده' in txt:
            txt.split(u'ده')
            return self.n.dah1[txt.split(u'ده')[0]]
        if u'صد' in txt:
            txt.split(u'صد')
            return self.n.sadha[txt.split(u'صد')[0]]
        if u'هزار' in txt:
            return self.n.hezar.values()[0]
        if u'ميليون' in txt:
            return self.n.milyoon.values()[0]
        if u'ميليارد' in txt:
            return self.n.milyard.values()[0]
        if u'تريليون' in txt:
            return self.n.trilyoon.values()[0]
        if txt in self.n.yekan.keys():
            return self.n.yekan[txt]
        if txt in self.n.dah2.keys():
            return self.n.dah2[txt]
        return 0
            
    def cntrol_fasele(self, txt):
        pass

    def error_massage(self , n):
        pass

    def Date2txt(self, txt):
        pass

    def Valid_input(self, txt):
        pass
    


class loadadadha(object):
    def __init__(self,file_name="adadfa1"):
        f = codecs.open(file_name,mode='r',encoding='utf-8')

        lines = f.readlines()
        f.close()

        self.yekan = []
        self.dah1 = []
        self.dah2 = []
        self.sadha = []
        
        for i in range(10):
            self.yekan.append(lines[i+1].rstrip('\r\n'))
            if i == 0:
                self.dah1.append(lines[11].rstrip('\r\n'))
                self.dah2.append(u' و ')
            elif i == 1:
                self.dah1.append(lines[12].rstrip('\r\n'))
                self.dah2.append(lines[11].rstrip('\r\n'))
            else:
                self.dah1.append(lines[i+11].rstrip('\r\n'))
                self.dah2.append(lines[i+19].rstrip('\r\n'))

        for i in range(10):
            if i == 0:
                self.sadha.append(lines[29].rstrip('\r\n'))
            elif i == 2:
                self.sadha.append(lines[30].rstrip('\r\n'))
            elif i == 3:
                self.sadha.append(lines[22].rstrip('\r\n'))
            elif i == 5:
                self.sadha.append(lines[31].rstrip('\r\n'))
            else:
                self.sadha.append(lines[i+1].rstrip('\r\n'))

        self.hezar =lines[32].rstrip('\r\n')
        self.milyoon = lines[33].rstrip('\r\n')
        self.milyard = lines[34].rstrip('\r\n')
        self.trilyoon = lines[35].rstrip('\r\n')
    def farsi(self,SA):
        if SA == 1000:
            return self.hezar
        elif SA == 1000000:
            return self.milyoon
        elif SA == 1000000000:
            return self.milyard
        elif SA == 1000000000000:
            return self.trilyoon
        else:
            return ''
        return ''
    
class loadhroof(object):
    def __init__(self,file_name="adadfa1"):
        f = codecs.open(file_name,mode='r',encoding='utf-8')

        lines = f.readlines()
        f.close()

        self.yekan = {}
        self.dah1 = {}
        self.dah2 = {}
        self.sadha = {}
        for i in range(10):
            self.yekan[lines[i+1].rstrip('\r\n')]=i
            if i == 0:
                self.dah1[lines[11].rstrip('\r\n')]=i+10
                self.dah2['و'] = 0
            elif i == 1:
                self.dah1[lines[12].rstrip('\r\n')] = i+10
                self.dah2[lines[11].rstrip('\r\n')] = i*10
            else:
                self.dah1[lines[i+11].rstrip('\r\n')]= i+10
                self.dah2[lines[i+19].rstrip('\r\n')]= i*10

        for i in range(10):
            if i == 0:
                self.sadha[lines[29].rstrip('\r\n')]= 100
            elif i == 2:
                self.sadha[lines[30].rstrip('\r\n')]= i*100
            elif i == 3:
                self.sadha[lines[22].rstrip('\r\n')]= i*100
            elif i == 5:
                self.sadha[lines[31].rstrip('\r\n')]= i*100
            else:
                self.sadha[lines[i+1].rstrip('\r\n')]= i*100

        self.hezar = {lines[32].rstrip('\r\n'):1000}
        self.milyoon = {lines[33].rstrip('\r\n'):1000000}
        self.milyard = {lines[34].rstrip('\r\n'):1000000000}
        self.trilyoon = {lines[35].rstrip('\r\n'):1000000000000}


        '''
        def checkme(s):
            if s in milyard:
                if 'و' in s:
                    return milyard.key()
            elif SA == 1000000:
                return milyoon
            elif SA == 1000000000:
                return milyard
            else:
                return ''
            return ''
        '''


        
        

        
        
