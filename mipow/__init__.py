# Python module for control of Mipow LED bulbs
#
# Copyright 2016 Arttu Mahlakaarto <Arttu.mahlakaarto@gmail.com>
# Based on work by Matthew Garret
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.

import time

from bluepy import btle


class Delegate(btle.DefaultDelegate):
    """Delegate Class."""

    def __init__(self, bulb):
        self.bulb = bulb
        btle.DefaultDelegate.__init__(self)



class mipow:
  def __init__(self, mac):
    self.mac = mac

  def set_state(self, white, red, green, blue, power):
    self.white = white
    self.red = red
    self.green = green
    self.blue = blue

  def connect(self):
    self.device = btle.Peripheral(self.mac, addrType=btle.ADDR_TYPE_PUBLIC)
    self.device.setDelegate(Delegate(self))
    self.get_state()

  def send_packet(self, handleId, data):
    initial = time.time()
    while True:
        if time.time() - initial >= 10:
            return False
        try:
            return self.device.writeCharacteristic(handleId, data)
        except:
            self.connect()

  def off(self):
    self.power = False
    packet = bytearray([0x00, 0x00, 0x00, 0x00])
    self.send_packet(37, packet)

  def on(self):
    self.power = True
    packet = bytearray([0xff, 0x00, 0x00, 0x00])
    self.send_packet(37, packet)

  def set_rgb(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue
    self.white = 0
    packet = bytearray([0x00, red, green, blue])
    self.send_packet(37, packet)

  def set_white(self, white):
    self.red = 0
    self.green = 0
    self.blue = 0
    self.white = white
    packet = bytearray([white, 0x00, 0x00, 0x00])
    self.send_packet(37, packet)

  def set_rgbw(self, red, green, blue, white):
    self.red = red
    self.green = green
    self.blue = blue
    self.white = white
    packet = bytearray([white, red, green, blue])
    self.send_packet(37, packet)

  def set_effect(self, red, green, blue, white, mode, speed):
    self.red = red
    self.green = green
    self.blue = blue
    self.white = white
    self.mode = mode
    self.speed = speed
    packet = bytearray([white, red, green, blue, mode, 0x00, 0x14, speed])
    self.send_packet(35, packet)

  def get_state(self):
    status = self.device.readCharacteristic(37)
    if bytearray(status) != bytearray([0, 0, 0, 0]):
        self.power = True
    else:
        self.power = False
    self.white = status[0]
    self.red = status[1]
    self.green = status[2]
    self.blue = status[3]
    return status



  def get_on(self):
    return self.power

  def get_colour(self):
    return (self.red, self.green, self.blue)

  def get_white(self):
    return self.white
