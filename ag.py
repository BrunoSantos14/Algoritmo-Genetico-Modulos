from deap import base, creator, tools, algorithms
import numpy as np
import random


class AG:
    def __init__(self,
                 max_lines:int = 200_000,
                 max_len_group:int = 20,
                 len_pop:int = 500):
        
        self._df = None
        self.max_lines = max_lines
        self.max_len_group = max_len_group
        self.len_pop = len_pop

        creator.create("FitnessMax", base.Fitness, weights=(1.0, ))
        creator.create("Individual", list, fitness=creator.FitnessMax)
        self.toolbox = base.Toolbox()


    @property
    def df(self): return self._df

    @df.setter
    def df(self, df):
        self._df = df


    def restricao(self, individuos: list)-> bool:
        ind_not_null = [i for i in individuos if i >= 0]
        if self.objetivo(ind_not_null)[0] > self.max_lines:
            return False
        return True


    def objetivo(self, individuo) -> tuple:
        ind_not_null = [i for i in individuo if i >= 0]
        return self._df.iloc[list(set(ind_not_null)), 1].sum(),


    def gerar_individuos(self, icls, random_func):
        cromossomo = []
        aprovado = False
        while not aprovado:
            individuos = random_func()
            if self.restricao(individuos):
                aprovado = True
        cromossomo.extend(individuos)
        return icls(cromossomo)
    

    def body_ag(self):
        # Definir o gerador de numeros aleatórios de numeros inteiros entre o intervalo (0 e 50)
        self.toolbox.register("attr_bool", random.sample, range(-1, len(self._df)-1), self.max_len_group)
        # self.toolbox.register("attr_bool", random.randint, -1, len(self._df)-1)
        # Inicialização do cromossomo (quantos genes o cromossomo deve possuir)
        self.toolbox.register("individual", self.gerar_individuos, creator.Individual, self.toolbox.attr_bool)
        # Registro do individuo na população
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        # Registro do nome da função objetivo
        self.toolbox.register("evaluate", self.objetivo)
        # Registro da função de penalidade caso o individuo não obedeça as restrições
        self.toolbox.decorate("evaluate", tools.DeltaPenalty(self.restricao, 0))
        # Registro de qual o tipo de cruzamento deve ser utilizado (não pode usar cxOrdered pq tem individuos de tamanhos diferentes)
        self.toolbox.register("mate", tools.cxTwoPoint)
        # Registro de qual tipo de mutação deve ser utilizado (evitando criação de indivíduos inválidos)
        self.toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.5)
        # Registro de qual o tipo do método de seleção que será utilizado
        self.toolbox.register("select", tools.selRoulette)

    
    def process(self):
        pop = self.toolbox.population(n=self.len_pop)             # inicialização da pop
        hof = tools.HallOfFame(1)                                 # melhor indivíduo
        stats = tools.Statistics(lambda ind: ind.fitness.values)

        stats.register("avg", np.mean)
        stats.register("std", np.std)
        stats.register("min", np.min)
        stats.register("max", np.max)

        pop, _ = algorithms.eaSimple(pop, self.toolbox, cxpb=0.5, mutpb=0.7, ngen=50, stats=stats, halloffame=hof, verbose=False)
        return hof[0]
    

    def get_group(self) -> list:
        self.body_ag()
        hof = self.process()
        return hof


    def evaluate_group(self, group: list):
        return int(self.objetivo(group)[0])
    