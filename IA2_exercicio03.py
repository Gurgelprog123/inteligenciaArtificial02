import random

# Função objetiva

def obj_function(x):

    # Ncrom = tamanho de x
    Ncrom = len(x)

    # obj_function = 10
    obj_function = 10

    # para j de 1 até Ncrom
    for j in range(Ncrom):
        obj_function = obj_function - x[j] * x[j]

    return obj_function

# Função fitness

# pop : população a ser codificada
def fitness(pop):

    # Nind = número de indivíduos na população
    Nind = len(pop)

    # Ncrom = número de cromossomos em cada indivíduo
    Ncrom = len(pop[0])

    fitness_values = [0] * Nind

    # para i de 1 até Nind
    for i in range(Nind):
        fitness_values[i] = obj_function(pop[i])

    return fitness_values

# Roleta

def roleta(pop, fitness_values):

    Nind = len(pop)

    soma_fitness = sum(fitness_values)

    probabilidades = []

    # calcular probabilidades
    for i in range(Nind):
        probabilidades.append(fitness_values[i] / soma_fitness)

    # probabilidade acumulada
    acumulado = []
    soma = 0

    for i in range(Nind):
        soma = soma + probabilidades[i]
        acumulado.append(soma)

    r = random.random()

    for i in range(Nind):
        if r <= acumulado[i]:
            return pop[i]

pop = [
    [1, 2, 3],
    [0, 1, 1],
    [2, 2, 2],
    [1, 1, 1]
]
6
# calcular fitness
fitness_values = fitness(pop)

print("População:")
print(pop)

print("\nFitness:")
print(fitness_values)

# seleção por roleta
selecionado = roleta(pop, fitness_values)

print("\nIndivíduo selecionado pela roleta:")
print(selecionado)