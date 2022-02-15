import time

from pyftdi import ftdi

class OpenDmxUsb:
    def __init__(self, device=None):
        if device is None:
            devices = ftdi.Ftdi.list_devices()
            device = devices[0][0]
        self.baud_rate = 250000
        self.data_bits = 8
        self.stop_bits = 2
        self.parity = 'N'
        self.flow_ctrl = ''
        self.rts_state = False
        self.vendor_id = device.vid
        self.product_id = device.pid
        self._init_dmx()
        self.current_vals = None
        ch = bytearray([0] * 513)
        ch[15] = 255
        ch[18] = 255
        
        self.send_dmx(ch)
        self.send_dmx(ch)
        self.send_dmx(ch)
        self.send_dmx(ch)
        self.send_dmx(ch)
        self.send_dmx(ch)


        time.sleep(200)

    def send_dmx(self, channel_vals):
        self.ftdi.set_break(True)
        time.sleep(0.1)
        self.ftdi.set_break(False)
        time.sleep(0.01)
        self.ftdi.write_data(channel_vals)

    def wait_dmx(self):
        pass

    def _init_dmx(self):
        self.ftdi = ftdi.Ftdi()
        self.ftdi.open(self.vendor_id, self.product_id)
        self.ftdi.set_baudrate(self.baud_rate)
        self.ftdi.set_line_property(self.data_bits, self.stop_bits, self.parity, break_=False)
        self.ftdi.set_flowctrl(self.flow_ctrl)
        self.ftdi.purge_rx_buffer()
        self.ftdi.purge_tx_buffer()
        self.ftdi.set_rts(self.rts_state)
        
OpenDmxUsb()
