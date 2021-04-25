# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys

from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMainWindow, QMessageBox, QGraphicsDropShadowEffect
from PySide2.QtGui import QColor

from ui import Ui_MainWindow
from splashscreen import Ui_SplashScreen
from end import Ui_End_Form

from widgets import CircularProgress
from widgets import CircularProgress2


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_btn()
        self.setWindowTitle('Rock Scissors Paper - WoW')
        self.user_points = 0
        self.ai_points = 0
        self.end = End()

        # IMPORT CIRCULAR PROGRESS
        self.progress = CircularProgress()
        self.progress.move(130, 150)  # двигает self.progress = CircularProgress() по экрану
        self.progress.setParent(self.centralwidget)
        self.counter_circle = 0

        # IMPORT CIRCULAR PROGRESS 2
        self.progress2 = CircularProgress2()
        self.progress2.move(128, 148)
        self.progress2.setParent(self.centralwidget)
        # self.counter_circle = 0

        # Q TIMER
        self.timer_circle = QtCore.QTimer()
        self.timer_circle.start(50)
        self.timer_circle.timeout.connect(self.update)

        self.buttons = {'rock': self.but_rock, 'fire': self.but_fire, 'dagger': self.but_dagger, 'tree': self.but_tree,
                        'snake': self.but_snake, 'human': self.but_human, 'light': self.but_light, 'gun': self.but_gun,
                        'wolf': self.but_wolf, 'curse': self.but_curse, 'paper': self.but_paper, 'air': self.but_air,
                        'water': self.but_water, 'dragon': self.but_dragon, 'devil': self.but_devil}

    # UPDATE PROGRESS CIRCLE BAR
    def update(self):
        self.progress.set_value(self.counter_circle)
        if self.counter_circle == 200:
            self.counter_circle = 0
            self.label.setPixmap(random.choice(img))
        self.counter_circle += 1

        self.progress2.set_value(self.counter_circle)
        if self.counter_circle == 200:
            self.counter_circle = 0
            self.label.setPixmap(random.choice(img))
        self.counter_circle += 1

    def set_btn(self):
        self.but_rock.clicked.connect(lambda: self.click('rock'))
        self.but_fire.clicked.connect(lambda: self.click('fire'))
        self.but_dagger.clicked.connect(lambda: self.click('dagger'))
        self.but_snake.clicked.connect(lambda: self.click('snake'))
        self.but_human.clicked.connect(lambda: self.click('human'))
        self.but_tree.clicked.connect(lambda: self.click('tree'))
        self.but_wolf.clicked.connect(lambda: self.click('wolf'))
        self.but_curse.clicked.connect(lambda: self.click('curse'))
        self.but_paper.clicked.connect(lambda: self.click('paper'))
        self.but_air.clicked.connect(lambda: self.click('air'))
        self.but_water.clicked.connect(lambda: self.click('water'))
        self.but_dragon.clicked.connect(lambda: self.click('dragon'))
        self.but_devil.clicked.connect(lambda: self.click('devil'))
        self.but_light.clicked.connect(lambda: self.click('light'))
        self.but_gun.clicked.connect(lambda: self.click('gun'))

        self.label.setPixmap(random.choice(img))
        self.label_background.setPixmap((random.choice(background)))

    def click(self, user_choice):
        ai = random.choice([i for i in win.keys()])  # компьютер выбирает кнопку
        QtCore.QTimer.singleShot(0, lambda: self.buttons[ai].setStyleSheet(
            'QPushButton {border: 10px solid #ae1e00;}'))  # подсветка кнопки компьютера
        QtCore.QTimer.singleShot(2000, lambda: self.buttons[ai].setStyleSheet(''))  # возврат цвета кнопки на прежний
        if user_choice == ai:
            self.ai_points += 50
            self.user_points += 50
            self.text_event(f'Draw - {ai}')
        elif ai in win[user_choice]:
            self.user_points += 100
            self.text_event(f'''Well done
Enemy chose {ai} and failed''')
        else:
            self.ai_points += 100
            self.text_event(f'''Fail
Enemy chose {ai}''')

        self.lcdNumber.display(self.user_points)
        self.lcdNumber_2.display(self.ai_points)

        text_on_List_user = self.list_user.text()
        text_on_List_enemy = self.list_enemy.text()
        self.list_user.setText(text_on_List_user + '\n' + user_choice)
        self.list_enemy.setText(text_on_List_enemy + '\n' + ai)

        if self.user_points >= 1000:
            text = 'Congratulations! You are a winner!                                               '
            ico = 'img//win.png'
            self.message_box(text, ico)
        elif self.ai_points >= 1000:
            text = 'You lose!                                                                        '
            ico = 'img//lose.png'
            self.message_box(text, ico)

    def text_event(self, text):
        self.label_event.setText(text)
        # QtCore.QTimer.singleShot(0, lambda: self.label_event.setText(text))
        # QtCore.QTimer.singleShot(3500, lambda: self.label_event.clear())

    def message_box(self, text, ico):  # функция выводит окно с сообщением
        message = QMessageBox()

        # message.setWindowTitle('End of the game')
        message.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        message.setStyleSheet('QMessageBox {background-color: rgb(66, 66, 66); font-size:15pt; } '
                              'QWidget {color: rgb(127, 253, 49); } '
                              'QMessageBox QPushButton {width: 150; height: 30; '
                              'font-size:10pt; '
                              'font-weight: bold;'
                              'color: rgb(127, 253, 49); '
                              'background-color: qlineargradient(spread:pad, x1:0.537, y1:0.987636, x2:0.532, '
                              'y2:0.0507273, stop:0 rgba(25, 59, 103, 255), stop:0.989691 rgba(140, 188, 219, 255)); '
                              'border: 6px solid rgb(127, 253, 49); border-radius: 15px;}'

                              'QPushButton:hover {border: 6px solid rgb(127, 253, 49); '
                              'background-color: qlineargradient(spread:pad, x1:0.537, y1:1, x2:0.561851, '
                              'y2:0, stop:0 rgba(25, 39, 103, 255), stop:1 rgba(140, 188, 219, 255));} '

                              'QPushButton:pressed {border: 6px solid rgb(127, 253, 49); '
                              'background-color: qlineargradient(spread:pad, x1:0.537, y1:1, x2:0.561851, '
                              'y2:0, stop:0 rgba(25, 149, 103, 255), stop:1 rgba(140, 188, 219, 255));}')
        message.setText(text)
        message.setIconPixmap(ico)

        message.addButton('Play again', QMessageBox.YesRole)
        message.addButton('Exit', QMessageBox.NoRole)
        message.buttonClicked.connect(self.popup_action)  # метод, который обрабатывает нажатие
        # на кнопку в окне MessageBox
        message.show()
        message.exec_()

    def popup_action(self, btn):
        if btn.text() == 'Play again':
            self.user_points = 0
            self.ai_points = 0
            self.label.setPixmap(random.choice(img))
            self.label_background.setPixmap(random.choice(background))
            self.lcdNumber.display(0)
            self.lcdNumber_2.display(0)
            self.label_event.clear()
            self.list_user.clear()
            self.list_enemy.clear()
        elif btn.text() == 'Exit':
            self.end.show()
            self.close()
            QtCore.QTimer.singleShot(1500, QtCore.QCoreApplication.quit)


class SplashScreen(QMainWindow, Ui_SplashScreen):
    def __init__(self):
        super().__init__()
        self.main = MyApp()
        self.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        # Q TIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(20)  # время в мс за которе меняется счетчик counter в progress

        # CHANGE DESCRIPTION
        QtCore.QTimer.singleShot(0, lambda: self.label_description.setText('<strong>LOADING</strong> DATABASE'))
        QtCore.QTimer.singleShot(2000, lambda: self.label_description.setText('<strong>LOADING</strong> '
                                                                              'USER INTERFACE'))
        self.show()

    def progress(self):
        global counter
        # SET VALUE TO progressBar
        self.progressBar.setValue(counter)
        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP Timer
            self.timer.stop()
            # SHOW MAIN WINDOW
            self.main.show()  # показывает окно приложения

            # CLOSE SPLASH SCREEN
            self.close()
        # INCREASE COUNTER
        counter += 1


class End(QMainWindow, Ui_End_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setText('<strong>THANKS</strong> FOR THE GAME')
        self.setStyleSheet('background-color: rgb(66, 66, 66); color: rgb(127, 253, 49); border-radius: 10px')


counter = 0  # счетчик для splash screen
# counter_circle = 0  # счетчик для сругов

img = ('img//1.png', 'img//2.png', 'img//3.png', 'img//4.png')
background = ('img//background1.jpg', 'img//background2.jpeg', 'img//background3.jpg',
              'img//background4.jpg', 'img//background5.jpg')

win = {'rock': ['fire', 'dagger', 'snake', 'human', 'tree', 'wolf', 'curse'],
       'fire': ['dagger', 'snake', 'human', 'tree', 'wolf', 'curse', 'paper'],
       'dagger': ['snake', 'human', 'tree', 'wolf', 'curse', 'paper', 'air'],
       'snake': ['human', 'tree', 'wolf', 'curse', 'paper', 'air', 'water'],
       'human': ['tree', 'wolf', 'curse', 'paper', 'air', 'water', 'dragon'],
       'tree': ['wolf', 'curse', 'paper', 'air', 'water', 'dragon', 'devil'],
       'wolf': ['curse', 'paper', 'air', 'water', 'dragon', 'devil', 'light'],
       'curse': ['paper', 'air', 'water', 'dragon', 'devil', 'light', 'gun'],
       'paper': ['air', 'water', 'dragon', 'devil', 'light', 'gun', 'rock'],
       'air': ['water', 'dragon', 'devil', 'light', 'gun', 'rock', 'fire'],
       'water': ['dragon', 'devil', 'light', 'gun', 'rock', 'fire', 'dagger'],
       'dragon': ['devil', 'light', 'gun', 'rock', 'fire', 'dagger', 'snake'],
       'devil': ['light', 'gun', 'rock', 'fire', 'dagger', 'snake', 'human'],
       'light': ['gun', 'rock', 'fire', 'dagger', 'snake', 'human', 'tree'],
       'gun': ['rock', 'fire', 'dagger', 'snake', 'human', 'tree', 'wolf']}

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # новый экземпляр QApplication
    # example = MyApp()  # создание объекта класса MyApp
    example = SplashScreen()
    # example.show()
    sys.exit(app.exec_())
