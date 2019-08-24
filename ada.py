#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import Adafruit_DHT
import datetime
import time


N = 10
T_tot = 0
H_tot = 0
sensor = Adafruit_DHT.DHT22
pin = 4
for i in range(N):
    h, t = Adafruit_DHT.read_retry(sensor, pin)
    H_tot += h
    T_tot += t
H_ave = H_tot / N
T_ave = ((T_tot / N)*1.8) + 32

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
with open('/home/pi/Desktop/pigpio_dht22/output.dat', 'a') as f:
    
    f.write("%s, %s, %s\n" % (H_ave, T_ave, st))
