import sys
import time
import board
import busio
import adafruit_sgp40
# from collections import Counter
import numpy as np

sample = 16
i2c = busio.I2C(board.SCL, board.SDA)
sgp = adafruit_sgp40.SGP40(i2c)
data_arr = np.empty(shape=(sample,16), dtype=np.int8)

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def data():
    while True:
        print("Raw Gas: ", decimalToBinary(sgp.raw))
        print("")
        time.sleep(1)

def stat(dataNum):
    type = input("Choose number (0: fresh air, 1: citrus, 3: peppermint, 4: fish): ")
    global data_arr
    print("Samples being collected... Please wait")
    for x in range(dataNum):
        for bit in range(16):
            data_arr[x, bit] = decimalToBinary(sgp.raw)[bit]
        time.sleep(0.5)

stat(sample)
saved = np.asarray(data_arr)
print("Generating a data file...")
np.savetxt('freshair.csv', saved, delimiter=',')
