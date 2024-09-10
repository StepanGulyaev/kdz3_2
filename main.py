from task1 import *
from task2 import *
from graphics import *
from imitation_model import *

A = [[6,3],
     [3,8]]

B = [[2,10],
     [5,4]]

def print_matrix(matrix : list):
     for row in matrix:
          print(' '.join(map(str, row)))

if __name__ == '__main__':
     print("Матрица игрока А:",end="\n\n")
     print_matrix(A)
     print()

     print("Матрица игрока B:",end="\n\n")
     print_matrix(B)
     print()

     print("Гарантированное решение игрока 1: ")
     task1 = Task1()
     vA = task1.getGarantSolution(A,"p")
     print()
     print("Гарантированное решение игрока 2: ")
     vB = task1.getGarantSolution(B,"q")
     print()

     print("f(p,q) игрока 1: ")
     coefs1 = task1.getPQFunction(A,"1")
     print()
     print("f(p,q) игрока 2: ")
     coefs2 = task1.getPQFunction(B,"2")
     print()

     status_quo_point = (vA,vB)
     task2 = Task2(5000, A, B, status_quo_point)

     task2.gen_random_pq_points()
     task2.get_fpq_points(coefs1,coefs2)
     graphics = Graphics(30, 5, 20, (-0.1, 0.05))
     graphics.draw_generated_pq_points(task2.pq_points)
     task2.get_pareto_points()
     task2.get_debatable_point()
     task2.get_nash_max()
     task2.show_pareto()
     task2.show_debatable()
     print("Функция Нэша: ")
     nash_coef = task1.getNashFunction(coefs1,coefs2,vA,vB)
     task2.show_nash_max()
     graphics.draw_pareto(task2.fpq_points,task2.status_quo_point)

     n = 1000
     print("Имитационная модель при константном q и меняющемся p:")
     imitation_model1 = ImitationModel(n,task1.p_sections,task1.q_sections, coefs1, coefs2, False)
     imitation_model1.run_model()
     imitation_model1.show_results()
     graphics.draw_model(n,imitation_model1.v, imitation_model1.avg,False)

     print()
     print("Имитационная модель при константном p и меняющемся q:")
     imitation_model2 = ImitationModel(n,task1.p_sections,task1.q_sections, coefs1, coefs2, True)
     imitation_model2.run_model()
     imitation_model2.show_results()
     graphics.draw_model(n,imitation_model2.v, imitation_model1.avg,True)

     plt.show()