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

# from pathlib import PurePath
# import jsonp
from enum import IntEnum
import zipfile
import tempfile
import toml
# import log
import constants as const
# from os.path import abspath
from jsons import JsonSerializable, decorators
from dataclasses import dataclass
from pathlib import Path

from jsonp import manifest_to_dict

from PyQt6.QtGui import QIcon
from shutil import copy


# class ModFile(object):
#     """
#     Object for a Minecraft Mod File.
#     Attributes:
#         loader: 0: Forge old Loader
#                 1: Forge new Loader
#                 2: Fabric Loader
#         path: Absolute path to the mod file.
#         file: ZipFile instance of the mod jar file.
#         manifest_dict: Jar manifest file(META-INF/MANIFEST.MF) stored in dict form.
#         metadata: Mod info file("META-INF/mods.toml" for Forge new, "mcmod.info" for Forge old
#                   and "fabric.mod.json" for
#                   Fabric loader) stored in dict form.

#     Args:
#         path: Path to the mod file.
#     """

#     def __init__(self, path: PurePath):
#         self.path = abspath(path)
#         self.file = zipfile.ZipFile(self.path, mode="r")
#         with tempfile.TemporaryDirectory() as tempdir:
#             jar_manifest = self.file.extract("META-INF/MANIFEST.MF", tempdir)
#             self.manifest_dict = jsonparse.ManifestAccess.manifest_to_dict(jar_manifest)
#         #   try:
#             extracted = self.file.extract("META-INF/mods.toml", tempdir)
#             self.metadata = toml.load(extracted)
#             self.loader = 1  # Forge new loader
#         # These codes will be uncommented soon.
#         #   except KeyError:
#         #       try:
#         #           extracted = self.file.extract("mcmod.info", tempdir)
#         #           self.metadata = jsonparse.QuickAccess.json_to_list(extracted)
#         #           self.loader = 0  # Forge old loader
#         #       except KeyError:
#         #           extracted = self.file.extract("fabric.mod.json", tempdir)
#         #           self.metadata = jsonparse.QuickAccess.json_to_dict(extracted)
#         #           self.loader = 2  # Fabric loader
#         if self.loader == 1:
#             try:
#                 self.name = str(self.metadata["mods"][0]["displayName"])
#                 self.id = str(self.metadata["mods"][0]["modId"])
#                 self.dependencies = list(self.metadata["dependencies"][self.id])
#                 self.version = str(self.metadata["mods"][0]["version"])
#                 self.url = str(self.metadata["mods"][0]["displayURL"])
#                 self.issue_url = str(self.metadata["issueTrackerURL"])
#                 self.description = str(self.metadata["mods"][0]["description"])
#             except KeyError as e:
#                 log.warn(str(e) + ' key does not exist in the mod info file of mod "'\
#                           + str(self.path) + '".')
#             if self.version == "${file.jarVersion}":
#                 # Some mods may use ${file.jarVersion} to
#                 # refer to the version number in the manifest
#                 ver = self.manifest_dict.get("Implementation-Version")
#                 if ver is not None:
#                     self.version = ver
#                 else:
#                     log.error('Cannot get version of mod "%s".' % self.name)
#                     # If the program cannot find version in both place, output an error.
#             for i in dir(self):  # Debug code. Will remove soon.
#                 if i[0] != "_":
#                     log.debug(i + "::" + str(getattr(self, i)))


# class Mod_old(object):
#     files: list[ModFile]
#     mod_id: str
#     json: dict[str, str]

#     def __init__(self, files: list[ModFile]):
#         self.files = files
#         self.mod_id = self.files[0].id
#         self.name = self.files[0].name
#         self.description = self.files[0].description


class Loader(IntEnum):
    FORGE_LEGACY = 0
    FORGE = 1
    FABRIC = 2


@dataclass
class Mod(JsonSerializable):
    id: str
    name: str
    authors: list[str]
    loader: int
    iconame: str
    desc: str
    # mrid = StringField()
    # mrslug = StringField()
    # cfid = StringField()
    # cfslug = StringField()
    # support_mc_versions = ListField(ListField(StringField()))
    # incompatible: list[str]

    @classmethod
    def parse_from_file(cls, file: str):
        with tempfile.TemporaryDirectory() as tempdir:
            jar = zipfile.ZipFile(Path(file))
            jar_manifest = manifest_to_dict(jar.extract("META-INF/MANIFEST.MF", tempdir))
            # try:
            meta = toml.load(jar.extract("META-INF/mods.toml", tempdir))
            loader = Loader.FORGE.value
            first_mod_spec = meta.get("mods")[0]
            name = first_mod_spec.get("displayName")
            id = first_mod_spec.get("modId")
            desc = first_mod_spec.get("description")
            _authors = first_mod_spec.get("authors")
            if isinstance(_authors, str):
                authors = [_authors]
            else:
                authors = _authors
            # Parse mod metadatas.
            # TODO: Other metadatas: issueTrackerURL, etc.

            _iconpath = Path(first_mod_spec.get("logoFile", "pack.png"))
            _dst = Path(f"./mod_assets/{id}/")
            try:
                jar.extract(str(_iconpath), _dst)
            except:
                _iconpath = Path("./mod_assets/pack.png")
                copy(_iconpath, _dst)
            # Extract mod icon
            return Mod(id, name, authors, loader, _iconpath.name, desc)
            # except  # TODO: Fabric loader, Forge-Legacy loader, etc.

    def geticon(self) -> QIcon:
        return QIcon(str(Path("./mod_assets/%s/%s" % (self.id, self.iconame))))
