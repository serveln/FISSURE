#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Time Sink 1 10 100 Usrp X410
# GNU Radio version: 3.10.7.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import sip



class time_sink_1_10_100_usrp_x410(gr.top_block, Qt.QWidget):

    def __init__(self, ip_address="192.168.140.2", rx_usrp_channel="A:0"):
        gr.top_block.__init__(self, "Time Sink 1 10 100 Usrp X410", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Time Sink 1 10 100 Usrp X410")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
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

        self.settings = Qt.QSettings("GNU Radio", "time_sink_1_10_100_usrp_x410")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Parameters
        ##################################################
        self.ip_address = ip_address
        self.rx_usrp_channel = rx_usrp_channel

        ##################################################
        # Variables
        ##################################################
        self.sample_rate = sample_rate = 1e6
        self.rx_usrp_gain = rx_usrp_gain = 50
        self.rx_usrp_antenna = rx_usrp_antenna = "TX/RX"
        self.rx_frequency = rx_frequency = 2412

        ##################################################
        # Blocks
        ##################################################

        # Create the options list
        self._sample_rate_options = [1000000.0, 5000000.0, 10000000.0, 20000000.0, 50000000.0, 100000000.0, 200000000.0, 300000000.0, 400000000.0, 500000000.0]
        # Create the labels list
        self._sample_rate_labels = ['1 MS/s', '5 MS/s', '10 MS/s', '20 MS/s', '50 MS/s', '100 MS/s', '200 MS/s', '300 MS/s', '400 MS/s', '500 MS/s']
        # Create the combo box
        self._sample_rate_tool_bar = Qt.QToolBar(self)
        self._sample_rate_tool_bar.addWidget(Qt.QLabel("Sample Rate" + ": "))
        self._sample_rate_combo_box = Qt.QComboBox()
        self._sample_rate_tool_bar.addWidget(self._sample_rate_combo_box)
        for _label in self._sample_rate_labels: self._sample_rate_combo_box.addItem(_label)
        self._sample_rate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._sample_rate_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._sample_rate_options.index(i)))
        self._sample_rate_callback(self.sample_rate)
        self._sample_rate_combo_box.currentIndexChanged.connect(
            lambda i: self.set_sample_rate(self._sample_rate_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._sample_rate_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_usrp_gain_range = Range(0, 60, 1, 50, 200)
        self._rx_usrp_gain_win = RangeWidget(self._rx_usrp_gain_range, self.set_rx_usrp_gain, "              Gain:", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._rx_usrp_gain_win, 1, 0, 1, 4)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._rx_usrp_antenna_options = ['TX/RX', 'RX2']
        # Create the labels list
        self._rx_usrp_antenna_labels = ['TX/RX', 'RX2']
        # Create the combo box
        self._rx_usrp_antenna_tool_bar = Qt.QToolBar(self)
        self._rx_usrp_antenna_tool_bar.addWidget(Qt.QLabel("        Antenna" + ": "))
        self._rx_usrp_antenna_combo_box = Qt.QComboBox()
        self._rx_usrp_antenna_tool_bar.addWidget(self._rx_usrp_antenna_combo_box)
        for _label in self._rx_usrp_antenna_labels: self._rx_usrp_antenna_combo_box.addItem(_label)
        self._rx_usrp_antenna_callback = lambda i: Qt.QMetaObject.invokeMethod(self._rx_usrp_antenna_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._rx_usrp_antenna_options.index(i)))
        self._rx_usrp_antenna_callback(self.rx_usrp_antenna)
        self._rx_usrp_antenna_combo_box.currentIndexChanged.connect(
            lambda i: self.set_rx_usrp_antenna(self._rx_usrp_antenna_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._rx_usrp_antenna_tool_bar, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_frequency_range = Range(1, 7200, .1, 2412, 200)
        self._rx_frequency_win = RangeWidget(self._rx_frequency_range, self.set_rx_frequency, " Freq. (MHz):", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._rx_frequency_win, 2, 0, 1, 4)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
            ",".join(("addr=" + str(ip_address), "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0_0.set_subdev_spec(rx_usrp_channel, 0)
        self.uhd_usrp_source_0_0.set_samp_rate(sample_rate)
        self.uhd_usrp_source_0_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_source_0_0.set_center_freq(rx_frequency*1e6, 0)
        self.uhd_usrp_source_0_0.set_antenna(rx_usrp_antenna, 0)
        self.uhd_usrp_source_0_0.set_gain(rx_usrp_gain, 0)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_c(
            100000, #size
            sample_rate, #samp_rate
            "1 in 100", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.1)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.005, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(True)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_1_win, 26, 0, 10, 4)
        for r in range(26, 36):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
            100000, #size
            sample_rate, #samp_rate
            "1 in 10", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.1)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.005, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 15, 0, 10, 4)
        for r in range(15, 25):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            100000, #size
            sample_rate, #samp_rate
            "1 in 1", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.1)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.005, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 3, 0, 10, 4)
        for r in range(3, 13):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, 100)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, 10)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.qtgui_time_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "time_sink_1_10_100_usrp_x410")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_ip_address(self):
        return self.ip_address

    def set_ip_address(self, ip_address):
        self.ip_address = ip_address

    def get_rx_usrp_channel(self):
        return self.rx_usrp_channel

    def set_rx_usrp_channel(self, rx_usrp_channel):
        self.rx_usrp_channel = rx_usrp_channel

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self._sample_rate_callback(self.sample_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.sample_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.sample_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.sample_rate)
        self.uhd_usrp_source_0_0.set_samp_rate(self.sample_rate)

    def get_rx_usrp_gain(self):
        return self.rx_usrp_gain

    def set_rx_usrp_gain(self, rx_usrp_gain):
        self.rx_usrp_gain = rx_usrp_gain
        self.uhd_usrp_source_0_0.set_gain(self.rx_usrp_gain, 0)

    def get_rx_usrp_antenna(self):
        return self.rx_usrp_antenna

    def set_rx_usrp_antenna(self, rx_usrp_antenna):
        self.rx_usrp_antenna = rx_usrp_antenna
        self._rx_usrp_antenna_callback(self.rx_usrp_antenna)
        self.uhd_usrp_source_0_0.set_antenna(self.rx_usrp_antenna, 0)

    def get_rx_frequency(self):
        return self.rx_frequency

    def set_rx_frequency(self, rx_frequency):
        self.rx_frequency = rx_frequency
        self.uhd_usrp_source_0_0.set_center_freq(self.rx_frequency*1e6, 0)



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--ip-address", dest="ip_address", type=str, default="192.168.140.2",
        help="Set 192.168.140.2 [default=%(default)r]")
    parser.add_argument(
        "--rx-usrp-channel", dest="rx_usrp_channel", type=str, default="A:0",
        help="Set A:0 [default=%(default)r]")
    return parser


def main(top_block_cls=time_sink_1_10_100_usrp_x410, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(ip_address=options.ip_address, rx_usrp_channel=options.rx_usrp_channel)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
