# 34. Cloud Storage Interface

# Methods:

# upload()
# download()

# Implement:

# GoogleDrive
# Dropbox
import ftplib
from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload(self):
        pass

    @abstractmethod
    def download(self):
        pass

class GoogleDrive(CloudStorage):
    def __init__(self):
        self.ftp = ftplib.FTP("ftp.dlptest.com","dlpuser","xc8IycnK7MvzRBWRR7272j1lr")
        self.ftp.encoding = "utf-8"

    def upload(self, file_path):
        print("Uploading with Google Drive")
        with open(file_path, "rb") as f:
            self.ftp.storbinary("STOR test.txt", f)
        print("Upload done")

    def download(self, remote_file, file_path):
        self.ftp.set_pasv(True)
        print("Downloading with Google Drive")
        with open(file_path, "wb") as f:
            self.ftp.retrbinary(f"RETR {remote_file}", f.write)
        print("Download done")
        self.ftp.close()   



class DropBox(CloudStorage):
    def __init__(self):
        self.ftp = ftplib.FTP("ftp.dlptest.com","dlpuser","xc8IycnK7MvzRBWRR7272j1lr")
        self.ftp.encoding = "utf-8"

    def upload(self, file_path):
        print("Uploading with DropBox")
        with open(file_path, "rb") as f:
            self.ftp.storbinary("STOR test.txt", f)
        print("Upload done")

    def download(self, remote_file, file_path):
        self.ftp.set_pasv(True)
        print("Downloading with DropBox")
        with open(file_path, "wb") as f:
            self.ftp.retrbinary(f"RETR {remote_file}", f.write)
        print("Download done")
        self.ftp.close()

g = GoogleDrive()
g.upload("/home/rt/ITEP-20/Assingment/Python-logic-building/assignment_class/assignment_inhe/test.txt")
g.download("test.txt","text.txt")

    
        