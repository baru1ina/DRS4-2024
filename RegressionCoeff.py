import matplotlib.pyplot as plt

from DRSCalibrationData import *
from DataCorrNaive import data_corr_naive
import numpy as np
np.float_ = np.float64
import intvalpy as ip
from intvalpy import mid, rad


def RegressionCoeff(ch, cells, fn=None):
    ys_int = calibration_data_all_bins(ch, cells, type="Int")
    ys_ext = calibration_data_all_bins(ch, cells, type="Ext")
    ys = [ys_int, ys_ext]
    ys_int_to_plot = [np.average(i) for i in ys_int]
    ys_ext_to_plot = [np.average(i) for i in ys_ext]

    # print("ys: ", ys)
    # print("rawData_instance.lvls: ", rawData_instance.lvls)
    # Xs = np.sort(rawData_instance.lvls)
    # print("Xs: ", Xs)
    # inds = np.argsort(rawData_instance.lvls)
    # print("inds: ", inds)
    # Ysint = ys_int[inds]
    # Ysout = ys_ext[inds]

    Ysint = ip.Interval(ys_int)
    Ysout = ip.Interval(ys_ext)
    Xs = rawData_instance.bins
    Xs_lvls = rawData_instance.lvls
    # print("Xs_lvls: ", Xs_lvls)
    # for x_i in Xs:
    #     print(" x_i: ", x_i.lvl, end=" ")
    # print()
    # print("Ysint: ", Ysint)
    # print("Ysout: ", Ysout)

    def gen_yi1(ys_int_to_plot):
        return np.abs(ys_int[:, 0] - ys_int_to_plot)

    def gen_yi2(ys_int_to_plot):
        return np.abs(ys_int[:, 1] - ys_int_to_plot)

    def gen_ye1(ys_ext_to_plot):
        return np.abs(ys_ext[:, 0] - ys_ext_to_plot)

    def gen_ye2(ys_ext_to_plot):
        return np.abs(ys_ext[:, 1] - ys_ext_to_plot)

    yerr_int = [
        gen_yi1(ys_int_to_plot),
        gen_yi2(ys_int_to_plot)
    ]
    yerr_ext = [
        gen_ye1(ys_ext_to_plot),
        gen_ye2(ys_ext_to_plot)
    ]

    plt.errorbar(Xs_lvls, ys_int_to_plot, yerr=yerr_int, marker=".", linestyle='none',
                 ecolor='k', elinewidth=0.8, capsize=4, capthick=1)
    plt.errorbar(Xs_lvls, ys_ext_to_plot, yerr=yerr_ext, linestyle='none',
                 ecolor='r', elinewidth=0.8, capsize=4, capthick=1)
    plt.xlim([1.5*np.min(Xs_lvls), 1.5*np.max(Xs_lvls)])
    plt.show()

    # !!!!!ИЗМЕНИТЬ: ТЕПЕРЬ Xs ЭТО НЕ УРОВНИ, А БИНЫ!!!!!
    # Регрессия
    # Получим матрицу линейных признаков:
    Xi = np.vstack(([1] * len(Xs_lvls), Xs_lvls)).T
    print("Xi: ", Xi)

    # получим точечную матрицу внешних оценок
    y_out = mid(Ysout) - 16384 * 0.5
    print("y_out: ", y_out)

    # получим точечную матрицу радиусов внешних оценок
    epsilon_out = rad(Ysout)
    print("epsilon_out: ", epsilon_out)

    # строим регрессию по внешним оценкам
    # irp_DRSout = ir_problem(Xi, y_out, epsilon_out)

    # получим точечную матрицу внутренних оценок
    y_int = mid(Ysint) - 16384 * 0.5
    print("y_int: ", y_int)

    # получим точечную матрицу радиусов внутренних оценок
    epsilon_int = rad(Ysint)
    print("epsilon_int: ", epsilon_int)

    # data_corr_naive(Ysint, Ysout, Xi)

    # строим регрессию по внешним оценкам
    # irp_DRSint = ir_problem(Xi, y_int, epsilon_int)

    # Получение коэффициентов
    # b_out = ir_outer(irp_DRSout)

    # Рассчет и количество несовместимых уравнений
    # b_int, indtoout = data_corr_naive(Ysint, Ysout, Xi)
    # NonCompCount = len(indtoout)

    # return b_int, b_out, NonCompCount


def ir_problem(Xi, y, epsilon):
    # Заглушка для ir_problem
    pass


def ir_outer(irp):
    # Заглушка для ir_outer
    pass


bin = rawData_instance.get_bin_by_lvl(-0.027)
RegressionCoeff(0, 10, bin)
# b_int, b_out, NonCompCount = RegressionCoeff(0, 10, bin)
