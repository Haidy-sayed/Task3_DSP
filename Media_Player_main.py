
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QColorDialog, QFileDialog, QFrame, QWidget, QInputDialog, QLineEdit,QComboBox
import os
import numpy as np
from PyQt5.QtWidgets import QMessageBox
import sys 
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor ,QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph.graphicsItems.ScatterPlotItem import Symbols
from pyqtgraph.graphicsItems.ImageItem import ImageItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import cv2
import io
from numpy.fft import fft, fftfreq, ifft
from scipy.fftpack import fft, ifft
from scipy import signal
import cmath
from scipy.io.wavfile import write
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph.exporters
from fpdf import FPDF
import statistics
from pyqtgraph import PlotWidget
import pyqtgraph
from pyqtgraph import *
import pyqtgraph as pg
from pyqtgraph import PlotWidget, PlotItem
#from matplotlib.pyplot import draw
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QColorDialog, QFileDialog, QFrame, QWidget, QInputDialog, QLineEdit,QComboBox
import os
import numpy as np
from PyQt5.QtWidgets import QMessageBox
import sys 
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph.graphicsItems.ScatterPlotItem import Symbols
from pyqtgraph.graphicsItems.ImageItem import ImageItem
from matplotlib.figure import Figure
import io
from numpy.fft import fft, fftfreq, ifft
from scipy.fftpack import fft, ifft
from scipy import signal
import cmath
import cv2

#libraries to play audio
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import librosa as lr
from scipy.io import wavfile
import scipy.io
import sounddevice as sd
from pydub import AudioSegment
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph.exporters
from fpdf import FPDF
import statistics
from pyqtgraph import PlotWidget
import pyqtgraph
from pyqtgraph import *
import pyqtgraph as pg
from PyQt5 import QtMultimedia
from pyqtgraph import PlotWidget, PlotItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.layoutWidget = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 0, 1000, 518))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.layoutWidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 300))
        self.widget.setObjectName("widget")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setGeometry(QtCore.QRect(0, 10, 961, 291))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.MainGraph = pyqtgraph.GraphicsLayoutWidget(self.splitter)
        self.MainGraph.setMinimumSize(QtCore.QSize(500, 0))
        self.MainGraph.setObjectName("MainGraph")   
        self.MainSpectroControls = QtWidgets.QWidget(self.splitter)
        self.MainSpectroControls.setMinimumSize(QtCore.QSize(60, 0))
        self.MainSpectroControls.setMaximumSize(QtCore.QSize(65, 16777215))
        self.MainSpectroControls.setObjectName("MainSpectroControls")
        self.MainControl = QtWidgets.QToolBox(self.MainSpectroControls)
        self.MainControl.setGeometry(QtCore.QRect(0, 2, 69, 281))
        self.MainControl.setObjectName("MainControl")
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setGeometry(QtCore.QRect(0, 0, 69, 219))
        self.page_13.setObjectName("page_13")
        self.SpectroButton = QtWidgets.QPushButton(self.page_13)
        self.SpectroButton.setGeometry(QtCore.QRect(0, 20, 61, 23))
        self.SpectroButton.setObjectName("SpectroButton")
        self.PlayButton = QtWidgets.QPushButton(self.page_13)
        self.PlayButton.setGeometry(QtCore.QRect(0, 60, 61, 23))
        self.PlayButton.setObjectName("PlayButton")
        self.OpenFileButton = QtWidgets.QPushButton(self.page_13)
        self.OpenFileButton.setGeometry(QtCore.QRect(0, 0, 61, 23))
      #  self.OpenFileButton.setStyleSheet("radius:\"3\";")
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.PauseButton = QtWidgets.QPushButton(self.page_13)
        self.PauseButton.setGeometry(QtCore.QRect(0, 80, 61, 23))
        self.PauseButton.setObjectName("PauseButton")
        self.FasterButton = QtWidgets.QPushButton(self.page_13)
        self.FasterButton.setGeometry(QtCore.QRect(0, 140, 61, 23))
        self.FasterButton.setObjectName("FasterButton")
        self.SlowerButton = QtWidgets.QPushButton(self.page_13)
        self.SlowerButton.setGeometry(QtCore.QRect(0, 120, 61, 23))
        self.SlowerButton.setObjectName("SlowerButton")
        self.ZoomInButton = QtWidgets.QPushButton(self.page_13)
        self.ZoomInButton.setGeometry(QtCore.QRect(0, 180, 61, 23))
        self.ZoomInButton.setObjectName("ZoomInButton")
        self.ZoomOutButton = QtWidgets.QPushButton(self.page_13)
        self.ZoomOutButton.setGeometry(QtCore.QRect(0, 200, 61, 23))
        self.ZoomOutButton.setObjectName("ZoomOutButton")
        self.MainControl.addItem(self.page_13, "")
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_14.setObjectName("page_14")
        self.AudioVolumeSlider = QtWidgets.QSlider(self.page_14)
        self.AudioVolumeSlider.setGeometry(QtCore.QRect(20, 20, 22, 61))     
        self.AudioVolumeSlider.setMaximum(100)
        self.AudioVolumeSlider.setMinimum(0)
        self.AudioVolumeSlider.setValue(50) 
        self.AudioVolumeSlider.setOrientation(QtCore.Qt.Vertical)
        self.AudioVolumeSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.AudioVolumeSlider.setTickInterval(1)
        self.AudioVolumeSlider.setObjectName("AudioVolumeSlider") 
        self.MainVolumeLabel = QtWidgets.QLabel(self.page_14)
        self.MainVolumeLabel.setGeometry(QtCore.QRect(10, -10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.MainVolumeLabel.setFont(font)
        self.MainVolumeLabel.setObjectName("MainVolumeLabel")
        self.SpectroLabel = QtWidgets.QLabel(self.page_14)
        self.SpectroLabel.setGeometry(QtCore.QRect(10, 90, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SpectroLabel.setFont(font)
        self.SpectroLabel.setObjectName("SpectroLabel")
        self.PaletteComboBox = QtWidgets.QComboBox(self.page_14)
        self.PaletteComboBox.setGeometry(QtCore.QRect(0, 120, 61, 22))
        self.PaletteComboBox.setObjectName("PaletteComboBox")
        self.PaletteComboBox.addItem("")
        self.Spec_minSLider = QtWidgets.QSlider(self.page_14)
        self.Spec_minSLider.setGeometry(QtCore.QRect(0, 162, 61, 20))
        self.Spec_minSLider.setMaximum(255)
        self.Spec_minSLider.setOrientation(QtCore.Qt.Horizontal)
        self.Spec_minSLider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Spec_minSLider.setObjectName("Spec_minSLider")
        self.Spec_MaxSlider = QtWidgets.QSlider(self.page_14)
        self.Spec_MaxSlider.setGeometry(QtCore.QRect(0, 202, 61, 20))
        self.Spec_MaxSlider.setMaximum(255)
        self.Spec_MaxSlider.setTracking(True)
        self.Spec_MaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Spec_MaxSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Spec_MaxSlider.setObjectName("Spec_MaxSlider")
        self.MainControl.addItem(self.page_14, "")
        self.SpectroChannel = PlotWidget(self.splitter)
        self.SpectroChannel.setObjectName("SpectroChannel")
        self.verticalLayout.addWidget(self.widget)
        self.Equalizer_5 = QtWidgets.QWidget(self.layoutWidget)
        self.Equalizer_5.setObjectName("Equalizer_5")
        self.EqualizerControl = QtWidgets.QToolBox(self.Equalizer_5)
        self.EqualizerControl.setGeometry(QtCore.QRect(10, 20, 91, 171))
        self.EqualizerControl.setObjectName("EqualizerControl")
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setGeometry(QtCore.QRect(0, 0, 91, 109))
        self.page_21.setObjectName("page_21")
        self.ImageOFInstHolder = QtWidgets.QLabel(self.page_21)
        self.ImageOFInstHolder.setGeometry(QtCore.QRect(6, 2, 81, 111))
        self.ImageOFInstHolder.setObjectName("ImageOFInstHolder")
        self.EqualizerControl.addItem(self.page_21, "")
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_22.setObjectName("page_22")
        self.Instrument_8 = QtWidgets.QPushButton(self.page_22)
        self.Instrument_8.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.Instrument_8.setObjectName("Instrument_8")
        self.Instrument_9 = QtWidgets.QPushButton(self.page_22)
        self.Instrument_9.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.Instrument_9.setObjectName("Instrument_9")
        self.Instrument_10 = QtWidgets.QPushButton(self.page_22)
        self.Instrument_10.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.Instrument_10.setObjectName("Instrument_10")
        self.EqualizerControl.addItem(self.page_22, "")
        self.EqualizerVolume = QtWidgets.QSlider(self.Equalizer_5)
        self.EqualizerVolume.setGeometry(QtCore.QRect(180, 20, 22, 141))
        self.EqualizerVolume.setMaximum(10)
        self.EqualizerVolume.setOrientation(QtCore.Qt.Vertical)
        self.EqualizerVolume.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.EqualizerVolume.setObjectName("EqualizerVolume")
        self.EqualizerGain = QtWidgets.QSlider(self.Equalizer_5)
        self.EqualizerGain.setGeometry(QtCore.QRect(280, 20, 22, 141))
        self.EqualizerGain.setMaximum(10)
        self.EqualizerGain.setOrientation(QtCore.Qt.Vertical)
        self.EqualizerGain.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.EqualizerGain.setObjectName("EqualizerGain")
        self.verticalSlider_24 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_24.setGeometry(QtCore.QRect(380, 20, 22, 141))
        self.verticalSlider_24.setMaximum(10)
        self.verticalSlider_24.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_24.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_24.setObjectName("verticalSlider_24")
        self.verticalSlider_25 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_25.setGeometry(QtCore.QRect(480, 20, 22, 141))
        self.verticalSlider_25.setMaximum(10)
        self.verticalSlider_25.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_25.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_25.setObjectName("verticalSlider_25")
        self.verticalSlider_26 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_26.setGeometry(QtCore.QRect(580, 20, 22, 141))
        self.verticalSlider_26.setMaximum(10)
        self.verticalSlider_26.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_26.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_26.setObjectName("verticalSlider_26")
        self.verticalSlider_27 = QtWidgets.QSlider(self.Equalizer_5)
        self.verticalSlider_27.setGeometry(QtCore.QRect(680, 20, 22, 141))
        self.verticalSlider_27.setMaximum(10)
        self.verticalSlider_27.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_27.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_27.setObjectName("verticalSlider_27")
        self.VolumeLabel_19 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_19.setGeometry(QtCore.QRect(170, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_19.setFont(font)
        self.VolumeLabel_19.setObjectName("VolumeLabel_19")
        self.VolumeLabel_20 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_20.setGeometry(QtCore.QRect(280, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_20.setFont(font)
        self.VolumeLabel_20.setObjectName("VolumeLabel_20")
        self.VolumeLabel_21 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_21.setGeometry(QtCore.QRect(380, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_21.setFont(font)
        self.VolumeLabel_21.setObjectName("VolumeLabel_21")
        self.Equalizer_6 = QtWidgets.QWidget(self.Equalizer_5)
        self.Equalizer_6.setGeometry(QtCore.QRect(420, 180, 800, 210))
        self.Equalizer_6.setObjectName("Equalizer_6")
        self.verticalSlider_28 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_28.setGeometry(QtCore.QRect(180, 20, 22, 141))
        self.verticalSlider_28.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_28.setObjectName("verticalSlider_28")
        self.verticalSlider_29 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider_29.setGeometry(QtCore.QRect(280, 20, 22, 141))
        self.verticalSlider_29.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_29.setObjectName("verticalSlider_29")
        self.verticalSlider0 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider0.setGeometry(QtCore.QRect(380, 20, 22, 141))
        self.verticalSlider0.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider0.setObjectName("verticalSlider0")
        self.verticalSlider1 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider1.setGeometry(QtCore.QRect(480, 20, 22, 141))
        self.verticalSlider1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider1.setObjectName("verticalSlider1")
        self.verticalSlider2 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider2.setGeometry(QtCore.QRect(580, 20, 22, 141))
        self.verticalSlider2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider2.setObjectName("verticalSlider2")
        self.verticalSlider3 = QtWidgets.QSlider(self.Equalizer_6)
        self.verticalSlider3.setGeometry(QtCore.QRect(680, 20, 22, 141))
        self.verticalSlider3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider3.setObjectName("verticalSlider3")
        self.VolumeLabel_22 = QtWidgets.QLabel(self.Equalizer_6)
        self.VolumeLabel_22.setGeometry(QtCore.QRect(170, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_22.setFont(font)
        self.VolumeLabel_22.setObjectName("VolumeLabel_22")
        self.VolumeLabel_23 = QtWidgets.QLabel(self.Equalizer_6)
        self.VolumeLabel_23.setGeometry(QtCore.QRect(280, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_23.setFont(font)
        self.VolumeLabel_23.setObjectName("VolumeLabel_23")
        self.VolumeLabel_24 = QtWidgets.QLabel(self.Equalizer_6)
        self.VolumeLabel_24.setGeometry(QtCore.QRect(380, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_24.setFont(font)
        self.VolumeLabel_24.setObjectName("VolumeLabel_24")
        self.VolumeLabel_25 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_25.setGeometry(QtCore.QRect(470, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_25.setFont(font)
        self.VolumeLabel_25.setObjectName("VolumeLabel_25")
        self.VolumeLabel_26 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_26.setGeometry(QtCore.QRect(570, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_26.setFont(font)
        self.VolumeLabel_26.setObjectName("VolumeLabel_26")
        self.VolumeLabel_27 = QtWidgets.QLabel(self.Equalizer_5)
        self.VolumeLabel_27.setGeometry(QtCore.QRect(670, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.VolumeLabel_27.setFont(font)
        self.VolumeLabel_27.setObjectName("VolumeLabel_27")
        self.verticalLayout.addWidget(self.Equalizer_5)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_6)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 0, 941, 591))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_19 = QtWidgets.QWidget()
        self.page_19.setObjectName("page_19")
        self.piano = QtWidgets.QPushButton(self.page_19)
        self.piano.setGeometry(QtCore.QRect(60, 20, 231, 241))
        self.piano.setText("")
        self.piano.setObjectName("piano")
        self.textEdit = QtWidgets.QTextEdit(self.page_19)
        self.textEdit.setGeometry(QtCore.QRect(360, 230, 241, 71))
        self.textEdit.setObjectName("textEdit")
        self.drums = QtWidgets.QPushButton(self.page_19)
        self.drums.setGeometry(QtCore.QRect(360, 340, 231, 241))
        self.drums.setText("")
        self.drums.setObjectName("drums")
        self.bongos = QtWidgets.QPushButton(self.page_19)
        self.bongos.setGeometry(QtCore.QRect(670, 20, 231, 241))
        self.bongos.setText("")
        self.bongos.setObjectName("bongos")
        self.stackedWidget.addWidget(self.page_19)
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setObjectName("page_20")
        self.label = QtWidgets.QLabel(self.page_20)
        self.label.setGeometry(QtCore.QRect(200, 200, 461, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/hp/anaconda3/envs/py38/Library/bin/pianoplay2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pianoA = QtWidgets.QPushButton(self.page_20)
        self.pianoA.setGeometry(QtCore.QRect(200, 360, 31, 28))
        self.pianoA.setObjectName("pianoA")
        self.pianoS = QtWidgets.QPushButton(self.page_20)
        self.pianoS.setGeometry(QtCore.QRect(250, 360, 31, 28))
        self.pianoS.setObjectName("pianoS")
        self.pianoD = QtWidgets.QPushButton(self.page_20)
        self.pianoD.setGeometry(QtCore.QRect(300, 360, 31, 28))
        self.pianoD.setObjectName("pianoD")
        self.pianoF = QtWidgets.QPushButton(self.page_20)
        self.pianoF.setGeometry(QtCore.QRect(340, 360, 31, 28))
        self.pianoF.setObjectName("pianoF")
        self.pianoG = QtWidgets.QPushButton(self.page_20)
        self.pianoG.setGeometry(QtCore.QRect(390, 360, 31, 28))
        self.pianoG.setObjectName("pianoG")
        self.pianoH = QtWidgets.QPushButton(self.page_20)
        self.pianoH.setGeometry(QtCore.QRect(440, 360, 31, 28))
        self.pianoH.setObjectName("pianoH")
        self.pianoJ = QtWidgets.QPushButton(self.page_20)
        self.pianoJ.setGeometry(QtCore.QRect(480, 360, 31, 28))
        self.pianoJ.setObjectName("pianoJ")
        self.pianoK = QtWidgets.QPushButton(self.page_20)
        self.pianoK.setGeometry(QtCore.QRect(530, 360, 31, 28))
        self.pianoK.setObjectName("pianoK")
        self.pianoL = QtWidgets.QPushButton(self.page_20)
        self.pianoL.setGeometry(QtCore.QRect(580, 360, 31, 28))
        self.pianoL.setObjectName("pianoL")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_20)
        self.pushButton_13.setGeometry(QtCore.QRect(620, 360, 31, 28))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pianoE = QtWidgets.QPushButton(self.page_20)
        self.pianoE.setGeometry(QtCore.QRect(230, 280, 31, 28))
        self.pianoE.setObjectName("pianoE")
        self.pianoR = QtWidgets.QPushButton(self.page_20)
        self.pianoR.setGeometry(QtCore.QRect(280, 280, 31, 28))
        self.pianoR.setObjectName("pianoR")
        self.pianoT = QtWidgets.QPushButton(self.page_20)
        self.pianoT.setGeometry(QtCore.QRect(370, 280, 31, 28))
        self.pianoT.setObjectName("pianoT")
        self.pianoY = QtWidgets.QPushButton(self.page_20)
        self.pianoY.setGeometry(QtCore.QRect(420, 280, 31, 28))
        self.pianoY.setObjectName("pianoY")
        self.pianoU = QtWidgets.QPushButton(self.page_20)
        self.pianoU.setGeometry(QtCore.QRect(550, 280, 31, 28))
        self.pianoU.setObjectName("pianoU")
        self.pianoI = QtWidgets.QPushButton(self.page_20)
        self.pianoI.setGeometry(QtCore.QRect(460, 280, 31, 28))
        self.pianoI.setObjectName("pianoI")
        self.pianoO = QtWidgets.QPushButton(self.page_20)
        self.pianoO.setGeometry(QtCore.QRect(600, 280, 31, 28))
        self.pianoO.setObjectName("pianoO")
        self.pushButton = QtWidgets.QPushButton(self.page_20)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page_20)
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.label_2 = QtWidgets.QLabel(self.page_23)
        self.label_2.setGeometry(QtCore.QRect(190, 130, 421, 281))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.page_23)
        self.label.setGeometry(QtCore.QRect(160, 150, 531, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/hp/anaconda3/envs/py38/Library/bin/bangos1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_23)
        self.pushButton_21.setGeometry(QtCore.QRect(540, 210, 31, 28))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.page_23)
        self.pushButton_22.setGeometry(QtCore.QRect(270, 200, 31, 28))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_23)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page_23)
        self.page_24 = QtWidgets.QWidget()
        self.page_24.setObjectName("page_24")
        self.label_4 = QtWidgets.QLabel(self.page_24)
        self.label_4.setGeometry(QtCore.QRect(150, 120, 671, 391))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/hp/anaconda3/envs/py38/Library/bin/blog-graphics-labeled-drum-kit.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_24 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_24.setGeometry(QtCore.QRect(540, 380, 31, 31))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_27 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_27.setGeometry(QtCore.QRect(580, 240, 31, 31))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_23 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_23.setGeometry(QtCore.QRect(260, 320, 31, 31))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_25 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_25.setGeometry(QtCore.QRect(390, 240, 31, 31))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_28 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_28.setGeometry(QtCore.QRect(660, 320, 31, 31))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton0 = QtWidgets.QPushButton(self.page_24)
        self.pushButton0.setGeometry(QtCore.QRect(360, 340, 31, 31))
        self.pushButton0.setObjectName("pushButton0")
        self.pushButton_29 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_29.setGeometry(QtCore.QRect(290, 190, 31, 31))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_26 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_26.setGeometry(QtCore.QRect(480, 250, 31, 31))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton1 = QtWidgets.QPushButton(self.page_24)
        self.pushButton1.setGeometry(QtCore.QRect(460, 350, 31, 31))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_24)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page_24)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #self.shortcut1 = QShortcut(QKeySequence('A') , self)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.MainControl.setCurrentIndex(0)
        self.EqualizerControl.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SpectroButton.setText(_translate("MainWindow", "Spectro"))
        self.PlayButton.setText(_translate("MainWindow", "Play"))
        self.OpenFileButton.setText(_translate("MainWindow", "Open File"))
        self.PauseButton.setText(_translate("MainWindow", "Pause"))
        self.FasterButton.setText(_translate("MainWindow", "Faster"))
        self.SlowerButton.setText(_translate("MainWindow", "Slower"))
        self.ZoomInButton.setText(_translate("MainWindow", "Zoom in"))
        self.ZoomOutButton.setText(_translate("MainWindow", "Zoom out"))
        self.MainControl.setItemText(self.MainControl.indexOf(self.page_13), _translate("MainWindow", "Page 1"))
        self.MainVolumeLabel.setText(_translate("MainWindow", "Volume"))
        self.SpectroLabel.setText(_translate("MainWindow", "Spectro"))
        self.PaletteComboBox.setItemText(0, _translate("MainWindow", "Palettes"))
        self.MainControl.setItemText(self.MainControl.indexOf(self.page_14), _translate("MainWindow", "Page 2"))
        self.ImageOFInstHolder.setText(_translate("MainWindow", "Image of Instr."))
        self.EqualizerControl.setItemText(self.EqualizerControl.indexOf(self.page_21), _translate("MainWindow", "Page 1"))
        self.Instrument_8.setText(_translate("MainWindow", "Inst 1"))
        self.Instrument_9.setText(_translate("MainWindow", "Inst 2"))
        self.Instrument_10.setText(_translate("MainWindow", "Inst 3"))
        self.EqualizerControl.setItemText(self.EqualizerControl.indexOf(self.page_22), _translate("MainWindow", "Page 2"))
        self.VolumeLabel_19.setText(_translate("MainWindow", "Volume"))
        self.VolumeLabel_20.setText(_translate("MainWindow", "Gain"))
        self.VolumeLabel_21.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_22.setText(_translate("MainWindow", "Volume"))
        self.VolumeLabel_23.setText(_translate("MainWindow", "Gain"))
        self.VolumeLabel_24.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_25.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_26.setText(_translate("MainWindow", "Label3"))
        self.VolumeLabel_27.setText(_translate("MainWindow", "Label3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Tab 1"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Choose an instrument to play</span></p></body></html>"))
        self.pianoA.setText(_translate("MainWindow", "A"))
        self.pianoA.setShortcut(_translate("MainWindow", "A"))
        self.pianoS.setText(_translate("MainWindow", "S"))
        self.pianoS.setShortcut(_translate("MainWindow", "S"))
        self.pianoD.setText(_translate("MainWindow", "D"))
        self.pianoD.setShortcut(_translate("MainWindow", "D"))
        self.pianoF.setText(_translate("MainWindow", "F"))
        self.pianoF.setShortcut(_translate("MainWindow", "F"))
        self.pianoG.setText(_translate("MainWindow", "G"))
        self.pianoG.setShortcut(_translate("MainWindow", "G"))
        self.pianoH.setText(_translate("MainWindow", "H"))
        self.pianoH.setShortcut(_translate("MainWindow", "H"))
        self.pianoJ.setText(_translate("MainWindow", "J"))
        self.pianoJ.setShortcut(_translate("MainWindow", "J"))
        self.pianoK.setText(_translate("MainWindow", "K"))
        self.pianoK.setShortcut(_translate("MainWindow", "K"))
        self.pianoL.setText(_translate("MainWindow", "L"))
        self.pushButton_13.setText(_translate("MainWindow", ":"))
        self.pushButton_13.setShortcut(_translate("MainWindow", ":"))
        self.pianoE.setText(_translate("MainWindow", "E"))
        self.pianoE.setShortcut(_translate("MainWindow", "E"))
        self.pianoR.setText(_translate("MainWindow", "R"))
        self.pianoR.setShortcut(_translate("MainWindow", "R"))
        self.pianoT.setText(_translate("MainWindow", "T"))
        self.pianoT.setShortcut(_translate("MainWindow", "T"))
        self.pianoY.setText(_translate("MainWindow", "Y"))
        self.pianoY.setShortcut(_translate("MainWindow", "Y"))
        self.pianoU.setText(_translate("MainWindow", "U"))
        self.pianoU.setShortcut(_translate("MainWindow", "U"))
        self.pianoI.setText(_translate("MainWindow", "I"))
        self.pianoI.setShortcut(_translate("MainWindow", "I"))
        self.pianoO.setText(_translate("MainWindow", "O"))
        self.pianoO.setShortcut(_translate("MainWindow", "O"))
        self.pushButton.setText(_translate("MainWindow", "back to menu"))
        self.pushButton_21.setText(_translate("MainWindow", "W"))
        self.pushButton_22.setText(_translate("MainWindow", "Q"))
        self.pushButton_4.setText(_translate("MainWindow", "back to menu"))
        self.pushButton_24.setText(_translate("MainWindow", "C"))
        self.pushButton_27.setText(_translate("MainWindow", "B"))
        self.pushButton_23.setText(_translate("MainWindow", "Z"))
        self.pushButton_25.setText(_translate("MainWindow", "M"))
        self.pushButton_28.setText(_translate("MainWindow", "V"))
        self.pushButton0.setText(_translate("MainWindow", "X"))
        self.pushButton_29.setText(_translate("MainWindow", ","))
        self.pushButton_26.setText(_translate("MainWindow", "N"))
        self.pushButton1.setText(_translate("MainWindow", "/"))
        self.pushButton_5.setText(_translate("MainWindow", "back to menu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Tab 2"))
        self.piano.clicked.connect(lambda: self.pianoPlay())
        self.bongos.clicked.connect(lambda: self.BongosPlay())
        self.drums.clicked.connect(lambda: self.drumsPlay())
        self.pushButton.clicked.connect(lambda : self.backToMenu())
        self.pushButton_4.clicked.connect(lambda : self.backToMenu())
        self.pushButton_5.clicked.connect(lambda : self.backToMenu())
        self.piano.setIcon(QtGui.QIcon('piano.jpg'))
        self.piano.setIconSize((QtCore.QSize(453,392)))
        self.bongos.setIcon(QtGui.QIcon('bongos.jpg'))
        self.bongos.setIconSize((QtCore.QSize(231,352)))
        self.drums.setIcon(QtGui.QIcon('drum.jpg'))
        self.drums.setIconSize((QtCore.QSize(493,392)))
        self.pushButton_21.clicked.connect(lambda : self.playRightBango())
        self.pianoA.clicked.connect(lambda: self.playC4())
        self.pianoS.clicked.connect(lambda: self.playD4())
        self.pianoD.clicked.connect(lambda: self.playE4())
        self.pianoF.clicked.connect(lambda: self.playF4())
        self.pianoG.clicked.connect(lambda: self.playG4())
        self.pianoH.clicked.connect(lambda: self.playA4())
        self.pianoJ.clicked.connect(lambda: self.playB4())
        self.pianoK.clicked.connect(lambda: self.playC5())
        self.pianoL.clicked.connect(lambda: self.playD5())
        self.pushButton_13.clicked.connect(lambda: self.playE5())
        self.pianoE.clicked.connect(lambda: self.playDb4())
        self.pianoR.clicked.connect(lambda: self.playEb4())
        self.pianoT.clicked.connect(lambda: self.playGb4())
        self.pianoY.clicked.connect(lambda: self.playAb4())
        self.pianoI.clicked.connect(lambda:self.playBb4())
        self.pianoU.clicked.connect(lambda: self.playDb5())
        self.pianoO.clicked.connect(lambda: self.playEb5())
        self.pushButton_21.clicked.connect(lambda: self.playRightBango())
        self.pushButton_22.clicked.connect(lambda: self.playLeftBango())
        self.pushButton_21.setShortcut(_translate("MainWindow", "W"))
        self.pushButton_22.setShortcut(_translate("MainWindow", "Q"))
        self.pushButton_24.clicked.connect(lambda: self.playFloorTom())
        self.pushButton_27.clicked.connect(lambda: self.playRideCymbal())
        self.pushButton_23.clicked.connect(lambda: self.playHiHat())
        self.pushButton_25.clicked.connect(lambda: self.playHighTom())
        self.pushButton_28.clicked.connect(lambda: self.playCrashCymbal())
        self.pushButton0.clicked.connect(lambda:   self.playSnareDrum())
        self.pushButton_29.clicked.connect(lambda: self.playCrashCymbal())
        self.pushButton_26.clicked.connect(lambda: self.playMidTom())
        self.pushButton1.clicked.connect(lambda:   self.playBuss())
        self.pushButton_24.setShortcut(_translate("MainWindow", "C"))
        self.pushButton_27.setShortcut(_translate("MainWindow", "B"))
        self.pushButton_23.setShortcut(_translate("MainWindow", "Z"))
        self.pushButton_25.setShortcut(_translate("MainWindow", "M"))
        self.pushButton_28.setShortcut(_translate("MainWindow", "V"))
        self.pushButton0.setShortcut(_translate("MainWindow", "X"))
        self.pushButton_29.setShortcut(_translate("MainWindow", ","))
        self.pushButton_26.setShortcut(_translate("MainWindow", "N"))
        self.pushButton1.setShortcut(_translate("MainWindow", "/"))


    #defining globals
        #setting the dafault to gary
        self.paletteName='viridis'
        self.rmin = 0
        self.rmax = 256
        self.gmin = 0
        self.gmax = 256
        self.bmin = 0
        self.bmax = 256
        self.spectroON=0

        #adding palettes to palette combobox
        self.PaletteComboBox.addItem('hsv')
        self.PaletteComboBox.addItem('summer')
        self.PaletteComboBox.addItem('viridis')
        self.PaletteComboBox.addItem('turbo')
        self.PaletteComboBox.addItem('gray')
        
        
        #connecting buttons
        self.OpenFileButton.clicked.connect(lambda: self.open_file())
        self.PauseButton.clicked.connect(lambda: self.pause_music())
        self.PlayButton.clicked.connect(lambda: self.play_music())
        self.FasterButton.clicked.connect(lambda: self.faster_audio())
        self.SpectroButton.clicked.connect(lambda: self.runSpectro())
        self.Spec_MaxSlider.valueChanged.connect(lambda: self.maxSlider(self.Spec_MaxSlider.value()))
        self.Spec_minSLider.valueChanged.connect(lambda: self.maxSlider(self.Spec_minSLider.value()))
        self.SlowerButton.clicked.connect(lambda: self.slower_audio())
        self.AudioVolumeSlider.valueChanged.connect(lambda: self.change_volume())
        self.ZoomInButton.clicked.connect(lambda: self.zoomIn())
        self.ZoomOutButton.clicked.connect(lambda: self.zoomOut())

        #connecting combobox 
        self.PaletteComboBox.currentTextChanged.connect(lambda: self.paletteComboBox())




        #initializing objects and variables
        self.player = QMediaPlayer() #object of the class
        self.timer = QtCore.QTimer()
        self.timerInterval = 100
        self.update_index=0
        
        #configuration of main graph plot 
        self.p=self.MainGraph.addPlot()   
        self.p.setLimits(xMin=0)
        self.p.setXRange(0, 0.5, padding=0)     

        self.curve = self.p.plot()
        self.curve.setData([0],[0])


        
    def open_file(self):
        """opens any music file from the local device"""
        self.update_index=0
        self.file_path=QFileDialog.getOpenFileName()[0]
        url = QUrl.fromLocalFile(self.file_path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.read_audio_data()
        self.play_music()
        
    def play_music(self):
        """plays the chosen music file"""
        self.player.play()
        self.timer.start()
    
    def pause_music(self):
        """pauses the playing music file"""
        self.player.pause()
        self.timer.stop()
        
        
    def faster_audio(self): 
        """makes the audio play speed faster"""
        self.current_speed=self.player.playbackRate()
        self.player.setPlaybackRate(self.current_speed+0.5)
        
    def slower_audio(self): 
        """makes the audio play speed slower"""
        self.current_speed=self.player.playbackRate()
        try:        
            self.player.setPlaybackRate(self.current_speed-0.5)
        except:
            self.player.setPlaybackRate(self.current_speed+0.5)
    
    def change_volume(self):
        """adjusts volume of the playing music file"""
        self.player.setVolume(self.AudioVolumeSlider.value())

    def zoomIn(self):
        """zooms in the plotted signal"""
        self.p.getViewBox().scaleBy((0.5,0.5))
    

    def zoomOut(self):
        """zooms out from the plotted signal"""
        self.p.getViewBox().scaleBy((2,2))  
            
    def read_audio_data(self):
        """reads amplitude and sampling rate of audio file"""
        try:
           self.audio_amplitude,self.sampling_rate=lr.load(self.file_path) 
           self.audio_time=list(np.arange(0,len(self.audio_amplitude))/self.sampling_rate)
           self.audio_amplitude=list(self.audio_amplitude)
           self.plot_audio_data()
        except:
            print("Please Choose a file ")
        
    def plot_audio_data(self):
        """plots time versus amplitude of the playing audio file"""    
        self.timer.setInterval(self.timerInterval)
        self.timer.timeout.connect(lambda:self.update_plot())
        self.timer.start()
        
    def last_plotted(self):
        """determines last plotted value on x-axis to set our range later"""
        last_point=self.curve.getData()[0][-1]

        return last_point        

    def update_plot(self):
        """updates plotted points according to the playing audio"""
        
        max_t=self.last_plotted()
        self.p.setXRange(max_t-0.5, max_t, padding=0) 
        self.update_index=self.audio_time.index(self.player.position()/self.sampling_rate)
        self.curve.setData(self.audio_time[0:self.update_index], self.audio_amplitude[0:self.update_index],pen='blue')

#Spectro 

#comboBox 

    def paletteComboBox(self):
        self.paletteName=self.PaletteComboBox.currentText()
        self.runSpectro()
        
    def maxSlider(self , value):
        slider_value=value
        self.rmax=slider_value 
        self.gmax=slider_value   
        self.bmax=slider_value 
        self.runSpectro()
        

    def minSlider(self , value):
        slider_value=value
        self.rmin=slider_value 
        self.gmin=slider_value  
        self.bmin=slider_value
        self.runSpectro()

    def figToImg(self ,fig ,dpi = 90):
        buf = io.BytesIO()
        fig.savefig(buf, format="jpeg", dpi=dpi)
        buf.seek(0)
        arrimg = np.frombuffer(buf.getvalue(), dtype=np.uint8)
        print(buf.getvalue())
        buf.close()
        self.img = cv2.imdecode(arrimg, 1)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        return self.img
    
    def runSpectro(self):
        self.spectroON=1   
        fig=plt.figure()
        self.spec_gram = plt.specgram(self.audio_amplitude, Fs=200 ,cmap=self.paletteName)
        self.plotGraph = pyqtgraph.PlotItem()
        pyqtgraph.PlotItem.enableAutoScale(self.plotGraph)
        pyqtgraph.PlotItem.hideAxis(self.plotGraph,'left')
        pyqtgraph.PlotItem.hideAxis(self.plotGraph,'bottom')
        self.SpectroChannel.setCentralItem(self.plotGraph)
        self.img=self.figToImg(fig)
        self.img = np.rot90(self.img , k=1 , axes= (1,0))
        self.image = pyqtgraph.ImageItem(self.img)
        self.image.setLevels([[ self.rmin , self.rmax] , [ self.gmin , self.gmax], [ self.bmin , self.bmax]])
        self.plotGraph.addItem(self.image)


    def backToMenu(self):
        self.stackedWidget.setCurrentIndex(0)
    def pianoPlay(self):
     self.stackedWidget.setCurrentIndex(1)
    def playC4 (self):
        samplerate, data = wavfile.read('C4.wav')
        sd.play(data , samplerate)
    def playD4 (self):
        samplerate, data = wavfile.read('D4.wav')
        sd.play(data , samplerate)
    def playE4 (self):
        samplerate, data = wavfile.read('E4.wav')
        sd.play(data , samplerate)
    def playF4 (self):
        samplerate, data = wavfile.read('F4.wav')
        sd.play(data , samplerate)
    def playG4 (self):
        samplerate, data = wavfile.read('G4.wav')
        sd.play(data , samplerate)
    def playA4 (self):
        samplerate, data = wavfile.read('A4.wav')
        sd.play(data , samplerate)
    def playB4 (self):
        samplerate, data = wavfile.read('B4.wav')
        sd.play(data , samplerate)
    def playDb4 (self):
        samplerate, data = wavfile.read('Db4.wav')
        sd.play(data , samplerate)
    def playEb4 (self):
        samplerate, data = wavfile.read('Eb4.wav')
        sd.play(data , samplerate)
    def playGb4 (self):
        samplerate, data = wavfile.read('Gb4.wav')
        sd.play(data , samplerate)
    def playAb4 (self):
        samplerate, data = wavfile.read('Ab4.wav')
        sd.play(data , samplerate)
    def playBb4 (self):
        samplerate, data = wavfile.read('Bb4.wav')
        sd.play(data , samplerate)
    def playC5 (self):
        samplerate, data = wavfile.read('C5.wav')
        sd.play(data , samplerate)
    def playD5 (self):
        samplerate, data = wavfile.read('D5.wav')
        sd.play(data , samplerate)
    def playE5(self):
        samplerate , data = wavfile.read('E5.wav')
        sd.play(data,samplerate)
    def playDb5 (self):
        samplerate, data = wavfile.read('Db5.wav')
        sd.play(data , samplerate)
    def playEb5 (self):
        samplerate, data = wavfile.read('Eb5.wav')
        sd.play(data , samplerate)
    def playGb5 (self):
        samplerate, data = wavfile.read('Gb5.wav')
        sd.play(data , samplerate)
    def playAb5 (self):
        samplerate, data = wavfile.read('Ab5.wav')
        sd.play(data , samplerate)
    def playBb5 (self):
        samplerate, data = wavfile.read('Bb5.wav')
        sd.play(data , samplerate)
    
    def playRightBango(self):
        samplerate, data = wavfile.read('bongoright.wav')
        sd.play(data , samplerate)
    def playLeftBango(self):
        samplerate, data = wavfile.read('bongoleft.wav')
        sd.play(data , samplerate)

    def playFloorTom(self):
        samplerate, data = wavfile.read('Floor-Tom-Drum.wav')
        sd.play(data , samplerate)
    def playRideCymbal(self):
        samplerate, data = wavfile.read('Ride-Cymbal.wav')
        sd.play(data , samplerate)
    def playHiHat(self):
        samplerate, data = wavfile.read('Hi-Hat-1.wav')
        sd.play(data , samplerate)
    def playHighTom(self):
        samplerate, data = wavfile.read('high-tom.wav')
        sd.play(data , samplerate)
    def playCrashCymbal(self):
        samplerate, data = wavfile.read('China-Cymbal.wav')
        sd.play(data , samplerate)
    def playSnareDrum(self):
        samplerate, data = wavfile.read('Snare-Drum.wav')
        sd.play(data , samplerate)
    def playMidTom(self):
        samplerate, data = wavfile.read('Medium-Tom-Drum.wav')
        sd.play(data , samplerate)
    def playBuss(self): 
        samplerate, data = wavfile.read('Bass-Drum-Hit.wav')
        sd.play(data , samplerate)
        
    def BongosPlay(self):
        self.stackedWidget.setCurrentIndex(2)

    def drumsPlay(self):
        self.stackedWidget.setCurrentIndex(3)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())