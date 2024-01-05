from guizero import *

class Messaggio():
    def __init__(self,data,da,a,testo):
        self.data = data
        self.da = da
        self.a = a
        self.testo = testo
    def __str__(self):
        return f'{self.data} - {self.da} - {self.a} - {self.testo}'

def filtro():
    global input 
    lista = []
    for line in input.value.splitlines():
        if len(line) > 0:
            lista.append(line.strip())
    messaggi = []
    for i in lista:
        elementi = []
        j = i.split()
        for k in j[:3]:
            q = k.split(':')
            elementi.append(q[1])
        testo = []
        parola1 = j[3].split(':')[1]
        testo += [parola1]
        for w in j[4:]:
            testo.append(w)
        elementi.append(' '.join(testo))
        oggetto = Messaggio(elementi[0],elementi[1],elementi[2],elementi[3])
        messaggi.append(oggetto)
    return messaggi
        
def fun1():
    global output
    t = 'PUNTO 1\n\n'
    d = filtro()
    com = {}
    for i in d:
        if i.da not in com.keys():
            com[i.da] = []
        if i.a not in com.keys():
            com[i.a] = []
        if i.a not in com[i.da]:
            com[i.da].append(i.a)
        if i.da not in com[i.a]:
            com[i.a].append(i.da)
    num = {}
    for k,v in com.items():
        num[k] = len(v)
    ord = dict(sorted(com.items(),key=lambda t:len(t[1]),reverse=True))
    persone = list(ord.keys())
    t += persone[0]
    output.value = t

def fun2():
    global output
    t = 'PUNTO 2\n\n'
    d = filtro()
    mexmesi = {}
    for i in d:
        mese = i.data.split('-')[1]
        if mese not in mexmesi.keys():
            mexmesi[mese] = 1
        else:
            mexmesi[mese] += 1
    for k,v in mexmesi.items():
        t += f'Mese: {k}, messaggi: {v}\n'
    output.value = t

def fun3():
    global output
    t = 'PUNTO 3\n\n'
    d = filtro()
    coppie = {}
    for i in d:
        coppia = sorted([i.da,i.a])
        e = f'{coppia[0]}-{coppia[1]}:{i.data}'
        if e not in coppie.keys():
            coppie[e] = 1
        else:
            coppie[e] += 1
    ord = dict(sorted(coppie.items(),key=lambda t:t[1],reverse=True))
    copp = list(ord.keys())
    t += copp[0]
    output.value = t

def fun4():
    global output
    t = 'PUNTO 4\n\n'
    d = filtro()
    coppie = {}
    for i in d:
        coppia = f'{i.da}-{i.a}'
        coppiainv = f'{i.a}-{i.da}'
        if coppiainv not in coppie.keys():
            coppie[coppiainv] = 0
        if coppia not in coppie.keys():
            coppie[coppia] = 1
        else:
            coppie[coppia] += 1
    valide = []
    for k,v in coppie.items():
        for x,y in coppie.items():
            primok = k.split('-')[0]
            secondok = k.split('-')[1]
            primox = x.split('-')[0]
            secondox = x.split('-')[1]
            if primok == secondox and primox == secondok:
                diff = v - y
                if (diff < -2) or (diff > 2):
                    if (k not in valide) and (x not in valide):
                        valide.append(k)
    for p in valide:
        t += f'{p}\n'
    output.value = t

def main():
    fun1()
    app.after(5000,fun2)
    app.after(10000,fun3)
    app.after(15000,fun4)

app = App('ESAME',layout='grid')

input = TextBox(app,multiline=True,width=70,height=15,grid=[0,0])
output = TextBox(app,multiline=True,width=70,height=15,grid=[0,2])
pulsante = PushButton(app,grid=[0,1],text='CALCOLA',command=main)

input.value = '''Data:11-07-2015  Da:Franco A:Marco   Testo:Ciao!
Data:12-07-2015  Da:Franco  A:Giulia   Testo:Ciao!
Data:12-07-2015    Da:Marco   A:Franco   Testo:Oggi tutto bene
Data:12-07-2015    Da:Marco   A:Franco   Testo:Oggi tutto bene
Data:12-07-2015    Da:Marco   A:Franco   Testo:Oggi tutto bene
Data:12-07-2015    Da:Marco   A:Franco   Testo:Oggi tutto bene
Data:13-08-2015    Da:Giulia   A:Anna   Testo:Oggi tutto bene
Data:13-08-2015    Da:Alex   A:Gianfranco   Testo:Oggi tutto bene
Data:14-08-2015    Da:Alex   A:Giulia   Testo:Oggi tutto bene
'''

for j in filtro():
    print(j)

app.display()