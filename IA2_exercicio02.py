import numpy as np
import random as rnd


"""
Rotina para criação de população inicial aleatória
Nind: número de indivíduos
CromLim: matriz (Ncrom x 2) com limites inferior e superior
"""
def newpop(Nind: int, CromLim: np.ndarray):
    Ncrom = CromLim.shape[0]
    pop = np.zeros((Nind, Ncrom))

    for i in range(Nind):
        for j in range(Ncrom):
            inf = CromLim[j, 0]
            sup = CromLim[j, 1]
            pop[i, j] = rnd.random() * (sup - inf) + inf

    return pop


"""
Rotina para codificação binária
pop: população real
CromLim: limites
Lbits: número de bits por cromossomo
"""
def code(pop: np.ndarray, CromLim: np.ndarray, Lbits: np.ndarray):
    Npop = pop.shape[0]
    Ncrom = CromLim.shape[0]
    total_bits = sum(Lbits)

    cod = np.zeros((Npop, total_bits), dtype=int)

    for i in range(Npop):
        start = 0

        for j in range(Ncrom):
            inf = CromLim[j, 0]
            sup = CromLim[j, 1]
            n_bits = Lbits[j]

            valor_real = pop[i, j]

            # converte valor real para inteiro proporcional
            inteiro = int((valor_real - inf) / (sup - inf) * (2**n_bits - 1))

            # converte para binário com padding
            bin_str = format(inteiro, f'0{n_bits}b')

            # armazena bits
            cod[i, start:start+n_bits] = list(map(int, bin_str))

            start += n_bits

    return cod


"""
Rotina para decodificação binária
binpop: população binária
CromLim: limites
Lbits: número de bits por cromossomo
"""
def decode(binpop: np.ndarray, CromLim: np.ndarray, Lbits: np.ndarray):
    Npop = binpop.shape[0]
    Ncrom = CromLim.shape[0]

    decod = np.zeros((Npop, Ncrom))

    for i in range(Npop):
        start = 0

        for j in range(Ncrom):
            inf = CromLim[j, 0]
            sup = CromLim[j, 1]
            n_bits = Lbits[j]

            bits = binpop[i, start:start+n_bits]

            # binário → inteiro
            inteiro = int("".join(map(str, bits)), 2)

            # inteiro → valor real
            valor_real = inteiro * (sup - inf) / (2**n_bits - 1) + inf

            decod[i, j] = valor_real

            start += n_bits

    return decod


"""
Teste das funções implementadas
"""
CromLim = np.array([[3, 7], [2, 4]])

# Número de bits por cromossomo (defina manualmente)
Lbits = np.array([8, 8])  # 8 bits para cada variável

# Gera população
nvpl = newpop(2, CromLim)
print("Nova população:\n", nvpl)

# Codifica
cd = code(nvpl, CromLim, Lbits)
print("\nPopulação codificada:\n", cd)

# Decodifica
dcd = decode(cd, CromLim, Lbits)
print("\nPopulação decodificada:\n", dcd)