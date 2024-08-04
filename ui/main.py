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

from pathlib import Path
from uic_ui import Ui_Main
from PyQt6 import QtWidgets, QtGui
import mods, jsonp
import constants as const
from constants import tr
import qfluentwidgets as qfw
from .modcard import ModCard


class MainUi(QtWidgets.QWidget, Ui_Main):
    mod_list: list[mods.Mod]
    update_count = 0
    def __init__(self, mw: qfw.MSFluentWindow):
        super().__init__()
        self.setupUi(self)
        self.AddModButton.setIcon(qfw.FluentIcon.ADD)
        self.AddModButton.clicked.connect(self.slot_addMod)
        self.RefreshButton.setIcon(QtGui.QIcon.fromTheme(
            QtGui.QIcon.ThemeIcon.ViewRefresh))
        self.RefreshButton.clicked.connect(self.updateJson)
        self.ModList.view = QtWidgets.QWidget()
        self.ModList.VLayout = QtWidgets.QVBoxLayout(self.ModList.view)
        self.mod_list = []
        if not Path(".\\mods.json").exists():
            with open(Path(".\\mods.json"), encoding="utf-8", mode="w") as f:
                f.write("[]")
        for mod in jsonp.jsonfile_to_obj(".\\mods.json", list[mods.Mod]):
            mod: mods.Mod
            print(mod.dumps())
            self.mod_list.append(mod)
            self.ModList.VLayout.addWidget(ModCard(mod, self.slot_deleteMod))
        self.ModList.setWidget(self.ModList.view)

    def slot_addMod(self):
        print("----------Import Mod Button Clicked----------")
        modpath = QtWidgets.QFileDialog.getOpenFileName(self,
                                                        tr("AddModDialog", "导入模组"),
                                                        filter=f"{tr("AddModDialog", "模组文件")} (*.jar)")[0]
        if not modpath == ".":
            self.mod_list.append(mods.Mod.parse_from_file(modpath))
            self.updateJson()
            self.updateModList()

    def updateJson(self):
        self.update_count += 1
        print(f"Update Mod List Method Called: {self.update_count}")
        print(self.mod_list)
        jsonp.obj_to_jsonfile(self.mod_list, "mods.json")
    
    def slot_deleteMod(self, mod: ModCard):
        self.mod_list.remove(mod.mod)
        self.updateJson()

    def updateModList(self):
        self.ModList.view.deleteLater()
        self.ModList.view = QtWidgets.QWidget()
        self.ModList.VLayout = QtWidgets.QVBoxLayout(self.ModList.view)
        for mod in self.mod_list:
            self.ModList.VLayout.addWidget(ModCard(mod, self.slot_deleteMod))
        self.ModList.setWidget(self.ModList.view)
