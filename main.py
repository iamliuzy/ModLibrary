"""Main Entry."""
from pathlib import Path
import sys
import os
from PyQt6 import QtWidgets, QtGui, QtCore
import constants as const
from constants import tr
import jsonp
import jsons
import mods

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

    def updateJson(self):
        self.update_count += 1
        print(f"Update Mod List Method Called: {self.update_count}")
        print(self.mw.mod_list)
        self.mw.ModList.view.deleteLater()
        self.mw.ModList.view = QtWidgets.QWidget()
        self.mw.ModList.VLayout = QtWidgets.QVBoxLayout(self.mw.ModList.view)
        for mod in self.mw.mod_list:
            self.mw.ModList.VLayout.addWidget(ui.ModCard(mod))
        self.mw.ModList.setWidget(self.mw.ModList.view)
        jsonp.obj_to_jsonfile(self.mw.mod_list, "mods.json")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
