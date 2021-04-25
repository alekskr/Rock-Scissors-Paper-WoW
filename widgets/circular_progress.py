from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtGui import QColor, QFont, QPainter


class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # CUSTOM PROPERTIES
        self.value = 0
        self.width = 300
        self.height = 300
        self.progress_width = 3
        self.add_shadow(True)
        # self.progress_rounded_cap = True
        # self.progress_color = 0x265f8b
        # self.progress_color = 0xff79c6
        self.progress_color = 0x7ffd31
        self.max_value = 100
        self.font_family = 'Segoe UI'
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0xff79c6

        # BG
        self.enable_bg = False
        self.bg_color = 0x44475a
        # SET DEFAULT SIZE WINDOW LAYOUT
        self.resize(self.width, self.height)

    # ADD DROP SHADOW
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 120))
            self.setGraphicsEffect(self.shadow)

    # SET VALUE
    def set_value(self, value):
        self.value = value
        self.repaint()  # Render progress bar after change value

    # PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)
    def paintEvent(self, event):
        # SET PROGRESS PARAMETERS
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = int(self.progress_width / 2)
        value = int(self.value * 360 / self.max_value)

        # PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)  # remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))

        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # ENABLE BG
        if self.enable_bg:
            pen = QPen()
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)
            pen.setCapStyle(Qt.RoundCap)

            paint.drawArc(margin, margin, width, height, 0, 360 * 16)

        # CREATE ARC CIRCULAR PROGRESS
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        pen.setCapStyle(Qt.RoundCap)

        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, 90 * 16, -value * 4)
        paint.drawArc(margin, margin, width, height, 90 * 16, value * 4)
        # paint.drawArc(margin, margin, width, height, 0 * 16, -value * 4)
        # paint.drawArc(margin, margin, width, height, 180 * 16, -value * 4)
        # paint.drawArc(margin, margin, width, height, -value * 16, 180 * 2)
        # paint.drawArc(margin, margin, width, height, value * 16, 180 * 2)

        paint.end()
