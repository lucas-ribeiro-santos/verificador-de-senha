import random
#import 
r = ''
ns = 0
nu = 5
while nu > 0:
    ns = random.randint(0, 9)
    r = str(r) + str(ns)
    nu = nu - 1
print(5*'-')
print(r)
print(5*'-')

x = str(r)
def senha (soma, x):

    r = []
    soma = str(soma)
    for i in range(len(soma)):
         
        if soma[i] in x:
            if soma[i] == x[i]:
                r.append(1)
            else:
                r.append(0)
        else:
            r.append (-1)
    return r
soma = input('digite uma senha --->')
print(senha(soma, x))
