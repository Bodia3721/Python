import math
from datetime import datetime
import io
import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(927, 526)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 581, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label5 = QtWidgets.QLabel(Form)

                ############################################

        coordinate = (50.249734, 30.830653)
        m = folium.Map(
            tiles='Stamen Terrain',
            # Здесь меняем карту (Stamen Toner, Stamen Terrain, Stamen Watercolor, openstreetmap, cartodbpositron)
            zoom_start=12,
            location=coordinate,
            # max_zoom=100,

        )
        folium.Marker([50.289276, 30.785045], popup='1 Sensor\n50.289276, 30.785045', icon=folium.Icon(color="green"),
                      tooltip='1 Sensor\n50.289276, 30.785045').add_to(m)
        folium.Marker([50.249734, 30.830653], popup='2 Sensor\n50.249734, 30.830653', icon=folium.Icon(color="green"),
                      tooltip='2 Sensor\n50.249734, 30.830653').add_to(m)
        folium.Marker([50.294291, 30.865382], popup='3 Sensor\n50.294291, 30.865382', icon=folium.Icon(color="green"),
                      tooltip='3 Sensor\n50.294291, 30.865382').add_to(m)


        data = io.BytesIO()
        m.save(data, close_file=False)
        self.webView = QWebEngineView()
        self.webView.setHtml(data.getvalue().decode())
        self.verticalLayout.addWidget(self.webView)



        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(590, 0, 331, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(590, 90, 331, 191))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lineEdit.setFont(font)
        self.lineEdit.setToolTipDuration(-1)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(32767)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)
        self.pushButton.clicked.connect(self.calculation)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def calculation(self, webView):
        sensor1 = self.lineEdit.text()
        sensor2 = self.lineEdit_2.text()
        sensor3 = self.lineEdit_3.text()
        # if not sensor1 or sensor2 or sensor3:
        #     msgBox = QMessageBox()
        #     msgBox.setText("The document has been modified.")
        #     msgBox.close()


        ####################################### РАСЧЕТ
        # Швидкість звуку (м/с)
        V = 330
        # Радіус Землі в метрах
        a = 6367449

        # Координати сенсорів S(x,y), x та y - в метрах
        S1 = (50.289276, 30.785045)
        S2 = (50.249734, 30.830653)
        S3 = (50.294291, 30.865382)

        # Масиви для пошуку розв"язків - географічні в метри
        X = [S1[1] * (math.pi / 180 * a * math.cos(S1[0] * math.pi / 180)),
             S2[1] * (math.pi / 180 * a * math.cos(S1[0] * math.pi / 180)),
             S3[1] * (math.pi / 180 * a * math.cos(S1[0] * math.pi / 180))]
        Y = [S1[0] * math.pi / 180 * a, S2[0] * math.pi / 180 * a, S3[0] * math.pi / 180 * a]

        # Функції для пошуку коефіцієнтів системи лінійних рівнянь
        def Aij(i, j):
            return X[i] - X[j]

        def Bij(i, j):
            return Y[i] - Y[j]

        def Dij(T, t, i, j):
            return ((X[i] ** 2 - X[j] ** 2) + (Y[i] ** 2 - Y[j] ** 2) + (t[j] ** 2) * V * V) / 2 + V * V * t[j] * T

        # Визначник матриці
        def det(a1, a2):
            dd = a1[0] * a2[1] - a2[0] * a1[1]
            return dd

        # Пошук координат джерела звуку в залежності від T
        def getXY(T, t):
            a = [Aij(0, 1), Aij(0, 2)]
            b = [Bij(0, 1), Bij(0, 2)]
            d = [Dij(T, t, 0, 1), Dij(T, t, 0, 2)]

            DD = det(a, b)
            Dx = det(d, b)
            Dy = det(a, d)

            x = Dx / DD
            y = Dy / DD
            return (x, y)

        # Функція перевірки точності наближень x,y,T
        def checkData(x, y, T):
            return math.sqrt((x - X[0]) ** 2 + (y - Y[0]) ** 2) - V * T

        J = 0

        # Зняття показників хронометрів сенсорів
        dt1 = datetime.strptime(sensor1, "%d-%m-%Y %H:%M:%S.%f")
        Tmin = dt1

        dt2 = datetime.strptime(sensor2, "%d-%m-%Y %H:%M:%S.%f")
        if dt2 < Tmin:
            J = 1
            Tmin = dt2

        dt3 = datetime.strptime(sensor3, "%d-%m-%Y %H:%M:%S.%f")
        if dt3 < Tmin:
            J = 1
            Tmin = dt3

        t1 = dt1 - Tmin
        t2 = dt2 - Tmin
        t3 = dt3 - Tmin

        t = [t1.total_seconds(), t2.total_seconds(), t2.total_seconds()]

        # Першим має бути сенсор, найближчий до джерела
        if J != 0:
            X[J], X[0] = X[0], X[J]
            Y[J], Y[0] = Y[0], Y[J]
            t[J], t[0] = t[0], t[J]

        T1 = 0
        T2 = 0

        x, y = getXY(T2, t)

        # Шукаємо верхню межу часу, щоб гарантовано отримати проміжок T1 та T2, в якому є розв"язок
        while checkData(x, y, T2) > 0:
            T2 += 100

        delta = 1000

        # Розвязок шукаємо методом поділу проміжку попалам, з точністю до півметра
        while abs(delta) > 0.005 and abs(T1 - T2) > 0.0000001:
            T = (T1 + T2) / 2
            x, y = getXY(T, t)
            delta = checkData(x, y, T)
            if delta < 0:
                T2 = T
            else:
                T1 = T

        xg = y / (math.pi / 180 * a)
        yg = x / (math.pi / 180 * a * math.cos(xg * math.pi / 180))

        # Виводимо результат - географічні координати
        lat = round(xg, 6)
        long = round(yg, 6)

        coordinate = (lat, long)
        m = folium.Map(
            tiles='Stamen Terrain',
            # Здесь меняем карту (Stamen Toner, Stamen Terrain, Stamen Watercolor, openstreetmap, cartodbpositron)
            zoom_start=12,
            location=coordinate,
            # max_zoom=100,

        )
        folium.Marker([50.289276, 30.785045], popup='1 Sensor\n50.289276, 30.785045', icon=folium.Icon(color="green"), tooltip='1 Sensor\n50.289276, 30.785045').add_to(m)
        folium.Marker([50.249734, 30.830653], popup='2 Sensor\n50.249734, 30.830653', icon=folium.Icon(color="green"), tooltip='2 Sensor\n50.249734, 30.830653').add_to(m)
        folium.Marker([50.294291, 30.865382], popup='3 Sensor\n50.294291, 30.865382', icon=folium.Icon(color="green"), tooltip='3 Sensor\n50.294291, 30.865382').add_to(m)
        # folium.Marker([lat, long], popup=f'HYPOCENTER\n{lat}, {long}', icon=folium.Icon(color="red"), tooltip=f'HYPOCENTER\n{lat}, {long}').add_to(m)
        folium.Circle([lat, long], radius=500, popup=f'HYPOCENTER\n{lat}, {long}', color="red", fill=True, tooltip=f'HYPOCENTER\n{lat}, {long}').add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)
        self.webView.setHtml(data.getvalue().decode())




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Received signal time"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Received signal time</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "1 Sensor"))
        self.lineEdit.setToolTip(_translate("Form", "Enter the date and time in the following format: dd-mm-yyyy hh:mi:ss.mmmmmm"))
        self.lineEdit.setPlaceholderText(_translate("Form", "dd-mm-yyyy hh:mi:ss.mmmmmm"))
        self.label_3.setText(_translate("Form", "2 Sensor"))
        self.lineEdit_2.setToolTip(_translate("Form", "Enter the date and time in the following format: dd-mm-yyyy hh:mi:ss.mmmmmm"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "dd-mm-yyyy hh:mi:ss.mmmmmm"))
        self.label_4.setText(_translate("Form", "3 Sensor"))
        self.lineEdit_3.setToolTip(_translate("Form", "Enter the date and time in the following format: dd-mm-yyyy hh:mi:ss.mmmmmm"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "dd-mm-yyyy hh:mi:ss.mmmmmm"))

        self.pushButton.setText(_translate("Form", "CALCULATE HYPOCENTER"))


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)



app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())