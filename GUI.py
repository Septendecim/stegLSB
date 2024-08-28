# https://habr.com/ru/company/skillfactory/blog/599599/


from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6 import QtGui
from PyQt5 import QtWidgets
from LSBMainWindow import Ui_MainWindow
from PySide6.QtCore import SIGNAL, QObject
from numpy import asarray
from PIL import Image
import sewar

import LSB
import Hamming

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.containerFilePath = ''
        self.messageFilePath = ''
        self.isHammingCode = False
        
        # Вкладка встраивания
        self.ui.Container_fileChoose_button.clicked.connect(self.getContainerFileName)
        self.ui.Message_fileChoose_button.clicked.connect(self.getMessageFileName)
        
        self.ui.Embed_button.clicked.connect(self.embedding)
        
        # Вкладка извлечения
        self.ui.Container_fileChoose_button_ext.clicked.connect(self.getContainerFileName_ext)
        self.ui.Message_fileChoose_button_ext.clicked.connect(self.getMessageFileName_ext)
        
        self.ui.Extract_button.clicked.connect(self.extract)

    def getFileName(self):
        app = QtWidgets.QApplication([])
        myFileDialog = QFileDialog()
        return myFileDialog.getOpenFileName()[0]
    
    def setContainerImage(self):
        pixmap = QtGui.QPixmap(self.containerFilePath)
        self.ui.ShowImage_label.setPixmap(pixmap)
    
    def setContainerImage_ext(self):
        pixmap = QtGui.QPixmap(self.containerFilePath)
        self.ui.ShowImage_label_ext.setPixmap(pixmap)
    
    def window(self, cont_len, msg_len):
        app = QtWidgets.QApplication([])
        widget = QtWidgets.QWidget()

        message = "Длина сообщения (биты)\t\t" + str(msg_len)
        message += "\nГлубина встраивания (биты)\t" + str(LSB.deep)
        message += "\nДля встраивания необходимо байт\t" + str(msg_len/LSB.deep)
        message += "\nОбъем контейнера (байты)\t" + str(cont_len)
        message += "\n\nСООБЩЕНИЕ НЕ ВМЕЩАЕТСЯ"
        
        textLabel = QtWidgets.QLabel(widget)
        textLabel.setText(message)
        textLabel.move(10,5)

        widget.setGeometry(350,350,320,200)
        widget.setWindowTitle("Внимание")
        widget.show()
        app.exec_()
    
    # Вкладка встраивания
    
    def embedding(self):
        
        # подготовка сообщения
        msg_path = self.messageFilePath
        
        # Открыть файл сообщения
        with open(msg_path, 'rb') as f:
            msg_data = bytearray(f.read())                      # получаем всю картинку
            bin_msg_list = LSB.bytearrayToBinlist(msg_data)     # конвертируем в двоичный формат ['01101010', '00110100', ...]
            bin_msg = ''.join(bin_msg_list)                     # соединяем в строку '010011000110111101110010...'
        
        
        # подготовка контейнера
        cont_path = self.containerFilePath
        img1 = asarray(Image.open(cont_path))                   # картинка до вставки
        
        # Открыть файл картинки
        with open(cont_path, 'rb') as f:
            cont_data = bytearray(f.read())                     # получаем всю картинку
            container = cont_data[LSB.offset:]                  # откидываем метаинформацию
            bin_cont = LSB.bytearrayToBinlist(container)        # конвертируем в двоичный формат ['01101010', '00110100', ...]
        
        
        # Код Хэмминга
        if(self.ui.Message_hammingCode_checkBox.isChecked()): bin_msg = Hamming.encode(bin_msg)
        
        
        # проверка вместимости
        if(len(bin_msg)/LSB.deep > len(bin_cont)):  self.window(len(bin_cont), len(bin_msg))
        
        # вставка сообщения в контейнер
        else:
            enc_container = LSB.lsb_enc(bin_cont, bin_msg, LSB.deep)
            enc_container = LSB.binlistToBytearray(enc_container)       # результат встраивания отформатировать в bytearray
            enc_data = cont_data[:LSB.offset] + enc_container           # соединить контейнер с пропущенной метой
            with open(cont_path, "wb") as f:
                f.write(enc_data)
                f.close()
        
        
        
        img2 = asarray(Image.open(cont_path))
        
        # метрики - cont_data vs. enc_data
        self.ui.PSNR_info.setText(str(sewar.psnr(img1, img2)))
        self.ui.SSIM_info.setText(str(sewar.ssim(img1, img2)[0]))
        self.ui.Metric1_info.setText(str(sewar.uqi(img1, img2)))
        self.ui.Metric2_info.setText(str(sewar.scc(img1, img2)))
        self.ui.Metric3_info.setText(str(sewar.mse(img1, img2)))

        
    def getContainerFileName(self):
        self.containerFilePath = self.getFileName()
        ext = self.containerFilePath[len(self.containerFilePath)-4:]
        if ext ==".bmp" :
            self.ui.Container_filePath_line.setText(self.containerFilePath)
            self.setContainerImage()
        else:
            self.ui.Container_filePath_line.setText("Выберите файл .bmp")
        
    def getMessageFileName(self):
        self.messageFilePath = self.getFileName()
        self.ui.Message_filePath_line.setText(self.messageFilePath)



    # Вкладка извлечения

    def extract(self):
        
        # подготовка контейнера
        cont_path = self.containerFilePath
                
        # Открыть файл картинки
        with open(cont_path, 'rb') as f:
            cont_data = bytearray(f.read())                     # получаем всю картинку
            container = cont_data[LSB.offset:]                  # откидываем метаинформацию
            bin_cont = LSB.bytearrayToBinlist(container)        # конвертируем в двоичный формат ['01101010', '00110100', ...]
        
        # извлечь сообщение    
            ext_message = LSB.lsb_dec(bin_cont, LSB.deep)       # возвращает bitstring
            
        # Код Хэмминга
        if(self.ui.Message_hammingCode_checkBox.isChecked()): ext_message = Hamming.decode(ext_message)
        
        # выдача результата
        msg_path = self.messageFilePath
        ext_message = LSB.bitstrToBytearray(ext_message)
        with open(msg_path, "wb") as f:
                f.write(ext_message)
    
    
    def getContainerFileName_ext(self):
        self.containerFilePath = self.getFileName()
        ext = self.containerFilePath[len(self.containerFilePath)-4:]
        if ext ==".bmp" :
            self.ui.Container_filePath_line_ext.setText(self.containerFilePath)
            self.setContainerImage_ext()
        else:
            self.ui.Container_filePath_line_ext.setText("Выберите файл .bmp")
        
    def getMessageFileName_ext(self):
        self.messageFilePath = self.getFileName()
        self.ui.Message_filePath_line_ext.setText(self.messageFilePath)
        
