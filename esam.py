class Ristoranti():
    def __init__(self,nome,stelle,prezzo,coord):
        self.nome = nome
        self.stelle = stelle
        self.prezzo = prezzo
        self.coord = coord

def filtro():
    with open('esame_ristoranti/t.txt') as f:
        t = f.read()

    listarighe = []
    for line in t.splitlines():
        if len(line) > 0:
            listarighe.append(line.strip())
    
    lista_ristoranti = []
    n = 0
    for i in range(int(len(listarighe)/4)):
        p = listarighe[n:n+4] #così ogni volta prende 4 righe 
        #trasformo le stelle in un numero
        p[1] = len(p[1])
        #tolgo 'euro' dal prezzo
        p[2] = float(p[2].split()[0])
        #coordinate
        p[3] = [float(p[3].split(',')[0]),float(p[3].split(',')[1])]
        #creo oggetto ristorante
        ristorante = Ristoranti(p[0],p[1],p[2],p[3])
        #aggiungo oggetto ristorante alla lista
        lista_ristoranti.append(ristorante)
        n += 4 
    return lista_ristoranti

def fun1(): #ordina per nome
    d = filtro()
    ord = sorted(d,key= lambda t:t.nome)
    for a in ord:
        print(a.nome,a.stelle,a.prezzo,a.coord)

for ristorante in filtro():
    print(ristorante.nome,ristorante.stelle,ristorante.prezzo,ristorante.coord)

print('Punto 1')
fun1()