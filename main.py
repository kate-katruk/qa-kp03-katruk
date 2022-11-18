import collections
from typing import List
from abc import ABC, abstractmethod

class FileSystem:
    def __init__(self) -> None:
        pass

    def listFilesAndSubdirections(self, path: str) -> List[str]:
        pass

    def createDirectory(self, path: str) -> None:
        pass

    def readContentFromFile(self, filePath: str) -> str:
        pass

    def appendContentToLogTextFile(self, filePath: str, content: str) -> None:
        pass

    def pushContentToBufferFile(self, filePath: str, content: str) -> None:
        pass

    def consumeContentFromBufferFile(self, filePath: str) -> str:
        pass

    def moveElemet(self, path: str, newPath: str) -> str:
        pass
    
    def deleteElement(self, path: str) -> str:
        pass

class Directory:
    def __init__(self, dir_max_elems: int) -> None:
        pass

class File(ABC):
    def __init__(self) -> None:
        super().__init__()

class BinaryFile(File):
    def __init__(self) -> None:
        pass

class LogTextFile(File):
    def __init__(self) -> None:
        pass

class BufferFile(File):
    def __init__(self, max_buf_file_size: int) -> None:
        pass

