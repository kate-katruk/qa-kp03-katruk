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



def test_createLogFile1(fileSystem):
    fileSystem.createLogFile("/dir", "logFile.log")
    assert fileSystem.listOfElements("/dir") == ['logFile.log']

def test_createLogFile2(fileSystem):
    fileSystem.createLogFile("/dir/dir1/dir2", "logFile.log")
    assert fileSystem.listOfElements("/dir/dir1/dir2") == ['logFile.log']

def test_createLogFile3(fileSystem):
    assert fileSystem.createLogFile("/", "logFile.log") == False

def test_createLogFile4(fileSystem):
    assert fileSystem.createLogFile("/dir", "file.l") == False

def test_createLogFile5(fileSystemFull):
    assert fileSystemFull.createLogFile("/dir1", "file.log") == False

def test_createLogFile6(fileSystemWithFiles):
    assert fileSystemWithFiles.createLogFile("/dir1/dir1_1", "logFile.log") == False

def test_createLogFile7(fileSystem):
    assert fileSystem.createLogFile("/dir/dir.log") == False



def test_deleteLogFile1(fileSystemWithFiles):
    fileSystemWithFiles.deleteLogFile("/dir1/dir1_1/logFile.log")
    assert fileSystemWithFiles.listOfElements("/dir1/dir1_1") == ['binaryFile.bin']

def test_deleteLogFile2(fileSystem):
    assert fileSystem.deleteLogFile("/dir/log.log") == False



def test_readLogFile1(fileSystemWithFiles):
    fileSystemWithFiles.appendContentToLogFile("/dir1/dir1_1/logFile.log", "some text")
    assert fileSystemWithFiles.readLogFile("/dir1/dir1_1/logFile.log") == "some text"

def test_readLogFile2(fileSystem):
    assert fileSystem.readLogFile("/dir/log.log") == None

def test_readLogFile3(fileSystemWithFiles):
    fileSystemWithFiles.appendContentToLogFile("/dir1/dir1_1/logFile.log", "some text")
    fileSystemWithFiles.appendContentToLogFile("/dir1/dir1_1/logFile.log", "another text")
    assert fileSystem.readLogFile("/dir1/dir1_1/logfile.log") == "some text\n\ranother text"



def test_appendContentToLogFile1(fileSystemWithFiles):
    fileSystemWithFiles.appendContentToLogFile("/dir1/dir1_1/logFile.log", "some text\n\ranother text\n\rsome more text here")
    assert fileSystem.readLogFile("/dir1/dir1_1/logFile.log") == "some text\n\ranother text\n\rsome more text here"

def test_appendContentToLogFile2(fileSystem):
    fileSystem.appendContentToLogFile("/dir/log.log", "some text")
    assert fileSystem.readLogFile("/dir/log.log") == "some text"



def test_moveLogFile1(fileSystemWithFiles):
    fileSystemWithFiles.moveLogFile("/dir1/dir1_1/logFile.log", "/dir1/dir1_3")
    assert fileSystemWithFiles("/dir1/dir1_1") == ['binaryFile.bin']

def test_moveLogFile2(fileSystemWithFiles):
    fileSystemWithFiles.moveLogFile("/dir1/dir1_1/logFile.log", "/dir1/dir1_3")
    assert fileSystemWithFiles.listOfElements("/dir1/dir1_3") == ['logFile.log']
