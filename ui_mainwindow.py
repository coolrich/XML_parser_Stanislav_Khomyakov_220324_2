# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpinBox, QStatusBar, QTabWidget,
    QTableView, QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(847, 630)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.open_action = QAction(MainWindow)
        self.open_action.setObjectName(u"open_action")
        self.exit_action = QAction(MainWindow)
        self.exit_action.setObjectName(u"exit_action")
        self.load_project_action = QAction(MainWindow)
        self.load_project_action.setObjectName(u"load_project_action")
        self.save_project_action = QAction(MainWindow)
        self.save_project_action.setObjectName(u"save_project_action")
        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.download_xml_action = QAction(MainWindow)
        self.download_xml_action.setObjectName(u"download_xml_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_21 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.offer_description_tab_widget = QTabWidget(self.centralwidget)
        self.offer_description_tab_widget.setObjectName(u"offer_description_tab_widget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.search_input_category_line_edit = QLineEdit(self.groupBox_4)
        self.search_input_category_line_edit.setObjectName(u"search_input_category_line_edit")

        self.horizontalLayout_2.addWidget(self.search_input_category_line_edit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.check_all_input_categories_push_button = QPushButton(self.groupBox_4)
        self.check_all_input_categories_push_button.setObjectName(u"check_all_input_categories_push_button")

        self.horizontalLayout.addWidget(self.check_all_input_categories_push_button)

        self.uncheck_all_input_categories_push_button = QPushButton(self.groupBox_4)
        self.uncheck_all_input_categories_push_button.setObjectName(u"uncheck_all_input_categories_push_button")

        self.horizontalLayout.addWidget(self.uncheck_all_input_categories_push_button)

        self.add_category_push_button = QPushButton(self.groupBox_4)
        self.add_category_push_button.setObjectName(u"add_category_push_button")

        self.horizontalLayout.addWidget(self.add_category_push_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.input_category_tree_view = QTreeView(self.groupBox_4)
        self.input_category_tree_view.setObjectName(u"input_category_tree_view")
        self.input_category_tree_view.setAlternatingRowColors(True)

        self.verticalLayout_3.addWidget(self.input_category_tree_view)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.search_output_category_line_edit = QLineEdit(self.groupBox_3)
        self.search_output_category_line_edit.setObjectName(u"search_output_category_line_edit")

        self.horizontalLayout_14.addWidget(self.search_output_category_line_edit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.check_all_output_categories_push_button = QPushButton(self.groupBox_3)
        self.check_all_output_categories_push_button.setObjectName(u"check_all_output_categories_push_button")

        self.horizontalLayout_13.addWidget(self.check_all_output_categories_push_button)

        self.uncheck_all_output_categories_push_button = QPushButton(self.groupBox_3)
        self.uncheck_all_output_categories_push_button.setObjectName(u"uncheck_all_output_categories_push_button")

        self.horizontalLayout_13.addWidget(self.uncheck_all_output_categories_push_button)

        self.delete_category_push_button = QPushButton(self.groupBox_3)
        self.delete_category_push_button.setObjectName(u"delete_category_push_button")

        self.horizontalLayout_13.addWidget(self.delete_category_push_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.output_category_tree_view = QTreeView(self.groupBox_3)
        self.output_category_tree_view.setObjectName(u"output_category_tree_view")
        self.output_category_tree_view.setAlternatingRowColors(True)

        self.verticalLayout_5.addWidget(self.output_category_tree_view)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.verticalLayout_4.addWidget(self.groupBox_3)


        self.verticalLayout_11.addLayout(self.verticalLayout_4)

        self.offer_description_tab_widget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -355, 784, 847))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 360))
        self.groupBox_5.setMaximumSize(QSize(16777215, 10000))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.search_input_product_line_edit = QLineEdit(self.groupBox_5)
        self.search_input_product_line_edit.setObjectName(u"search_input_product_line_edit")

        self.horizontalLayout_3.addWidget(self.search_input_product_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(50)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.check_all_input_products_push_button = QPushButton(self.groupBox_5)
        self.check_all_input_products_push_button.setObjectName(u"check_all_input_products_push_button")

        self.horizontalLayout_8.addWidget(self.check_all_input_products_push_button)

        self.uncheck_all_input_products_push_button = QPushButton(self.groupBox_5)
        self.uncheck_all_input_products_push_button.setObjectName(u"uncheck_all_input_products_push_button")

        self.horizontalLayout_8.addWidget(self.uncheck_all_input_products_push_button)

        self.add_product_push_button = QPushButton(self.groupBox_5)
        self.add_product_push_button.setObjectName(u"add_product_push_button")

        self.horizontalLayout_8.addWidget(self.add_product_push_button)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.input_products_table_view = QTableView(self.groupBox_5)
        self.input_products_table_view.setObjectName(u"input_products_table_view")
        self.input_products_table_view.setMinimumSize(QSize(0, 245))
        self.input_products_table_view.setMaximumSize(QSize(16777215, 16777215))
        self.input_products_table_view.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.input_products_table_view)


        self.verticalLayout_8.addLayout(self.verticalLayout)


        self.verticalLayout_12.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 461))
        self.groupBox_6.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 7, -1, -1)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_15.addWidget(self.label_8)

        self.search_output_product_line_edit = QLineEdit(self.groupBox_6)
        self.search_output_product_line_edit.setObjectName(u"search_output_product_line_edit")

        self.horizontalLayout_15.addWidget(self.search_output_product_line_edit)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(50)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.check_all_output_products_push_button = QPushButton(self.groupBox_6)
        self.check_all_output_products_push_button.setObjectName(u"check_all_output_products_push_button")

        self.horizontalLayout_7.addWidget(self.check_all_output_products_push_button)

        self.uncheck_all_output_products_push_button = QPushButton(self.groupBox_6)
        self.uncheck_all_output_products_push_button.setObjectName(u"uncheck_all_output_products_push_button")

        self.horizontalLayout_7.addWidget(self.uncheck_all_output_products_push_button)

        self.remove_product_push_button = QPushButton(self.groupBox_6)
        self.remove_product_push_button.setObjectName(u"remove_product_push_button")

        self.horizontalLayout_7.addWidget(self.remove_product_push_button)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.output_products_table_view = QTableView(self.groupBox_6)
        self.output_products_table_view.setObjectName(u"output_products_table_view")
        self.output_products_table_view.setMinimumSize(QSize(0, 245))
        self.output_products_table_view.setMaximumSize(QSize(16777215, 267))
        self.output_products_table_view.setAlternatingRowColors(True)

        self.verticalLayout_9.addWidget(self.output_products_table_view)

        self.frame = QFrame(self.groupBox_6)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 94))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_6.setContentsMargins(-1, 16, -1, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(76, 0))
        self.label_12.setMaximumSize(QSize(68, 16777215))

        self.horizontalLayout_12.addWidget(self.label_12)

        self.price_category_combo_box = QComboBox(self.frame)
        self.price_category_combo_box.addItem("")
        self.price_category_combo_box.addItem("")
        self.price_category_combo_box.setObjectName(u"price_category_combo_box")
        self.price_category_combo_box.setMaximumSize(QSize(94, 16777215))

        self.horizontalLayout_12.addWidget(self.price_category_combo_box)


        self.gridLayout.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        self.apply_multiplier_push_button = QPushButton(self.frame)
        self.apply_multiplier_push_button.setObjectName(u"apply_multiplier_push_button")
        self.apply_multiplier_push_button.setMaximumSize(QSize(128, 16777215))

        self.gridLayout.addWidget(self.apply_multiplier_push_button, 0, 4, 1, 1)

        self.add_drop_price_check_box = QCheckBox(self.frame)
        self.add_drop_price_check_box.setObjectName(u"add_drop_price_check_box")
        self.add_drop_price_check_box.setTristate(False)

        self.gridLayout.addWidget(self.add_drop_price_check_box, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(14)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(54, 16777215))

        self.horizontalLayout_6.addWidget(self.label_7)

        self.multiplier_double_spin_box = QDoubleSpinBox(self.frame)
        self.multiplier_double_spin_box.setObjectName(u"multiplier_double_spin_box")
        self.multiplier_double_spin_box.setMaximumSize(QSize(77, 16777215))

        self.horizontalLayout_6.addWidget(self.multiplier_double_spin_box)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(74, 16777215))

        self.horizontalLayout_4.addWidget(self.label_6)

        self.bottom_price_limit_spin_box = QSpinBox(self.frame)
        self.bottom_price_limit_spin_box.setObjectName(u"bottom_price_limit_spin_box")
        self.bottom_price_limit_spin_box.setMinimumSize(QSize(55, 0))
        self.bottom_price_limit_spin_box.setMaximumSize(QSize(69, 16777215))
        self.bottom_price_limit_spin_box.setMaximum(999999999)

        self.horizontalLayout_4.addWidget(self.bottom_price_limit_spin_box)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 2, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(73, 16777215))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.upper_price_limit_spin_box = QSpinBox(self.frame)
        self.upper_price_limit_spin_box.setObjectName(u"upper_price_limit_spin_box")
        self.upper_price_limit_spin_box.setMaximumSize(QSize(70, 16777215))
        self.upper_price_limit_spin_box.setMaximum(999999999)

        self.horizontalLayout_5.addWidget(self.upper_price_limit_spin_box)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 3, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)


        self.verticalLayout_9.addWidget(self.frame)


        self.verticalLayout_23.addLayout(self.verticalLayout_9)


        self.verticalLayout_12.addWidget(self.groupBox_6)


        self.verticalLayout_22.addLayout(self.verticalLayout_12)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.offer_description_tab_widget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_19 = QVBoxLayout(self.tab_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.search_category_for_replace_line_edit = QLineEdit(self.groupBox)
        self.search_category_for_replace_line_edit.setObjectName(u"search_category_for_replace_line_edit")
        self.search_category_for_replace_line_edit.setMaximumSize(QSize(260, 16777215))

        self.horizontalLayout_10.addWidget(self.search_category_for_replace_line_edit)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_20.addWidget(self.label)

        self.replace_category_name_line_edit = QLineEdit(self.groupBox)
        self.replace_category_name_line_edit.setObjectName(u"replace_category_name_line_edit")
        self.replace_category_name_line_edit.setMaximumSize(QSize(260, 16777215))

        self.horizontalLayout_20.addWidget(self.replace_category_name_line_edit)


        self.verticalLayout_13.addLayout(self.horizontalLayout_20)

        self.replace_category_name_push_button = QPushButton(self.groupBox)
        self.replace_category_name_push_button.setObjectName(u"replace_category_name_push_button")

        self.verticalLayout_13.addWidget(self.replace_category_name_push_button)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_13.addWidget(self.label_9)

        self.input_category_names_table_view = QTableView(self.groupBox)
        self.input_category_names_table_view.setObjectName(u"input_category_names_table_view")
        self.input_category_names_table_view.setAlternatingRowColors(True)
        self.input_category_names_table_view.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_13.addWidget(self.input_category_names_table_view)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_13.addWidget(self.label_14)

        self.output_category_names_table_view = QTableView(self.groupBox)
        self.output_category_names_table_view.setObjectName(u"output_category_names_table_view")
        self.output_category_names_table_view.setAlternatingRowColors(True)

        self.verticalLayout_13.addWidget(self.output_category_names_table_view)


        self.verticalLayout_15.addLayout(self.verticalLayout_13)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.add_category_row_push_button = QPushButton(self.groupBox)
        self.add_category_row_push_button.setObjectName(u"add_category_row_push_button")

        self.horizontalLayout_9.addWidget(self.add_category_row_push_button)

        self.delete_category_row_push_button = QPushButton(self.groupBox)
        self.delete_category_row_push_button.setObjectName(u"delete_category_row_push_button")

        self.horizontalLayout_9.addWidget(self.delete_category_row_push_button)


        self.verticalLayout_15.addLayout(self.horizontalLayout_9)


        self.verticalLayout_18.addLayout(self.verticalLayout_15)


        self.horizontalLayout_17.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.search_product_for_replace_line_edit = QLineEdit(self.groupBox_2)
        self.search_product_for_replace_line_edit.setObjectName(u"search_product_for_replace_line_edit")
        self.search_product_for_replace_line_edit.setMaximumSize(QSize(260, 16777215))

        self.horizontalLayout_11.addWidget(self.search_product_for_replace_line_edit)


        self.verticalLayout_14.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_21.addWidget(self.label_2)

        self.replace_product_name_line_edit = QLineEdit(self.groupBox_2)
        self.replace_product_name_line_edit.setObjectName(u"replace_product_name_line_edit")
        self.replace_product_name_line_edit.setMaximumSize(QSize(260, 16777215))

        self.horizontalLayout_21.addWidget(self.replace_product_name_line_edit)


        self.verticalLayout_14.addLayout(self.horizontalLayout_21)

        self.replace_product_name_push_button = QPushButton(self.groupBox_2)
        self.replace_product_name_push_button.setObjectName(u"replace_product_name_push_button")

        self.verticalLayout_14.addWidget(self.replace_product_name_push_button)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_14.addWidget(self.label_15)

        self.input_product_names_table_view = QTableView(self.groupBox_2)
        self.input_product_names_table_view.setObjectName(u"input_product_names_table_view")
        self.input_product_names_table_view.setAlternatingRowColors(True)
        self.input_product_names_table_view.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_14.addWidget(self.input_product_names_table_view)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_14.addWidget(self.label_16)

        self.output_product_names_table_view = QTableView(self.groupBox_2)
        self.output_product_names_table_view.setObjectName(u"output_product_names_table_view")
        self.output_product_names_table_view.setAlternatingRowColors(True)

        self.verticalLayout_14.addWidget(self.output_product_names_table_view)


        self.verticalLayout_16.addLayout(self.verticalLayout_14)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.add_product_row_push_button = QPushButton(self.groupBox_2)
        self.add_product_row_push_button.setObjectName(u"add_product_row_push_button")

        self.horizontalLayout_22.addWidget(self.add_product_row_push_button)

        self.delete_product_row_push_button = QPushButton(self.groupBox_2)
        self.delete_product_row_push_button.setObjectName(u"delete_product_row_push_button")

        self.horizontalLayout_22.addWidget(self.delete_product_row_push_button)


        self.verticalLayout_16.addLayout(self.horizontalLayout_22)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)


        self.horizontalLayout_17.addWidget(self.groupBox_2)


        self.verticalLayout_19.addLayout(self.horizontalLayout_17)

        self.offer_description_tab_widget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_24 = QVBoxLayout(self.tab_4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.offer_description_plain_text_edit = QPlainTextEdit(self.tab_4)
        self.offer_description_plain_text_edit.setObjectName(u"offer_description_plain_text_edit")
        self.offer_description_plain_text_edit.setMinimumSize(QSize(0, 433))
        self.offer_description_plain_text_edit.setMaximumSize(QSize(16777215, 500))

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.offer_description_plain_text_edit)

        self.add_description_push_button = QPushButton(self.tab_4)
        self.add_description_push_button.setObjectName(u"add_description_push_button")
        self.add_description_push_button.setMaximumSize(QSize(100, 16777215))

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.add_description_push_button)

        self.description_text_indicator_label = QLabel(self.tab_4)
        self.description_text_indicator_label.setObjectName(u"description_text_indicator_label")
        self.description_text_indicator_label.setEnabled(True)
        self.description_text_indicator_label.setMaximumSize(QSize(27, 16777215))
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.description_text_indicator_label.setFont(font)
        self.description_text_indicator_label.setLineWidth(1)
        self.description_text_indicator_label.setTextFormat(Qt.PlainText)
        self.description_text_indicator_label.setWordWrap(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.description_text_indicator_label)

        self.widget = QWidget(self.tab_4)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 25))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.bold_text_push_button = QPushButton(self.widget)
        self.bold_text_push_button.setObjectName(u"bold_text_push_button")
        self.bold_text_push_button.setMaximumSize(QSize(30, 16777215))
        font1 = QFont()
        font1.setBold(True)
        self.bold_text_push_button.setFont(font1)

        self.horizontalLayout_16.addWidget(self.bold_text_push_button)

        self.anchor_text_push_button = QPushButton(self.widget)
        self.anchor_text_push_button.setObjectName(u"anchor_text_push_button")
        self.anchor_text_push_button.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_16.addWidget(self.anchor_text_push_button)

        self.set_plain_text_push_button = QPushButton(self.widget)
        self.set_plain_text_push_button.setObjectName(u"set_plain_text_push_button")
        self.set_plain_text_push_button.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_16.addWidget(self.set_plain_text_push_button)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout_16)


        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.widget)


        self.verticalLayout_24.addLayout(self.formLayout_2)

        self.offer_description_tab_widget.addTab(self.tab_4, "")

        self.verticalLayout_20.addWidget(self.offer_description_tab_widget)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.get_output_xml_push_button = QPushButton(self.centralwidget)
        self.get_output_xml_push_button.setObjectName(u"get_output_xml_push_button")

        self.horizontalLayout_19.addWidget(self.get_output_xml_push_button)

        self.get_output_csv_push_button = QPushButton(self.centralwidget)
        self.get_output_csv_push_button.setObjectName(u"get_output_csv_push_button")

        self.horizontalLayout_19.addWidget(self.get_output_csv_push_button)


        self.verticalLayout_20.addLayout(self.horizontalLayout_19)


        self.verticalLayout_21.addLayout(self.verticalLayout_20)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 847, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.open_action)
        self.menu.addAction(self.download_xml_action)
        self.menu.addAction(self.load_project_action)
        self.menu.addAction(self.save_project_action)
        self.menu.addAction(self.exit_action)
        self.menu_2.addAction(self.action_about_qt)

        self.retranslateUi(MainWindow)
        self.exit_action.triggered.connect(MainWindow.close)

        self.offer_description_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"XML parser", None))
        self.open_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0456\u0434\u043a\u0440\u0438\u0442\u0438 XML...", None))
        self.exit_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0445\u0456\u0434", None))
        self.load_project_action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0456\u0434\u043a\u0440\u0438\u0442\u0438 \u0448\u0430\u0431\u043b\u043e\u043d...", None))
        self.save_project_action.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438 \u0448\u0430\u0431\u043b\u043e\u043d...", None))
        self.action_about_qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.download_xml_action.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0438\u0442\u0438 xml \u0444\u0430\u0439\u043b...", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0456 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457 \u0442\u043e\u0432\u0430\u0440\u0456\u0432", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0443\u043a:", None))
        self.check_all_input_categories_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0432\u0441\u0456", None))
        self.uncheck_all_input_categories_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u044f\u0442\u0438 \u0432\u0438\u0431\u0456\u0440 \u0437 \u0443\u0441\u0456\u0445", None))
        self.add_category_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0434\u043e\n"
"XML", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u043d\u0456 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457 \u0442\u043e\u0432\u0430\u0440\u0456\u0432 \u0434\u043b\u044f \u0432\u0438\u0432\u0430\u043d\u0442\u0430\u0436\u0435\u043d\u043d\u044f \u0434\u043e XML \u0444\u0430\u0439\u043b\u0443", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0443\u043a:", None))
        self.check_all_output_categories_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0432\u0441\u0456", None))
        self.uncheck_all_output_categories_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u044f\u0442\u0438 \u0432\u0438\u0431\u0456\u0440 \u0437 \u0443\u0441\u0456\u0445", None))
        self.delete_category_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u0438 \u0437\n"
"XML", None))
        self.offer_description_tab_widget.setTabText(self.offer_description_tab_widget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u0438 \u0437 \u043e\u0431\u0440\u0430\u043d\u0438\u0445 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0439", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0443\u043a:", None))
        self.check_all_input_products_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0432\u0441\u0456", None))
        self.uncheck_all_input_products_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u044f\u0442\u0438 \u0432\u0438\u0431\u0456\u0440 \u0437 \u0443\u0441\u0456\u0445", None))
        self.add_product_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0434\u043e\n"
"XML", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u043d\u0456 \u0442\u043e\u0432\u0430\u0440\u0438 \u0434\u043b\u044f \u0432\u0438\u0432\u0430\u043d\u0442\u0430\u0436\u0435\u043d\u043d\u044f \u0432 XML \u0444\u0430\u0439\u043b", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0443\u043a:", None))
        self.check_all_output_products_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0432\u0441\u0456", None))
        self.uncheck_all_output_products_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u044f\u0442\u0438 \u0432\u0438\u0431\u0456\u0440 \u0437 \u0443\u0441\u0456\u0445", None))
        self.remove_product_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u0438 \u0437\n"
"XML", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f \u0446\u0456\u043d", None))
        self.price_category_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0442\u043e\u0432\u0430 \u0426\u0456\u043d\u0430", None))
        self.price_category_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0414\u0440\u043e\u043f \u0426\u0456\u043d\u0430", None))

        self.apply_multiplier_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0441\u0442\u043e\u0441\u0443\u0432\u0430\u0442\u0438 \u043c\u043d\u043e\u0436\u043d\u0438\u043a", None))
        self.add_drop_price_check_box.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0434\u0440\u043e\u043f \u0446\u0456\u043d\u0443 \u0434\u043e XML", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043d\u043e\u0436\u043d\u0438\u043a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0436\u043d\u044f \u043c\u0435\u0436\u0430\n"
"(\u0432\u043a\u043b\u044e\u0447\u043d\u043e)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0445\u043d\u044f \u043c\u0435\u0436\u0430\n"
"(\u0432\u043a\u043b\u044e\u0447\u043d\u043e)", None))
        self.offer_description_tab_widget.setTabText(self.offer_description_tab_widget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0440\u0430\u0437\u0430 \u0434\u043b\u044f \u0437\u0430\u043c\u0456\u043d\u0438:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0456\u043d\u0438\u0442\u0438 \u043d\u0430:", None))
        self.replace_category_name_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0456\u043d\u0438\u0442\u0438", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0456 \u043d\u0430\u0437\u0432\u0438 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0439 \u0442\u043e\u0432\u0430\u0440\u0456\u0432", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d\u0438 \u0434\u043b\u044f \u0437\u0430\u043c\u0456\u043d\u0438 \u043d\u0430\u0437\u0432 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0439", None))
        self.add_category_row_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0440\u044f\u0434\u043e\u043a", None))
        self.delete_category_row_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0440\u044f\u0434\u043e\u043a(-\u043a\u0438)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0432\u0430\u0440\u0438", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0440\u0430\u0437\u0430 \u0434\u043b\u044f \u0437\u0430\u043c\u0456\u043d\u0438:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0456\u043d\u0438\u0442\u0438 \u043d\u0430:", None))
        self.replace_product_name_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0456\u043d\u0438\u0442\u0438", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0456 \u043d\u0430\u0437\u0432\u0438 \u0442\u043e\u0432\u0430\u0440\u0456\u0432", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d\u0438 \u0434\u043b\u044f \u0437\u0430\u043c\u0456\u043d\u0438 \u043d\u0430\u0437\u0432 \u0442\u043e\u0432\u0430\u0440\u0456\u0432", None))
        self.add_product_row_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0440\u044f\u0434\u043e\u043a", None))
        self.delete_product_row_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0440\u044f\u0434\u043e\u043a(-\u043a\u0438)", None))
        self.offer_description_tab_widget.setTabText(self.offer_description_tab_widget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0456\u043d\u0430 \u0441\u043b\u0456\u0432", None))
        self.add_description_push_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043e\u043f\u0438\u0441", None))
        self.description_text_indicator_label.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.bold_text_push_button.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.anchor_text_push_button.setText(QCoreApplication.translate("MainWindow", u"<a>", None))
        self.set_plain_text_push_button.setText(QCoreApplication.translate("MainWindow", u"text", None))
        self.offer_description_tab_widget.setTabText(self.offer_description_tab_widget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441 \u0442\u043e\u0432\u0430\u0440\u0443", None))
        self.get_output_xml_push_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0438\u043c\u0430\u0442\u0438 XML", None))
        self.get_output_csv_push_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0438\u043c\u0430\u0442\u0438 CSV", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0432\u0456\u0434\u043a\u0430", None))
    # retranslateUi

