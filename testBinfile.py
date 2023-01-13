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



def test_createBinFile1(fileSystem):   #new dir
    fileSystem.createBinFile("/dir", "binaryFile.bin")
    assert fileSystem.listOfElements("/dir") == ['binaryFile.bin']

def test_createBinFile2(fileSystem):   #nested dir
    fileSystem.createBinFile("dir/dir1/dir2", "binaryFile.bin")
    assert fileSystem.listOfElements("dir/dir1/dir2") == ['binaryFile.bin']

def test_createBinFile3(fileSystem):
    assert fileSystem.createBinFile("/", "binaryFile.bin") == False

def test_createBinFile4(fileSystem):   #wrong file type
    assert fileSystem.createBinFile("/dir", "file.bi") == False

def test_createBinFile5(fileSystemFull):   #overflowed file
    assert fileSystemFull.createBinFile("/dir1", "file.bin") == False

def test_createBinFile6(fileSystemWithFiles):   #file already exists
    assert fileSystemWithFiles.createBinFile("/dir1/dir1_1", "binaryFile.bin") == False

def test_createBinFile(fileSystem):   #wrong path
    assert fileSystem.createBinFile("/dir/dir.bin", "file.bin") == False



def test_deleteBinFile1(fileSystemWithFile):
    fileSystemWithFiles.deleteBinFile("/dir1/dir1_1/binaryFile.bin")
    assert fileSystemWithFiles.listOfElements("/dir1/dir1_1") == ['logFile.log']

def test_deleteBinFile2(fileSystem):   #file don`t exist
    assert fileSystem.deleteBinFile("/dir/bin.bin") == False



def test_readBinFile1(filrSystemWithFiles):
    assert fileSystemWithFiles.readBinFile("/dir1/dir1_1/binaryFile.bin") == "bin file content"

def test_readBinFile(fileSystem):   #don`t exist
    assert fileSystem.readBinFile("/dir/bin.bin") == None



def test_moveBinFile1(fileSystemWithFiles):
    fileSystemWithFiles.moveBinFile("/dir1/dir1_1/binaryFile.bin", "/dir1/dir1_2")
    assert fileSystemWithFiles.listOfElements("/dir1/dir1_1") ==['logFile.log']

def test_moveBinFile2(fileSystemWithFiles):
    fileSystemWithFiles.moveBinFile("/dir1/dir1_1/binaryFile.bin", "/dir1/dir1_2")
    assert fileSystemWithFiles.licstOfElements("/dir1/dir1_2") == ['binaryFile.bin', 'bufferFile.buf', 'logFile.log']

def test_moveBinFile3(fileSystemWithFiles):  #file don't exist
    assert fileSystemWithFiles.moveBinFile("/dir1/dir1_2/binaryFile.bin", "/dir1/dir1_1") == False

def test_moveBinFile4(fileSystemWithFiles):   #already exist
    fileSystemWithFiles.createBinFile("/dir1/dir1_2", "binaryFile.bin")
    assert fileSystemWithFiles.moveBinFile("/dir1/dir1_1/binaryFile.bin", "/dir1/dir1_2") == False