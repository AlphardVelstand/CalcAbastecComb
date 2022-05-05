import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtWidgets import QMessageBox, QApplication, QMainWindow, QFileDialog, QMessageBox

from ui_main import Ui_Form

precoGeral = 0
precoComDesc = 0
qtdLitrosTanque = 0
tanqueCheioGeral = 0
tanqueCheioDesc = 0
difEmReais = 0
litrosPorLitro = 0
percDesc = 0


# Clase principal
class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Calcular Preço Combustivel")

        self.pushButtonCalcular.clicked.connect(self.calcular)
        self.pushButtonSair.clicked.connect(self.sair)
        self.pushButtonLimpar.clicked.connect(self.limpar)


    def calcular(self):
        global precoGeral, precoComDesc, qtdLitrosTanque, tanqueCheioGeral
        global tanqueCheioDesc, difEmReais, litrosPorLitro, percDesc

        # Capturando dados e armazenando nas variaveis
        precoGeral = self.lineEditPosto1.text()
        precoComDesc = self.lineEditPosto2.text()
        qtdLitrosTanque = self.lineEditTanque.text()

        # Convertendo a variável de string para float e armazenando na variavel global
        precoGeral1 = float(precoGeral)
        precoComDesc1 = float(precoComDesc)
        qtdLitrosTanque1 = float(qtdLitrosTanque)

        # Calcular quanto devo abastecer para economizar 1 litro
        tanqueCheioGeral1 = (qtdLitrosTanque1 * precoGeral1)
        tanqueCheioDesc1 = (qtdLitrosTanque1 * precoComDesc1)
        difEmReais1 = (precoGeral1 - precoComDesc1)
        litrosPorLitro1 = (precoGeral1 / difEmReais1)
        percDesc1 = (precoGeral1 - precoComDesc1) * 10  # Achando o percentual de desconto
        custoAbastPt1 = (precoComDesc1 * litrosPorLitro1)
        custoAbastPt2 = (precoGeral1 * litrosPorLitro1)

        # Convertendo de float para string antes de imprimir os dados
        precoGeral = str(precoGeral1)
        precoComDesc = str(precoComDesc1)
        qtdLitrosTanque = str(qtdLitrosTanque1)
        tanqueCheioGeral = str(tanqueCheioGeral1)
        tanqueCheioDesc = str(tanqueCheioDesc1)
        difEmReais = str(difEmReais1)
        litrosPorLitro = str(litrosPorLitro1)
        percDesc = str(percDesc1)

        # Mensagem com resultado
        msgRespo = QMessageBox()
        msgRespo.setIcon(QMessageBox.Information)
        msgRespo.setWindowTitle("Valor: '{:.2f}'".format(precoGeral1))
        msgRespo.setText("Valor para encher o tanque de: {:.0f} Litros há {:.2f} = {:.2f}".format(qtdLitrosTanque1,precoGeral1, tanqueCheioGeral1))
        msgRespo.exec()

        # Mensagem com resultado
        msgRespo2 = QMessageBox()
        msgRespo2.setIcon(QMessageBox.Information)
        msgRespo2.setWindowTitle("Valor: '{:.2f}'".format(precoComDesc1))
        msgRespo2.setText("Valor para encher o tanque de: {:.0f} Litros há: {:.2f} = {:.2f}".format(qtdLitrosTanque1,precoComDesc1, tanqueCheioDesc1))
        msgRespo2.exec()

        # Mensagem com resultado
        msgRespo3 = QMessageBox()
        msgRespo3.setIcon(QMessageBox.Information)
        msgRespo3.setWindowTitle("Diferenção de um posto para outro")
        msgRespo3.setText("Valor da diferença em R$ no litro de um posto para o outro: R$ {:.2f}".format(difEmReais1))
        msgRespo3.exec()

        # Mensagem com resultado
        msgRespo4 = QMessageBox()
        msgRespo4.setIcon(QMessageBox.Information)
        msgRespo4.setWindowTitle("Percentual de desconto")
        msgRespo4.setText("Percentual de desconto: {:.0f}%".format(percDesc1))
        msgRespo4.exec()

        # Mensagem com resultado
        msgRespo5 = QMessageBox()
        msgRespo5.setIcon(QMessageBox.Information)
        msgRespo5.setWindowTitle("Economizando 1 Litro: {:.2f}".format(litrosPorLitro1))
        msgRespo5.setText("Quantos litros abastecer para economizar 1 Litro: {:.2f} Litros".format(litrosPorLitro1))
        msgRespo5.exec()

        # Mensagem com resultado
        msgRespo6 = QMessageBox()
        msgRespo6.setIcon(QMessageBox.Information)
        msgRespo6.setWindowTitle("Custo abastecimento")
        msgRespo6.setText(
            "O custo para abastecer: {:.2f} Litros no valor: {:.2f} será R$ {:.2f} ".format(litrosPorLitro1, precoComDesc1, custoAbastPt1))
        msgRespo6.exec()

        # Mensagem com resultado
        msgRespo7 = QMessageBox()
        msgRespo7.setIcon(QMessageBox.Information)
        msgRespo7.setWindowTitle("Custo abastecimento")
        msgRespo7.setText(
            "O custo para abastecer: {:.2f} Litros no valor: {:.2f} será R$ {:.2f}".format(litrosPorLitro1,precoGeral1,custoAbastPt2))
        msgRespo7.exec()

        self.limpar()


    def limpar(self):
        # Limpando campos de digitação
        self.lineEditPosto1.setText('')
        self.lineEditPosto2.setText('')
        self.lineEditTanque.setText('')
        # Limpando campo resultado
        # tela.listWidgetResultado.clear()

    def sair(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
