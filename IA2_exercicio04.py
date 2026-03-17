import random

# Atividade 04 Inteligência artificial 2 

# Função cross em ponto unico

def cross(binpop, selected, pelit):

    # Nind = tamanho dos individuos selecionados
    Nind = len(selected)

    # Lind = tamanho da sequencia binaria
    Lind = len(binpop[0])

    # estrutura para armazenar filhos
    cross_pop = [None] * Nind

    for i in range(Nind // 2):

        # sorteio de pai e mae 
        pai = random.randint(0, Nind - 1)
        mae = random.randint(0, Nind - 1)

        # ponto de corte
        cp = random.randint(1, Lind - 1)

        filho_um = []
        filho_dois = []

        # construção dos filhos
        for j in range(Lind):

            if j < cp:
                filho_um.append(binpop[selected[pai]][j])
                filho_dois.append(binpop[selected[mae]][j])
            else:
                filho_um.append(binpop[selected[mae]][j])
                filho_dois.append(binpop[selected[pai]][j])

        cross_pop[i] = filho_um
        cross_pop[i + (Nind // 2)] = filho_dois

    return cross_pop

# Função de Mutação 

def mutate(binpop, pmut, pelit):

    # Nind = tamanho da populacao
    Nind = len(binpop)

    # Lind = tamanho da sequencia binaria
    Lind = len(binpop[0])

    for i in range(Nind):

        r = random.random()

        if r < pmut:

            # ponto de mutacao
            mp = random.randint(0, Lind - 1)

            if binpop[i][mp] == 0:
                binpop[i][mp] = 1
            else:
                binpop[i][mp] = 0

    return binpop

# EXEMPLO DE USO

if __name__ == "__main__":

    # populacao binaria
    binpop = [
        [1, 0, 1, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 1, 1]
    ]

    # indices selecionados
    selected = [0, 1, 2, 3]

    pelit = 0

    print("População inicial:")
    for ind in binpop:
        print(ind)

    # cruzamento
    nova_pop = cross(binpop, selected, pelit)

    print("\nApós cruzamento:")
    for ind in nova_pop:
        print(ind)

    # mutacao
    nova_pop = mutate(nova_pop, 0.1, pelit)

    print("\nApós mutação:")
    for ind in nova_pop:
        print(ind)