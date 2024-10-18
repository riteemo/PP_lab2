from PyQt5 import QtCore, QtGui, QtWidgets


class MeasureWindow(object):

    def __init__(self, measure: str, measure_list: list[str]):
        super().__init__()
        self.measure = measure
        self.measure_list = measure_list
        self.connections = {}  # {lineEdit_5: cubic football fields}

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(421, 378)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

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

            def get_field(label):
                def inner():
                    print(label)
                return inner

            self.connections[f"lineEdit_{measure_unit}"] = self.measure_list[measure_unit]
            (self.__dict__[f"lineEdit_{measure_unit}"]
             .textChanged
             .connect(get_field(self.connections[f"lineEdit_{measure_unit}"])))


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
