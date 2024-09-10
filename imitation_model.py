import random
import numpy as np
from prettytable import PrettyTable
class ImitationModel:
    def __init__(self,n : int, p : list, q : list , coef1 : list, coef2 : list,f1_static : bool):
        self.number_of_games = n
        self.p = p
        self.q = q
        self.coef1 = coef1
        self.coef2 = coef2
        self.f1_static = f1_static
        self.v = {}
        self.avg = 0

    def __calculate_fpq(self, p : float, q : float, coefs : list):
        fpq = coefs[0] * p * q + coefs[1] * q + coefs[2] * p + coefs[3]
        return fpq

    def run_model(self):
        if self.f1_static:
            p = self.p[0]
            for i in range(self.number_of_games):
                q = random.uniform(0,1)
                fpq = self.__calculate_fpq(p,q,self.coef2)
                self.v.update({i:fpq})
        else:
            q = self.q[0]
            for i in range(self.number_of_games):
                p = random.random()
                fpq = self.__calculate_fpq(p,q,self.coef1)
                self.v.update({i:fpq})
        self.avg = np.mean(list(self.v.values()))


    def show_results(self):
        print("Этапы работы модели:")
        game_table = PrettyTable()
        if self.f1_static:
            f = "f2"
        else:
            f = "f1"
        game_table.field_names = ["№", f]
        for el in self.v:
            game_table.add_row([el,self.v[el]])
        print(game_table)

        print(f'Средее значение выигрыша {f}: {self.avg}')






