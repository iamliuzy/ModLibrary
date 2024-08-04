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


class Ui_ModCard(object):
    def setupUi(self, ModCard):
        ModCard.setObjectName("ModCard")
        ModCard.resize(256, 80)
        ModCard.setMinimumSize(QtCore.QSize(0, 80))
        ModCard.setWindowTitle("ModCard")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ModCard)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ModIcon = IconWidget(parent=ModCard)
        self.ModIcon.setMinimumSize(QtCore.QSize(60, 60))
        self.ModIcon.setMaximumSize(QtCore.QSize(60, 60))
        self.ModIcon.setObjectName("ModIcon")
        self.horizontalLayout_2.addWidget(self.ModIcon)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ModName = StrongBodyLabel(parent=ModCard)
        self.ModName.setMaximumSize(QtCore.QSize(16777215, 20))
        self.ModName.setText("")
        self.ModName.setObjectName("ModName")
        self.horizontalLayout.addWidget(self.ModName)
        self.ModAuthors = CaptionLabel(parent=ModCard)
        self.ModAuthors.setMaximumSize(QtCore.QSize(16777215, 20))
        self.ModAuthors.setText("")
        self.ModAuthors.setObjectName("ModAuthors")
        self.horizontalLayout.addWidget(self.ModAuthors)
        self.More = TransparentToolButton(parent=ModCard)
        self.More.setMinimumSize(QtCore.QSize(0, 20))
        self.More.setMaximumSize(QtCore.QSize(20, 20))
        self.More.setObjectName("More")
        self.horizontalLayout.addWidget(self.More)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ModDesc = BodyLabel(parent=ModCard)
        self.ModDesc.setText("")
        self.ModDesc.setWordWrap(True)
        self.ModDesc.setObjectName("ModDesc")
        self.verticalLayout.addWidget(self.ModDesc)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ModCard)
        QtCore.QMetaObject.connectSlotsByName(ModCard)

    def retranslateUi(self, ModCard):
        pass
from qfluentwidgets import BodyLabel, CaptionLabel, CardWidget, IconWidget, StrongBodyLabel, TransparentToolButton
