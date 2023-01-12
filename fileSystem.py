import collections
from typing import List
from abc import ABC, abstractmethod

class FileSystem:
    dir_max_elems: int
    max_buf_file_size: int

    def __init__(self, max_elems:int, max_buf_file_size:int) -> None:
        pass

    def listFilesAndSubdirections(self, path: str) -> List[str]:
        pass

    def createDirectory(self, path: str) -> bool:
        pass

    def deleteDirectory(self, path:str) -> bool:
        pass

    def moveDirectory(self, pathFrom: str, pathTo: str) -> bool:
        pass



    def createBinFile(self, path: str, fileName: str) -> bool:
        pass

    def deleteBinFile(self, filePath: str) -> bool:
        pass

    def readBinFile(self, filePath: str) -> str:
        pass

    def moveBinFile(self, filePath:str, pathTo: str) -> bool:
        pass



    def createLogFile(self, path: str, fileName: str) -> bool:
        pass

    def deleteLogFile(self, filePath: str) -> bool:
        pass

    def appendContentToLogFile(self, filePath: str, content: str) -> bool:
        pass

    def readLogFile(self, filePath:str) -> str:
        pass

    def moveLogFile(self, filePath:str, pathTo: str) -> bool:
        pass
    

    def createBufFile(self, path: str, fileName: str) -> bool:
        pass

    def deleteBufFile(self, filePath: str) -> bool:
        pass

    def pushToBufFile(self, filePath: str, elem) -> bool:
        pass

    def consumeFromBufFile(self, filePath:str):
        pass

    def moveBufFile(self, filePath:str, pathTo: str) -> bool:
        pass