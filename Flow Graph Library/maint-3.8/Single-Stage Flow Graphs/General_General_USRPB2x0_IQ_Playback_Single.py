#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: General General Usrpb2X0 Iq Playback Single
# GNU Radio version: 3.8.5.0

from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time


class General_General_USRPB2x0_IQ_Playback_Single(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "General General Usrpb2X0 Iq Playback Single")

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 70
        self.tx_frequency = tx_frequency = 2425.715e6
        self.tx_channel = tx_channel = "A:A"
        self.serial = serial = "False"
        self.sample_rate = sample_rate = 1e6
        self.notes = notes = "Replays an IQ file once."
        self.filepath = filepath = ""

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join((serial, "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            '',
        )
        self.uhd_usrp_sink_0.set_subdev_spec(tx_channel, 0)
        self.uhd_usrp_sink_0.set_center_freq(float(tx_frequency), 0)
        self.uhd_usrp_sink_0.set_gain(float(tx_gain), 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_samp_rate(float(sample_rate))
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec())
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, filepath, False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.uhd_usrp_sink_0, 0))


    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0.set_gain(float(self.tx_gain), 0)

    def get_tx_frequency(self):
        return self.tx_frequency

    def set_tx_frequency(self, tx_frequency):
        self.tx_frequency = tx_frequency
        self.uhd_usrp_sink_0.set_center_freq(float(self.tx_frequency), 0)

    def get_tx_channel(self):
        return self.tx_channel

    def set_tx_channel(self, tx_channel):
        self.tx_channel = tx_channel

    def get_serial(self):
        return self.serial

    def set_serial(self, serial):
        self.serial = serial

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.uhd_usrp_sink_0.set_samp_rate(float(self.sample_rate))

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

    def get_filepath(self):
        return self.filepath

    def set_filepath(self, filepath):
        self.filepath = filepath
        self.blocks_file_source_0.open(self.filepath, False)





def main(top_block_cls=General_General_USRPB2x0_IQ_Playback_Single, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()
