# Python module for control of Mipow bluetooth LED bulbs

# Copyright 2016 Arttu Mahlakaarto <Arttu.mahlakaarto@gmail.com>
# Copyright 2017 Matthew Garrett <mjg59@srcf.ucam.org>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.

import time

from bluepy import btle

class mipow:
  def __init__(self, mac):
    self.mac = mac

  def connect(self):
    self.device = btle.Peripheral(self.mac, addrType=btle.ADDR_TYPE_PUBLIC)
    self.rgbwhandle = None
    self.effecthandle = None
    self.mono = False
    handles = self.device.getCharacteristics()
    for handle in handles:
      if handle.uuid == "fffb":
        self.effecthandle = handle
      if handle.uuid == "fffc":
        self.rgbwhandle = handle
      if handle.uuid == "2a39":
        self.whitehandle = handle

    if self.rgbwhandle == None:
        self.mono = True

    self.get_state()

  def get_state(self):
      initial = time.time()
      while True:
          if time.time() - initial >= 10:
              return False
          try:            
            if self.mono:
              data = self.whitehandle.read()
              self.white = data[0]
              if self.white > 0:
                self.power = True
              else:
                self.power = False
            else:
              data = self.rgbwhandle.read()
              self.white = data[0]
              self.red = data[1]
              self.green = data[2]
              self.blue = data[3]
              if bytearray(data) != bytearray([0, 0, 0, 0]):
                self.power = True
              else:
                self.power = False
            return
          except Exception as e:
            self.connect()

  def send_packet(self, handle, data):
    initial = time.time()
    while True:
      if time.time() - initial >= 10:
        return False
      try:
        return handle.write(bytes(data))
      except:
        self.connect()

  def set_effect(self, red, green, blue, white, mode, speed):
    self.red = red
    self.green = green
    self.blue = blue
    self.white = white
    self.mode = mode
    self.speed = speed
    packet = bytearray([white, red, green, blue, mode, 0x00, 0x14, speed])
    self.send_packet(self.effecthandle, packet)

  def set_rgb(self, red, green, blue):
    self.set_rgbw(red, green, blue, 0)

  def set_rgbw(self, red, green, blue, white):
    self.red = red
    self.green = green
    self.blue = blue
    self.white = white
    packet = bytearray([white, red, green, blue])
    self.send_packet(self.rgbwhandle, packet)

  def get_rgbw(self):
    if self.mono:
      return None
    self.get_state()
    return (self.red, self.green, self.blue, self.white)

  def set_white(self, white):
    self.white = white
    if self.mono:
      packet = bytearray([white])
      self.send_packet(self.monohandle, packet)
    else:
      self.set_rgbw(0, 0, 0, white)

  def get_white(self):
    self.get_state()
    return self.white

  def get_on(self):
    return self.power
