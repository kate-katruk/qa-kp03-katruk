from fileSystem import FileSystem
import pytest

@pytest.fixture
def fileSystem():
    fs = FileSystem(5, 5)
    fs.mkdir("/dir")
    return fs

@pytest.fixture
def fileSystemWithFiles():
    fs = FileSystem(5, 5)
    fs.mkdir("/dir1")
    fs.mkdir("/dir1/dir1_1")
    fs.mkdir("/dir1/dir1_2")

    fs.create_binary_file("/dir1/dir1_1", "binaryFile.bin")
    fs.create_log_file("/dir1/dir1_1", "logFile.log")
    fs.create_buf_file("/dir1/dir1_2", "bufFile.buf")
    fs.create_log_file("/dir1/dir1_2", "logFile.log")
    return fs

@pytest.fixture
def fileSystemFull():
    fs = FileSystem(5, 5)
    fs.mkdir("/dir1")
    fs.create_binary_file("/dir1", "binaryFile1.bin")
    fs.create_binary_file("/dir1", "binaryFile2.bin")
    fs.create_binary_file("/dir1", "binaryFile3.bin")
    fs.create_binary_file("/dir1", "binaryFile4.bin")
    fs.create_binary_file("/dir1", "binaryFile5.bin")
    return fs


def test_createBufFile1(fileSystem):
    fileSystem.createBufFile("/dir", "bufFile.buf")
    assert fileSystem.listOfElements("/dir") == ['bufFile.buf']

def test_createBufFile2(fileSystem):
    fileSystem.createBufFile("/dir/dir1/dir2", "bufFile.buf")
    assert fileSystem.listOfElements("/dir/dir1/dir2") == ['bufFile.buf']

def test_createBufFile3(fileSystem):
    assert fileSystem.createBufFile("/", "bufFile.buf") == False

def test_createBufFile4(fileSystem):
    assert fileSystem.createBufFile("dir", "file.b") == False

def test_createBufFile5(fileSystemFull):
    assert fileSystemFull.createBufFile("/dir1", "file.buf") == False

def test_createBufFile6(fileSystemWithFiles):
    assert fileSystemWithFiles.createBufFile("dir1/dir1_2", "bufFile.buf") == False



def test_deleteBufFile(fileSystemWithFiles):
    fileSystemWithFiles.deleteBufFile("/dir1/dir1_2/bufFile.buf")
    assert fileSystemWithFiles.listOfElements("/dir1/dir1_2") == ['logFile.log']

def test_deleteBufFile(fileSystem):
    assert fileSystem.deleteBufFile("/dir/buf.buf") == False



def test_consumeFromBufFile1(fileSystemWithFiles):
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "some element")
    assert fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf") == "some element"

def test_consumeFromBufFile2(fileSystemWithFiles):
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "first elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "second elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "third elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "fourth elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "fifth elem")

    fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf")
    fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf")
    fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf")
    fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf")
    assert fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf") == "fifth elem"

def test_consumeFromBufFile3(fileSystemWithFiles):
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "first elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "second elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "third elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "fourth elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "fifth elem")

    fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf")
    fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf")
    fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf")
    fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf")
    fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf")
    assert fileSystemWithFiles.consumeFromBufFile("/dir1/dir1_2/bufFile.buf") == False
    
def test_PushToBufFile1(fileSystemWithFiles):
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "first elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "second elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "third elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "fourth elem")
    assert fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "fifth elem") == True

def test_PushToBufFile2(fileSystemWithFiles):
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "first elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "second elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "third elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "fourth elem")
    fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "fifth elem")
    assert fileSystemWithFiles.pushToBufFile("/dir1/dir1_2/bufFile.buf", "error elem") == False
