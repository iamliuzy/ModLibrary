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
    def __init__(self, mw: qfw.MSFluentWindow):
        super().__init__()
        self.setupUi(self)
        self.mw = mw
        self.AddModButton.setIcon(qfw.FluentIcon.ADD)
        self.AddModButton.clicked.connect(self.slot_addMod)
        self.RefreshButton.setIcon(QtGui.QIcon.fromTheme(
            QtGui.QIcon.ThemeIcon.ViewRefresh))
        self.RefreshButton.clicked.connect(mw.updateJson)
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
            self.ModList.VLayout.addWidget(ModCard(mod))
        self.ModList.setWidget(self.ModList.view)

    def slot_addMod(self):
        print("----------Import Mod Button Clicked----------")
        modpath = QtWidgets.QFileDialog.getOpenFileName(self,
                                                        tr("AddModDialog", "导入模组"),
                                                        filter=f"{tr("AddModDialog", "模组文件")} (*.jar)")[0]
        if not modpath == ".":
            self.mod_list.append(mods.Mod.parse_from_file(modpath))
            self.mw.updateJson()
