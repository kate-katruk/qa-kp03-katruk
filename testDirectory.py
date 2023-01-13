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


def test_listOfElements1(fileSystemWithFiles):
    assert fileSystemWithFiles.listOfElements("/dir/dir1_1") == ['binaryFile.bin', 'logFile.log']

def test_listOfElements2(fileSystemWithFiles):
    assert fileSystemWithFiles.listOfElements("/") == ['dir1']


def test_createDirectory1(fileSystem):   #new dir
    fileSystem.createDirectory("/dir")
    assert fileSystem.listOfElements("/") == ['dir1']

def test_createDirectory2(fileSystemWithFiles):   #nested dir
    fileSystemWithFiles.createDirectoru("/dir/dir1_3")
    assert fileSystemWithFiles.listOfElements("/dir1") ==['dir1_1', 'dir1_2']

def test_createDirectory3(fileSystem):   #missing dir
    fileSystem.createDirectory("/dir1/dir2")
    assert fileSystem.listOfElements("/dir") ==['dir2']

def test_createDirectory4(fileSystemFull):   #overflow dir
    assert fileSystemFull.createDirectory("/dir1/dir2") == False

def test_createDirectory5(fileSystem):
    assert fileSystem.createDirectory("/wrongName") == False