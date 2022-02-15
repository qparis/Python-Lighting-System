import math
import threading
import time

from pyftdi import ftdi

def usleep(tps):
    time.sleep(tps / 1000)

class OpenDmxUsb(threading.Thread):
    def __init__(self, device=None):
        threading.Thread.__init__(self)
        if device is None:
            devices = ftdi.Ftdi.list_devices()
            device = devices[0][0]
        self.baud_rate = 250000
        self.data_bits = 8
        self.stop_bits = 2
        self.parity = 'N'
        self.flow_ctrl = ''
        self.rts_state = True
        self.vendor_id = device.vid
        self.product_id = device.pid
        self._init_dmx()
        self.current_vals = None
        self._running = True

    def run(self):
        frameTime = math.floor(1000 / 30) + 0.5
        DMX_BREAK = 110
        DMX_MAB = 16
        usleep(1000)

        print("Frame time is %s" % frameTime)
        while self._running:
            if self.current_vals is not None:
                self.ftdi.set_break(True)
                usleep(DMX_BREAK)
                self.ftdi.set_break(False)
                usleep(DMX_MAB)
                self.ftdi.write_data(self.current_vals)
                usleep(frameTime)
            else:
                usleep(100)

    def send_dmx(self, channel_vals):
        self.current_vals = channel_vals

    def wait_dmx(self):
        pass

    def stop(self):
        self._running = False

    def _init_dmx(self):
        self.ftdi = ftdi.Ftdi()
        self.ftdi.open(self.vendor_id, self.product_id)
        self.ftdi.set_baudrate(self.baud_rate)
        self.ftdi.set_line_property(self.data_bits, self.stop_bits, self.parity, break_=False)
        self.ftdi.set_flowctrl(self.flow_ctrl)
        self.ftdi.purge_rx_buffer()
        self.ftdi.purge_tx_buffer()
        self.ftdi.set_rts(self.rts_state)
