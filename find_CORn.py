

import os
import time
import tkinter.filedialog
#from PyQt5.QtGui import QIcon, QPixmap
#from PyQt5.uic.properties import QtWidgets
from PyQt5 import QtWidgets, uic
from scipy import ndimage
from PyQt5.uic import loadUiType
import sys

#further imports 

from pyqtgraph import ImageView



class Find_CORn(QtWidgets.QMainWindow):

    # we need to connect model to the view by adding model library here 
    #for now we add ImageLibrary and defult value would be none 
    def __init__(self): 
        super(Find_CORn,self).__init__()
        uic.loadUi('Find_CORn.ui',self)


        #ImageView from pyqtgraph was connected to the gui
        #using qtDesigner and the promote widget command 
        

        self.show()


        # connect the bottun 


    #write functions here 


    def selectImage(self):
        #this functions runs when button is clicked : 
        #therefore it needs to connect to the model (ImageLibrary) and 
        #wait for the response of the model and update the Image

        print('select image ')
        self.image = self.imageLibrary.loadImage('path')
        #initiate the update Image function 
        self.updateImage()

    def updateImage(self):
        #this is initiated when ever we need to update the Imageviewer's image
        self.pyqtgraphWidget.setImage(self.image)


    
    def nextSlice(self):
        print('next slice ')
        
def main():
    
    app = QtWidgets.QApplication(sys.argv)
    main = Find_CORn()
    app.exec_()
    #sys.exit(app.exec_())

if __name__ == '__main__':
    main()
