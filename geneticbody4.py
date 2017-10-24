#geneticbody.py

import random
import math
import re
import pickle

strlis = [' , ']

def con(fac,m):
    try:
        defstr = 'def func(a,b):'+fac+'\n return c'
        func = funcexec(defstr)
        r = 0
        pl = random.sample(range(0,30),2*m)
        for i in range(0,m):
            try:
                r += abs(func(pl[2*i],pl[2*i+1]) - (pl[2*i]**2+pl[2*i+1]**2)**(1/2))**2
            except:
                return round(math.log(len(defstr)))*10**10
        return r
    except:
         return 10**15

#실행 및 평가 함수

def funcexec(strl):
    namespace = {}
    exec(strl,namespace)
    return namespace['func']
#실행 보호 함수

grammarli = ['a','b','c','+','=','\n','1','/','2',' ','*','(',')']

def cre(arr):
    sor = sorted(arr, key = lambda x: x[0])[:50]
    print(sor)
    parstr = 'def func(a,b): ' + sor[0][1] + ' return c'
    rec(parstr)
    newlis = []
    for (i,fac) in sor:
        if i==sor[0][0]:
            t=10
            y=2
        elif len(sor)<6:
            t=5
            y=5
        elif i<sor[5][0]:
            t=5
            y=5
        elif len(sor)<21:
            t=3
            y=10
        elif i<sor[20][0]:
            t=3
            y=10
        else:
            t=2
            y=30
        evomi = evolu(fac,t,y)
        failrec(list(filter(lambda x: con(x,10)==10**15, evomi)))
        birth = list(filter(lambda x:  (random.randint(1,1+round(math.log(len(arr)))))*con(x,10)<=5*10**10, evomi))
        newlis += birth
    newlis = list(set(newlis))
    print('newborn %d' %len(newlis))
    metaevo = strlis[0].join(newlis)
    return metaevo
#생성 및 진화 함수

def evolu(parentcode,capy,mutation):
    evolis = [parentcode, ]
    nowcode = parentcode
    le = len(nowcode)
    while len(evolis)<capy:
        newcode = nowcode
        for j in range(0,mutation):
            deloradd = random.randint(0, 1)
            if deloradd >= le:
                deloradd = 0
            seat = random.randint(deloradd, le)
            if deloradd == 1:
                # del
                newcode = newcode[:seat - 1] + newcode[seat:]
            else:
                # add
                newcode = newcode[:seat] + random.choice(grammarli) + newcode[seat:]
        newcode = fix(newcode)
        if failmatch(newcode) != -1:
            pass
        else:
            evolis.append(newcode)
            evolis = list(set(evolis))
    return evolis
#진화 함수

def fix(strl):
    return str(re.sub(r'([^*])\1{2,}', r'\1', strl))
#보정 함수

def failrec(lis):
    try:
        dicr = open('dict.txt', 'rb')
        diclis = pickle.load(dicr)
        dicr.close()
    except:
        diclis =[]
    diclis += lis
    diclis = list(set(diclis))
    dicw = open('dict.txt', 'wb')
    pickle.dump(diclis, dicw)
    dicw.close()
#실패 기록 저장

def failmatch(strl):
    try:
        dicr = open('dict.txt', 'rb')
        diclis = pickle.load(dicr)
        dicr.close()
        return diclis.find(strl)
    except:
        return -1
#실패기록 매칭

def recfind(strl):
    print(strl)
    coder = open('rec.py','r')
    codeall = coder.read()
    coder.close()
    print('find %d' % codeall.find(strl))
    if codeall.find(strl) != -1:
        print('find %d' %codeall.find(strl))
        return False
    else:
        return True
#역사 찾기 함수

def rec(par):
    try:
        coder = open('rec.py','r')
        codeall = coder.read()
        coder.close()
        n = str(codeall.count('def')+1)
        print('mutant %d' %codeall.count('def'))
        ind = codeall.rfind('def')
        oldcode = codeall[ind:]
        if oldcode != (par+'\n'):
            codea = open('rec.py', 'a')
            codea.write(n + '\n'+ par + '\n')
            codea.close()
    except:
        codew = open('rec.py', 'w')
        codew.write('1'+ '\n'+ par+'\n')
        codew.close()
#기록 함수

def turn():
    coder = open('cod.py', 'r')
    codestr = coder.read()
    coder.close()
    codearr = codestr.split(strlis[0])
    val_num = list()
    va_num = []
    for fac in codearr:
        num = con(fac,5)
        va_num.append(num)
        val_num.append((num,fac))
    evo = cre(val_num)
    codew = open('cod.py','w')
    codew.write(evo)
    codew.close()
    return all(va_num)
#한턴 함수

try:
    coder = open('cod.py', 'r')
    codestr = coder.read()
    codearr = codestr.split(strlis[0])
    coder.close()
except:
    codew = open('cod.py','w')
    stli =[]
    for i in range(0,1):
        strl =  '\n c=a'
        stli.append(strl)
    metastr = strlis[0].join(stli)
    codew.write(metastr)
    codew.close()
    codew = open('rec.py', 'w')
    codew.close()
result = True
t = 1
while result:
    print(t)
    result = turn()
    t+=1
    if not result:
        print('success')