# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 630)
        MainWindow.setMinimumSize(QSize(1000, 630))
        MainWindow.setMaximumSize(QSize(1000, 630))
        icon = QIcon()
        icon.addFile(u"img/win.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton { \n"
"     border: 10px solid #000000;\n"
"     border-radius: 20px;}\n"
"QPushButton:hover { background-color: white;\n"
"	border: 10px solid rgb(127, 253, 49);\n"
"	/*border: 10px solid #ae1e00; */}\n"
"QPushButton:pressed{\n"
"	/*border: 10px solid rgb(127, 253, 49);*/\n"
"	\n"
"	border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 150, 300, 300))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(300, 300))
        self.label.setMaximumSize(QSize(300, 300))
        self.label.setStyleSheet(u"font: 10pt \"WarCraft\";")
        self.label.setPixmap(QPixmap(u"img/4.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.but_curse = QPushButton(self.centralwidget)
        self.but_curse.setObjectName(u"but_curse")
        self.but_curse.setGeometry(QRect(247, 505, 70, 70))
        self.but_curse.setMinimumSize(QSize(70, 70))
        self.but_curse.setMaximumSize(QSize(70, 70))
        self.but_curse.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_curse.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon1 = QIcon()
        icon1.addFile(u"img/curse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_curse.setIcon(icon1)
        self.but_curse.setIconSize(QSize(60, 60))
        self.but_light = QPushButton(self.centralwidget)
        self.but_light.setObjectName(u"but_light")
        self.but_light.setGeometry(QRect(382, 88, 70, 70))
        self.but_light.setMinimumSize(QSize(70, 70))
        self.but_light.setMaximumSize(QSize(70, 70))
        self.but_light.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_light.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon2 = QIcon()
        icon2.addFile(u"img/light.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_light.setIcon(icon2)
        self.but_light.setIconSize(QSize(60, 60))
        self.but_light.setCheckable(True)
        self.but_light.setChecked(False)
        self.but_light.setAutoDefault(False)
        self.but_light.setFlat(False)
        self.but_dragon = QPushButton(self.centralwidget)
        self.but_dragon.setObjectName(u"but_dragon")
        self.but_dragon.setGeometry(QRect(477, 250, 70, 70))
        self.but_dragon.setMinimumSize(QSize(70, 70))
        self.but_dragon.setMaximumSize(QSize(70, 70))
        self.but_dragon.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_dragon.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon3 = QIcon()
        icon3.addFile(u"img/dragon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_dragon.setIcon(icon3)
        self.but_dragon.setIconSize(QSize(60, 60))
        self.but_dragon.setCheckable(True)
        self.but_dragon.setChecked(False)
        self.but_dragon.setAutoDefault(False)
        self.but_dragon.setFlat(False)
        self.but_snake = QPushButton(self.centralwidget)
        self.but_snake.setObjectName(u"but_snake")
        self.but_snake.setGeometry(QRect(12, 250, 70, 70))
        self.but_snake.setMinimumSize(QSize(70, 70))
        self.but_snake.setMaximumSize(QSize(70, 70))
        self.but_snake.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_snake.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon4 = QIcon()
        icon4.addFile(u"img/snake.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_snake.setIcon(icon4)
        self.but_snake.setIconSize(QSize(60, 60))
        self.but_tree = QPushButton(self.centralwidget)
        self.but_tree.setObjectName(u"but_tree")
        self.but_tree.setGeometry(QRect(67, 430, 70, 70))
        self.but_tree.setMinimumSize(QSize(70, 70))
        self.but_tree.setMaximumSize(QSize(70, 70))
        self.but_tree.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_tree.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon5 = QIcon()
        icon5.addFile(u"img/tree.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_tree.setIcon(icon5)
        self.but_tree.setIconSize(QSize(60, 60))
        self.but_rock = QPushButton(self.centralwidget)
        self.but_rock.setObjectName(u"but_rock")
        self.but_rock.setGeometry(QRect(197, 50, 70, 70))
        self.but_rock.setMinimumSize(QSize(70, 70))
        self.but_rock.setMaximumSize(QSize(70, 70))
        self.but_rock.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_rock.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon6 = QIcon()
        icon6.addFile(u"img/rock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_rock.setIcon(icon6)
        self.but_rock.setIconSize(QSize(60, 60))
        self.but_water = QPushButton(self.centralwidget)
        self.but_water.setObjectName(u"but_water")
        self.but_water.setGeometry(QRect(467, 345, 70, 70))
        self.but_water.setMinimumSize(QSize(70, 70))
        self.but_water.setMaximumSize(QSize(70, 70))
        self.but_water.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_water.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon7 = QIcon()
        icon7.addFile(u"img/water.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_water.setIcon(icon7)
        self.but_water.setIconSize(QSize(60, 60))
        self.but_dagger = QPushButton(self.centralwidget)
        self.but_dagger.setObjectName(u"but_dagger")
        self.but_dagger.setGeometry(QRect(37, 160, 70, 70))
        self.but_dagger.setMinimumSize(QSize(70, 70))
        self.but_dagger.setMaximumSize(QSize(70, 70))
        self.but_dagger.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_dagger.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon8 = QIcon()
        icon8.addFile(u"img/knife.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_dagger.setIcon(icon8)
        self.but_dagger.setIconSize(QSize(60, 60))
        self.but_fire = QPushButton(self.centralwidget)
        self.but_fire.setObjectName(u"but_fire")
        self.but_fire.setGeometry(QRect(107, 90, 70, 70))
        self.but_fire.setMinimumSize(QSize(70, 70))
        self.but_fire.setMaximumSize(QSize(70, 70))
        self.but_fire.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_fire.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon9 = QIcon()
        icon9.addFile(u"img/fire.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_fire.setIcon(icon9)
        self.but_fire.setIconSize(QSize(60, 60))
        self.but_gun = QPushButton(self.centralwidget)
        self.but_gun.setObjectName(u"but_gun")
        self.but_gun.setGeometry(QRect(292, 50, 70, 70))
        self.but_gun.setMinimumSize(QSize(70, 70))
        self.but_gun.setMaximumSize(QSize(70, 70))
        self.but_gun.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_gun.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon10 = QIcon()
        icon10.addFile(u"img/gun.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_gun.setIcon(icon10)
        self.but_gun.setIconSize(QSize(60, 60))
        self.but_paper = QPushButton(self.centralwidget)
        self.but_paper.setObjectName(u"but_paper")
        self.but_paper.setGeometry(QRect(340, 485, 70, 70))
        self.but_paper.setMinimumSize(QSize(70, 70))
        self.but_paper.setMaximumSize(QSize(70, 70))
        self.but_paper.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_paper.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon11 = QIcon()
        icon11.addFile(u"img/paper.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_paper.setIcon(icon11)
        self.but_paper.setIconSize(QSize(60, 60))
        self.but_human = QPushButton(self.centralwidget)
        self.but_human.setObjectName(u"but_human")
        self.but_human.setGeometry(QRect(22, 345, 70, 70))
        self.but_human.setMinimumSize(QSize(70, 70))
        self.but_human.setMaximumSize(QSize(70, 70))
        self.but_human.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_human.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon12 = QIcon()
        icon12.addFile(u"img/human.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_human.setIcon(icon12)
        self.but_human.setIconSize(QSize(60, 60))
        self.label_background = QLabel(self.centralwidget)
        self.label_background.setObjectName(u"label_background")
        self.label_background.setGeometry(QRect(0, 0, 1000, 630))
        self.label_background.setStyleSheet(u"color: rgb(0, 255, 0);")
        self.label_background.setPixmap(QPixmap(u"img/background1.jpg"))
        self.label_background.setScaledContents(True)
        self.list_user = QLabel(self.centralwidget)
        self.list_user.setObjectName(u"list_user")
        self.list_user.setGeometry(QRect(680, 100, 130, 500))
        self.list_user.setMinimumSize(QSize(130, 500))
        self.list_user.setMaximumSize(QSize(130, 500))
        font = QFont()
        font.setFamily(u"WarCraft")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.list_user.setFont(font)
        self.list_user.setStyleSheet(u"color: rgb(0, 255, 0);")
        self.list_user.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.list_enemy = QLabel(self.centralwidget)
        self.list_enemy.setObjectName(u"list_enemy")
        self.list_enemy.setGeometry(QRect(820, 100, 130, 500))
        self.list_enemy.setMinimumSize(QSize(130, 500))
        self.list_enemy.setMaximumSize(QSize(120, 480))
        self.list_enemy.setFont(font)
        self.list_enemy.setStyleSheet(u"color: rgb(0, 255, 0);")
        self.list_enemy.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.but_wolf = QPushButton(self.centralwidget)
        self.but_wolf.setObjectName(u"but_wolf")
        self.but_wolf.setGeometry(QRect(150, 485, 70, 70))
        self.but_wolf.setMinimumSize(QSize(70, 70))
        self.but_wolf.setMaximumSize(QSize(70, 70))
        self.but_wolf.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_wolf.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon13 = QIcon()
        icon13.addFile(u"img/wolf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_wolf.setIcon(icon13)
        self.but_wolf.setIconSize(QSize(60, 60))
        self.but_air = QPushButton(self.centralwidget)
        self.but_air.setObjectName(u"but_air")
        self.but_air.setGeometry(QRect(417, 430, 70, 70))
        self.but_air.setMinimumSize(QSize(70, 70))
        self.but_air.setMaximumSize(QSize(70, 70))
        self.but_air.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_air.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon14 = QIcon()
        icon14.addFile(u"img/air.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_air.setIcon(icon14)
        self.but_air.setIconSize(QSize(60, 60))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(691, 0, 249, 89))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 40))
        self.label_2.setMaximumSize(QSize(120, 40))
        font1 = QFont()
        font1.setFamily(u"WarCraft")
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(0, 255, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 40))
        self.label_3.setMaximumSize(QSize(120, 40))
        font2 = QFont()
        font2.setFamily(u"WarCraft")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(0, 255, 0);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.lcdNumber = QLCDNumber(self.layoutWidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(120, 40))
        self.lcdNumber.setMaximumSize(QSize(120, 40))
        self.lcdNumber.setStyleSheet(u"QLCDNumber{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(112, 255, 110);\n"
"}")
        self.lcdNumber.setFrameShape(QFrame.Box)
        self.lcdNumber.setFrameShadow(QFrame.Plain)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setMode(QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lcdNumber)

        self.lcdNumber_2 = QLCDNumber(self.layoutWidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setMinimumSize(QSize(120, 40))
        self.lcdNumber_2.setMaximumSize(QSize(120, 40))
        self.lcdNumber_2.setStyleSheet(u"QLCDNumber{\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: rgb(112, 255, 110);\n"
"}")
        self.lcdNumber_2.setFrameShape(QFrame.Box)
        self.lcdNumber_2.setFrameShadow(QFrame.Plain)
        self.lcdNumber_2.setLineWidth(1)
        self.lcdNumber_2.setMidLineWidth(0)
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setDigitCount(5)
        self.lcdNumber_2.setMode(QLCDNumber.Dec)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Flat)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lcdNumber_2)

        self.but_devil = QPushButton(self.centralwidget)
        self.but_devil.setObjectName(u"but_devil")
        self.but_devil.setGeometry(QRect(447, 160, 70, 70))
        self.but_devil.setMinimumSize(QSize(70, 70))
        self.but_devil.setMaximumSize(QSize(70, 70))
        self.but_devil.setCursor(QCursor(Qt.PointingHandCursor))
        self.but_devil.setStyleSheet(u"font: 10pt \"WarCraft\";")
        icon15 = QIcon()
        icon15.addFile(u"img/devil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_devil.setIcon(icon15)
        self.but_devil.setIconSize(QSize(60, 60))
        self.but_devil.setCheckable(True)
        self.but_devil.setChecked(False)
        self.but_devil.setAutoDefault(False)
        self.but_devil.setFlat(False)
        self.label_event = QLabel(self.centralwidget)
        self.label_event.setObjectName(u"label_event")
        self.label_event.setGeometry(QRect(130, 260, 300, 80))
        font3 = QFont()
        font3.setFamily(u"WarCraft")
        font3.setPointSize(15)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_event.setFont(font3)
        self.label_event.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"font: 15pt \"WarCraft\";")
        self.label_event.setLineWidth(1)
        self.label_event.setAlignment(Qt.AlignCenter)
        self.label_event.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_background.raise_()
        self.layoutWidget.raise_()
        self.label.raise_()
        self.but_gun.raise_()
        self.but_fire.raise_()
        self.but_dagger.raise_()
        self.but_water.raise_()
        self.but_rock.raise_()
        self.but_tree.raise_()
        self.but_curse.raise_()
        self.but_light.raise_()
        self.but_dragon.raise_()
        self.but_paper.raise_()
        self.but_human.raise_()
        self.list_user.raise_()
        self.list_enemy.raise_()
        self.but_wolf.raise_()
        self.but_air.raise_()
        self.but_devil.raise_()
        self.but_snake.raise_()
        self.label_event.raise_()

        self.retranslateUi(MainWindow)

        self.but_light.setDefault(False)
        self.but_dragon.setDefault(False)
        self.but_devil.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.but_curse.setToolTip(QCoreApplication.translate("MainWindow", u"Curse", None))
#endif // QT_CONFIG(tooltip)
        self.but_curse.setText("")
#if QT_CONFIG(tooltip)
        self.but_light.setToolTip(QCoreApplication.translate("MainWindow", u"Light", None))
#endif // QT_CONFIG(tooltip)
        self.but_light.setText("")
#if QT_CONFIG(tooltip)
        self.but_dragon.setToolTip(QCoreApplication.translate("MainWindow", u"Dragon", None))
#endif // QT_CONFIG(tooltip)
        self.but_dragon.setText("")
#if QT_CONFIG(tooltip)
        self.but_snake.setToolTip(QCoreApplication.translate("MainWindow", u"Snake", None))
#endif // QT_CONFIG(tooltip)
        self.but_snake.setText("")
#if QT_CONFIG(tooltip)
        self.but_tree.setToolTip(QCoreApplication.translate("MainWindow", u"Tree", None))
#endif // QT_CONFIG(tooltip)
        self.but_tree.setText("")
#if QT_CONFIG(tooltip)
        self.but_rock.setToolTip(QCoreApplication.translate("MainWindow", u"Rock", None))
#endif // QT_CONFIG(tooltip)
        self.but_rock.setText("")
#if QT_CONFIG(tooltip)
        self.but_water.setToolTip(QCoreApplication.translate("MainWindow", u"Water", None))
#endif // QT_CONFIG(tooltip)
        self.but_water.setText("")
#if QT_CONFIG(tooltip)
        self.but_dagger.setToolTip(QCoreApplication.translate("MainWindow", u"Dagger", None))
#endif // QT_CONFIG(tooltip)
        self.but_dagger.setText("")
#if QT_CONFIG(tooltip)
        self.but_fire.setToolTip(QCoreApplication.translate("MainWindow", u"Fire", None))
#endif // QT_CONFIG(tooltip)
        self.but_fire.setText("")
#if QT_CONFIG(tooltip)
        self.but_gun.setToolTip(QCoreApplication.translate("MainWindow", u"Gun", None))
#endif // QT_CONFIG(tooltip)
        self.but_gun.setText("")
#if QT_CONFIG(tooltip)
        self.but_paper.setToolTip(QCoreApplication.translate("MainWindow", u"Paper", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.but_paper.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.but_paper.setText("")
#if QT_CONFIG(tooltip)
        self.but_human.setToolTip(QCoreApplication.translate("MainWindow", u"Human", None))
#endif // QT_CONFIG(tooltip)
        self.but_human.setText("")
        self.label_background.setText("")
        self.list_user.setText("")
        self.list_enemy.setText("")
#if QT_CONFIG(tooltip)
        self.but_wolf.setToolTip(QCoreApplication.translate("MainWindow", u"Wolf", None))
#endif // QT_CONFIG(tooltip)
        self.but_wolf.setText("")
#if QT_CONFIG(tooltip)
        self.but_air.setToolTip(QCoreApplication.translate("MainWindow", u"Air", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.but_air.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.but_air.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"You", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enemy", None))
#if QT_CONFIG(tooltip)
        self.but_devil.setToolTip(QCoreApplication.translate("MainWindow", u"Devil", None))
#endif // QT_CONFIG(tooltip)
        self.but_devil.setText("")
        self.label_event.setText("")
    # retranslateUi

