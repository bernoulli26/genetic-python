#geneticbody.py

import random
import importlib

strlis = ['func = [','\n, ',']']
strarr = ['lambda ',' : ']

def con(n,m):
    #try:
        r = 0
        pl = random.sample(range(0,100),2*m)
        print(func[0](1,2))
        for i in range(0,m):
            try:
                r += abs(func[n](pl[2*i],pl[2*i+1]) - (pl[2*i]+pl[2*i+1]))
            except:
                return 10**7
        return r
    #except:
     #    return 10**8

#실행 및 평가 함수

grammarli = ['a','b',',','+']

def cre(arr,codearr):
    sor = sorted(arr, key = lambda x: x[0])
    if sor[0][0] == sor[1][0]:
        parent = sor[1][1]
    else:
        parent = sor[0][1]
    parentcode = codearr[parent]
    print(parentcode)
    evoarr = [parentcode,]
    nowcodearr = parentcode[len(strarr[0]):].split(strarr[1])
    print(nowcodearr)
    le = [len(nowcodearr[0]),len(nowcodearr[1])]
    for i in range(2,6):
        newcodearr = nowcodearr
        part = random.randint(0,1)
        deloradd = random.randint(0,1)
        if deloradd >= le[part]:
            deloradd = 0
        seat = random.randint(deloradd, le[part])
        if deloradd == 1:
            #del
            newcodearr[part] = nowcodearr[part][:seat-1] + nowcodearr[part][seat:]
        else:
            #add
            newcodearr[part] = nowcodearr[part][:seat] + random.choice(grammarli)+ nowcodearr[part][seat:]
        newcodearr = [strarr[0],newcodearr[0],strarr[1],newcodearr[1]]
        newcode = ''.join(newcodearr)
        evoarr.append(newcode)
    metaevo = strlis[0] + strlis[1].join(evoarr) + strlis[2]
    return metaevo
#생성 및 진화 함수

def fix(str):
    return
#보정 함수

def rec(par):
    try:
        coder = open('rec.py','r')
        codeall = coder.read()
        coder.close()
        ind = codeall.rfind('lambda')
        oldcode = codeall[ind:]
        if oldcode != (par + '/n'):
            codea = open('rec.py', 'a')
            codea.write(par + '/n')
            codea.close()
    except:
        codew = open('rec.py', 'w')
        codew.write(par + '/n')
        codew.close()
#기록 함수

def turn():
    coder = open('cod.py', 'r')
    codestr = coder.read()
    coder.close()
    codearr = codestr[len(strlis[0]):-1].split(strlis[1])
    print(codearr)
    com = compile(codestr, 'cod.py', 'exec')
    exec(com)
    print(func)
    val_num = list()
    for n in range(0,5):
        num = con(n,10)
        print(num)
        val_num.append((num,n))
    evo = cre(val_num,codearr)
    print(evo)
    codew = open('cod.py','w')
    codew.write(evo)
    codew.close()
    return all(val_num)
#한턴 함수

try:
    coder = open('cod.py', 'r')
    codestr = coder.read()
    codearr = codestr[len(strlis[0]):-1].split(strlis[1])
    print(codearr)
    coder.close()
except:
    codew = open('cod.py','w')
    stli =[]
    for i in range(0,5):
        str = strarr[0] + 'a,b' + strarr[1] + 'a+b'
        stli.append(str)
    metastr = strlis[0]+strlis[1].join(stli)+strlis[2]
    codew.write(metastr)
    codew.close()
result = True
t = 0
turn()
'''while result:
    print(t)
    result = turn()
    t+=1
    if not result:
        print('success')'''