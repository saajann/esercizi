d = {'Modena':{'Mantova':50,'Parma':60}, 'Reggio Emilia':{'Modena':20,'Piacenza':42}, 'Milano':{'Parma':100,'Roma':300}}
def fun1():
    global d 
    percorsoLungo = {}
    for k,v in d.items():
        lungMax = 0
        cittaArrivo = ''
        for i,j in v.items():
            if j > lungMax:
                lungMax = j
                cittaArrivo = i
        percorsoLungo[k] = cittaArrivo
    return percorsoLungo

print(fun1())