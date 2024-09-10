class Task1:

    def __init__(self):
        self.p_sections = []
        self.q_sections = []
        self.p_turning_point = None
        self.q_turning_point = None
        self.nash_balance_points = []

    def __get_coef_first(self, matrix : list):
        return matrix[0] - matrix[1]

    def __print_formula(self, coef_one : int, coef_two : int, variable : str, line : str):
        print(f'f({variable}1,{line}) = {coef_one}{variable}1 + {coef_two}')

    def getGarantSolution(self, Matr : list, variable : str):
        coef_one=self.__get_coef_first(Matr[0])
        self.__print_formula(coef_one,Matr[0][1],variable,"1")

        coef_two=self.__get_coef_first(Matr[1])
        self.__print_formula(coef_two, Matr[1][1], variable, "2")

        var1 = (Matr[1][1] - Matr[0][1])/(coef_one-coef_two)
        print(f'{variable}1*= {var1}')
        var2 = 1 - var1;
        print(f'{variable}2*= {var2}')

        if variable=="p":
            self.p_sections.extend([var1,var2])
        else:
            self.q_sections.extend([var1,var2])

        v = coef_one * var1 + Matr[0][1]
        print(f'v = {v}')
        return v

    def getPQFunction(self, Matr : list, num : str):
        coefs=[]
        coef1_1=self.__get_coef_first(Matr[0])
        coef1_2=Matr[0][1]
        coef2_1=self.__get_coef_first(Matr[1])
        coef2_2=Matr[1][1]
        coefs.append(coef1_1+(-1)*(coef2_1))
        coefs.append(coef1_2 - coef2_2)
        coefs.append(coef2_1)
        coefs.append(coef2_2)
        print(f'f{num}(p,q)={coefs[0]}pq + {coefs[1]}q + {coefs[2]}p + {coefs[3]}')
        return coefs

    def getNashFunction(self,coefs1 : list, coefs2 : list, f1_opt : float, f2_opt : float):
        nash_coef = []
        nash_coef.extend([coefs1[0],coefs1[1],coefs1[2],coefs1[3]-f1_opt])
        nash_coef.extend([coefs2[0], coefs2[1], coefs2[2], coefs2[3] - f2_opt])
        print(f'N(p,q) = ({nash_coef[0]}pq + {nash_coef[1]}q + {nash_coef[2]}p + {nash_coef[3]}) '
              f'* ({nash_coef[4]}pq + {nash_coef[5]}q + {nash_coef[6]}p + {nash_coef[7]})')
        return nash_coef

