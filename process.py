import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

from functions import pend, fak_1, fak_2, fak_3, fak_4, fak_6, fak_7
from radar_diagram import RadarDiagram
from uidialog import *
from utils import get_initial_equations_from_inputs, get_faks_from_inputs, get_equations_from_inputs, lines, \
    get_restrictions

data_sol = []


def handle(ui):
    ui.pushButton.clicked.connect(lambda: process(
        ui,
        get_initial_equations_from_inputs(ui),
        get_faks_from_inputs(ui),
        get_equations_from_inputs(ui),
        get_restrictions(ui)
    ))


def fill_diagrams(ui, data, initial_equations, labels, restrictions):
    radar1 = RadarDiagram()
    radar1.draw('./graphics/diagram.png', initial_equations, labels,
                "Характеристики системы в начальный момент времени", restrictions)
    radar1.draw('./graphics/diagram2.png', data[int(len(data) / 4)], labels,
                "Характеристики системы в 1 четверти", restrictions)
    radar1.draw('./graphics/diagram3.png', data[int(len(data) / 2)], labels,
                "Характеристики системы во 2 четверти", restrictions)
    radar1.draw('./graphics/diagram4.png', data[int(len(data) / 4 * 3)], labels,
                "Характеристики системы в 3 четверти", restrictions)
    radar1.draw('./graphics/diagram5.png', data[-1, :], labels,
                "Характеристики системы в последний момент времени", restrictions)
    ui.label_53.setPixmap(QtGui.QPixmap('graphics/diagram.png'))
    ui.label_54.setPixmap(QtGui.QPixmap('graphics/diagram2.png'))
    ui.label_38.setPixmap(QtGui.QPixmap('graphics/diagram3.png'))
    ui.label_55.setPixmap(QtGui.QPixmap('graphics/diagram4.png'))
    ui.label_62.setPixmap(QtGui.QPixmap('graphics/diagram5.png'))


def create_graphic(t, data, labels, faks):
    fig, axs = plt.subplots(figsize=(15, 10))
    plt.subplot(111)
    for i in range(23):
        plt.plot(t, data[:, i], color=lines[i][0], linestyle=lines[i][1], label=labels[i])
    plt.xlabel("t")
    plt.legend(loc=(.75, .64), labelspacing=0.1, fontsize='small')
    plt.draw()
    plt.xlim([0, 1])
    draw_third_graphic(t, faks)
    fig.savefig('./graphics/figure.png')


def draw_third_graphic(t, faks):
    fig, axs = plt.subplots(figsize=(15, 10))
    plt.subplot(1, 1, 1)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    for i in t:
        y1.append(fak_1(i, faks[0]))
        y2.append(fak_2(i, faks[1]))
        y3.append(fak_3(i, faks[2]))
        y4.append(fak_4(i, faks[3]))
        y5.append(fak_6(i, faks[4]))
        y6.append(fak_7(i, faks[5]))

    plt.plot(t, y1, label='Fak1')
    plt.plot(t, y2, label='Fak2')
    plt.plot(t, y3, label='Fak3')
    plt.plot(t, y4, label='Fak4')
    plt.plot(t, y5, label='Fak6')
    plt.plot(t, y6, label='Fak7')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.draw()
    fig.savefig("./graphics/figure2.png")


def process(ui, initial_equations, faks, equations, restrictions):
    global data_sol

    t = np.linspace(0, 1)
    data_sol = odeint(pend, initial_equations, t, args=(faks, equations))

    ui.expression_lineEdit_41.setText("Выполнено")

    create_graphic(t, data_sol, ui.u_list, faks)

    ui.label_15.setPixmap(QtGui.QPixmap('./graphics/figure.png'))
    fill_diagrams(ui, data_sol, initial_equations, ui.u_list, restrictions)
    ui.label_56.setPixmap(QtGui.QPixmap('./graphics/figure2.png'))
