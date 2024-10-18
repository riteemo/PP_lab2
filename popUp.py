from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Callable

#  Класс, описывающий всплывающее окно
class MeasureWindow(object):
    def __init__(self, measure: str, measure_list: list[str], measure_proportions: dict[str, tuple[Callable]]):
        super().__init__()
        self.measure = measure
        self.measure_list = measure_list
        self.connections = {}  # Словарь, в котором хранится строка и соответствующая единица измерения
        self.measure_proportions = measure_proportions
        self.zero_value: float = 0 #  Величина СИ
        self.error_occurred = False #  Флаг ошибки

    # Создание окна
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(421, 378)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        #  Функция для заполнения полей
        def get_field(label, le):
            def inner():
                #  Обработка пустых строк
                if self.__dict__[le].text() == "":
                    self.__dict__[le].setText("0")
                try:
                    self.zero_value = self.measure_proportions[label][1](float(self.__dict__[le].text()))
                    if self.error_occurred:
                        self.label.setText(self.label.text()[:self.label.text().find(' ')])
                    self.error_occurred = False
                    for lineEdit in self.connections:
                        if lineEdit != le:
                            (self.__dict__[lineEdit]
                            .setText(
                                str(self.measure_proportions[self.connections[lineEdit]][0](self.zero_value))))
                except ValueError:
                    print("oh no")
                    if not self.error_occurred:
                        self.label.setText(
                            self.label.text() + " (it's allowed to input only digits and one dot)")
                    self.error_occurred = True

            return inner

        for measure_unit in range(len(self.measure_list)):
            # Автоматическое создание лейблов и инпутов
            self.__dict__[f"label_{measure_unit + 2}"] = QtWidgets.QLabel(Form)
            font = QtGui.QFont()
            font.setFamily("Fixedsys")
            font.setPointSize(12)
            self.__dict__[f"label_{measure_unit + 2}"].setFont(font)
            self.__dict__[f"label_{measure_unit + 2}"].setObjectName(f"label_{measure_unit + 2}")
            self.gridLayout.addWidget(self.__dict__[f"label_{measure_unit + 2}"], measure_unit + 1, 0, 1, 1)

            self.__dict__[f"lineEdit_{measure_unit}"] = QtWidgets.QLineEdit(Form)
            self.__dict__[f"lineEdit_{measure_unit}"].setObjectName(f"lineEdit_{measure_unit}")
            self.gridLayout.addWidget(self.__dict__[f"lineEdit_{measure_unit}"], measure_unit + 1, 1, 1, 1)

            self.connections[f"lineEdit_{measure_unit}"] = self.measure_list[measure_unit]
            #  По изменении пользователем строки, вызывается функция
            (self.__dict__[f"lineEdit_{measure_unit}"]
             .textEdited
             .connect(get_field(self.connections[f"lineEdit_{measure_unit}"], f"lineEdit_{measure_unit}")))

        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", self.measure.capitalize() + " converter"))
        for measure_unit in range(len(self.measure_list)):
            self.__dict__[f"label_{measure_unit + 2}"].setText(_translate("Form", f"{self.measure_list[measure_unit].replace('_', ' ').capitalize()} "))

        self.label.setText(_translate("Form", self.measure.capitalize()))