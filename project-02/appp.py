# import modules

from PyQt5.QtWidgets import (
QApplication,
QWidget,
QLabel,
QPushButton,
QHBoxLayout,
QVBoxLayout,
QComboBox,
QListWidget,
)

# app settings

app = QApplication([])

main_window = QWidget()

main_window.setWindowTitle("Photo Qt")
main_window.resize(500, 400)


# all app objects

btn_folder = QPushButton("Folder")
file_list = QListWidget()

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")

mirror = QPushButton("Mirror")
sharpness = QPushButton("Sharpness")

gray = QPushButton("A/B")
saturation = QPushButton("Color")
contrast = QPushButton("Contrast")
blur = QPushButton("Blur")


# dropdown box

filter_box = QComboBox()

filter_box.addItem("Original")
filter_box.addItem("Left")
filter_box.addItem("Right")
filter_box.addItem("Mirror")
filter_box.addItem("Sharpen")
filter_box.addItem("A/B")
filter_box.addItem("Color")
filter_box.addItem("Contrast")
filter_box.addItem("Blur")

picture_box = QLabel("Image will appear here!")


# app design

master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()


col2.addWidget(picture_box)
col2.addWidget(filter_box)
col2.addWidget(btn_left)
col2.addWidget(btn_right)
col2.addWidget(mirror)
col2.addWidget(sharpness)
col2.addWidget(gray)
col2.addWidget(saturation)
col2.addWidget(contrast)
col2.addWidget(blur)


# add widgets to column 1

col1.addWidget(btn_folder)
col1.addWidget(file_list)



# add columns to main layout

master_layout.addLayout(col1)
master_layout.addLayout(col2)



# set layout for window

main_window.setLayout(master_layout)


# show window

main_window.show()

app.exec_()
