# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MalnutritionApp(object):
    def setupUi(self, MalnutritionApp):
        if not MalnutritionApp.objectName():
            MalnutritionApp.setObjectName(u"MalnutritionApp")
        MalnutritionApp.resize(1008, 709)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MalnutritionApp.sizePolicy().hasHeightForWidth())
        MalnutritionApp.setSizePolicy(sizePolicy)
        MalnutritionApp.setMinimumSize(QSize(1008, 709))
        MalnutritionApp.setMaximumSize(QSize(1008, 709))
        MalnutritionApp.setStyleSheet(u"QPushButton {\n"
"            font-size: 12px;\n"
"            padding: 10px;\n"
"            border-radius: 8px;\n"
"            color: white;\n"
"            border: none;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #45a049;\n"
"        }\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #2980b9; /* Darker color on click */\n"
"    transform: scale(0.95); /* Slightly shrink the button */\n"
"}")
        self.centralwidget = QWidget(MalnutritionApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1011, 691))
        self.stackedWidget.setStyleSheet(u"")
        self.Login = QWidget()
        self.Login.setObjectName(u"Login")
        self.page11 = QFrame(self.Login)
        self.page11.setObjectName(u"page11")
        self.page11.setGeometry(QRect(0, 0, 1011, 701))
        self.page11.setAutoFillBackground(False)
        self.page11.setStyleSheet(u"QFrame#page11{border-image: url(:/child1/child2.jpg) 0 0 0 0 stretch stretch;}")
        self.page11.setFrameShape(QFrame.Shape.StyledPanel)
        self.page11.setFrameShadow(QFrame.Shadow.Raised)
        self.LoginBox_2 = QFrame(self.page11)
        self.LoginBox_2.setObjectName(u"LoginBox_2")
        self.LoginBox_2.setGeometry(QRect(80, 190, 331, 201))
        self.LoginBox_2.setStyleSheet(u"QWidget{color: rgb(255, 255, 255);}\n"
"QFrame#LoginBox_2{\n"
"	\n"
"	\n"
"	background-color: rgb(44, 62, 80);\n"
"border: 2px solid #3498db; /* Optional border with color */\n"
"border-radius: 15px; /* Adjust the radius to control the curvature */\n"
"}\n"
"\n"
"")
        self.LoginBox = QVBoxLayout(self.LoginBox_2)
        self.LoginBox.setObjectName(u"LoginBox")
        self.label = QLabel(self.LoginBox_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label.setStyleSheet(u"color: rgb(189, 195, 199);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.LoginBox.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.LoginBox_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.userInput = QLineEdit(self.LoginBox_2)
        self.userInput.setObjectName(u"userInput")
        sizePolicy.setHeightForWidth(self.userInput.sizePolicy().hasHeightForWidth())
        self.userInput.setSizePolicy(sizePolicy)
        self.userInput.setMinimumSize(QSize(160, 0))
        self.userInput.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.userInput)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.LoginBox.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.LoginBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.pswdInput = QLineEdit(self.LoginBox_2)
        self.pswdInput.setObjectName(u"pswdInput")
        sizePolicy.setHeightForWidth(self.pswdInput.sizePolicy().hasHeightForWidth())
        self.pswdInput.setSizePolicy(sizePolicy)
        self.pswdInput.setMinimumSize(QSize(160, 0))
        self.pswdInput.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.pswdInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout.addWidget(self.pswdInput)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.LoginBox.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.loginBtn = QPushButton(self.LoginBox_2)
        self.loginBtn.setObjectName(u"loginBtn")
        font2 = QFont()
        font2.setBold(True)
        self.loginBtn.setFont(font2)
        self.loginBtn.setStyleSheet(u"background-color: rgb(41, 128, 185);\n"
"font-size:13px;")

        self.horizontalLayout_3.addWidget(self.loginBtn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.LoginBox.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.Login)
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.Dashboard.setStyleSheet(u"QWidget#Dashboard{\n"
"	\n"
"	border-image: url(:/child1/26807.jpg);\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(52, 73, 94);\n"
"	font-size: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(75, 70, 94);\n"
";}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(154, 17, 13);\n"
";}")
        self.label_4 = QLabel(self.Dashboard)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 10, 851, 61))
        font3 = QFont()
        font3.setFamilies([u"Barlow"])
        font3.setPointSize(35)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.dashboardPredictionBtn = QPushButton(self.Dashboard)
        self.dashboardPredictionBtn.setObjectName(u"dashboardPredictionBtn")
        self.dashboardPredictionBtn.setGeometry(QRect(50, 190, 211, 51))
        font4 = QFont()
        font4.setFamilies([u"Barlow"])
        font4.setBold(True)
        self.dashboardPredictionBtn.setFont(font4)
        self.dashboardPredictionBtn.setStyleSheet(u"background-color: rgb(52, 73, 94);")
        self.dashboardDietBtn = QPushButton(self.Dashboard)
        self.dashboardDietBtn.setObjectName(u"dashboardDietBtn")
        self.dashboardDietBtn.setGeometry(QRect(50, 280, 211, 51))
        self.dashboardDietBtn.setFont(font4)
        self.dashboardDietBtn.setStyleSheet(u"background-color: rgb(52, 73, 94);")
        self.dashboardScaleBtn = QPushButton(self.Dashboard)
        self.dashboardScaleBtn.setObjectName(u"dashboardScaleBtn")
        self.dashboardScaleBtn.setGeometry(QRect(50, 370, 211, 51))
        self.dashboardScaleBtn.setFont(font4)
        self.dashboardScaleBtn.setStyleSheet(u"background-color: rgb(52, 73, 94);")
        self.dashboardModelsBtn = QPushButton(self.Dashboard)
        self.dashboardModelsBtn.setObjectName(u"dashboardModelsBtn")
        self.dashboardModelsBtn.setGeometry(QRect(50, 460, 211, 51))
        self.dashboardModelsBtn.setFont(font4)
        self.dashboardModelsBtn.setStyleSheet(u"background-color: rgb(52, 73, 94);")
        self.dashboardRecordsBtn = QPushButton(self.Dashboard)
        self.dashboardRecordsBtn.setObjectName(u"dashboardRecordsBtn")
        self.dashboardRecordsBtn.setGeometry(QRect(50, 550, 211, 51))
        self.dashboardRecordsBtn.setFont(font4)
        self.dashboardRecordsBtn.setStyleSheet(u"background-color: rgb(52, 73, 94);")
        self.dashboardRegisterBtn = QPushButton(self.Dashboard)
        self.dashboardRegisterBtn.setObjectName(u"dashboardRegisterBtn")
        self.dashboardRegisterBtn.setGeometry(QRect(760, 190, 211, 51))
        self.dashboardRegisterBtn.setFont(font4)
        self.dashboardRegisterBtn.setStyleSheet(u"background-color: rgb(52, 73, 94);")
        self.dashboardAboutBtn = QPushButton(self.Dashboard)
        self.dashboardAboutBtn.setObjectName(u"dashboardAboutBtn")
        self.dashboardAboutBtn.setGeometry(QRect(760, 360, 211, 51))
        self.dashboardAboutBtn.setFont(font4)
        self.dashboardAboutBtn.setStyleSheet(u"background-color: rgb(52, 73, 94);")
        self.dashboardLogoutBtn = QPushButton(self.Dashboard)
        self.dashboardLogoutBtn.setObjectName(u"dashboardLogoutBtn")
        self.dashboardLogoutBtn.setGeometry(QRect(760, 450, 211, 51))
        self.dashboardLogoutBtn.setFont(font4)
        self.dashboardLogoutBtn.setStyleSheet(u"background-color: rgb(52, 73, 94);")
        self.label_28 = QLabel(self.Dashboard)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(920, 20, 51, 51))
        self.label_28.setStyleSheet(u"\n"
"border-image: url(:/child1/user.png);")
        self.usernamelabel = QLabel(self.Dashboard)
        self.usernamelabel.setObjectName(u"usernamelabel")
        self.usernamelabel.setGeometry(QRect(890, 80, 111, 21))
        font5 = QFont()
        font5.setFamilies([u"Barlow"])
        font5.setPointSize(9)
        font5.setBold(True)
        self.usernamelabel.setFont(font5)
        self.usernamelabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.usernamelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dashboardDataBtn = QPushButton(self.Dashboard)
        self.dashboardDataBtn.setObjectName(u"dashboardDataBtn")
        self.dashboardDataBtn.setGeometry(QRect(760, 270, 211, 51))
        self.dashboardDataBtn.setFont(font4)
        self.dashboardDataBtn.setStyleSheet(u"background-color: rgb(52, 73, 94);")
        self.stackedWidget.addWidget(self.Dashboard)
        self.Prediction = QWidget()
        self.Prediction.setObjectName(u"Prediction")
        self.Prediction.setStyleSheet(u"QWidget#Prediction{background-color: rgb(52, 73, 94);}\n"
"QLabel{color: rgb(255, 255, 255);}\n"
"QLineEdit {\n"
"            font-size: 15px;\n"
"            padding: 5px;\n"
"            border-radius: 8px;\n"
"            border: 2px solid #ccc;\n"
"            background: white;\n"
"        }\n"
"        QComboBox {\n"
"            font-size: 15px;\n"
"            padding: 5px;\n"
"            border-radius: 8px;\n"
"            border: 2px solid #ccc;\n"
"            background: white;\n"
"        }")
        self.label_5 = QLabel(self.Prediction)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 10, 831, 61))
        font6 = QFont()
        font6.setFamilies([u"Barlow"])
        font6.setPointSize(25)
        font6.setBold(True)
        self.label_5.setFont(font6)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.Prediction)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 80, 941, 294))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setFamilies([u"Barlow"])
        font7.setPointSize(15)
        font7.setBold(False)
        self.label_6.setFont(font7)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.patientIDInput = QLineEdit(self.verticalLayoutWidget)
        self.patientIDInput.setObjectName(u"patientIDInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.patientIDInput.sizePolicy().hasHeightForWidth())
        self.patientIDInput.setSizePolicy(sizePolicy2)
        self.patientIDInput.setMinimumSize(QSize(700, 0))
        self.patientIDInput.setBaseSize(QSize(100, 0))
        self.patientIDInput.setFont(font4)

        self.horizontalLayout_4.addWidget(self.patientIDInput)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.heightInput = QLineEdit(self.verticalLayoutWidget)
        self.heightInput.setObjectName(u"heightInput")
        sizePolicy2.setHeightForWidth(self.heightInput.sizePolicy().hasHeightForWidth())
        self.heightInput.setSizePolicy(sizePolicy2)
        self.heightInput.setMinimumSize(QSize(700, 0))
        font8 = QFont()
        font8.setFamilies([u"Barlow"])
        font8.setBold(False)
        self.heightInput.setFont(font8)

        self.horizontalLayout_7.addWidget(self.heightInput)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font7)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.WeightInput = QLineEdit(self.verticalLayoutWidget)
        self.WeightInput.setObjectName(u"WeightInput")
        sizePolicy2.setHeightForWidth(self.WeightInput.sizePolicy().hasHeightForWidth())
        self.WeightInput.setSizePolicy(sizePolicy2)
        self.WeightInput.setMinimumSize(QSize(700, 0))
        font9 = QFont()
        font9.setFamilies([u"Barlow"])
        self.WeightInput.setFont(font9)

        self.horizontalLayout_6.addWidget(self.WeightInput)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.AgeInput = QLineEdit(self.verticalLayoutWidget)
        self.AgeInput.setObjectName(u"AgeInput")
        sizePolicy2.setHeightForWidth(self.AgeInput.sizePolicy().hasHeightForWidth())
        self.AgeInput.setSizePolicy(sizePolicy2)
        self.AgeInput.setMinimumSize(QSize(700, 0))
        self.AgeInput.setFont(font9)

        self.horizontalLayout_8.addWidget(self.AgeInput)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font7)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.sexInput = QComboBox(self.verticalLayoutWidget)
        self.sexInput.setObjectName(u"sexInput")
        sizePolicy2.setHeightForWidth(self.sexInput.sizePolicy().hasHeightForWidth())
        self.sexInput.setSizePolicy(sizePolicy2)
        self.sexInput.setMinimumSize(QSize(700, 29))

        self.horizontalLayout_9.addWidget(self.sexInput)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_18)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font7)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.modelInput = QComboBox(self.verticalLayoutWidget)
        self.modelInput.setObjectName(u"modelInput")
        sizePolicy2.setHeightForWidth(self.modelInput.sizePolicy().hasHeightForWidth())
        self.modelInput.setSizePolicy(sizePolicy2)
        self.modelInput.setMinimumSize(QSize(700, 29))

        self.horizontalLayout_5.addWidget(self.modelInput)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.backBtn = QPushButton(self.Prediction)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(930, 20, 71, 31))
        self.backBtn.setFont(font2)
        self.backBtn.setStyleSheet(u"background-color: rgb(192, 57, 43);")
        self.predictBtn = QPushButton(self.Prediction)
        self.predictBtn.setObjectName(u"predictBtn")
        self.predictBtn.setGeometry(QRect(230, 390, 691, 41))
        self.predictBtn.setFont(font4)
        self.predictBtn.setStyleSheet(u"QPushButton{font-size: 25px;\n"
"	background-color: rgb(41, 128, 185);\n"
"}\n"
"")
        self.resultLabel = QLabel(self.Prediction)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setGeometry(QRect(230, 470, 491, 41))
        font10 = QFont()
        font10.setPointSize(20)
        self.resultLabel.setFont(font10)
        self.accuracyLabel = QLabel(self.Prediction)
        self.accuracyLabel.setObjectName(u"accuracyLabel")
        self.accuracyLabel.setGeometry(QRect(230, 540, 491, 31))
        font11 = QFont()
        font11.setPointSize(15)
        self.accuracyLabel.setFont(font11)
        self.nutrtionbtn = QPushButton(self.Prediction)
        self.nutrtionbtn.setObjectName(u"nutrtionbtn")
        self.nutrtionbtn.setGeometry(QRect(230, 610, 461, 51))
        self.nutrtionbtn.setStyleSheet(u"font: 16pt \"Barlow\";\n"
"background-color: rgb(155, 89, 182);")
        self.stackedWidget.addWidget(self.Prediction)
        self.PredictorScale = QWidget()
        self.PredictorScale.setObjectName(u"PredictorScale")
        self.PredictorScale.setStyleSheet(u"QWidget#PredictorScale{background-color: rgb(236, 240, 241);}")
        self.backBtn_2 = QPushButton(self.PredictorScale)
        self.backBtn_2.setObjectName(u"backBtn_2")
        self.backBtn_2.setGeometry(QRect(920, 20, 71, 31))
        self.backBtn_2.setFont(font2)
        self.backBtn_2.setStyleSheet(u"background-color: rgb(192, 57, 43);")
        self.label_14 = QLabel(self.PredictorScale)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(60, 40, 731, 631))
        font12 = QFont()
        font12.setFamilies([u"Barlow"])
        font12.setPointSize(15)
        self.label_14.setFont(font12)
        self.label_14.setWordWrap(True)
        self.stackedWidget.addWidget(self.PredictorScale)
        self.Records = QWidget()
        self.Records.setObjectName(u"Records")
        self.Records.setStyleSheet(u"QWidget#Records{background-color: rgb(127, 140, 141);}")
        self.label_12 = QLabel(self.Records)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(440, 10, 131, 61))
        self.label_12.setFont(font6)
        self.backBtn2 = QPushButton(self.Records)
        self.backBtn2.setObjectName(u"backBtn2")
        self.backBtn2.setGeometry(QRect(920, 20, 71, 31))
        self.backBtn2.setFont(font2)
        self.backBtn2.setStyleSheet(u"background-color: rgb(192, 57, 43);")
        self.tableWidget = QTableWidget(self.Records)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 80, 921, 581))
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.stackedWidget.addWidget(self.Records)
        self.DietPage = QWidget()
        self.DietPage.setObjectName(u"DietPage")
        self.DietPage.setStyleSheet(u"QWidget#DietPage{\n"
"	\n"
"	background-color: rgb(236, 240, 241);\n"
"}\n"
"")
        self.label_13 = QLabel(self.DietPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 30, 631, 651))
        font13 = QFont()
        font13.setFamilies([u"Barlow"])
        font13.setPointSize(12)
        self.label_13.setFont(font13)
        self.dietBackBtn = QPushButton(self.DietPage)
        self.dietBackBtn.setObjectName(u"dietBackBtn")
        self.dietBackBtn.setGeometry(QRect(920, 20, 71, 31))
        self.dietBackBtn.setFont(font2)
        self.dietBackBtn.setStyleSheet(u"background-color: rgb(192, 57, 43);")
        self.label_15 = QLabel(self.DietPage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(540, 180, 451, 471))
        self.label_15.setStyleSheet(u"border-image: url(:/child1/deit.jpg);")
        self.stackedWidget.addWidget(self.DietPage)
        self.ModelPage = QWidget()
        self.ModelPage.setObjectName(u"ModelPage")
        self.ModelPage.setStyleSheet(u"QWidget#ModelPage{\n"
"	background-color: rgb(189, 195, 199);\n"
"}")
        self.label_16 = QLabel(self.ModelPage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 40, 1001, 561))
        self.ModelBackBtn = QPushButton(self.ModelPage)
        self.ModelBackBtn.setObjectName(u"ModelBackBtn")
        self.ModelBackBtn.setGeometry(QRect(920, 20, 71, 31))
        self.ModelBackBtn.setFont(font2)
        self.ModelBackBtn.setStyleSheet(u"background-color: rgb(192, 57, 43);")
        self.stackedWidget.addWidget(self.ModelPage)
        self.RegisterPage = QWidget()
        self.RegisterPage.setObjectName(u"RegisterPage")
        self.RegisterPage.setStyleSheet(u"QWidget#RegisterPage{\n"
"	\n"
"	background-color: rgb(41, 128, 185);\n"
"}")
        self.RegisterBackBtn = QPushButton(self.RegisterPage)
        self.RegisterBackBtn.setObjectName(u"RegisterBackBtn")
        self.RegisterBackBtn.setGeometry(QRect(920, 20, 71, 31))
        self.RegisterBackBtn.setFont(font2)
        self.RegisterBackBtn.setStyleSheet(u"background-color: rgb(52, 73, 94);")
        self.label_17 = QLabel(self.RegisterPage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(230, 20, 571, 61))
        self.label_17.setFont(font3)
        self.verticalLayoutWidget_2 = QWidget(self.RegisterPage)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 100, 1311, 311))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_19)

        self.label_18 = QLabel(self.verticalLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")
        font14 = QFont()
        font14.setFamilies([u"Barlow"])
        font14.setPointSize(12)
        font14.setBold(True)
        self.label_18.setFont(font14)

        self.horizontalLayout_10.addWidget(self.label_18)

        self.nameInput = QLineEdit(self.verticalLayoutWidget_2)
        self.nameInput.setObjectName(u"nameInput")
        sizePolicy.setHeightForWidth(self.nameInput.sizePolicy().hasHeightForWidth())
        self.nameInput.setSizePolicy(sizePolicy)
        self.nameInput.setMinimumSize(QSize(500, 0))
        font15 = QFont()
        font15.setFamilies([u"Barlow"])
        font15.setPointSize(12)
        font15.setBold(False)
        self.nameInput.setFont(font15)

        self.horizontalLayout_10.addWidget(self.nameInput)

        self.horizontalSpacer_20 = QSpacerItem(650, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_20)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_27)

        self.label_22 = QLabel(self.verticalLayoutWidget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font14)

        self.horizontalLayout_14.addWidget(self.label_22)

        self.comboBox = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(500, 0))
        self.comboBox.setFont(font13)

        self.horizontalLayout_14.addWidget(self.comboBox)

        self.horizontalSpacer_28 = QSpacerItem(650, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_28)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_25)

        self.label_21 = QLabel(self.verticalLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font14)

        self.horizontalLayout_13.addWidget(self.label_21)

        self.nameInput_4 = QLineEdit(self.verticalLayoutWidget_2)
        self.nameInput_4.setObjectName(u"nameInput_4")
        sizePolicy.setHeightForWidth(self.nameInput_4.sizePolicy().hasHeightForWidth())
        self.nameInput_4.setSizePolicy(sizePolicy)
        self.nameInput_4.setMinimumSize(QSize(500, 0))
        self.nameInput_4.setFont(font15)

        self.horizontalLayout_13.addWidget(self.nameInput_4)

        self.horizontalSpacer_26 = QSpacerItem(650, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_26)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_23)

        self.label_20 = QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font14)

        self.horizontalLayout_12.addWidget(self.label_20)

        self.nameInput_3 = QLineEdit(self.verticalLayoutWidget_2)
        self.nameInput_3.setObjectName(u"nameInput_3")
        sizePolicy.setHeightForWidth(self.nameInput_3.sizePolicy().hasHeightForWidth())
        self.nameInput_3.setSizePolicy(sizePolicy)
        self.nameInput_3.setMinimumSize(QSize(500, 0))
        self.nameInput_3.setFont(font15)

        self.horizontalLayout_12.addWidget(self.nameInput_3)

        self.horizontalSpacer_24 = QSpacerItem(650, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_24)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_33)

        self.label_25 = QLabel(self.verticalLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font14)

        self.horizontalLayout_17.addWidget(self.label_25)

        self.nameInput_8 = QLineEdit(self.verticalLayoutWidget_2)
        self.nameInput_8.setObjectName(u"nameInput_8")
        sizePolicy.setHeightForWidth(self.nameInput_8.sizePolicy().hasHeightForWidth())
        self.nameInput_8.setSizePolicy(sizePolicy)
        self.nameInput_8.setMinimumSize(QSize(500, 0))
        self.nameInput_8.setFont(font15)

        self.horizontalLayout_17.addWidget(self.nameInput_8)

        self.horizontalSpacer_34 = QSpacerItem(650, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_34)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_21)

        self.label_19 = QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font14)

        self.horizontalLayout_11.addWidget(self.label_19)

        self.nameInput_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.nameInput_2.setObjectName(u"nameInput_2")
        sizePolicy.setHeightForWidth(self.nameInput_2.sizePolicy().hasHeightForWidth())
        self.nameInput_2.setSizePolicy(sizePolicy)
        self.nameInput_2.setMinimumSize(QSize(500, 0))
        self.nameInput_2.setFont(font15)

        self.horizontalLayout_11.addWidget(self.nameInput_2)

        self.horizontalSpacer_22 = QSpacerItem(650, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_22)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayoutWidget_6 = QWidget(self.RegisterPage)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(280, 640, 909, 252))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_29)

        self.label_23 = QLabel(self.horizontalLayoutWidget_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font14)

        self.horizontalLayout_15.addWidget(self.label_23)

        self.nameInput_6 = QLineEdit(self.horizontalLayoutWidget_6)
        self.nameInput_6.setObjectName(u"nameInput_6")
        sizePolicy.setHeightForWidth(self.nameInput_6.sizePolicy().hasHeightForWidth())
        self.nameInput_6.setSizePolicy(sizePolicy)
        self.nameInput_6.setMinimumSize(QSize(500, 0))
        self.nameInput_6.setFont(font15)

        self.horizontalLayout_15.addWidget(self.nameInput_6)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_30)

        self.ModelBackBtn_3 = QPushButton(self.RegisterPage)
        self.ModelBackBtn_3.setObjectName(u"ModelBackBtn_3")
        self.ModelBackBtn_3.setGeometry(QRect(160, 480, 491, 51))
        self.ModelBackBtn_3.setFont(font2)
        self.ModelBackBtn_3.setStyleSheet(u"background-color: rgb(52, 73, 94);\n"
"font-size:15px;")
        self.ERRORLABEL = QLabel(self.RegisterPage)
        self.ERRORLABEL.setObjectName(u"ERRORLABEL")
        self.ERRORLABEL.setGeometry(QRect(160, 440, 491, 21))
        self.ERRORLABEL.setFont(font14)
        self.label_27 = QLabel(self.RegisterPage)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(110, 10, 111, 81))
        self.label_27.setStyleSheet(u"border-image: url(:/child1/It_is_a_official_logo_of_SDM_Institute_of_Technology,_Ujire.jpg);")
        self.stackedWidget.addWidget(self.RegisterPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.aboutPage.setStyleSheet(u"QWidget#aboutPage{\n"
"	background-color: rgb(255, 255, 250);\n"
"}")
        self.aboutbackBtn = QPushButton(self.aboutPage)
        self.aboutbackBtn.setObjectName(u"aboutbackBtn")
        self.aboutbackBtn.setGeometry(QRect(930, 30, 71, 31))
        self.aboutbackBtn.setFont(font2)
        self.aboutbackBtn.setStyleSheet(u"background-color: rgb(192, 57, 43);")
        self.label_26 = QLabel(self.aboutPage)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 60, 911, 631))
        font16 = QFont()
        font16.setFamilies([u"Barlow"])
        font16.setPointSize(10)
        self.label_26.setFont(font16)
        self.label_26.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_31 = QLabel(self.aboutPage)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 10, 501, 50))
        self.label_31.setFont(font6)
        self.label_31.setStyleSheet(u"color: rgb(13, 50, 77);")
        self.label_24 = QLabel(self.aboutPage)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(590, 70, 411, 321))
        self.label_24.setStyleSheet(u"border-image: url(:/child1/WhatsApp Image 2024-12-19 at 11.11.12 AM.jpeg);")
        self.stackedWidget.addWidget(self.aboutPage)
        self.graphpage = QWidget()
        self.graphpage.setObjectName(u"graphpage")
        self.graphpage.setStyleSheet(u"QWidget#graphpage{\n"
"	background-color: rgb(189, 195, 199);\n"
"}")
        self.label_29 = QLabel(self.graphpage)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(370, 10, 281, 61))
        self.label_29.setFont(font6)
        self.label_29.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.graphbackbtn = QPushButton(self.graphpage)
        self.graphbackbtn.setObjectName(u"graphbackbtn")
        self.graphbackbtn.setGeometry(QRect(930, 30, 71, 31))
        self.graphbackbtn.setFont(font2)
        self.graphbackbtn.setStyleSheet(u"background-color: rgb(192, 57, 43);")
        self.graphwidget = QWidget(self.graphpage)
        self.graphwidget.setObjectName(u"graphwidget")
        self.graphwidget.setGeometry(QRect(10, 80, 981, 601))
        self.stackedWidget.addWidget(self.graphpage)
        MalnutritionApp.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MalnutritionApp)
        self.statusbar.setObjectName(u"statusbar")
        MalnutritionApp.setStatusBar(self.statusbar)

        self.retranslateUi(MalnutritionApp)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MalnutritionApp)
    # setupUi

    def retranslateUi(self, MalnutritionApp):
        MalnutritionApp.setWindowTitle(QCoreApplication.translate("MalnutritionApp", u"Malnutrition App", None))
        self.label.setText(QCoreApplication.translate("MalnutritionApp", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("MalnutritionApp", u"Username: ", None))
        self.label_2.setText(QCoreApplication.translate("MalnutritionApp", u"Password: ", None))
        self.loginBtn.setText(QCoreApplication.translate("MalnutritionApp", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("MalnutritionApp", u"Nutrition Diagnosis & Detection App", None))
        self.dashboardPredictionBtn.setText(QCoreApplication.translate("MalnutritionApp", u"Malnutrition Prediction", None))
        self.dashboardDietBtn.setText(QCoreApplication.translate("MalnutritionApp", u"Diet & Nutrition Guide", None))
        self.dashboardScaleBtn.setText(QCoreApplication.translate("MalnutritionApp", u"Predictor Scale", None))
        self.dashboardModelsBtn.setText(QCoreApplication.translate("MalnutritionApp", u"AI Models", None))
        self.dashboardRecordsBtn.setText(QCoreApplication.translate("MalnutritionApp", u"Records", None))
        self.dashboardRegisterBtn.setText(QCoreApplication.translate("MalnutritionApp", u"Register", None))
        self.dashboardAboutBtn.setText(QCoreApplication.translate("MalnutritionApp", u"About Us", None))
        self.dashboardLogoutBtn.setText(QCoreApplication.translate("MalnutritionApp", u"Logout", None))
        self.label_28.setText("")
        self.usernamelabel.setText("")
        self.dashboardDataBtn.setText(QCoreApplication.translate("MalnutritionApp", u"Data Analysis", None))
        self.label_5.setText(QCoreApplication.translate("MalnutritionApp", u"AI MALNUTRITION PREDICTOR TOOL", None))
        self.label_6.setText(QCoreApplication.translate("MalnutritionApp", u"Patient ID:", None))
        self.label_9.setText(QCoreApplication.translate("MalnutritionApp", u"Height (cm): ", None))
        self.label_8.setText(QCoreApplication.translate("MalnutritionApp", u"Weight (kg): ", None))
        self.label_10.setText(QCoreApplication.translate("MalnutritionApp", u"Age: ", None))
        self.label_11.setText(QCoreApplication.translate("MalnutritionApp", u"Sex: ", None))
        self.label_7.setText(QCoreApplication.translate("MalnutritionApp", u"ML Model:", None))
        self.backBtn.setText(QCoreApplication.translate("MalnutritionApp", u"BACK", None))
        self.predictBtn.setText(QCoreApplication.translate("MalnutritionApp", u"PREDICT", None))
        self.resultLabel.setText(QCoreApplication.translate("MalnutritionApp", u"Result: ", None))
        self.accuracyLabel.setText(QCoreApplication.translate("MalnutritionApp", u"Accuracy: ", None))
        self.nutrtionbtn.setText(QCoreApplication.translate("MalnutritionApp", u"See Nutrition & Diet Guide", None))
        self.backBtn_2.setText(QCoreApplication.translate("MalnutritionApp", u"BACK", None))
        self.label_14.setText(QCoreApplication.translate("MalnutritionApp", u"<html>\n"
"<head>\n"
"    <style>\n"
"        table {\n"
"            border-collapse: collapse;\n"
"            width: 100%;\n"
"            margin-top: 10px;\n"
"        }\n"
"        th, td {\n"
"            border: 1px solid #ddd;\n"
"            text-align: center;\n"
"            padding: 8px;\n"
"            color: #2c3e50; /* Dark text color for contrast */\n"
"        }\n"
"        th {\n"
"            background-color: #f4f4f4;\n"
"            font-weight: bold;\n"
"        }\n"
"        h1, h3 {\n"
"            color: #2c3e50;\n"
"            font-family: Arial, sans-serif;\n"
"        }\n"
"        p {\n"
"            font-family: Arial, sans-serif;\n"
"            font-size: 14px;\n"
"            color: #34495e;\n"
"        }\n"
"    </style>\n"
"</head>\n"
"<body>\n"
"    <h1>Malnutrition Predictor Scale</h1>\n"
"    <p>The application predicts the nutritional status of children based on the following classifications:</p>\n"
"    <table>\n"
"        <tr>\n"
"            <th>Indicator</th>\n"
"   "
                        "         <th>Description</th>\n"
"            <th>Scale</th>\n"
"        </tr>\n"
"        <tr>\n"
"            <td>Stunting</td>\n"
"            <td>Low height for age, indicating chronic malnutrition.</td>\n"
"            <td>&lt; -2 SD (Standard Deviations)</td>\n"
"        </tr>\n"
"        <tr>\n"
"            <td>Overweight</td>\n"
"            <td>Excess weight for height, indicating risk of obesity.</td>\n"
"            <td>&gt; +2 SD</td>\n"
"        </tr>\n"
"        <tr>\n"
"            <td>Underweight</td>\n"
"            <td>Low weight for age, indicating undernourishment.</td>\n"
"            <td>&lt; -2 SD</td>\n"
"        </tr>\n"
"        <tr>\n"
"            <td>Wasting</td>\n"
"            <td>Low weight for height, indicating acute malnutrition.</td>\n"
"            <td>&lt; -2 SD</td>\n"
"        </tr>\n"
"    </table>\n"
"    <p>\n"
"        Each classification uses the World Health Organization (WHO) standards for child growth to evaluate the nutritional status of children.\n"
"    </p>\n"
""
                        "</body>\n"
"</html>\n"
"", None))
        self.label_12.setText(QCoreApplication.translate("MalnutritionApp", u"Records", None))
        self.backBtn2.setText(QCoreApplication.translate("MalnutritionApp", u"BACK", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MalnutritionApp", u"PatientID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MalnutritionApp", u"Height (cm)", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MalnutritionApp", u"Weight (kg)", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MalnutritionApp", u"Age", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MalnutritionApp", u"Sex", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MalnutritionApp", u"ML Model", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MalnutritionApp", u"Diagnosis", None));
        self.label_13.setText(QCoreApplication.translate("MalnutritionApp", u"<html>\n"
"<head>\n"
"    <style>\n"
"        h1, h3 {\n"
"            color: #2c3e50;\n"
"            font-family: Arial, sans-serif;\n"
"        }\n"
"        p, ul {\n"
"            font-family: Arial, sans-serif;\n"
"            font-size: 14px;\n"
"            color: #34495e;\n"
"        }\n"
"        ul {\n"
"            margin-top: 10px;\n"
"        }\n"
"        .highlight-stunting {\n"
"            color: #e74c3c; /* Vibrant red */\n"
"            font-weight: bold;\n"
"        }\n"
"        .highlight-overweight {\n"
"            color: #f39c12; /* Bright orange */\n"
"            font-weight: bold;\n"
"        }\n"
"        .highlight-underweight {\n"
"            color: #2ecc71; /* Fresh green */\n"
"            font-weight: bold;\n"
"        }\n"
"        .highlight-wasting {\n"
"            color: #3498db; /* Cool blue */\n"
"            font-weight: bold;\n"
"        }\n"
"    </style>\n"
"</head>\n"
"<body>\n"
"    <h1 style=\"color: #8e44ad;\">Diet Recommendations</h1>\n"
"\n"
"    <h3 class=\""
                        "highlight-stunting\">Stunting</h3>\n"
"    <p>\n"
"        To address <span class=\"highlight-stunting\">stunting</span>, focus on nutrient-dense foods that support growth and development:\n"
"    </p>\n"
"    <ul>\n"
"        <li><span style=\"color: #e74c3c;\">Protein-rich foods</span> like eggs, fish, chicken, and legumes.</li>\n"
"        <li>Fruits and vegetables high in <span style=\"color: #9b59b6;\">vitamins and minerals</span>.</li>\n"
"        <li>Whole grains like rice and wheat for <span style=\"color: #f39c12;\">adequate calorie intake</span>.</li>\n"
"        <li>Iron and zinc supplements, as advised by a doctor.</li>\n"
"    </ul>\n"
"\n"
"    <h3 class=\"highlight-overweight\">Overweight</h3>\n"
"    <p>\n"
"        For children at risk of <span class=\"highlight-overweight\">overweight</span> or obesity:\n"
"    </p>\n"
"    <ul>\n"
"        <li>Limit <span style=\"color: #c0392b;\">sugary drinks</span> and processed snacks.</li>\n"
"        <li>Encourage <span style=\"color: #27ae60;\">whole "
                        "fruits</span>, vegetables, and whole grains.</li>\n"
"        <li>Incorporate <span style=\"color: #2980b9;\">lean proteins</span> like fish, beans, and tofu.</li>\n"
"        <li>Promote <span style=\"color: #8e44ad;\">regular physical activity</span> and active play.</li>\n"
"    </ul>\n"
"\n"
"    <h3 class=\"highlight-underweight\">Underweight</h3>\n"
"    <p>\n"
"        For <span class=\"highlight-underweight\">underweight</span> children, prioritize foods that are calorie-dense and nutrient-rich:\n"
"    </p>\n"
"    <ul>\n"
"        <li><span style=\"color: #d35400;\">Frequent meals</span> with nuts, seeds, and dairy products.</li>\n"
"        <li>Energy-dense staples like <span style=\"color: #27ae60;\">potatoes</span>, rice, and bananas.</li>\n"
"        <li>Healthy fats such as <span style=\"color: #f1c40f;\">olive oil</span>, avocado, and peanut butter.</li>\n"
"        <li>Consult a pediatrician for <span style=\"color: #e67e22;\">supplements</span> if necessary.</li>\n"
"    </ul>\n"
"\n"
"    <h"
                        "3 class=\"highlight-wasting\">Wasting</h3>\n"
"    <p>\n"
"        Address <span class=\"highlight-wasting\">wasting</span> with immediate and targeted nutritional interventions:\n"
"    </p>\n"
"    <ul>\n"
"        <li>Therapeutic foods like <span style=\"color: #3498db;\">Ready-to-Use Therapeutic Foods (RUTF)</span>.</li>\n"
"        <li>Meals rich in <span style=\"color: #e74c3c;\">protein</span> and <span style=\"color: #f39c12;\">healthy fats</span>.</li>\n"
"        <li>Small, <span style=\"color: #27ae60;\">frequent meals</span> with fortified foods if possible.</li>\n"
"        <li>Seek <span style=\"color: #9b59b6;\">medical advice</span> to address underlying causes of malnutrition.</li>\n"
"    </ul>\n"
"</body>\n"
"</html>\n"
"", None))
        self.dietBackBtn.setText(QCoreApplication.translate("MalnutritionApp", u"BACK", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MalnutritionApp", u"<html>\n"
"<head>\n"
"    <style>\n"
"        body {\n"
"            font-family: Arial, sans-serif;\n"
"            color: #34495e;\n"
"            margin: 10px;\n"
"        }\n"
"        h1 {\n"
"            color: #2c3e50;\n"
"            text-align: center;\n"
"            margin-bottom: 20px;\n"
"        }\n"
"        table {\n"
"            width: 80%;\n"
"            border-collapse: collapse;\n"
"            margin-top: 10px;\n"
"            word-wrap: break-word;\n"
"            table-layout: fixed;\n"
"        }\n"
"        th, td {\n"
"            text-align: left;\n"
"            padding: 12px;\n"
"            border: 1px solid #bdc3c7;\n"
"        }\n"
"        th {\n"
"            background-color: #3498db;\n"
"            color: white;\n"
"        }\n"
"        td {\n"
"            background-color: #ecf0f1;\n"
"            vertical-align: top;\n"
"        }\n"
"        .highlight {\n"
"            font-weight: bold;\n"
"            color: #2980b9;\n"
"        }\n"
"    </style>\n"
"</head>\n"
""
                        "<body>\n"
"    <h1>Machine Learning Models</h1>\n"
"    <table>\n"
"        <thead>\n"
"            <tr>\n"
"                <th style=\"width: 20%;\">Model</th>\n"
"                <th style=\"width: 30%;\">Description</th>\n"
"                <th style=\"width: 45%;\">Usage</th>\n"
"            </tr>\n"
"        </thead>\n"
"        <tbody>\n"
"            <tr>\n"
"                <td><span class=\"highlight\">Random Forest</span></td>\n"
"                <td>\n"
"                    An ensemble learning method that builds multiple decision trees. <br>\n"
"                    Combines their outputs to improve accuracy and prevent overfitting. <br>\n"
"                    Robust for classification problems and works well on large datasets.\n"
"                </td>\n"
"                <td>\n"
"                    Identifies complex patterns in nutritional indicators. <br>\n"
"                    Helps classify conditions like <em>stunting</em> and <em>underweight</em>.\n"
"                </td>\n"
"          "
                        "  </tr>\n"
"            <tr>\n"
"                <td><span class=\"highlight\">Naive Bayes</span></td>\n"
"                <td>\n"
"                    A probabilistic classifier based on Bayes' theorem. <br>\n"
"                    Assumes predictor independence, making it computationally efficient. <br>\n"
"                    Particularly effective for categorical data.\n"
"                </td>\n"
"                <td>\n"
"                    Quickly predicts conditions like <em>overweight</em> and <em>wasting</em>. <br>\n"
"                    Works well with smaller datasets.\n"
"                </td>\n"
"            </tr>\n"
"            <tr>\n"
"                <td><span class=\"highlight\">K-Nearest Neighbors (KNN)</span></td>\n"
"                <td>\n"
"                    A simple and intuitive algorithm. <br>\n"
"                    Classifies data based on the majority class of its nearest neighbors. <br>\n"
"                    Effective for smaller, structured datasets.\n"
"                </td"
                        ">\n"
"                <td>\n"
"                    Compares patient data with similar cases. <br>\n"
"                    Ensures accurate classification of nutritional statuses.\n"
"                </td>\n"
"            </tr>\n"
"            <tr>\n"
"                <td><span class=\"highlight\">Logistic Regression</span></td>\n"
"                <td>\n"
"                    A statistical model for binary classification problems. <br>\n"
"                    Predicts probabilities and is effective for linear relationships. <br>\n"
"                    Works well for datasets with direct feature relationships.\n"
"                </td>\n"
"                <td>\n"
"                    Predicts malnutrition indicators like <em>underweight</em>. <br>\n"
"                    Analyzes features such as weight, height, and age for accuracy.\n"
"                </td>\n"
"            </tr>\n"
"            <tr>\n"
"                <td><span class=\"highlight\">Neural Networks</span></td>\n"
"                <td>\n"
"   "
                        "                 A model inspired by the structure of the human brain. <br>\n"
"                    Consists of layers of interconnected nodes that process data. <br>\n"
"                    Extremely powerful for identifying complex, nonlinear relationships.\n"
"                </td>\n"
"                <td>\n"
"                    Detects subtle patterns in nutritional data. <br>\n"
"                    Useful for advanced classifications like combined malnutrition\n"
"	<br> conditions.\n"
"                </td>\n"
"            </tr>\n"
"            <tr>\n"
"                <td><span class=\"highlight\">Linear Regression</span></td>\n"
"                <td>\n"
"                    A statistical model for predicting a continuous output variable. <br>\n"
"                    Assumes a linear relationship between input features and the target variable. <br>\n"
"                    Simple and interpretable for straightforward problems.\n"
"                </td>\n"
"                <td>\n"
"                    Es"
                        "timates trends in nutritional data over time. <br>\n"
"                    Assesses growth and weight trends relative to age and height.\n"
"                </td>\n"
"            </tr>\n"
"        </tbody>\n"
"    </table>\n"
"</body>\n"
"</html>\n"
"", None))
        self.ModelBackBtn.setText(QCoreApplication.translate("MalnutritionApp", u"BACK", None))
        self.RegisterBackBtn.setText(QCoreApplication.translate("MalnutritionApp", u"BACK", None))
        self.label_17.setText(QCoreApplication.translate("MalnutritionApp", u"USER REGISTRATION:", None))
        self.label_18.setText(QCoreApplication.translate("MalnutritionApp", u"Full Name: ", None))
        self.label_22.setText(QCoreApplication.translate("MalnutritionApp", u"Title: ", None))
        self.label_21.setText(QCoreApplication.translate("MalnutritionApp", u"Phone Number: ", None))
        self.label_20.setText(QCoreApplication.translate("MalnutritionApp", u"Email ID: ", None))
        self.label_25.setText(QCoreApplication.translate("MalnutritionApp", u"User Name: ", None))
        self.label_19.setText(QCoreApplication.translate("MalnutritionApp", u"Password: ", None))
        self.label_23.setText(QCoreApplication.translate("MalnutritionApp", u"Full Name: ", None))
        self.ModelBackBtn_3.setText(QCoreApplication.translate("MalnutritionApp", u"REGISTER", None))
        self.ERRORLABEL.setText("")
        self.label_27.setText("")
        self.aboutbackBtn.setText(QCoreApplication.translate("MalnutritionApp", u"BACK", None))
        self.label_26.setText(QCoreApplication.translate("MalnutritionApp", u"Combating Malnutrition in Children with Machine Learning\n"
"\n"
"At SDM Institute of Technology, Ujire, we are committed to addressing malnutrition in children \n"
"through the transformative power of Machine Learning (ML). By combining advanced technology \n"
"with a deep understanding of public health, we aim to create effective solutions that ensure \n"
"every child has access to adequate nutrition and the opportunity to thrive.\n"
"\n"
"Who We Are\n"
"We are a multidisciplinary team of data scientists, healthcare professionals, nutritionists, \n"
"and social impact advocates working together to fight childmalnutrition. Our approach combines \n"
"cutting-edge ML algorithms, community engagement, and strategic partnerships to make a lasting \n"
"difference in children's lives.\n"
"\n"
"What We Do\n"
"Our solutions focus on:\n"
"\n"
"Identifying at-risk children using predictive models based on health, environmental, and \n"
"socio-economic data.\n"
"\n"
"Providing personalized nutritional plans for children"
                        " based on their unique needs.\n"
"\n"
"Supporting healthcare providers and NGOs with actionable insights forresource allocation and impact measurement.\n"
"\n"
"Monitoring progress and outcomes through real-time analytics to ensure sustainable improvements.\n"
"\n"
"Our Vision\n"
"A world free from child malnutrition. Through innovation and collaboration, we aim to empower families, communities, \n"
"and organizations with the tools and knowledge to eradicate malnutrition and improve quality of life for children everywhere.\n"
"\n"
"Contact Us\n"
"We'd love to hear from you and collaborate to make a difference. Reach out to us:\n"
"\n"
"Email: info@nutriaicare.org\n"
"Phone: 080-812856\n"
"Address: SDM Institute of Technology, Ujire\n"
"Website: www.nutriaisolutions.org\n"
"\n"
"Join us in our mission to use Machine", None))
        self.label_31.setText(QCoreApplication.translate("MalnutritionApp", u"ABOUT US:", None))
        self.label_24.setText("")
        self.label_29.setText(QCoreApplication.translate("MalnutritionApp", u"Data Analysis", None))
        self.graphbackbtn.setText(QCoreApplication.translate("MalnutritionApp", u"BACK", None))
    # retranslateUi

