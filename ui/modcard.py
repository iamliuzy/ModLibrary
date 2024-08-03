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