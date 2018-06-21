import re
import sys
from shutil import copyfile

from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QGraphicsScene

import steglsb
from GUI.decode import Ui_dialog as Decode_dialog
from GUI.encode import Ui_dialog as Encode_dialog
from GUI.lsb import Ui_MainWindow


class LSBGUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.encode_image_btn.clicked.connect(self.encode)
        self.decode_im_btn.clicked.connect(self.decode)

    def encode(self):
        self.encode_gui = EncodeGUI()
        self.encode_gui.show()

    def decode(self):
        self.decode_gui = DecodeGUI()
        self.decode_gui.show()


class MainGUI(QWidget):
    FILTER = "PNG image (*.png);; JPEG image(*.jpg);; All files (*)"

    def __init__(self):
        super().__init__()

    def _parse_mime(self, string):
        reg = re.search(r"(?<=\.)\w+", string)
        if reg:
            return reg.group()

    def _get_filename(self, name):
        mime = self._parse_mime(name)
        if not self.mime:
            return name
        else:
            if mime:
                name = name.strip("." + mime)
            return "{}.{}".format(name, self.mime)

    def exit(self):
        self.hide()


class EncodeGUI(MainGUI, Encode_dialog):
    TEMP = "tempe"

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cover_img_btn.clicked.connect(self.get_cover)
        self.secret_img_btn.clicked.connect(self.get_secret)
        self.encode_save_btn.clicked.connect(self.save_image)
        self.encode_cancel_btn.clicked.connect(self.exit)
        self.encode_slider.valueChanged.connect(self.slide_bits)
        self.cover = self.secret = self.mime = None

    def _get_image(self, header="Select file"):
        return tuple(QFileDialog.getOpenFileName(self, header, QDir.homePath(), self.FILTER))

    def _show_image(self, image, bits):
        steglsb.LSBEncode(self.cover, self.secret, bits, self._get_filename(image))
        view = QGraphicsScene()
        pix = QPixmap(image)
        view.addPixmap(pix)
        self.encode_graphic.setScene(view)

    def get_cover(self):
        self.cover, file_mime = self._get_image("Select cover image")
        if self.cover:
            self.mime = self._parse_mime(file_mime)
        self.slide_bits()

    def get_secret(self):
        self.secret, _ = self._get_image("Select secret image")
        self.slide_bits()

    def slide_bits(self):
        bits = self.encode_slider.value()
        if self.secret and self.cover:
            self._show_image(self._get_filename(self.TEMP), bits)

    def save_image(self):
        if self.cover and self.secret:
            file_path = QFileDialog.getSaveFileName(self, 'Select save location', QDir.currentPath())[0]
            if file_path:
                copyfile(self._get_filename(self.TEMP), file_path)


class DecodeGUI(MainGUI, Decode_dialog):
    TEMP = "tempd"

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.decode_save_btn.clicked.connect(self.save_image)
        self.decode_cancel_btn.clicked.connect(self.exit)
        self.decode_file_btn.clicked.connect(self.get_image)
        self.decode_slider.valueChanged.connect(self.slide_bits)
        self.file = self.mime = None

    def _show_image(self, image, bits):
        steglsb.LSBDecode(self.file, bits, image)
        view = QGraphicsScene()
        pix = QPixmap(image)
        view.addPixmap(pix)
        self.decode_graphic.setScene(view)

    def slide_bits(self):
        bits = self.decode_slider.value()
        if self.file:
            self._show_image(self._get_filename(self.TEMP), bits)

    def get_image(self):
        self.file, file_mime = tuple(
            QFileDialog.getOpenFileName(self, 'Select file', QDir.homePath(), self.FILTER))
        if self.file:
            self.mime = self._parse_mime(file_mime)
            self.slide_bits()

    def save_image(self):
        if self.file:
            file_path = QFileDialog.getSaveFileName(self, 'Select save location', QDir.currentPath())[0]
            if file_path:
                copyfile(self._get_filename(self.TEMP), file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LSBGUI()
    window.show()
    sys.exit(app.exec_())
