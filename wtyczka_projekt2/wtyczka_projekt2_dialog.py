# -*- coding: utf-8 -*-
"""
/***************************************************************************
 wtyczka_projekt2Dialog
                                 A QGIS plugin
 obliczenie przewyższen między punktami oraz pól powierzchni
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-09
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Kacper Linke, Bartek Kużela
        email                : bartekkuzela1@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

from qgis.utils import iface
from qgis.core import QgsWkbTypes
import numpy as np
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wtyczka_projekt2_dialog_base.ui'))


class wtyczka_projekt2Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(wtyczka_projekt2Dialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.radioButton_przewyzszenia.clicked.connect(self.liczenie)
        self.radioButton_pole.clicked.connect(self.liczenie)
        
    
    def liczenie(self):
        aktywna_warstwa = iface.activeLayer()
        zliczenie_obiektow = aktywna_warstwa.selectedFeatureCount()
        
        x = []
        y = []
        z = []
        nr = []
        
        for punkt in aktywna_warstwa.selectedFeatureCount():
            x.append(punkt[" x_92 "])
            y.append(punkt[" y_92 "])
            z.append(punkt[" z_92 "])
            nr.append(punkt[" nr "])
            
        if self.radioButton.isChecked() == True and zliczenie_obiektow == 2:
            dh = z[1] - z[0]
            punkt_1 = nr[0]
            punkt_2 = nr[1]
            iface.messageBar().pushMessage("przewyższenie wysokosci między punktem '+ str(punkt_1)+ 'a punktem '+str(punkt_2)+' rowna sie: '+str(round(dh,3))+' [m]")
            
            
            
        
            
        
        
        
        
        
        
        
        
        
