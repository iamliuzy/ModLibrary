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

"""Main Entry."""
import sys
import os
from PyQt6 import QtWidgets, QtGui
import constants as const
from constants import tr
import jsonp

import qfluentwidgets as qfw

import ui


class MainWindow(qfw.MSFluentWindow):
    """Main Window
    """
    update_count = 0

    def __init__(self):
        super().__init__()
        self.setWindowTitle(const.NAME + " " + const.VERSION)

        qfw.setTheme(qfw.Theme.AUTO)

        if os.name == "nt":
            # Set theme color to user's preferred color
            from winrt.windows.ui.viewmanagement import UISettings, UIColorType
            self.themecolors = const.Namespace()
            ui_settings = UISettings()
            for colorname, colorid in zip(("ACC_DARK1", "ACC_LIGHT2"), (4, 7)):
                color = ui_settings.get_color_value(UIColorType(colorid))
                setattr(self.themecolors, colorname, (color.r, color.g,
                                                      color.b, color.a))

            if qfw.common.config.isDarkTheme():
                self.themecolors.ACC = self.themecolors.ACC_LIGHT2
            else:
                self.themecolors.ACC = self.themecolors.ACC_DARK1
            qfw.setThemeColor(QtGui.QColor(*self.themecolors.ACC))
        else:
            from qfluentwidgets import FluentThemeColor
            qfw.setThemeColor(FluentThemeColor.DEFAULT_BLUE.value)
        self.mw = ui.MainUi(self)
        self.addSubInterface(self.mw, qfw.FluentIcon.BOOK_SHELF, tr("Sidebar", "LIBRARY"))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if sys.platform == 'win32' and sys.getwindowsversion().build >= 22000:
        app.setStyle("fusion")

    window = MainWindow()
    window.show()
    app.exec()
