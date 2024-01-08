#input/output e 4 pulsanti
from guizero import *

app = App('Esame',layout='grid')

class Chat():
    def __init__(self,data):
        self.data = data
        self.messaggi = {} 

def filtro():
    global input
    lista = []
    for line in input.value.splitlines():
        if len(line) > 0:
            lista.append(line.strip())
    chat = []
    for i in lista:
        if i[0] in '0123456789':
            dati = [i]
            for j in lista[lista.index(i)+1:]:
                if j[0] == '-':
                    dati.append(j)
                else:
                    break
            oggetto = Chat(i)
            for p in dati[1:]:
                y = p.split(':')
                if y[0][1:] not in oggetto.messaggi.keys():
                    oggetto.messaggi[y[0][1:]] = []
                oggetto.messaggi[y[0][1:]].append(y[1])
            chat.append(oggetto)
    return chat

def fun1(): 
    global output
    d = filtro()
    t = 'PUNTO 1\n'
    

    output.value = t

def fun2():
    global output
    d = filtro()
    t = 'PUNTO 2\n'
    felici = []
    global input
    lista = []
    for line in input.value.splitlines():
        if len(line) > 0:
            lista.append(line.strip())
    for i in lista:
        if ':-)' in i:
            indice = i.index(':')
            felici.append(i[indice+1:])
    for u in felici:
        t += f'\n{u}'
    output.value = t

def fun3():
    global output
    d = filtro()
    t = 'PUNTO 3\n\n'
    parole = {}
    mex = []
    for i in d:
        for k,v in i.messaggi.items():
            for j in v:
                senza = ''
                for carattere in j:
                    if carattere.lower() in 'qwertyuiopasdfghjklzxcvbnmèéàòìù ':
                        senza += f'{carattere}'
                mex.append(senza)
    for m in mex:
        n = m.split()
        for b in n:
            if b.lower() not in parole.keys():
                parole[b.lower()] = 1
            else:
                parole[b.lower()] += 1
    ord = dict(sorted(parole.items(),key=lambda t:t[1],reverse=True))
    chiavi = list(ord.keys())
    t += f'{chiavi[0]}'
    output.value = t

def fun4(): 
    global output
    d = filtro()
    t = 'PUNTO 4\n'
    comuni = []
    mex = []
    for i in d:
        for k,v in i.messaggi.items():
            for j in v:
                senza = ''
                for carattere in j:
                    if carattere.lower() in 'qwertyuiopasdfghjklzxcvbnmèéàòìù ':
                        senza += f'{carattere}'
                mex.append(senza.lower().split())
    for i in mex:
        for j in mex:
            if mex.index(i) != mex.index(j):
                for k in i:
                    if k in j:
                        if sorted([' '.join(i),' '.join(j)]) not in comuni:
                            comuni.append(sorted([' '.join(i),' '.join(j)]))
    for e in comuni:
        t += f'{e[0].capitalize()} - {e[1].capitalize()}\n'
    output.value = t

input = TextBox(app,multiline=True,grid=[0,0,4,1],width=70,height=15)
PushButton(app,text='1',grid=[0,1], command=fun1)
PushButton(app,text='2',grid=[1,1], command=fun2)
PushButton(app,text='3',grid=[2,1], command=fun3)
PushButton(app,text='4',grid=[3,1], command=fun4)
output = TextBox(app,multiline=True,grid=[0,2,4,1],width=70,height=15)

input.value = '''11-07-2017
-Marco:Ciao
-Roberta:Come stai? :-)
-Roberta:A dopo!
-Diego:Ciao ragazzi! :-)
12-07-2017
-Marco:Oggi torno tardi
-Saajan:Non ti preoccupare
-Marco:Oggi torno tardi come stai?
'''

for i in filtro():
    print(i.data,i.messaggi)

app.display()