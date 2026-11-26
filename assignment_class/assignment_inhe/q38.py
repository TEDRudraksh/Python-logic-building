# 38. File Compression Tool

# Methods:

# compress()

# Implement:

# ZIPCompression
# RARCompression
import gzip
import shutil
from abc import ABC,abstractmethod

class Compression(ABC):

    @abstractmethod
    def compress(self):
        pass


class ZIPCompression(Compression):

    def compress(self,path):
        print("Compress Started..")
        with open(f"{path}", 'rb') as f_in, gzip.open(f"{path}.gz", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

        print("Compress Done")


z = ZIPCompression()
z.compress("test.txt")