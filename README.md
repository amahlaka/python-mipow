Python control for Mipow smart LED bulbs
=========================================

A simple python API for [Mipow Smart](http://www.mipow.de/smart-home/46/mipow-playbulb-smart) Bluetooth LE lightbulbs
Based on the work by Matthew Garret on [python-zengge](https://github.com/mjg59/python-zengge) 


Example use
-----------

This will connect and set the bulb to full red, no green and no blue.
```
import mipow

bulb = mipow.mipow("00:21:4d:00:00:01")
bulb.connect()
bulb.set_rgb(255, 0, 0)
```

This will set the intensity of the warm white LEDs to 50%
```
bulb.set_white(0x80)
```

This will turn on the white LEDs at the same time as the colour LEDs (note that this may result in a small quantity of flickering during colour changes)
```
bulb.set_rgbw(255, 255, 100, 255)
```

This will turn the bulb on
```
bulb.on()
```

This will turn the bulb off
```
bulb.off()
```

Get a list of the current red, green and blue values
```
(red, green, blue) = bulb.get_colour()
```

Get the current white intensity
```
white = bulb.get_white()
```

Get aboolean describing whether the bulb is on or off
```
on = bulb.get_on()
```

Notes
-----

Note that this has been written against a specific bulb, and may misbehave on some other bulbs that speak a similar protocol. Please get in touch if you have a bulb that partially works with this code.
