#geneticbody.py

import random
import math
import re

strlis = [' , ']
strarr = ['$']

def con(n,m,codearr):
    fac = codearr[n].split(strarr[0])
    try:
        defstr = 'def func(' + fac[0] + '):'+fac[1]+'\n return ' + fac[2]
        func = funcexec(defstr)
        r = 0
        pl = random.sample(range(0,100),2*m)
        for i in range(0,m):
            try:
                r += abs(func(pl[2*i],pl[2*i+1]) - (pl[2*i]*pl[2*i+1]))
            except:
                return round(math.log(len(defstr)))*10**6
        return r
    except:
         return 10**7

#실행 및 평가 함수

def funcexec(strl):
    namespace = {}
    exec(strl,namespace)
    return namespace['func']
#실행 보호 함수

grammarli = ['a','b',',','+','/','*','-','=','\n']

def cre(arr,codearr):
    sor = sorted(arr, key = lambda x: x[0])
    if sor[0][0] == sor[1][0]:
        oldsum = sum(int(v) for v,name in sor)
        excode = evolu(codearr[sor[1][1]])
        v_num =[]
        for n in range(0, 10):
            num = con(n, 10, excode)
            v_num.append(num)
        newsum = sum(v_num)
        if newsum < oldsum:
            parent = sor[1][1]
        else:
            parent = sor[0][1]
    else:
        parent = sor[0][1]
    parentcode = codearr[parent]
    parfac = parentcode.split(strarr[0])
    parstr = 'def func(' + parfac[0] + '):'+parfac[1]+' return ' + parfac[2]
    rec(parstr)
    evoarr = evolu(parentcode)
    metaevo = strlis[0].join(evoarr)
    return metaevo
#생성 및 진화 함수

def evolu(parentcode):
    evolis = [parentcode, ]
    nowcodearr = parentcode.split(strarr[0])
    le = [len(nowcodearr[0]), len(nowcodearr[1]), len(nowcodearr[1])]
    for i in range(2, 11):
        newcodearr = nowcodearr
        part = random.randint(0, 2)
        deloradd = random.randint(0, 1)
        if deloradd >= le[part]:
            deloradd = 0
        seat = random.randint(deloradd, le[part])
        if deloradd == 1:
            # del
            newcodearr[part] = nowcodearr[part][:seat - 1] + nowcodearr[part][seat:]
        else:
            # add
            newcodearr[part] = nowcodearr[part][:seat] + random.choice(grammarli) + nowcodearr[part][seat:]
        newcodearr = [newcodearr[0], strarr[0], newcodearr[1], strarr[0], newcodearr[2]]
        newcode = ''.join(newcodearr)
        newcode = fix(newcode)
        evolis.append(newcode)
    return evolis
#진화 함수

def fix(strl):
    return str(re.sub(r'([^$])\1+', r'\1', strl))
#보정 함수

def rec(par):
    try:
        coder = open('rec.py','r')
        codeall = coder.read()
        coder.close()
        n = str(codeall.count('def')+1)
        print(n)
        ind = codeall.rfind('def')
        oldcode = codeall[ind:]
        if oldcode != (par+'\n'):
            codea = open('rec.py', 'a')
            codea.write(n + '\n'+ par + '\n')
            codea.close()
    except:
        print('exception')
        codew = open('rec.py', 'w')
        codew.write('1'+ '\n'+ par+'\n')
        codew.close()
#기록 함수

def turn():
    coder = open('cod.py', 'r')
    codestr = coder.read()
    coder.close()
    codearr = codestr.split(strlis[0])
    print(codearr)
    val_num = list()
    va_num = []
    for n in range(0,10):
        num = con(n,10,codearr)
        print(num)
        va_num.append(num)
        val_num.append((num,n))
    evo = cre(val_num,codearr)
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
    for i in range(0,10):
        strl =  strarr[0]*2
        stli.append(strl)
    metastr = strlis[0].join(stli)
    codew.write(metastr)
    codew.close()
result = True
t = 1
while result:
    print(t)
    result = turn()
    t+=1
    if not result:
        print('success')