
from openpyxl import Workbook


class Excel:
    def __init__(self):
        self.workbook = Workbook()
        self.arquivo = self.workbook.active        

    def setTitle(self, title):
        self.arquivo.title = title

    def setHeader(self, headers):
        self.arquivo.append(headers)

    def setBody(self, body):
        self.arquivo.append(body)

    def setValueInPosition(self, row, column, value):
        self.arquivo.cell(row=row, column=column, value=value)

    def setFunctionInPosition(self, position, func):
        self.arquivo[position] = func

    def save(self, nomeArquivo):
        self.workbook.save('save/'+nomeArquivo)




