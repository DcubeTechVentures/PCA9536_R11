# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# PCA9536_R11
# This code is designed to work with the PCA9536_I2CR_R11 I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# PCA9536_R11 address, 0x41(65)
# Select configuration register, 0x03(03)
#		0x00(00)	Set all pins as OUTPUT
bus.write_byte_data(0x41, 0x03, 0x00)
# PCA9536_R11 address, 0x41(65)
# Select output port register, 0x01(01)
#		0x01(01)	Set Pin-1 HIGH
bus.write_byte_data(0x41, 0x01, 0x01)

time.sleep(0.5)

# PCA9536_R11 address, 0x41(65)
# Read data back from 0x01(01), 1 byte
data = bus.read_byte_data(0x41, 0x01)

# Output to screen
if (data & 0x01) :
	print "Pin 1 : HIGH"
else :
	print "Pin 1 : LOW"
