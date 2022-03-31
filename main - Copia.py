import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

precoGeral = 0
precoComDesc = 0
qtdLitrosTanque = 0
tanqueCheioGeral = 0
tanqueCheioDesc = 0
difEmReais = 0
litrosPorLitro = 0
percDesc = 0

def calcular():
    global precoGeral, precoComDesc, qtdLitrosTanque, tanqueCheioGeral
    global tanqueCheioDesc, difEmReais, litrosPorLitro, percDesc

    #Capturando dados e armazenando nas variaveis
    precoGeral = tela.lineEditPosto1.text()
    precoComDesc = tela.lineEditPosto2.text()
    qtdLitrosTanque = tela.lineEditTanque.text()
    #Convertendo a variável de string para float e armazenando na variavel global
    precoGeral1 = float(precoGeral)
    precoComDesc1 = float(precoComDesc)
    qtdLitrosTanque1 = float(qtdLitrosTanque)

    # Calcular quanto devo abastecer para economizar 1 litro
    tanqueCheioGeral1 = (qtdLitrosTanque1 * precoGeral1)
    tanqueCheioDesc1 = (qtdLitrosTanque1 * precoComDesc1)
    difEmReais1 = (precoGeral1 - precoComDesc1)
    litrosPorLitro1 = (precoGeral1 / difEmReais1)
    percDesc1 = (precoGeral1 - precoComDesc1) * 10  # Achando o percentual de desconto

    #Convertendo de float para string antes de imprimir os dados
    precoGeral = str(precoGeral1)
    precoComDesc = str(precoComDesc1)
    qtdLitrosTanque = str(qtdLitrosTanque1)
    tanqueCheioGeral = str(tanqueCheioGeral1)
    tanqueCheioDesc = str(tanqueCheioDesc1)
    difEmReais = str(difEmReais1)
    litrosPorLitro = str(litrosPorLitro1)
    percDesc = str(percDesc1)

    #tipo da variavel
    #Exibindo o tipo da variavel
    print(type(precoGeral))
    print(type(precoComDesc))
    print(type(qtdLitrosTanque))
    print('=-'*20)
    print(type(tanqueCheioGeral))
    print(type(tanqueCheioDesc))
    print(type(difEmReais))
    print(type(litrosPorLitro))
    print(type(percDesc))
    print('%'*40)

    #print(precoGeral, precoComDesc, qtdLitrosTanque, tanqueCheioGeral,tanqueCheioDesc, difEmReais, litrosPorLitro, percDesc)


    #Apresentando os dados no ListWidget
    tela.listWidgetResultado.addItem(precoGeral)
    tela.listWidgetResultado.addItem(precoComDesc)
    tela.listWidgetResultado.addItem(qtdLitrosTanque)

    limpar()


def limpar():
    #Limpando campos de digitação
    tela.lineEditPosto1.setText('')
    tela.lineEditPosto2.setText('')
    tela.lineEditTanque.setText('')
    #Limpando campo resultado
    #tela.listWidgetResultado.clear()

def sair(self):
    sys.exit()

app = QtWidgets.QApplication([])
tela = uic.loadUi("Tela.ui")

tela.pushButtonCalcular.clicked.connect(calcular)
tela.pushButtonSair.clicked.connect(sair)
tela.pushButtonLimpar.clicked.connect(limpar)

tela.show()
app.exec()