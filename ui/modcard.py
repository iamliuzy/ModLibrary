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

from qfluentwidgets import CardWidget
from uic_ui import Ui_ModCard
from mods import Mod
import constants as const
class ModCard(CardWidget, Ui_ModCard):
    def __init__(self, mod: Mod):
        super().__init__()
        self.setupUi(self)
        self.ModIcon.setIcon(mod.geticon())
        self.ModName.setText(mod.name)
        authors = ""
        authors_length = len(mod.authors)
        for i in range(authors_length):
            author = mod.authors[i]
            if authors_length == 1:
                authors += author
            else:
                if not i == authors_length - 1:
                    authors += f"{author}, "
                else:
                    authors += f"{const.tr("ModCard", "和")} {author}"
        
        self.ModAuthors.setText(authors)
        self.ModDesc.setText(mod.desc)