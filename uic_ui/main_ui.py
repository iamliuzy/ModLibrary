# ModLibrary, a Minecraft mod manager
# Copyright (C) 2024  iamliuzy
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Contact the author: iamliuzy <liuzhiyu.sh@outlook.com>

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(480, 348)
        self.verticalLayout = QtWidgets.QVBoxLayout(Main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopBar = QtWidgets.QHBoxLayout()
        self.TopBar.setObjectName("TopBar")
        self.SearchBox = SearchLineEdit(parent=Main)
        self.SearchBox.setObjectName("SearchBox")
        self.TopBar.addWidget(self.SearchBox)
        self.RefreshButton = ToolButton(parent=Main)
        self.RefreshButton.setObjectName("RefreshButton")
        self.TopBar.addWidget(self.RefreshButton)
        self.AddModButton = ToolButton(parent=Main)
        self.AddModButton.setAutoRaise(False)
        self.AddModButton.setObjectName("AddModButton")
        self.TopBar.addWidget(self.AddModButton)
        self.verticalLayout.addLayout(self.TopBar)
        self.ModList = SingleDirectionScrollArea(parent=Main)
        self.ModList.setWidgetResizable(True)
        self.ModList.setObjectName("ModList")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 460, 287))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.ModList.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.ModList)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
from qfluentwidgets import SearchLineEdit, SingleDirectionScrollArea, ToolButton
