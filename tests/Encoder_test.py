SA1_base = 0x48
SD1_base = 0x8A
D1 = 3
_TAC2X = 5

from PiStorms_GRX import RCServo
s = RCServo("BAM1", 1400)
i2c = s.bankA
# Set_type
i2c.writeArray(SA1_base+D1*22, [_TAC2X, 1])
# set_Target
i2c.writeArray(SA1_base+8+D1*22, [180, 0, 0, 0])
# read_TACH1
i2c.readArray(SD1_base+4, 4)

import ctypes
ctypes.c_int(sum([b<<(n*8) for n,b in enumerate(i2c.readArray(SD1_base+4, 4))])).value

# or, across multiple lines
v = i2c.readArray(SD1_base+4, 4)
v = sum([b<<(n*8) for n,b in enumerate(v)])
v = ctypes.c_int(v).value

