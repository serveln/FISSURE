#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Wideband Plutosdr
# GNU Radio version: 3.8.5.0

from gnuradio import analog
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import ainfosec
import iio


class wideband_plutosdr(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Wideband Plutosdr")

        ##################################################
        # Variables
        ##################################################
        self.threshold = threshold = -70
        self.serial = serial = ""
        self.sample_rate = sample_rate = 20000000
        self.rx_freq = rx_freq = 1200e6
        self.ip_address = ip_address = "192.168.2.1"
        self.gain = gain = 64
        self.fft_size = fft_size = 512*1
        self.channel = channel = ""
        self.antenna = antenna = "TX/RX"

        ##################################################
        # Blocks
        ##################################################
        self.iio_pluto_source_0 = iio.pluto_source("ip:" + str(ip_address), int(rx_freq), int(sample_rate), 20000000, 32768, True, True, True, 'manual', gain, '', True)
        self.fft_vxx_0 = fft.fft_vcc(fft_size, True, window.blackmanharris(fft_size), True, 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-10, 1e-4, 0, True)
        self.ainfosec_wideband_detector1_0 = ainfosec.wideband_detector1("tcp://127.0.0.1:5060",rx_freq,fft_size,sample_rate)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.ainfosec_wideband_detector1_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.analog_pwr_squelch_xx_0, 0))


    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold

    def get_serial(self):
        return self.serial

    def set_serial(self, serial):
        self.serial = serial

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.ainfosec_wideband_detector1_0.set_sample_rate(self.sample_rate)
        self.iio_pluto_source_0.set_params(int(self.rx_freq), int(self.sample_rate), 20000000, True, True, True, 'manual', self.gain, '', True)

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.ainfosec_wideband_detector1_0.set_rx_freq(self.rx_freq)
        self.iio_pluto_source_0.set_params(int(self.rx_freq), int(self.sample_rate), 20000000, True, True, True, 'manual', self.gain, '', True)

    def get_ip_address(self):
        return self.ip_address

    def set_ip_address(self, ip_address):
        self.ip_address = ip_address

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.iio_pluto_source_0.set_params(int(self.rx_freq), int(self.sample_rate), 20000000, True, True, True, 'manual', self.gain, '', True)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size
        self.ainfosec_wideband_detector1_0.set_fft_size(self.fft_size)

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna





def main(top_block_cls=wideband_plutosdr, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
