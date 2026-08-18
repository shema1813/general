switches = 0

LIGHT = 1 << 0       # Bit 0
FAN = 1 << 1         # Bit 1
TV = 1 << 2          # Bit 2
DOOR = 1 << 3        # Bit 3
ALARM = 1 << 4       # Bit 4

switches |= LIGHT
switches |= FAN
switches |= ALARM

print("Smart Switch Bit Monitor")
print("------------------------")
print("Binary value:", format(switches, "05b"))
print()

if switches & LIGHT:
    print("Light: ON")
else:
    print("Light: OFF")

if switches & FAN:
    print("Fan: ON")
else:
    print("Fan: OFF")

if switches & TV:
    print("TV: ON")
else:
    print("TV: OFF")

if switches & DOOR:
    print("Door: ON")
else:
    print("Door: OFF")

if switches & ALARM:
    print("Alarm: ON")
else:
    print("Alarm: OFF")
