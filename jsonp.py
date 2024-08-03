from pathlib import Path
from json import loads, dumps
from typing import Any
import jsons


class JsonFile:
    """
    Provide access for a JSON file.
    """

    def __init__(self, path: str, filetype: str = "") -> None:
        """
        Create a new JsonFile instance.

        :param path: Path to the JSON file.
        :param filetype: Type of the JSON file.
        :raises TypeError: If the filetype is not specified and cannot be
                           determined.
        :raises json.JSONDecodeError: If the JSON file contains invalid data.
        """
        self.path = Path(path)
        with open(self.path, "r", encoding="utf-8") as file:
            text = file.read()
        if filetype == "":
            try:
                self.obj = loads(text)
            except ValueError:
                raise TypeError(f"Cannot determine the JSON file type: {self.
                                                                        path}")
        elif filetype == "list":
            self.obj = list(loads(text))
        elif filetype == "dict":
            self.obj = dict(loads(text))
        else:
            raise ValueError(f"Unknown JSON file type: {filetype}")

    def get(self) -> dict | list:
        """
        Get the JSON data.

        :return: The JSON data.
        """
        return self.obj

    def store(self, new: dict | list) -> None:
        """
        Store the JSON data.

        :param new: The new JSON data.
        """
        with open(self.path, mode="w", encoding="utf-8") as file:
            file.write(dumps(new))


def qread(path: str, encoding='utf-8') -> str:
    """Shortcut to read a file.

    :param path: The file to read
    :type path: str
    :param encoding: The encoding, defaults to 'utf-8'
    :type encoding: str, optional
    :return: The content of the file
    :rtype: str
    """
    with open(Path(path), encoding=encoding, mode='r') as f:
        return f.read()


def json_to_dict(path) -> dict:
    """
    Read json file and return the content.
    """
    return dict(JsonFile(path, "dict").get())


def json_to_list(path) -> list:
    """
    Read json file and return the content.
    """
    return list(JsonFile(path, "list").get())


def jsonfile_to_obj(path: str, cls: type) -> Any:
    """Get json content as object using `jsons`

    :param path: Path to the json file
    :type path: str
    :param cls: Content type of the json file
    :type cls: type
    :return: An instance of `cls` that initialized with json content
    :rtype: cls
    """
    r = qread(path)
    if issubclass(cls, jsons.JsonSerializable):
        return cls.loads(r)
    else:
        return jsons.loads(r, cls)


def obj_to_json(obj: Any) -> str:
    """Serialize an object to json string using `jsons`

    :param obj: The object to serialize
    :type obj: Any
    :return: The serialized json string.
    :rtype: str
    """
    if isinstance(obj, jsons.JsonSerializable):
        return obj.dumps()
    else:
        return jsons.dumps(obj)


def obj_to_jsonfile(obj: Any, path: str) -> None:
    """Serialize an object to json string using `jsons`
    
    :param obj: The object to serialize
    :type obj: Any
    :return: The serialized json string.
    :rtype: str
    """
    with open(Path(path), encoding='utf-8', mode='w') as f:
        f.write(obj_to_json(obj))


def manifest_to_dict(path):
    result = {}
    with open(Path(path), mode="r", encoding="utf-8") as file:
        for line in map(str.strip, file.readlines()):
            if not (":" in line):
                continue
            key, value = line.split(":", maxsplit=1)
            result[key] = value.strip()
    return result
