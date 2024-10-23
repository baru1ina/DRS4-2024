import numpy as np
np.float_ = np.float64
import intvalpy as ip
from intvalpy import mid, rad
from Tolsolvty import tolsolvty

def convert_yo_array(interval):
    pass


def data_corr_naive(Ysint, Ysout, Xi):
    Ys = ip.Interval(Ysint.copy())
    y = mid(Ys) - 16384 * 0.5
    epsilon = rad(Ys)

    tolmax, argmax, env = tolsolvty(Xi, Xi, y - epsilon, y + epsilon, 1)
    print(tolmax)
    print(argmax)
    print(env)

    # if tolmax > 0:
    #     b_int = ir_outer(ir_problem(Xi, y, epsilon))
    #     print('tolmax > 0')
    #     return b_int, None  # Возвращаем None для indtoout, если он не нужен
    #
    # print('tolmax < 0')
    # envnegind = np.where(env[:, 1] < 0)[0]
    # indtoout = env[envnegind, 0]
    #
    # y[indtoout] = mid(Ysout[indtoout]) - 16384 * 0.5
    # epsilon[indtoout] = rad(Ysout[indtoout])
    #
    # tolmax, argmax, env = tolsolvty(Xi, Xi, y - epsilon, y + epsilon, 1)
    #
    # irp_DRSint = ir_problem(Xi, y, epsilon)
    # b_int = ir_outer(irp_DRSint)
    #
    # return b_int, indtoout


# Зависимые функции
def ir_problem(Xi, y, epsilon):
    """Функция для решения проблемы интервалов."""
    # Здесь должна быть логика для решения задачи
    pass


def ir_outer(irp_DRS):
    """Вычисляет итоговые коэффициенты."""
    # Здесь должна быть логика для вычисления результатов
    pass

