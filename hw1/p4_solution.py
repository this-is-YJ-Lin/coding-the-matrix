from GF2 import *import itertoolsdef gen_comb(input_vector):    D = { 'a':[one,one,0,0,0,0,0], 'b':[0,one,one,0,0,0,0], 'c':[0,0,one,one,0,0,0],          'd':[0,0,0,one,one,0,0], 'e':[0,0,0,0,one,one,0], 'f':[0,0,0,0,0,one,one] }    comb = set()    l = range(2, len(D.keys())+1)    print(l)    print("\n")    for L in range(2, len(D.keys())+1):        for subset in itertools.combinations(D.keys(), L):            sub = [D[s] for s in subset]            t = [0]*len(sub[0])            for p in range(len(sub)):                t = [t[i] + sub[p][i] for i in range(len(t))]            if t == list(input_vector):                comb.add(subset)    return combu_0010010 = [0,0,one,0,0,one,0]u_0100010 = [0,one,0,0,0,one,0]print(gen_comb(u_0010010))print("\n")print(gen_comb(u_0100010))