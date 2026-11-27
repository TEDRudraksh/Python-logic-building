# 13. File Export System
# Problem Statement

# Application exports files in multiple formats.

# Create:

# abstract class Exporter

# Child:

# PDFExporter
# ExcelExporter
# CSVExporter

from abc import ABC,abstractmethod

class Exporter(ABC):

    @abstractmethod
    def export(self):
        pass


class PDFExporter(Exporter):

    def export(self):
            try:
                with open("export.pdf","xb") as f:
                     data = 0

            except OSError as e:
                print(e)

class ExcelExporter(Exporter):

    def export(self):
            try:
                with open("export.xlsx","xb") as f:
                     data = 0
                     
            except OSError as e:
                print(e)

class CSVExporter(Exporter):

    def export(self):
            try:
                with open("export.csv","xb") as f:
                     data = 0
                     
            except OSError as e:
                print(e)


p = PDFExporter()
p.export()