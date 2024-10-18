import math
from PyQt5 import QtCore, QtGui, QtWidgets
from popUp import MeasureWindow


#  Класс, описывающий главное окно
class Ui_MainWindow(object):
    def __init__(self):
        #  Словарь вида: физическая величина: единицы измерения
        self.measures = {
            "time": ["nanoseconds", "microseconds", "milliseconds", "seconds", "minutes", "hours", "days"],
            "mass": ["gram", "kilogram", "centner", "ton", "ounce", "lb"],
            "length": ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "mile", "yard"],
            "velocity": ["meter_per_second", "kilometer_per_hour", "mile_per_hour"],
            "square": ["square_meter", "hectare", "square_kilometer", "acre", "square_foot"],
            "volume": ["cubic_millimeter", "cubic_centimeter", "cubic_meter", "milliliter", "liter"],
            "temperature": ["Celsius", "Fahrenheit", "Kelvin"],
            "angle": ["degree", "radian"]
        }
        self.new_window = None #  объект нового окна
        #  Словарь, содержащий функции для перевода единиц измерения, 1 переводит из СИ в единицу измерения, 2 наоборот
        self.converter = {
            "time": {
                "seconds": (lambda x: abs(x), lambda x: abs(x)),
                "nanoseconds": (lambda x: abs(x * 10 ** 9), lambda x: abs(x / 10 ** 9)),
                "microseconds": (lambda x: abs(x * 10 ** 6), lambda x: abs(x / 10 ** 6)),
                "milliseconds": (lambda x: abs(x * 10 ** 3), lambda x: abs(x / 10 ** 3)),
                "minutes": (lambda x: abs(x / 60), lambda x: abs(x * 60)),
                "hours": (lambda x: abs(x / 3600), lambda x: abs(x * 3600)),
                "days": (lambda x: abs(x / (3600 * 24)), lambda x: abs(x * (3600 * 24)))
            },
            "mass": {
                "gram": (lambda x: abs(x), lambda x: abs(x)),
                "kilogram": (lambda x: abs(x / 1000), lambda x: abs(x * 1000)),
                "centner": (lambda x: abs(x / 10 ** 5), lambda x: abs(x * 10 ** 5)),
                "ton": (lambda x: abs(x / 10 ** 6), lambda x: abs(x * 10 ** 6)),
                "ounce": (lambda x: abs(x / 28.3), lambda x: abs(x * 28.3)),
                "lb": (lambda x: abs(x / 483.6), lambda x: abs(x * 28.3))
            },
            "length": {
                "millimeter": (lambda x: abs(x * 1000), lambda x: abs(x / 1000)),
                "centimeter": (lambda x: abs(x * 100), lambda x: abs(x / 100)),
                "meter": (lambda x: abs(x), lambda x: abs(x)),
                "kilometer": (lambda x: abs(x / 1000), lambda x: abs(x * 1000)),
                "inch": (lambda x: abs(x * 39.37), lambda x: abs(x / 39.37)),
                "foot": (lambda x: abs(x * 3.28), lambda x: abs(x / 3.28)),
                "mile": (lambda x: abs(x / 1609.34), lambda x: abs(x * 1609.34)),
                "yard": (lambda x: abs(x * 1.09), lambda x: abs(x / 1.09))
            },
            "velocity": {
                "meter_per_second": (lambda x: x, lambda x: x),
                "kilometer_per_hour": (lambda x: x * 3.6, lambda x: x / 3.6),
                "mile_per_hour": (lambda x: x * 2.24, lambda x: x / 2.24)
            },
            "square": {
                "square_meter": (lambda x: abs(x), lambda x: abs(x)),
                "hectare": (lambda x: abs(x / 10 ** 4), lambda x: abs(x * 10 ** 4)),
                "square_kilometer": (lambda x: abs(x / 10 ** 6), lambda x: abs(x * 10 ** 6)),
                "acre": (lambda x: abs(x / 4046.86), lambda x: abs(x * 4046.86)),
                "square_foot": (lambda x: abs(x * 10.76), lambda x: abs(x / 10.76))
            },
            "volume": {
                "cubic_millimeter": (lambda x: abs(x * 10 ** 9), lambda x: abs(x / 10 ** 9)),
                "cubic_centimeter": (lambda x: abs(x * 10 ** 6), lambda x: abs(x / 10 ** 6)),
                "cubic_meter": (lambda x: abs(x), lambda x: abs(x)),
                "milliliter": (lambda x: abs(x * 10 ** 6), lambda x: abs(x / 10 ** 6)),
                "liter": (lambda x: abs(x * 1000), lambda x: abs(x / 1000))
            },
            "temperature": {
                "Celsius": (lambda x: x, lambda x: x),
                "Fahrenheit": (lambda x: (x * 9 / 5) + 32, lambda x: (x - 32) * 5 / 9),
                "Kelvin": (lambda x: x + 273.15, lambda x: x - 273.15)
            },
            "angle": {
                "degree": (lambda x: x, lambda x: x),
                "radian": (lambda x: x * math.pi / 180, lambda x: x * 180 / math.pi)
            }
        }

    #  Создание главного окна (меню)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 504)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("QTabWidget::pane\n"
"{\n"
"background-color:rgb(255, 0, 0);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 2, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        palette = QtGui.QPalette()
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 1, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_3.addWidget(self.pushButton_8, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(lambda: self.print_info("time"))
        self.pushButton_2.clicked.connect(lambda: self.print_info("length"))
        self.pushButton_3.clicked.connect(lambda: self.print_info("mass"))
        self.pushButton_4.clicked.connect(lambda: self.print_info("velocity"))
        self.pushButton_5.clicked.connect(lambda: self.print_info("temperature"))
        self.pushButton_6.clicked.connect(lambda: self.print_info("volume"))
        self.pushButton_7.clicked.connect(lambda: self.print_info("angle"))
        self.pushButton_8.clicked.connect(lambda: self.print_info("square"))

    #  Функция, которая вызывается при нажатии на одну из кнопок. Создаёт новое окно на основе названия величины,
    #  единиц измерения и функций для перевода
    def print_info(self, btn_text: str):
        window = MeasureWindow(btn_text, self.measures[btn_text], self.converter[btn_text])
        self.new_window = QtWidgets.QWidget()
        window.setupUi(self.new_window) # создание окна self.new_window на основе класса MeasureWindow
        self.new_window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Converter"))
        self.pushButton_7.setText(_translate("MainWindow", "Angle"))
        self.pushButton.setText(_translate("MainWindow", "Time"))
        self.pushButton_6.setText(_translate("MainWindow", "Volume"))
        self.pushButton_5.setText(_translate("MainWindow", "Temperature"))
        self.pushButton_4.setText(_translate("MainWindow", "Velocity"))
        self.pushButton_2.setText(_translate("MainWindow", "Length"))
        self.pushButton_3.setText(_translate("MainWindow", "Mass"))
        self.pushButton_8.setText(_translate("MainWindow", "Square"))
        self.label.setText(_translate("MainWindow", "Choose the measure you want to convert:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
