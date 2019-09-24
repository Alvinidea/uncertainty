import numpy as np
import math
import matplotlib.pyplot as plt


def self_average(self_list):
    _sum = sum(self_list)
    avg = _sum / len(self_list)
    return avg


def self_pow_sum(self_list, ex, pownum):
    # (xi - ex) ^  pownum
    sum_ = 0.0
    for x in self_list:
        xx = (x - ex) ** pownum
        xx = abs(xx)
        sum_ = sum_ + xx
    return sum_


'''
@ 正向云算法
@ Ex 期望
@ En 熵
@ He 超熵（熵的熵）
'''


def pos_guass(Ex, En, He,n_drop):
    x_axis = []
    y_axis = []
    np.random.seed(0)
    for n in range(0, n_drop):
        yi = np.random.normal(En, He)
        yi = abs(yi)
        xi = np.random.normal(Ex, yi)
        u_xi = math.exp(-((xi - Ex)**2) / (2*yi**2))
        x_axis.append(xi)
        y_axis.append(u_xi)
    # print(x_axis)
    # print(y_axis)
    plt.plot(x_axis, y_axis, 'bo', ms=1)
    plt.show()
    return x_axis, y_axis


def neg_guass(x_axis, u_axis):
    n = len(x_axis)
    # 计算 Ex
    ex = self_average(x_axis)
    sum_ = self_pow_sum(x_axis, ex, 2)
    # 计算 En
    en = (1/(n-1) * sum_)**0.5
    y_list = []
    sum_ = 0.0
    for i in range(n):
        ln_u = math.log(math.e, u_axis[i])
        yi = (- ((x_axis[i] - ex) ** 2)/(2 * ln_u)) ** 0.5
        sum_ = sum_ + yi
        y_list.append(yi)
    sum_ = self_pow_sum(y_list, sum_ / n, 2)
    # 计算 He
    he = ((1/(n-1)) * sum_)**0.5
    print("Ex: ", ex, "En: ", en, "He: ", he)
    return ex, en, he


def neg_guass_nocertain(x_axis):
    n = len(x_axis)
    ex = self_average(x_axis)
    s_pow = (1/(n-1)) * self_pow_sum(x_axis, ex, 2)
    en = (math.pi/2)**0.5 * (1/n) * self_pow_sum(x_axis, ex, 1)
    he = (s_pow**2 - en**2)**0.5
    print("Ex: ", ex, "En: ", en, "He: ", he)
    return ex, en, he


def neg_guass_nocertain2(x_axis):
    n = len(x_axis)
    ex = self_average(x_axis)
    s_pow = (1 / (n - 1)) * self_pow_sum(x_axis, ex, 2)
    m4 = (1 / n) * self_pow_sum(x_axis, ex, 4)
    en = ((9*(s_pow**2)**2 - m4)/6)**0.25
    he = (s_pow**2 - en**2)**0.05
    print("Ex: ", ex, "En: ", en, "He: ", he)
    return ex, en, he


if __name__ == "__main__":
    '''Ex = float(input("输入 Ex："))
    En = float(input("输入 En："))
    He = float(input("输入 He："))
    N = int(input("输入 点的数目："))'''
    # pos_guass(Ex, En, He, N)
    x_axis, y_axis = pos_guass(25, 3, 0.55, 5000)

    neg_guass(x_axis, y_axis)

    neg_guass_nocertain(x_axis)

    neg_guass_nocertain2(x_axis)