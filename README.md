Python control for Mipow LED bulbs
==================================

A simple Python API for controlling LED bulbs compatible from [Mipow](https://www.mipow.com/).

Example use
-----------

This will connect and set the bulb to full red, no green, no blue and 50% white
```
import mipow

bulb = mipow.mipow("00:21:4d:00:00:01")
bulb.connect()
bulb.set_rgb(0xff, 0x00, 0x00, 0x80)
```

This will set the intensity of the white LEDs to 50%
```
bulb.set_white(0x80)
```

Get a list of the current red, green, blue and white values
```
(red, green, blue, white) = bulb.get_rgbw()
```

Get the current white intensity
```
white = bulb.get_white()
```

Check whether the bulb is monochrome

```
if bulb.mono:
  print("Monochrome")
```