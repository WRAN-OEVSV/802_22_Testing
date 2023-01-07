#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: HackRF Test
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import digital
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time

from gnuradio import qtgui

class hackrf(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "HackRF Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("HackRF Test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "hackrf")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.ncarrier = ncarrier = 720*2
        self.sync_word = sync_word = [0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, 1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, -1.41421356, 0.0, 0.0, 0.0, 1.41421356]
        self.samp_rate = samp_rate = 2.285e6
        self.pilot_symbols_e = pilot_symbols_e = ((1,-1),)
        self.pilot_symbols = pilot_symbols = ((1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1),)
        self.pilot_carriers_e = pilot_carriers_e = ((-(ncarrier+1),(ncarrier+1)),)
        self.pilot_carriers = pilot_carriers = ((-420, -413, -406, -399, -392, -385, -378, -371, -364, -357, -350, -343, -336, -329, -322, -315, -308, -301, -294, -287, -280, -273, -266, -259, -252, -245, -238, -231, -224, -217, -210, -203, -196, -189, -182, -175, -168, -161, -154, -147, -140, -132, -125, -118, -111, -104, -97, -90, -83, -76, -69, -62, -55, -48, -41, -34, -27, -20, -13, -6, 1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99, 106, 113, 120, 127, 134, 141, 148, 155, 162, 169, 176, 183, 190, 197, 204, 211, 218, 225, 232, 239, 246, 253, 260, 267, 274, 281, 288, 295, 302, 309, 316, 323, 330, 337, 344, 351, 358, 365, 372, 379, 386, 393, 400, 407, 414),)
        self.occupied_carriers_e = occupied_carriers_e = [list(range(-(int)(ncarrier/2),0)) + list(range(1,(int)(ncarrier/2+1)))]
        self.occupied_carriers = occupied_carriers = [-419, -418, -417, -416, -415, -414, -412, -411, -410, -409, -408, -407, -405, -404, -403, -402, -401, -400, -398, -397, -396, -395, -394, -393, -391, -390, -389, -388, -387, -386, -384, -383, -382, -381, -380, -379, -377, -376, -375, -374, -373, -372, -370, -369, -368, -367, -366, -365, -363, -362, -361, -360, -359, -358, -356, -355, -354, -353, -352, -351, -349, -348, -347, -346, -345, -344, -342, -341, -340, -339, -338, -337, -335, -334, -333, -332, -331, -330, -328, -327, -326, -325, -324, -323, -321, -320, -319, -318, -317, -316, -314, -313, -312, -311, -310, -309, -307, -306, -305, -304, -303, -302, -300, -299, -298, -297, -296, -295, -293, -292, -291, -290, -289, -288, -286, -285, -284, -283, -282, -281, -279, -278, -277, -276, -275, -274, -272, -271, -270, -269, -268, -267, -265, -264, -263, -262, -261, -260, -258, -257, -256, -255, -254, -253, -251, -250, -249, -248, -247, -246, -244, -243, -242, -241, -240, -239, -237, -236, -235, -234, -233, -232, -230, -229, -228, -227, -226, -225, -223, -222, -221, -220, -219, -218, -216, -215, -214, -213, -212, -211, -209, -208, -207, -206, -205, -204, -202, -201, -200, -199, -198, -197, -195, -194, -193, -192, -191, -190, -188, -187, -186, -185, -184, -183, -181, -180, -179, -178, -177, -176, -174, -173, -172, -171, -170, -169, -167, -166, -165, -164, -163, -162, -160, -159, -158, -157, -156, -155, -153, -152, -151, -150, -149, -148, -146, -145, -144, -143, -142, -141, -139, -138, -137, -136, -135, -134, -133, -131, -130, -129, -128, -127, -126, -124, -123, -122, -121, -120, -119, -117, -116, -115, -114, -113, -112, -110, -109, -108, -107, -106, -105, -103, -102, -101, -100, -99, -98, -96, -95, -94, -93, -92, -91, -89, -88, -87, -86, -85, -84, -82, -81, -80, -79, -78, -77, -75, -74, -73, -72, -71, -70, -68, -67, -66, -65, -64, -63, -61, -60, -59, -58, -57, -56, -54, -53, -52, -51, -50, -49, -47, -46, -45, -44, -43, -42, -40, -39, -38, -37, -36, -35, -33, -32, -31, -30, -29, -28, -26, -25, -24, -23, -22, -21, -19, -18, -17, -16, -15, -14, -12, -11, -10, -9, -8, -7, -5, -4, -3, -2, -1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 100, 101, 102, 103, 104, 105, 107, 108, 109, 110, 111, 112, 114, 115, 116, 117, 118, 119, 121, 122, 123, 124, 125, 126, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 142, 143, 144, 145, 146, 147, 149, 150, 151, 152, 153, 154, 156, 157, 158, 159, 160, 161, 163, 164, 165, 166, 167, 168, 170, 171, 172, 173, 174, 175, 177, 178, 179, 180, 181, 182, 184, 185, 186, 187, 188, 189, 191, 192, 193, 194, 195, 196, 198, 199, 200, 201, 202, 203, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 219, 220, 221, 222, 223, 224, 226, 227, 228, 229, 230, 231, 233, 234, 235, 236, 237, 238, 240, 241, 242, 243, 244, 245, 247, 248, 249, 250, 251, 252, 254, 255, 256, 257, 258, 259, 261, 262, 263, 264, 265, 266, 268, 269, 270, 271, 272, 273, 275, 276, 277, 278, 279, 280, 282, 283, 284, 285, 286, 287, 289, 290, 291, 292, 293, 294, 296, 297, 298, 299, 300, 301, 303, 304, 305, 306, 307, 308, 310, 311, 312, 313, 314, 315, 317, 318, 319, 320, 321, 322, 324, 325, 326, 327, 328, 329, 331, 332, 333, 334, 335, 336, 338, 339, 340, 341, 342, 343, 345, 346, 347, 348, 349, 350, 352, 353, 354, 355, 356, 357, 359, 360, 361, 362, 363, 364, 366, 367, 368, 369, 370, 371, 373, 374, 375, 376, 377, 378, 380, 381, 382, 383, 384, 385, 387, 388, 389, 390, 391, 392, 394, 395, 396, 397, 398, 399, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 415, 416, 417, 418, 419,420]
        self.fft_len = fft_len = 1024

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-70, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(52e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.fft_vxx_0 = fft.fft_vcc(fft_len, False, (), True, 1)
        self.digital_ofdm_cyclic_prefixer_0 = digital.ofdm_cyclic_prefixer(fft_len, fft_len + (int)(fft_len/4), 0, "packet_len")
        self.digital_ofdm_carrier_allocator_cvc_0 = digital.ofdm_carrier_allocator_cvc( fft_len, [occupied_carriers,occupied_carriers], pilot_carriers, pilot_symbols, [sync_word], "packet_len", True)
        self.digital_glfsr_source_x_0 = digital.glfsr_source_b(16, True, 0, 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([-1-1j, -1+1j, 1-1j, 1+1j], 1)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, 1, ncarrier, "packet_len")
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, 2, "", False, gr.GR_LSB_FIRST)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_ofdm_carrier_allocator_cvc_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.digital_glfsr_source_x_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_ofdm_carrier_allocator_cvc_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.digital_ofdm_cyclic_prefixer_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.digital_ofdm_cyclic_prefixer_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "hackrf")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_ncarrier(self):
        return self.ncarrier

    def set_ncarrier(self, ncarrier):
        self.ncarrier = ncarrier
        self.set_occupied_carriers_e([list(range(-(int)(self.ncarrier/2),0)) + list(range(1,(int)(self.ncarrier/2+1)))])
        self.set_pilot_carriers_e(((-(self.ncarrier+1),(self.ncarrier+1)),))
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.ncarrier)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.ncarrier)

    def get_sync_word(self):
        return self.sync_word

    def set_sync_word(self, sync_word):
        self.sync_word = sync_word

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)

    def get_pilot_symbols_e(self):
        return self.pilot_symbols_e

    def set_pilot_symbols_e(self, pilot_symbols_e):
        self.pilot_symbols_e = pilot_symbols_e

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols

    def get_pilot_carriers_e(self):
        return self.pilot_carriers_e

    def set_pilot_carriers_e(self, pilot_carriers_e):
        self.pilot_carriers_e = pilot_carriers_e

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers

    def get_occupied_carriers_e(self):
        return self.occupied_carriers_e

    def set_occupied_carriers_e(self, occupied_carriers_e):
        self.occupied_carriers_e = occupied_carriers_e

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len





def main(top_block_cls=hackrf, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
