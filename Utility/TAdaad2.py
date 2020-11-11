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
        #print self.t.yekan
        #print self.t.dahgan



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
            return mtxt + ' ' + self.t.yekan[num]
        
            
        if num < 100 and num >= 10 :
            mtxt = mtxt + ' ' + self.t.dahgan[(num//10)-1]
            if num % 10 == 0 :
                return mtxt  + self.YektaSad(num%10)
            else:
                return mtxt  +  self.YektaSad(num%10)
            
        if num < 1000 and num >= 100 :
            if num // 100 == 1 :
                mtxt = mtxt + self.t.sad
                if num % 100 == 0 :
                    return mtxt 
                else:
                    return mtxt  +' '+ self.YektaSad(num%100)
            else:
                mtxt = mtxt + ' '+self.YektaSad(num//100) +' '+ self.t.sad+' '+ self.YektaSad(num%100)
                
                
        return mtxt            
            


    def num2txt(self,num,SBT=MAX):
        mtxt = ''
        
        if num > MAX or num < MIN :
            return mtxt
        elif num // SBT > 0:
            #print SBT
            if num // SBT == 1:
                mtxt = mtxt + self.t.hezar
            elif num // SBT != 1:
                mtxt = mtxt + self.YektaSad(num//SBT) + ' '+self.t.hezar
                
            if num%SBT > 0:
                return mtxt + ' '+self.YektaSad(num%SBT)
            #if num%SBT != 0:
            #    mtxt = mtxt + ' '+self.t.dahgan[0]
                
        else:
            if num < Dste :
                return mtxt + ' '+self.YektaSad(num)
                     
        return mtxt + ' '+self.num2txt(num%SBT,SBT/Dste)   

    def Shifnum(self, num , sh):
        pass

    def Ril2Tmn(self, num):
        pass

    def abjad(self, txt):
        num = 0
        for ch in txt:
            print unichr(ord(ch))
            if unichr(ord(ch)) in abjad:
                #print num,
                num = num + abjad[unichr(ord(ch))]
        return num

    def txt2num(self, txt):
        pass
                

    def cntrltxt(self,num , txt):
        pass


    def checktxt(self, txt):
        pass
            
    def cntrol_fasele(self, txt):
        pass

    def error_massage(self , n):
        pass

    def Date2txt(self, txt):
        pass

    def Valid_input(self, txt):
        pass
    


class loadadadha(object):
    def __init__(self,file_name="adadtr1"):
        f = codecs.open(file_name,mode='r',encoding='utf-8')

        lines = f.readlines()
        f.close()

        self.yekan = []
        self.dahgan = []
        
        
        for i in range(10):
            self.yekan.append(lines[i+1].rstrip('\r\n'))
            

        for i in range(10):
            self.dahgan.append(lines[i+11].rstrip('\r\n'))

        self.sad = lines[20].rstrip('\r\n')    

        self.hezar =lines[21].rstrip('\r\n')

        
        #self.milyoon = lines[33].rstrip('\r\n')
        #self.milyard = lines[34].rstrip('\r\n')
        #self.trilyoon = lines[35].rstrip('\r\n')

    '''    
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

     '''   
    
class loadhroof(object):
    def __init__(self,file_name="adadtr1"):
        f = codecs.open(file_name,mode='r',encoding='utf-8')

        lines = f.readlines()
        f.close()

        self.yekan = {}
        self.dahgan = {}
        
        for i in range(10):
            self.yekan[lines[i+1].rstrip('\r\n')]=i
            

        for i in range(10):
            self.dahgan[lines[i+11].rstrip('\r\n')]=(i+1)*10
            

                
        self.sad  = {lines[20].rstrip('\r\n'):100} 
        self.hezar = {lines[21].rstrip('\r\n'):1000}

        '''
        
        self.milyoon = {lines[33].rstrip('\r\n'):1000000}
        self.milyard = {lines[34].rstrip('\r\n'):1000000000}
        self.trilyoon = {lines[35].rstrip('\r\n'):1000000000000}

        '''


        
        

        
        
