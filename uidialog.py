import random

from PyQt5 import QtCore, QtGui, QtWidgets

from process import handle

defaultLineEditStyleSheet = "min-width:40px;\nmax-width:40px;\nwidth:40px"


class UiDialog(object):
    def __init__(self):
        self.equations_scroll_widget_layout = None
        self.equations_scroll_area_widget = None
        self.equations_scroll_area_layout = None
        self.initial_equations_scroll_widget_layout = None
        self.initial_equations_scroll_area_widget = None
        self.initial_equations_scroll_area_layout = None
        self.equations_scroll_area = None
        self.initial_equations_scroll_area = None
        self.initial_equations_group_box = None
        self.fak_group_box = None
        self.control_group_box = None
        self.equations_group_box = None
        self.labels = dict()
        self.lineEdits = dict()
        self.u_list = [
            "качество",
            "доступность",
            "завершенность",
            "устойчивость к ошибкам",
            "восстановляемость",
            "ошибки надежды",
            "сбои и отказы при работы системы",
            "ошибки завершенности",
            "отказы при работе программного обеспечения",
            "сбои при работе программного обеспечения",
            "отсутствие требований по восстановлению данных при отказах операционной системы и аппаратного обеспечения",
            "потери данных при отказах операционной системы и аппаратного обеспечения",
            "ошибка восстановления предшествующего состояния системы после повторного запуска программного обеспечения",
            "отсутствие требований по восстановлению вычислительного процесса в случае сбоя операционной системы и аппаратного обеспечения",
            "ошибка восстановления процесса в случае сбоев оборудования",
            "ошибка восстановления данных в случае их искажений или разрушения",
            "несоответствие требованиям стандартов, соглашений, законов или других предписаний, связанных с качеством",
            "неполнота обработки ошибочных ситуаций",
            "неполнота контроля корректности, полноты и непротиворечивости входных, выходных данных и баз данных",
            "отсутствие возможности функционирования в сокращенном объеме в случае ошибок или помех",
            "недостатки средств контроля работоспособности и диагностирования аппаратных и программных средств",
            "отсутствие диагностического сообщения в случае сбоя или отказа",
            "неполнота контроля непротиворечивости входных и баз данных"
        ]

    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1127, 831)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setToolTipDuration(6)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1068, 750))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.init_group_boxes()

        self.label_42 = QtWidgets.QLabel(self.control_group_box)
        self.label_42.setGeometry(QtCore.QRect(90, 120, 49, 16))
        self.label_42.setObjectName("label_42")
        self.expression_lineEdit_41 = QtWidgets.QLineEdit(self.control_group_box)
        self.expression_lineEdit_41.setGeometry(QtCore.QRect(155, 120, 113, 22))
        self.expression_lineEdit_41.setAlignment(QtCore.Qt.AlignCenter)
        self.expression_lineEdit_41.setObjectName("expression_lineEdit_41")
        self.pushButton = QtWidgets.QPushButton(self.control_group_box)
        self.pushButton.setGeometry(QtCore.QRect(150, 160, 121, 31))
        self.pushButton.setObjectName("pushButton")
        # self.pushButton_2 = QtWidgets.QPushButton(self.control_group_box)
        # self.pushButton_2.setGeometry(QtCore.QRect(150, 120, 121, 31))
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_3 = QtWidgets.QPushButton(self.control_group_box)
        # self.pushButton_3.setGeometry(QtCore.QRect(150, 170, 121, 31))
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_4 = QtWidgets.QPushButton(self.control_group_box)
        # self.pushButton_4.setGeometry(QtCore.QRect(150, 220, 121, 31))
        # self.pushButton_4.setObjectName("pushButton_4")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_15.setStyleSheet("max-height : 800px;\n"
                                    "max-width:1100px;\n"
                                    "margin-top: 10px;\n"
                                    "margin-bottom: 10px;")
        self.label_15.setText("")
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setIndent(-3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(True)
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, -1875, 1051, 2642))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_55 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_55.setStyleSheet("max-height : 800px;\n"
                                    "max-width:900px;\n"
                                    "margin-top: 10px;\n"
                                    "margin-bottom: 10px;")
        self.label_55.setText("")
        self.label_55.setScaledContents(True)
        self.label_55.setObjectName("label_55")
        self.gridLayout_5.addWidget(self.label_55, 3, 0, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_54.setMaximumSize(QtCore.QSize(700, 520))
        self.label_54.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_54.setStyleSheet("max-height : 800px;\n"
                                    "max-width:900px;\n"
                                    "margin-top: 10px;\n"
                                    "margin-bottom: 10px;")
        self.label_54.setText("")
        self.label_54.setScaledContents(True)
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setIndent(-3)
        self.label_54.setObjectName("label_54")
        self.gridLayout_5.addWidget(self.label_54, 1, 0, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_53.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_53.setStyleSheet("max-height : 800px;\n"
                                    "max-width:900px;\n"
                                    "margin-top: 10px;\n"
                                    "margin-bottom: 10px;")
        self.label_53.setText("")
        self.label_53.setScaledContents(True)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setIndent(-3)
        self.label_53.setObjectName("label_53")
        self.gridLayout_5.addWidget(self.label_53, 0, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_38.setMaximumSize(QtCore.QSize(700, 520))
        self.label_38.setText("")
        self.label_38.setScaledContents(True)
        self.label_38.setObjectName("label_38")
        self.label_38.setStyleSheet("max-height : 800px;\n"
                                    "max-width:900px;\n"
                                    "margin-top: 10px;\n"
                                    "margin-bottom: 10px;")
        self.gridLayout_5.addWidget(self.label_38, 2, 0, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_62.setMaximumSize(QtCore.QSize(700, 520))
        self.label_62.setText("")
        self.label_62.setScaledContents(True)
        self.label_62.setObjectName("label_62")
        self.label_62.setStyleSheet("max-height : 800px;\n"
                                    "max-width:900px;\n"
                                    "margin-top: 10px;\n"
                                    "margin-bottom: 10px;")
        self.gridLayout_5.addWidget(self.label_62, 4, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.scrollArea_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setEnabled(True)
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_56 = QtWidgets.QLabel(self.tab_4)
        self.label_56.setStyleSheet("max-height : 800px;\n"
                                    "max-width:1100px;\n"
                                    "margin-top: 10px;\n"
                                    "margin-bottom: 10px;")
        self.label_56.setText("")
        self.label_56.setScaledContents(True)
        self.label_56.setObjectName("label_56")
        self.gridLayout_6.addWidget(self.label_56, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.horizontalLayout_8.addWidget(self.tabWidget)

        self.retranslate_ui(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        handle(self)

    def retranslate_ui(self, Dialog):
        Dialog.setWindowTitle("Dialog")
        self.label_42.setText("Статус")
        self.pushButton.setText("Вычислить")
        # self.pushButton_2.setText("График")
        # self.pushButton_3.setText("Диаграмма")
        # self.pushButton_4.setText("Возмущения")

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Параметры")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Графики")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), "Диаграмма")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), "Возмущение")

    def init_group_boxes(self):
        self.equations_group_box = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.equations_group_box.setGeometry(QtCore.QRect(640, 10, 421, 380))
        self.equations_group_box.setObjectName("equations_group_box")
        self.equations_group_box.setTitle("Уравнения")
        self.init_scroll_area_for_equations()
        self.init_equations()

        self.control_group_box = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.control_group_box.setGeometry(QtCore.QRect(640, 380, 421, 360))
        self.control_group_box.setCheckable(False)
        self.control_group_box.setObjectName("control_group_box")
        self.control_group_box.setTitle("Управление")

        self.fak_group_box = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.fak_group_box.setGeometry(QtCore.QRect(10, 10, 631, 380))
        self.fak_group_box.setObjectName("fak_group_box")
        self.fak_group_box.setTitle("Возмущения")
        self.init_faks()

        self.initial_equations_group_box = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.initial_equations_group_box.setGeometry(QtCore.QRect(10, 380, 631, 360))
        self.initial_equations_group_box.setStyleSheet("max-width: 1000px")
        self.initial_equations_group_box.setObjectName("initial_equations_group_box")
        self.initial_equations_group_box.setTitle("Начальные уравнения")
        self.init_scroll_area_for_initial_equations()
        self.init_u()

    def init_scroll_area_for_equations(self):
        self.equations_scroll_area = QtWidgets.QScrollArea(self.equations_group_box)
        self.equations_scroll_area.setMaximumSize(QtCore.QSize(401, 17100))
        self.equations_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.equations_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.equations_scroll_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.equations_scroll_area.setWidgetResizable(True)
        self.equations_scroll_area.setObjectName("equations_scroll_area")
        self.equations_scroll_area_layout = QtWidgets.QGridLayout(self.equations_group_box)
        self.equations_scroll_area_layout.setObjectName("equations_scroll_area_layout")
        self.equations_scroll_area_layout.addWidget(self.equations_scroll_area, 1, 0, 1, 1)

        self.equations_scroll_area_widget = QtWidgets.QWidget()
        self.equations_scroll_area_widget.setGeometry(QtCore.QRect(0, -51, 612, 740))
        self.equations_scroll_area_widget.setMaximumSize(QtCore.QSize(1000, 17940))
        self.equations_scroll_area_widget.setObjectName("equations_scroll_area_widget")
        self.equations_scroll_widget_layout = QtWidgets.QGridLayout(self.equations_scroll_area_widget)
        self.equations_scroll_widget_layout.setObjectName("equations_scroll_widget_layout")

    def init_scroll_area_for_initial_equations(self):
        self.initial_equations_scroll_area = QtWidgets.QScrollArea(self.initial_equations_group_box)
        self.initial_equations_scroll_area.setMaximumSize(QtCore.QSize(1002, 710))
        self.initial_equations_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.initial_equations_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.initial_equations_scroll_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.initial_equations_scroll_area.setWidgetResizable(True)
        self.initial_equations_scroll_area.setObjectName("initial_equations_scroll_area")
        self.initial_equations_scroll_area_layout = QtWidgets.QGridLayout(self.initial_equations_group_box)
        self.initial_equations_scroll_area_layout.setObjectName("initial_equations_scroll_area_layout")
        self.initial_equations_scroll_area_layout.addWidget(self.initial_equations_scroll_area, 1, 0, 1, 1)

        self.initial_equations_scroll_area_widget = QtWidgets.QWidget()
        self.initial_equations_scroll_area_widget.setGeometry(QtCore.QRect(0, -51, 612, 740))
        self.initial_equations_scroll_area_widget.setMaximumSize(QtCore.QSize(1000, 794))
        self.initial_equations_scroll_area_widget.setObjectName("initial_equations_scroll_area_widget")
        self.initial_equations_scroll_widget_layout = QtWidgets.QGridLayout(self.initial_equations_scroll_area_widget)
        self.initial_equations_scroll_widget_layout.setObjectName("initial_equations_scroll_widget_layout")

    def init_u(self):
        for i in range(1, 24):
            self.labels[f"u{i}"] = QtWidgets.QLabel(self.initial_equations_scroll_area_widget)
            self.labels[f"u{i}"].setObjectName(f"labels_u{i}")
            self.labels[f"u{i}"].setText(self.u_list[i - 1])
            self.initial_equations_scroll_widget_layout.addWidget(self.labels[f"u{i}"], i - 1, 0, 1, 7)

            self.lineEdits[f"u{i}"] = QtWidgets.QLineEdit(self.initial_equations_scroll_area_widget)
            self.lineEdits[f"u{i}"].setStyleSheet("min-width:50px;\nwidth:50px")
            self.lineEdits[f"u{i}"].setObjectName(f"lineEdits_{i}")
            self.lineEdits[f"u{i}"].setText(str(round(random.random() * 0.7 + 0.01, 2)))
            self.initial_equations_scroll_widget_layout.addWidget(self.lineEdits[f"u{i}"], i - 1, 7, 1, 1)

            self.labels[f"u_restrictions{i}"] = QtWidgets.QLabel(self.initial_equations_scroll_area_widget)
            self.labels[f"u_restrictions{i}"].setObjectName(f"labels_u_restrictions{i}")
            self.labels[f"u_restrictions{i}"].setText("Ограничение:")
            self.initial_equations_scroll_widget_layout.addWidget(self.labels[f"u_restrictions{i}"], i - 1, 8, 1, 2)

            self.lineEdits[f"u_restrictions{i}"] = QtWidgets.QLineEdit(self.initial_equations_scroll_area_widget)
            self.lineEdits[f"u_restrictions{i}"].setStyleSheet("min-width:50px;\nwidth:50px")
            self.lineEdits[f"u_restrictions{i}"].setObjectName(f"lineEdits_u_restrictions_{i}")
            self.lineEdits[f"u_restrictions{i}"].setText("1")
            self.initial_equations_scroll_widget_layout.addWidget(self.lineEdits[f"u_restrictions{i}"], i - 1, 10, 1, 1)
        self.initial_equations_scroll_area.setWidget(self.initial_equations_scroll_area_widget)

    def init_faks(self):
        for index, i in enumerate([1, 2, 3, 4, 6, 7]):
            margin_top = 20 + index * 50
            self.labels[f"fak{i}_1"] = QtWidgets.QLabel(self.fak_group_box)
            self.labels[f"fak{i}_1"].setGeometry(QtCore.QRect(11, margin_top, 50, 16))
            self.labels[f"fak{i}_1"].setObjectName(f"labels_fak{i}_1")
            self.labels[f"fak{i}_1"].setText(f"Fak{i}(x)=")

            self.lineEdits[f"fak{i}_1"] = QtWidgets.QLineEdit(self.fak_group_box)
            self.lineEdits[f"fak{i}_1"].setGeometry(QtCore.QRect(68, margin_top, 42, 20))
            self.lineEdits[f"fak{i}_1"].setStyleSheet(defaultLineEditStyleSheet)
            self.lineEdits[f"fak{i}_1"].setObjectName(f"lineEdits_fak{i}_1")
            self.lineEdits[f"fak{i}_1"].setText(str(round(random.random() * 0.7 + 0.01, 2)))

            self.labels[f"fak{i}_2"] = QtWidgets.QLabel(self.fak_group_box)
            self.labels[f"fak{i}_2"].setGeometry(QtCore.QRect(113, margin_top, 41, 16))
            self.labels[f"fak{i}_2"].setObjectName(f"labels_fak{i}_2")
            self.labels[f"fak{i}_2"].setText("*x^3+")

            self.lineEdits[f"fak{i}_2"] = QtWidgets.QLineEdit(self.fak_group_box)
            self.lineEdits[f"fak{i}_2"].setGeometry(QtCore.QRect(156, margin_top, 42, 20))
            self.lineEdits[f"fak{i}_2"].setStyleSheet(defaultLineEditStyleSheet)
            self.lineEdits[f"fak{i}_2"].setObjectName(f"lineEdits_fak{i}_2")
            self.lineEdits[f"fak{i}_2"].setText(str(round(random.random() * 0.7 + 0.01, 2)))

            self.labels[f"fak{i}_3"] = QtWidgets.QLabel(self.fak_group_box)
            self.labels[f"fak{i}_3"].setGeometry(QtCore.QRect(201, margin_top, 41, 16))
            self.labels[f"fak{i}_3"].setObjectName(f"labels_fak{i}_3")
            self.labels[f"fak{i}_3"].setText("*x^2+")

            self.lineEdits[f"fak{i}_3"] = QtWidgets.QLineEdit(self.fak_group_box)
            self.lineEdits[f"fak{i}_3"].setGeometry(QtCore.QRect(243, margin_top, 42, 20))
            self.lineEdits[f"fak{i}_3"].setStyleSheet(defaultLineEditStyleSheet)
            self.lineEdits[f"fak{i}_3"].setObjectName(f"lineEdits_fak{i}_3")
            self.lineEdits[f"fak{i}_3"].setText(str(round(random.random() * 0.7 + 0.01, 2)))

            self.labels[f"fak{i}_4"] = QtWidgets.QLabel(self.fak_group_box)
            self.labels[f"fak{i}_4"].setGeometry(QtCore.QRect(289, margin_top, 41, 16))
            self.labels[f"fak{i}_4"].setObjectName(f"labels_fak{i}_4")
            self.labels[f"fak{i}_4"].setText("*x+")

            self.lineEdits[f"fak{i}_4"] = QtWidgets.QLineEdit(self.fak_group_box)
            self.lineEdits[f"fak{i}_4"].setGeometry(QtCore.QRect(316, margin_top, 42, 20))
            self.lineEdits[f"fak{i}_4"].setStyleSheet(defaultLineEditStyleSheet)
            self.lineEdits[f"fak{i}_4"].setObjectName(f"lineEdits_fak{i}_4")
            self.lineEdits[f"fak{i}_4"].setText(str(round(random.random() * 0.7 + 0.01, 2)))

    def init_equations(self):
        for i in range(1, 317):
            self.labels[f"f{i}_1"] = QtWidgets.QLabel(self.equations_group_box)
            self.labels[f"f{i}_1"].setObjectName(f"labels_f{i}_1")
            self.labels[f"f{i}_1"].setText(f"F{i}(x)=")
            self.equations_scroll_widget_layout.addWidget(self.labels[f"f{i}_1"], i - 1, 0, 1, 1)

            self.lineEdits[f"f{i}_1"] = QtWidgets.QLineEdit(self.equations_group_box)
            self.lineEdits[f"f{i}_1"].setStyleSheet(defaultLineEditStyleSheet)
            self.lineEdits[f"f{i}_1"].setObjectName(f"lineEdits_f{i}_1")
            self.lineEdits[f"f{i}_1"].setText(str(round(random.random() * 0.7 + 0.01, 2)))
            self.equations_scroll_widget_layout.addWidget(self.lineEdits[f"f{i}_1"], i - 1, 1, 1, 1)

            self.labels[f"f{i}_2"] = QtWidgets.QLabel(self.equations_group_box)
            self.labels[f"f{i}_2"].setObjectName(f"labels_f{i}_2")
            self.labels[f"f{i}_2"].setText("*x^3+")
            self.equations_scroll_widget_layout.addWidget(self.labels[f"f{i}_2"], i - 1, 2, 1, 1)

            self.lineEdits[f"f{i}_2"] = QtWidgets.QLineEdit(self.equations_group_box)
            self.lineEdits[f"f{i}_2"].setStyleSheet(defaultLineEditStyleSheet)
            self.lineEdits[f"f{i}_2"].setObjectName(f"lineEdits_f{i}_2")
            self.lineEdits[f"f{i}_2"].setText(str(round(random.random() * 0.7 + 0.01, 2)))
            self.equations_scroll_widget_layout.addWidget(self.lineEdits[f"f{i}_2"], i - 1, 3, 1, 1)

            self.labels[f"f{i}_3"] = QtWidgets.QLabel(self.equations_group_box)
            self.labels[f"f{i}_3"].setObjectName(f"labels_f{i}_3")
            self.labels[f"f{i}_3"].setText("*x^2+")
            self.equations_scroll_widget_layout.addWidget(self.labels[f"f{i}_3"], i - 1, 4, 1, 1)

            self.lineEdits[f"f{i}_3"] = QtWidgets.QLineEdit(self.equations_group_box)
            self.lineEdits[f"f{i}_3"].setStyleSheet(defaultLineEditStyleSheet)
            self.lineEdits[f"f{i}_3"].setObjectName(f"lineEdits_f{i}_3")
            self.lineEdits[f"f{i}_3"].setText(str(round(random.random() * 0.7 + 0.01, 2)))
            self.equations_scroll_widget_layout.addWidget(self.lineEdits[f"f{i}_3"], i - 1, 5, 1, 1)

            self.labels[f"f{i}_4"] = QtWidgets.QLabel(self.equations_group_box)
            self.labels[f"f{i}_4"].setObjectName(f"labels_f{i}_4")
            self.labels[f"f{i}_4"].setText("*x+")
            self.equations_scroll_widget_layout.addWidget(self.labels[f"f{i}_4"], i - 1, 6, 1, 1)

            self.lineEdits[f"f{i}_4"] = QtWidgets.QLineEdit(self.equations_group_box)
            self.lineEdits[f"f{i}_4"].setStyleSheet(defaultLineEditStyleSheet)
            self.lineEdits[f"f{i}_4"].setObjectName(f"lineEdits_f{i}_4")
            self.lineEdits[f"f{i}_4"].setText(str(round(random.random() * 0.7 + 0.01, 2)))
            self.equations_scroll_widget_layout.addWidget(self.lineEdits[f"f{i}_4"], i - 1, 7, 1, 1)
        self.equations_scroll_area.setWidget(self.equations_scroll_area_widget)
